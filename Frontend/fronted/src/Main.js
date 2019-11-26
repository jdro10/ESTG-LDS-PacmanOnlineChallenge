import React from "react";
import "./Main.css";
import logo from "./assets/logo.png";

// import { Container } from './styles';

export default function src() {
  return (
    <div className="container">
      <div className="header-container">
        <h1>POC </h1>
        <img src={logo} alt="Logo" />
      </div>
      <div className="level-container">
        <h1>Level </h1>
      </div>
      <div className="challenges-container">
        <h1>challenges </h1>
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
