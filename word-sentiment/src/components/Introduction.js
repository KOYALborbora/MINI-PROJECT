import React from 'react';
import './Introduction.css';

const Introduction = () => {
    return (
        <div className="introduction">
            <h1 style={{fontSize:'5rem'}}>Word Sentiment Predictor</h1>
            <p style={{fontSize:'1.5rem'}}>This application predicts the sentiment of a word as positive or negative. 
               Enter a word in the prediction box and find out the sentiment associated with it.</p>
        </div>
    );
};

export default Introduction;
