import React from 'react';
import SentimentResult from './SentimentResult';
import TopicResult from './TopicResult';

function ResultContainer({ sentiment, topic }) {
    return (
        <div className="result-container">
            {sentiment && <SentimentResult sentiment={sentiment} />}
            {topic && <TopicResult topic={topic} />}
        </div>
    );
}

export default ResultContainer;
