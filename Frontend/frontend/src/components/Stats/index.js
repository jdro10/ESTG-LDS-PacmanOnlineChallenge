import React from "react";

import "./styles.css";
import ImageLevel from "./../ImageLevel/index";

export default function Stats({ nivel, score, rank }) {
  return (
    <>
      <ImageLevel nivel={nivel} />
      <p>level:{nivel}</p>

      <p>score:{score}</p>
      <p>rank:{rank}</p>
    </>
  );
}
