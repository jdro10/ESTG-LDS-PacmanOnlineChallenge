import React, { useState } from "react";
import "./styles.css";
import logo from "../../assets/logo.png";
import ImageLevel from "./../../components/ImageLevel/index";
import api from "../../services/api";

export default function Dashboard({ history }) {
  const user_id = localStorage.getItem("userId");
  const token = localStorage.getItem("userToken");

  const [level, setLevel] = useState();
  const [score, setScore] = useState();
  const [rank, setRank] = useState();

  console.log(user_id);
  console.log(token);

  async function load() {
    const response = await api.get("/api/ranks", {
      headers: { id: user_id, Authorization: `Bearer ${token}` }
    });

    setLevel(response.data.level);
    setScore(response.data.level);
    setRank(response.data.rank);
  }

  console.log(level);
  console.log(score);
  console.log(rank);

  load();
  function handleClickRegister(event) {
    event.preventDefault();
    history.push("/");
  }

  return (
    <div className="container-dashboard">
      <div className="header-container">
        <div className="header">
          <h1>PacmanOnlineChallenge</h1>
          <img src={logo} alt="Logo" />
        </div>
      </div>
      <div className="stats-container">
        <div className="cashier">
          <h1>Stats</h1>
          <ImageLevel nivel={level} />
        </div>
      </div>
      <div className="challenges-container">
        <div className="cashier">
          <h1>Challenges</h1>
        </div>
      </div>
      <div className="footer-container">
        <div className="social">
          <a href="https://github.com/RAJ66">
            <img
              src="https://img.icons8.com/ios-filled/50/000000/facebook-new.png"
              alt="Facebook"
            />
          </a>
          <a href="https://github.com/RAJ66">
            <img
              src="https://img.icons8.com/material/50/000000/instagram-new--v1.png"
              alt="Instagram"
            />
          </a>
          <a href="https://github.com/RAJ66">
            <img
              src="https://img.icons8.com/ios-filled/50/000000/twitter-circled.png"
              alt="Twitter"
            />
          </a>
          <button onClick={handleClickRegister} className="link-button ">
            <img
              src="https://img.icons8.com/ios-filled/50/000000/exit.png"
              alt="Exit"
            />
          </button>
        </div>
      </div>
    </div>
  );
}
