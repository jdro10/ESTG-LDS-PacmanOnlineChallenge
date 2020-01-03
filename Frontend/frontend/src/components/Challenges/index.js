import React from "react";

import "./styles.css";

import logo from "../../assets/logo.png";
export default function Challenges({
  nameCha1,
  nameCha2,
  nameCha3,
  pointCha1,
  pointCha2,
  pointCha3,
  valid1,
  valid2,
  valid3
}) {
  return (
    <>
      {valid1 === "0" ? (
        <>
          <h3>
            <img src={logo} className="logo" alt="It a match" />
            {nameCha1}
          </h3>
          <h3>
            <b> Reward:</b>
            {pointCha1}
          </h3>
          <hr />
        </>
      ) : (
        console.log("")
      )}

      {valid2 === "0" ? (
        <>
          <h3>
            <img src={logo} className="logo" alt="It a match" />

            {nameCha2}
          </h3>
          <h3>
            <b> Reward:</b>
            {pointCha2}
          </h3>
          <hr />
        </>
      ) : (
        console.log("")
      )}

      {valid3 === "0" ? (
        <>
          <h3>
            <img src={logo} className="logo" alt="It a match" />

            {nameCha3}
          </h3>

          <h3>
            <b> Reward:</b>
            {pointCha3}
          </h3>
        </>
      ) : (
        console.log("")
      )}
    </>
  );
}
