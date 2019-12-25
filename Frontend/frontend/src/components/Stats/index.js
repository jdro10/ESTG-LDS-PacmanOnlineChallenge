import React from "react";

import "./styles.css";
import ProgressBar from "./../ProgressBar/index";

export default function Stats({ nivel, score, rank }) {
  return (
    <>
      <p>Level: {nivel}</p>
      <ProgressBar nivel={nivel} score={score} />
      <p>Score: {score}</p>

      <p>Rank: {rank}</p>
    </>
  );
}
