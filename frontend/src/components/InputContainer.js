import React from 'react';

function InputContainer({ tweet, setTweet, analyzeTweet }) {
    return (
        <div className="input-container">
            <textarea
                className="tweet-input"
                placeholder="Enter your ChatGPT-related tweet"
                value={tweet}
                onChange={(e) => setTweet(e.target.value)}
            ></textarea>
            <button className="analyze-button" onClick={analyzeTweet}>Analyze</button>
        </div>
    );
}

export default InputContainer;
