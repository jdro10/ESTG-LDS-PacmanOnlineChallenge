import React from "react";
import "./App.css";

function App() {
  return (
    <div className="login-container">
      <form>
        <input placeholder="Email" />
        <input placeholder="Password" type="password" />

        <button type="submit">Login</button>
      </form>
      <button type="submit">Register</button>
    </div>
  );
}

export default App;
