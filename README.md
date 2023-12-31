# ChatGPT Tweet Analysis

ChatGPT Tweet Analysis is a web application built with ReactJS and Flask that allows users to analyze the sentiment and topic of ChatGPT-related tweets.

## Features

- Analyze the sentiment of a ChatGPT-related tweet
- Determine the topic of a ChatGPT-related tweet
- User-friendly interface with real-time analysis results

## Technologies Used

- ReactJS: A JavaScript library for building user interfaces
- Flask: A micro web framework for building web applications
- BERTopic: A library for topic modeling using BERT embeddings
- Sentence Transformers: A library for state-of-the-art sentence embeddings
- Transformers: A library for natural language processing using transformer models

## Prerequisites

- Node.js (version 20.2.0)
- Python (version 3.9.13)

## Getting Started

0. Install [**`python`**](https://www.python.org/downloads/release/python-3913/), [**`Node.js`**](https://nodejs.org/dist/v20.2.0/) and [**`git`**](https://git-scm.com/downloads)
1. Open a terminal and clone the repository:
```
git clone https://github.com/bilbisli/ChatGPTweetTopicSentiment.git
```
2. Create and activate a virtual environment for the Flask app:
```
cd ChatGPTweetTopicSentiment
py -3.9 -m venv venv
```
 * For macOS and Linux:
```
source venv/bin/activate
```
 * For Windows:
```
venv\Scripts\activate
```
3. Install the dependencies for the Flask app:
```
pip install -r requirements.txt
```
4. Start the Flask app:
```
python app.py
```
5. In a separate terminal (opened at the root of the project), Install the dependencies for the React app:
```
cd frontend
npm install
```
6. Start the React server:
```
npm start
```
7. Access the application in your web browser:
    [http://localhost:3000](http://localhost:3000)

## Configuration

The following environment variables can be set or configured in the `.env` file:

- `TWEET_ANALYSIS_API_HOST`: The hostname or IP address of the Tweet Analysis API (default: localhost)
- `TWEET_ANALYSIS_API_PORT`: The port number of the Tweet Analysis API (default: 5000)

## Usage

1. Enter a ChatGPT-related tweet in the provided input field.
2. Click the "Analyze" button to analyze the sentiment and topic of the tweet.
3. The sentiment (positive, negative, neutral) and topic of the tweet will be displayed below.
4. Repeat the process for additional tweets.

## Demo

[System Demo](https://github.com/bilbisli/ChatGPTweetTopicSentiment/assets/73055024/5221a1c0-cdc5-45ce-a392-7760942f0319)

## Data

The data used for creating this project is available at:
[ChatGPT Twitter Dataset](https://www.kaggle.com/datasets/tariqsays/chatgpt-twitter-dataset)

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).



   

   

