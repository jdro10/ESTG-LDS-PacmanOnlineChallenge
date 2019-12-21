import React from "react";
import { shallow } from "enzyme";
import Login from "../src/pages/Login/index";

describe("Testing Login Component", () => {
  it("should render correctly", () => {
    const wrapper = shallow(<Login />);

    expect(wrapper).toMatchSnapshot();
  });
});
