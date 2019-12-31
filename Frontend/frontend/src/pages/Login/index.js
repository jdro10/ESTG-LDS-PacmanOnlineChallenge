import React, { useState } from "react";
import api from "../../services/api";
import logo from "../../assets/logo.png";
import "./styles.css";

export default function Login({ history }) {
  const [user, setUser] = useState("");
  const [pass, setPass] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    console.log(user);
    console.log(pass);

    const response = await api.post("/api/user/auth", {
      username: user,
      password: pass
    });

    var token = response.data.token;
    var id = response.data.id;

    console.log(token);
    console.log(id);
    console.log(response);

    localStorage.setItem("userId", id);
    localStorage.setItem("userToken", token);

    if (id) {
      console.log("connect");
      history.push("/dashboard");
    } else {
      alert("Incorrect username or password");
    }
  }

  function handleClickRegister(event) {
    event.preventDefault();
    history.push("/register");
  }

  function handleClickForgot(event) {
    event.preventDefault();
    alert("Email send");
    history.push("/");
  }

  return (
    <div className="container-inicio">
      <form className="login-container" onSubmit={handleSubmit}>
        <img src={logo} className="logoLogin" alt="It a match" />
        <input
          placeholder="Username"
          value={user}
          onChange={event => setUser(event.target.value)}
        />
        <input
          placeholder="Password"
          type="password"
          value={pass}
          onChange={event => setPass(event.target.value)}
        />

        <button type="submit" className="glow-on-hover basebutton">
          Login
        </button>
        <button
          type="reset"
          onClick={handleClickRegister}
          className="glow-on-hover basebutton"
        >
          Register
        </button>

        <button onClick={handleClickForgot} className="forgotButton ">
          Forgot account?
        </button>
      </form>
    </div>
  );
}
