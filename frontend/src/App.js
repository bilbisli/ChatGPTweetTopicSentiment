import logo from './logo.svg';
import React, { useState } from 'react';
import './App.css';

const TWEET_ANALYSIS_API_HOST = process.env.TWEET_ANALYSIS_API_HOST || 'localhost';
const TWEET_ANALYSIS_API_PORT = process.env.TWEET_ANALYSIS_API_PORT || 5000;
const TWEET_ANALYSIS_API_URL = `http://${TWEET_ANALYSIS_API_HOST}:${TWEET_ANALYSIS_API_PORT}`;

function App() {
  const [tweet, setTweet] = useState('');
  const [sentiment, setSentiment] = useState('');
  const [topic, setTopic] = useState('');

  const analyzeTweet = async () => {
    try {
      const responseSentiment = await fetch(`${TWEET_ANALYSIS_API_URL}/sentiment`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tweet }),
      });
      const sentimentResult = await responseSentiment.json();
      setSentiment(sentimentResult.sentiment);

      const responseTopic = await fetch(`${TWEET_ANALYSIS_API_URL}/topic`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tweet }),
      });
      const topicResult = await responseTopic.json();
      console.log('topicResult:', topicResult)
      setTopic(topicResult.topic);
    } catch (error) {
      console.error('Error analyzing tweet:', error);
    }
  };

  return (
    <div className="app-container">
      <div className="App">
        <h1 className="title">ChatGPT Tweet Analysis</h1>
        <div className="input-container">
          <textarea
            className="tweet-input"
            placeholder="Enter your ChatGPT-related tweet"
            value={tweet}
            onChange={(e) => setTweet(e.target.value)}
          ></textarea>
          <button className="analyze-button" onClick={analyzeTweet}>Analyze</button>
        </div>
        <div className="result-container">
          {sentiment && (
            <div className="sentiment">
              <p className="sentiment-label">Sentiment:</p>
              <p className={`sentiment-value ${sentiment}`}>{sentiment}</p>
            </div>
          )}
          {topic && (
            <div>
              <p className="result-label">Topic:</p>
              <ul className="topic-list">
                {topic.map((pair, index) => (
                  <li key={index} className="topic-item">
                    <div className="topic-text">
                      <span className="word">{pair[0]}</span>
                      <span className="probability">{pair[1]}</span>
                    </div>
                    <div className="topic-item"></div>
                    <div className="probability-bar">
                      <div
                        className="probability-fill"
                        style={{ width: `${pair[1] * 100}%` }}
                      ></div>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </div>
  );  
}

export default App;
