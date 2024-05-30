import React, { useState } from 'react';
import axios from 'axios';
import './WordInput.css';

const WordInput = () => {
    const [word, setWord] = useState('');
    const [result, setResult] = useState({});
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleInputChange = (event) => {
        // Update word state when input changes
        setWord(event.target.value);
    };

    const handlePredict = async () => {
        // Reset previous result and error
        setResult({});
        setError('');
        setLoading(true); // Show loading indicator
        try {
            const response = await axios.post('http://127.0.0.1:5000/predict', { word });
            setResult(response.data);
            console.log(response.data);
        } catch (err) {
            console.error('Error predicting sentiment:', err);
            setError('Error: Unable to predict sentiment. Please try again.');
        } finally {
            setLoading(false); // Hide loading indicator
        }
    };

    const handleReset = () => {
        // Reset input, result, and error
        setWord('');
        setResult({});
        setError('');
    };

    return (
        <div className="word-input-container">
            <h2>Word Sentiment Prediction</h2>
            <div className="word-input-form">
                <input
                    type="text"
                    value={word.toLowerCase()}
                    onChange={handleInputChange}
                    className="word-input"
                    placeholder="Enter a word"
                />
                <div className="button-container">
                    <button onClick={handlePredict} className="predict-button">Predict</button>
                    <button onClick={handleReset} className="reset-button">Reset</button>
                </div>
            </div>
            {error && <div className="error-message">{error}</div>}
            {loading && <div className="loading-message">Loading...</div>}
            {result["word"] && (
                <div className="prediction-box">
                    <h3>Prediction Result</h3>
                    <div className="result-field">{result["word"]} is a {result["prediction"]} word.</div>
                </div>
            )}
        </div>
    );
};

export default WordInput;
