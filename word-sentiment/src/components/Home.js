import React from 'react';
import Introduction from './Introduction';
import WordInput from './WordInput';
import './Home.css';

const Home = () => {
    return (
        <div className="home" style={{marginBottom: '5rem'}}>
            <Introduction />
            <WordInput />
        </div>
    );
};

export default Home;
