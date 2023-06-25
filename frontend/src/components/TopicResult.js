import React from 'react';

function TopicResult({ topic }) {
    return (
        <div>
            <p className="result-label">Topic:</p>
            <ul className="topic-list">
                {topic.map((pair, index) => (
                    <li key={index} className="topic-item">
                        <div className="topic-text">
                            <span className="word">{pair[0]}</span>
                            <span className="probability">{pair[1]}</span>
                        </div>
                        <div className="probability-bar">
                            <div
                                className="probability-fill"
                                style={{ width: `${pair[1] * 100}%` }}
                        ></div>
                    </div>
                </li>
                ))}
        </ul>
        </div >
    );
}

export default TopicResult;