import React from "react";
import { mount } from "enzyme";
import toJson from "enzyme-to-json";

import Register from "./../pages/Register/index";

describe("Testing Pacman Component", () => {
  it("should render correctly", () => {
    const wrapper = mount(<Register />);

    expect(toJson(wrapper)).toMatchSnapshot();
  });
});
