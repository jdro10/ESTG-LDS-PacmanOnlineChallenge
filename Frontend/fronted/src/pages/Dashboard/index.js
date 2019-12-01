import React from "react";
import "../../Main.css";
import logo from "../../assets/logo.png";

// import { Container } from './styles';

export default function Dashboard() {
  return (
    <div className="container-main">
      <div className="header-container">
        <div className="header">
          <h1>PacmanOnlineChallenge</h1>
          <img src={logo} alt="Logo" />
        </div>
      </div>
      <div className="level-container">
        <div className="caixa">
          <h1>Level</h1>
        </div>
      </div>
      <div className="challenges-container">
        <div className="caixa">
          <h1>Challenges</h1>
        </div>
      </div>
      <div className="footer-container">
        <div className="social">
          <a href="https://github.com/RAJ66">
            <img src="https://img.icons8.com/ios-filled/50/000000/facebook-new.png" />
          </a>
          <a href="https://github.com/RAJ66">
            <img src="https://img.icons8.com/material/50/000000/instagram-new--v1.png" />
          </a>
          <a href="https://github.com/RAJ66">
            <img src="https://img.icons8.com/ios-filled/50/000000/twitter-circled.png" />
          </a>
          <a href="https://github.com/RAJ66">
            <img src="https://img.icons8.com/ios-filled/50/000000/exit.png" />
          </a>
        </div>
      </div>
    </div>
  );
}
