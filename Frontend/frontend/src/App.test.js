import React from "react";
import { shallow, mount } from "enzyme";
import App from "./App";
import Login from "./pages/Login/index.js";
import ShallowRenderer from "react-test-renderer/shallow"; // ES6
import toJson from "enzyme-to-json";

describe("Testing Login Component", () => {
  it("should render correctly", () => {
    const wrapper = shallow(
      <div className="my-component">
        <strong>ola World!</strong>
      </div>
    );

    expect(toJson(wrapper)).toMatchSnapshot();
  });

  it("knows that 2 and 2 make 4", () => {
    expect(2 + 2).toBe(4);
  });
});
