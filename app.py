from typing import Tuple
import os
import logging

from flask import Flask, request, jsonify
from bertopic import BERTopic
from transformers import pipeline
from dotenv import load_dotenv
# import gdown


# def download_models(model_path,
#                     topic_model_gdrive_id, 
#                     sentiment_model_name, 
#                     topic_model_folder="topic_model"):
#     os.makedirs(model_path, exist_ok=True)
    
#     files = {
#         topic_model_folder: topic_model_gdrive_id,
#     }
    
#     for file_name, file_id in files.items():
#         file_path = os.path.join(model_path, file_name)
#         if not os.path.isfile(file_path):
#             url = f"https://drive.google.com/uc?id={file_id}"
#             gdown.download(url, file_path, quiet=False)
#             assert os.path.isfile(file_path), f"Failed to download {file_name}"

#     topic_model = BERTopic.load(os.path.join(model_path, topic_model_folder))
#     sentiment_model = pipeline("sentiment-analysis", model=sentiment_model_name)

#     return topic_model, sentiment_model

app = Flask(__name__)
logging.basicConfig(filename='record.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

def load_models(topic_model_path, sentiment_model, topic_embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
    topic_model = BERTopic.load(topic_model_path, topic_embedding_model)
    app.logger.info(f"Successfully loaded topic model from {topic_model_path}")
    sentiment_model = pipeline(model=sentiment_model)
    app.logger.info(f"Successfully loaded sentiment model from {sentiment_model}")
    return topic_model, sentiment_model

load_dotenv()
topic_model_path = 'models/bertopic_model'
sentiment_model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
topic_model, sentiment_model = load_models(topic_model_path, sentiment_model_name, sentiment_model_name)



def get_data_from_request(request, payload_name='tweet'):
    '''
    This function gets the data from the request.
    '''
    try:
        data: str = request.json[payload_name]
        app.logger.info(f"Successfully got {payload_name} from request")
        return data
    except KeyError:
        app.logger.error(f"Failed to get {payload_name} from request")
        return jsonify({"error": f"Please provide a {payload_name}."}), 400
    except TypeError:
        app.logger.error(f"Failed to get {payload_name} from request")
        return jsonify({"error": "Please provide a valid JSON."}), 400

@app.route("/topic", methods=["POST"])
def get_topic() -> jsonify or Tuple[jsonify, int]:
    '''
    This endpoint returns the topic of a tweet.
    Example:
    curl -X POST -H "Content-Type: application/json" -d '{"tweet":"I love the new features of the iPhone!"}' http://localhost:5000/topic
    '''
    app.logger.info("Request received for /topic")
    request_data = get_data_from_request(request, payload_name='tweet')
    # in case of error
    if isinstance(request_data, tuple):
        return request_data
    tweet: str = request_data
    topics, _ = topic_model.transform([tweet])
    topic = topics[0]
    return jsonify({"topic": topic})
    
@app.route("/sentiment", methods=["POST"])
def get_sentiment() -> jsonify or Tuple[jsonify, int]:
    '''
    This endpoint returns the sentiment of a tweet.
    Example:
    curl -X POST -H "Content-Type: application/json" -d '{"tweet":"I love the new features of the iPhone!"}' http://localhost:5000/sentiment
    '''
    app.logger.info("Request received for /sentiment")
    
    request_data = get_data_from_request(request, payload_name='tweet')
    # in case of error
    if isinstance(request_data, tuple):
        return request_data
    tweet: str = request_data
    sentiment = sentiment_model(tweet)[0]
    return jsonify({"sentiment": sentiment["label"], "score": sentiment["score"]})


if __name__ == "__main__":
    app.run(debug=True)
