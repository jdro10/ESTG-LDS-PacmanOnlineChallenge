import React from "react";

import "./styles.css";
import logo from "../../assets/logo.png";

export default function BoxRank({ classification, name, score }) {
  return (
    <div className="BoxRank">
      <p>
        <img src={logo} className="logo" alt="It a match" />
        {classification}º {name} <br />
        Score: {score}
      </p>
    </div>
  );
}
