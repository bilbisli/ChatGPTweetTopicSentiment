import React from 'react';

function SentimentResult({ sentiment }) {
    return (
        <div className="sentiment">
            <p className="sentiment-label">Sentiment:</p>
            <p className={`sentiment-value ${sentiment}`} > { sentiment }</p>
        </div >
    );
}

export default SentimentResult;
