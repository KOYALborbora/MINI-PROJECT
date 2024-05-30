import React from 'react';
import './AboutUs.css';

const teamMembers = [
    {
        name: "Parthajeet Deva Sarmah",
        bio: "A passionate developer with expertise in machine learning.",
        linkedin: "https://www.linkedin.com/in/parthajeet-deva-sarmah/",
        github: "https://github.com/Parthajeet-Sarmah",
    },
    {
        name: "Koyal Borbora",
        bio: "Enthusiastic about AI and data science.",
        linkedin: "https://www.linkedin.com/in/koyal-borbora-a2716724b",
        github: "https://github.com/koyalborbora",
    },
    {
        name: "Keshab Sen",
        bio: "Loves coding and developing innovative solutions.",
        linkedin: "https://www.linkedin.com/in/keshab-sen",
        github: "https://github.com/Keshab002",
    }
];

const AboutUs = () => {
    return (
        <div className='about'>
        <div className="about-us">
            <h1>About Us</h1>
            {teamMembers.map(member => (
                <div key={member.name} className="team-member">
                    <h2>{member.name}</h2>
                    <p>{member.bio}</p>
                    <div className="links">
                        <a href={member.linkedin} target="_blank" rel="noopener noreferrer">LinkedIn</a>
                        <a href={member.github} target="_blank" rel="noopener noreferrer">GitHub</a>
                    </div>
                </div>
            ))}
        </div>
        </div>
    );
};

export default AboutUs;
