import React, { useState } from "react";

import "./styles.css";

export default function ResetPassword() {
  const [email, setEmail] = useState("");
  function handleSubmit(event) {}
  return (
    <div className="container-reset">
      <div className="reset-container">
        <h3>
          Already have an account? <a href="/">Log in</a>
        </h3>
        <form onSubmit={handleSubmit}>
          <input
            placeholder="Email address"
            value={email}
            onChange={event => setEmail(event.target.value)}
          />

          <button type="submit" className="glow-on-hover basebutton">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
