import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Pacman from "./components/Pacman/index";
import Register from "./pages/Register/index";
import Leaderboards from "./pages/Leaderboards/index";
import ResetPassword from "./pages/ResetPassword/index";
export default function Routes() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact component={Login} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/register" component={Register} />
        <Route path="/leaderboards" component={Leaderboards} />
        <Route path="/resetpass" component={ResetPassword} />

        <Route path="/pacman" component={Pacman} />
      </Switch>
    </BrowserRouter>
  );
}
