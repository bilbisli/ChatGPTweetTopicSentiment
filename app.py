from typing import Tuple
import json

from flask import Flask, request, jsonify
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from dotenv import load_dotenv


app = Flask(__name__)

def load_models(topic_model_path, sentiment_model, topic_embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
    sentence_model = SentenceTransformer(topic_embedding_model)
    topic_model = BERTopic.load(topic_model_path, embedding_model=sentence_model)
    app.logger.info(f"Successfully loaded topic model from {topic_model_path}")
    sentiment_model = pipeline(model=sentiment_model)
    app.logger.info(f"Successfully loaded sentiment model from {sentiment_model}")
    return topic_model, sentence_model, sentiment_model

load_dotenv()
topic_model_path = 'models/bertopic_model'
topic_embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"
sentiment_model_name = "finiteautomata/bertweet-base-sentiment-analysis"
topic_model, sentence_model, sentiment_model = load_models(topic_model_path, sentiment_model_name, topic_embedding_model_name)

def get_data_from_request(request, payload_name='tweet'):
    '''
    This function gets the data from the request.
    '''
    try:
        data: str = request.json[payload_name]
        app.logger.info(f"Successfully got {payload_name} from request\n: {data}")
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
    app.logger.info("Request received for /topic:\n", request.json)

    request_data = get_data_from_request(request, payload_name='tweet')
    # in case of error
    if isinstance(request_data, tuple):
        return request_data
    tweet: str = request_data
    res = topic_model.transform([tweet])
    print(res)
    topic = topic_model.get_topic(res[0][0])
    app.logger.info(topic)
    return json.dumps({"topic": topic})
    
@app.route("/sentiment", methods=["POST"])
def get_sentiment() -> jsonify or Tuple[jsonify, int]:
    '''
    This endpoint returns the sentiment of a tweet.
    Example:
    curl -X POST -H "Content-Type: application/json" -d '{tweet:"I love the new features of the iPhone!"}' http://localhost:5000/sentiment
    '''
    app.logger.info("Request received for /sentiment")
    
    request_data = get_data_from_request(request, payload_name='tweet')
    # in case of error
    if isinstance(request_data, tuple):
        return request_data
    tweet: str = request_data
    sentiment = sentiment_model(tweet)[0]
    app.logger.info(sentiment)
    return jsonify({"sentiment": sentiment["label"], "score": sentiment["score"]})


if __name__ == "__main__":
    app.run(debug=True)
