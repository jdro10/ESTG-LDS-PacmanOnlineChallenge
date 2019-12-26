import React from "react";

import "./styles.css";

export default function ProgressBar({ nivel, score }) {
  var tmp1 = nivel * 1000;
  var tmp2 = score - tmp1;

  var mostrar = (100 * tmp2) / 1000;
  return (
    <div className="progress-bar">
      <div className="filler" style={{ width: `${mostrar}%` }} />
    </div>
  );
}
