import React from "react";

import "./styles.css";

export default function Challenges({
  nameCha1,
  nameCha2,
  nameCha3,
  pointCha1,
  pointCha2,
  pointCha3
}) {
  return (
    <>
      <h3>
        {nameCha1}
        {pointCha1}
      </h3>
      <h3>
        {nameCha2}
        {pointCha2}
      </h3>
      <h3>
        {nameCha3}
        {pointCha3}
      </h3>
    </>
  );
}
