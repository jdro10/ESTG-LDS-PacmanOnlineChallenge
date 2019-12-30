import React, { useState } from "react";

import "./styles.css";
import api from "./../../services/api";
import BoxRank from "./../../components/BoxRank/index";

export default function Leaderboards() {
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

  return (
    <div className="container-leaderboard">
      <div className="leaderboard-container">
        {player0Name === "" ? (
          console.log("clear")
        ) : (
          <BoxRank classification="1" name={player0Name} score={player0Score} />
        )}

        {player1Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player1Name}
            {player1Score}
          </p>
        )}

        {player2Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player2Name}
            {player2Score}
          </p>
        )}

        {player3Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player3Name}
            {player3Score}
          </p>
        )}

        {player4Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player4Name}
            {player4Score}
          </p>
        )}

        {player5Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player5Name}
            {player5Score}
          </p>
        )}

        {player6Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player6Name}
            {player6Score}
          </p>
        )}

        {player7Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player7Name}
            {player7Score}
          </p>
        )}

        {player8Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player8Name}
            {player8Score}
          </p>
        )}

        {player9Name === "" ? (
          console.log("clear")
        ) : (
          <p>
            {player9Name}
            {player9Score}
          </p>
        )}
      </div>
    </div>
  );
}
