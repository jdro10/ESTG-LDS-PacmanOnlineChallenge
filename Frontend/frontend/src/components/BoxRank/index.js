import React from "react";

import "./styles.css";

export default function BoxRank({ classification, name, score }) {
  return (
    <div>
      <p>
        {classification}
        {name}
        {score}
      </p>
    </div>
  );
}
