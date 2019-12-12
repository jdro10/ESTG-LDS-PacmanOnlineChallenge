import React, { useState } from "react";

import "./styles.css";
import Pacman from "./../../components/Pacman/index";
import ValidatedRegisterForm from "../../components/ValidatedRegisterForm/index";
export default function Register() {
  const [email, setEmail] = useState("");
  const [user, setUser] = useState("");
  const [pass, setPass] = useState("");

  return (
    <div className="container-register">
      <form className="register-container">
        <Pacman className="register-pacman" />
        <ValidatedRegisterForm />
      </form>
    </div>
  );
}
