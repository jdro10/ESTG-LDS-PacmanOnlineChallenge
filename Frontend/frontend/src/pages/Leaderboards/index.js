import React, { useState } from "react";

import "./styles.css";
import api from "./../../services/api";
import BoxRank from "./../../components/BoxRank/index";
import logo from "../../assets/logo.png";

export default function Leaderboards({ history }) {
  const [player0Name, setPlayer0Name] = useState("");
  const [player0Score, setPlayer0Score] = useState("");

  const [player1Name, setPlayer1Name] = useState("");
  const [player1Score, setPlayer1Score] = useState("");

  const [player2Name, setPlayer2Name] = useState("");
  const [player2Score, setPlayer2Score] = useState("");

  const [player3Name, setPlayer3Name] = useState("");
  const [player3Score, setPlayer3Score] = useState("");

  const [player4Name, setPlayer4Name] = useState("");
  const [player4Score, setPlayer4Score] = useState("");

  const [player5Name, setPlayer5Name] = useState("");
  const [player5Score, setPlayer5Score] = useState("");

  const [player6Name, setPlayer6Name] = useState("");
  const [player6Score, setPlayer6Score] = useState("");

  const [player7Name, setPlayer7Name] = useState("");
  const [player7Score, setPlayer7Score] = useState("");

  const [player8Name, setPlayer8Name] = useState("");
  const [player8Score, setPlayer8Score] = useState("");

  const [player9Name, setPlayer9Name] = useState("");
  const [player9Score, setPlayer9Score] = useState("");

  async function load() {
    const response = await api.get("/api/ranks/topten");

    console.log(response);

    if (response.data[0] == null) {
      console.log("null");
    } else {
      setPlayer0Name(response.data[0].username);
      setPlayer0Score(response.data[0].score);
    }

    if (response.data[1] == null) {
      console.log("null");
    } else {
      setPlayer1Name(response.data[1].username);
      setPlayer1Score(response.data[1].score);
    }

    if (response.data[2] == null) {
      console.log("null");
    } else {
      setPlayer2Name(response.data[2].username);
      setPlayer2Score(response.data[2].score);
    }

    if (response.data[3] == null) {
      console.log("null");
    } else {
      setPlayer3Name(response.data[3].username);
      setPlayer3Score(response.data[3].score);
    }

    if (response.data[4] == null) {
      console.log("null");
    } else {
      setPlayer4Name(response.data[4].username);
      setPlayer4Score(response.data[4].score);
    }

    if (response.data[5] == null) {
      console.log("null");
    } else {
      setPlayer5Name(response.data[5].username);
      setPlayer5Score(response.data[5].score);
    }

    if (response.data[6] == null) {
      console.log("null");
    } else {
      setPlayer6Name(response.data[6].username);
      setPlayer6Score(response.data[6].score);
    }

    if (response.data[7] == null) {
      console.log("null");
    } else {
      setPlayer7Name(response.data[7].username);
      setPlayer7Score(response.data[7].score);
    }
    if (response.data[8] == null) {
      console.log("null");
    } else {
      setPlayer8Name(response.data[8].username);
      setPlayer8Score(response.data[8].score);
    }

    if (response.data[9] == null) {
      console.log("null");
    } else {
      setPlayer9Name(response.data[9].username);
      setPlayer9Score(response.data[9].score);
    }
  }

  load();

  function handleClickExit(event) {
    event.preventDefault();
    history.push("/dashboard");
  }

  return (
    <div className="container-leaderboard">
      <div className="leaderboard-container">
        <div className="header">
          <h1>Pacman Online Challenge Leaderboards</h1>
          <img src={logo} alt="Logo" />
        </div>
        {player0Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="1" name={player0Name} score={player0Score} />
        )}

        {player1Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="2" name={player1Name} score={player1Score} />
        )}

        {player2Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="3" name={player2Name} score={player2Score} />
        )}

        {player3Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="4" name={player3Name} score={player3Score} />
        )}

        {player4Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="5" name={player4Name} score={player4Score} />
        )}

        {player5Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="6" name={player5Name} score={player5Score} />
        )}

        {player6Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="7" name={player6Name} score={player6Score} />
        )}

        {player7Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="8" name={player7Name} score={player7Score} />
        )}

        {player8Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="9" name={player8Name} score={player8Score} />
        )}

        {player9Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank
            classification="10"
            name={player9Name}
            score={player9Score}
          />
        )}
        <button className="back" onClick={handleClickExit} />
      </div>
    </div>
  );
}
