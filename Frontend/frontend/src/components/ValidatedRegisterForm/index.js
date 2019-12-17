import React from "react";

import { Formik } from "formik";
import * as Yup from "yup";

import api from "../../services/api";

export default function ValidatedRegisterForm({ history }) {
  async function handleSubmmit(values) {
    //event.preventDefault();
    console.log("sent2");
    console.log(values);

    const response = await api.post("/api/user", {
      Username: values.userName,
      Email: values.email,
      Password: values.password
    });
    console.log(response);
  }

  return (
    <Formik
      initialValues={{ userName: "", email: "", password: "" }}
      onSubmit={values => {
        console.log("sent");
        handleSubmmit(values);
      }}
      validationSchema={Yup.object().shape({
        userName: Yup.string()
          .required("Required")
          .min(3, "UserName is too short - should be 3 chars minimum."),
        email: Yup.string()
          .email("Email must be a valid email")
          .required("Required"),
        password: Yup.string()
          .required("No password provided.")
          .min(8, "Password is too short - should be 8 chars minimum.")
          .matches(
            /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
            "Password must contain number and letter."
          )
      })}
    >
      {props => {
        const {
          values,
          touched,
          errors,
          isSubmitting,
          handleChange,
          handleBlur,
          handleSubmit
        } = props;
        return (
          <form onSubmit={handleSubmit} className="register-container">
            <input
              name="userName"
              type="text"
              placeholder="Username"
              value={values.userName}
              onChange={handleChange}
              onBlur={handleBlur}
              className={errors.userName && touched.userName && "error"}
            />
            {errors.userName && touched.userName && (
              <div className="input-feedback">{errors.userName}</div>
            )}

            <input
              name="email"
              type="text"
              placeholder="Email"
              value={values.email}
              onChange={handleChange}
              onBlur={handleBlur}
              className={errors.email && touched.email && "error"}
            />
            {errors.email && touched.email && (
              <div className="input-feedback">{errors.email}</div>
            )}
            <input
              name="password"
              type="password"
              placeholder="Password"
              value={values.password}
              onChange={handleChange}
              onBlur={handleBlur}
              className={errors.password && touched.password && "error"}
            />
            {errors.password && touched.password && (
              <div className="input-feedback">{errors.password}</div>
            )}
            <button
              type="submit"
              disabled={isSubmitting}
              className="glow-on-hover"
            >
              Register
            </button>
          </form>
        );
      }}
    </Formik>
  );
}
