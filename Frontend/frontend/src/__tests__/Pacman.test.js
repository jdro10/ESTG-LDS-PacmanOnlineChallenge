import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";
import Pacman from "../components/Pacman/index";

describe("Testing Pacman Component", () => {
  it("should render correctly", () => {
    const wrapper = shallow(<Pacman />);

    expect(toJson(wrapper)).toMatchSnapshot();
  });
});
