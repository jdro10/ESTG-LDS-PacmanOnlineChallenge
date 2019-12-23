import React from "react";
import { mount } from "enzyme";
import toJson from "enzyme-to-json";

import Dashboard from "./../pages/Dashboard/index";

describe("Testing Pacman Component", () => {
  it("should render correctly", () => {
    const wrapper = mount(<Dashboard />);

    expect(toJson(wrapper)).toMatchSnapshot();
  });
});
