import React, { Component } from "react";
import { render } from "react-dom";
import Sample from "./Sample";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h1>thor</h1>
        <Sample />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);