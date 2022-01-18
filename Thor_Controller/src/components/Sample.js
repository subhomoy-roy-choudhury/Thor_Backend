import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

import {
  BrowserRouter as Router,
  Routes ,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
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
          <Route path="/frontend/join" element={<RoomJoinPage/>} />
          <Route path="/frontend/create" element={<CreateRoomPage/>} />
        </Routes>
      </Router>
    );
  }
}