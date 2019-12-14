import React from "react";

import "./styles.css";
import Pacman from "./../../components/Pacman/index";
import ValidatedRegisterForm from "../../components/ValidatedRegisterForm/index";

export default function Register({ history }) {
  return (
    <div className="container-register">
      <div className="register-container">
        <Pacman className="register-pacman" />
        <ValidatedRegisterForm history={history} />
      </div>
    </div>
  );
}
