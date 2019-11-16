import React from "react";
import "./App.css";

import logo from "./assets/logo.png";

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
