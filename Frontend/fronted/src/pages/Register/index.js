import React, { useState } from "react";

import "./styles.css";

export default function Register() {
  const [email, setEmail] = useState("");
  const [user, setUser] = useState("");
  const [pass, setPass] = useState("");

  return (
    <div className="container-register">
      <form className="register-container">
        <input
          placeholder="UserName"
          value={user}
          onChange={event => setUser(event.target.value)}
        />
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

        <button type="submit">Register</button>
      </form>
    </div>
  );
}
