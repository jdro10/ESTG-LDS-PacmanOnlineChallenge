import React from "react";

import "./styles.css";
import ImageLevel from "./../ImageLevel/index";
import ProgressBar from "./../ProgressBar/index";

export default function Stats({ nivel, score, rank }) {
  return (
    <>
      <ImageLevel nivel={nivel} />
      <p>Level: {nivel}</p>
      <ProgressBar nivel={nivel} score={score} />
      <p>Score: {score}</p>

      <p>Rank: {rank}</p>
    </>
  );
}
