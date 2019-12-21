import React from "react";
import { shallow } from "enzyme";
import App from "./App";

describe("Testing Login Component", () => {
  it("should render correctly", () => {
    const wrapper = shallow(<App />);

    expect(wrapper).toMatchSnapshot();
  });

  it("knows that 2 and 2 make 4", () => {
    expect(2 + 2).toBe(4);
  });
});
