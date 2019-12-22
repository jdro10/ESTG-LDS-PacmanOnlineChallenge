import React from "react";
import { mount } from "enzyme";
import toJson from "enzyme-to-json";
import Login from "./../pages/Login/index";

describe("Testing Pacman Component", () => {
  it("should render correctly", () => {
    const wrapper = mount(<Login />);

    expect(toJson(wrapper)).toMatchSnapshot();
  });
});
