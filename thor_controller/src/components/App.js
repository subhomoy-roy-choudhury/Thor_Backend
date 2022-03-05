
  
import React, { Component } from "react";
import { render } from "react-dom";
import {
    BrowserRouter as Router,
    Routes ,
    Route,
    Link,
    Redirect,
  } from "react-router-dom";
import HomePage from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <Router>
            <Routes>
            {/* <Route exact path="/">
                <p>This is the home page</p>
            </Route> */}
            {/* <Route path="/about" element={<RoomJoinPage/>} /> */}
            <Route path="" element={<HomePage/>} />
            </Routes>
        </Router>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);