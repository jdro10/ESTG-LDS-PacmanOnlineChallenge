import React, { useState } from "react";
import "./styles.css";
import api from "./../../services/api";

export default function ResetPassword({ history }) {
  const [email, setEmail] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();

    const response = await api.get("/api/user/forgotPassword", {
      headers: { email: email }
    });

    console.log(response);
    if (response.data.success === "true") {
      alert("Email sent");
      history.push("/");
    } else {
      alert("Email does not exist");
    }
  }

  return (
    <div className="container-reset">
      <div className="reset-container">
        <h3>
          Already have an account? <a href="/">Log in</a>
        </h3>
        <form className="resetForm" onSubmit={handleSubmit}>
          <input
            placeholder="Email address"
            value={email}
            type="email"
            onChange={event => setEmail(event.target.value)}
          />

          <button type="submit" className="glow-on-hover basebutton">
            Reset password
          </button>
        </form>
      </div>
    </div>
  );
}
