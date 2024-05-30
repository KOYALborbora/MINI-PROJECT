import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './components/Home';
import AboutUs from './components/AboutUs';
import './App.css';

const App = () => {
    return (
        <Router>
            <div className="App">
                <div className="App-header">
                    <nav>
                        <ul>
                            <li><Link style={{textDecoration: 'none', color:'white'}} to="/">Home</Link></li>
                            <li><Link style={{textDecoration: 'none', color:'white'}} to="/about">About Us</Link></li>
                        </ul>
                    </nav>
                </div>
                <main>
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/about" element={<AboutUs />} />
                    </Routes>
                </main>
            </div>
        </Router>
    );
};

export default App;
