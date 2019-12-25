import React from "react";

// import { Container } from './styles';
import ImageLevel from "./../ImageLevel/index";

export default function Stats({ nivel, score, rank }) {
  return (
    <div>
      <ImageLevel nivel={nivel} />
      <p>level:{nivel}</p>

      <p>score:{score}</p>
      <p>rank:{rank}</p>
    </div>
  );
}
