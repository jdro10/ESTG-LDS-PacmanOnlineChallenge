import React, { useState } from "react";
import api from "../../services/api";
import logo from "../../assets/logo.png";

export default function Login({ history }) {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    console.log(email);
    console.log(pass);

    api.post("/api/users", {
      UserEmail: email,
      Password: pass
    });

    history.push("/dashboard");
  }

  return (
    <form className="login-container" onSubmit={handleSubmit}>
      <img src={logo} alt="It a match" />
      <input
        placeholder="Email"
        value={email}
        onChange={event => setEmail(event.target.value)}
      />
      <input
        placeholder="Password"
        type="password"
        value={pass}
        onChange={event => setPass(event.target.value)}
      />

      <button type="submit" className="glow-on-hover">
        Login
      </button>
      <button type="" className="glow-on-hover">
        Register
      </button>
    </form>
  );
}
