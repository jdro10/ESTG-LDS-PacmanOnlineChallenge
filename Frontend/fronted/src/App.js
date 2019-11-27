import React from "react";
import "./App.css";
import api from "./assets/api";

import logo from "./assets/logo.png";
import api from "./services/api";

function App() {
  return (
    <div className="container">
      <form className="login-container">
        <img src={logo} alt="It a match" />
        <input placeholder="Email" />
        <input placeholder="Password" type="password" />

        <button type="submit" className="glow-on-hover">
          Login
        </button>
        <button type="submit" className="glow-on-hover">
          Register
        </button>
      </form>
    </div>
  );
}

export default App;
