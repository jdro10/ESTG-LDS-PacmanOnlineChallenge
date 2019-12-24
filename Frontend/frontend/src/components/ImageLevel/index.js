import React from "react";

import img0 from "../../assets/0.png";
import img1 from "../../assets/1.png";
import img2 from "../../assets/2.png";
import img3 from "../../assets/3.png";
import img4 from "../../assets/4.png";
import img5 from "../../assets/5.png";
import img6 from "../../assets/6.png";
import img7 from "../../assets/7.png";
import img8 from "../../assets/8.png";
import img9 from "../../assets/9.png";
import img10 from "../../assets/10.png";
import img11 from "../../assets/11.png";
import img12 from "../../assets/12.png";
import img13 from "../../assets/13.png";
import img14 from "../../assets/14.png";
import img15 from "../../assets/15.png";
import img16 from "../../assets/16.png";
import img17 from "../../assets/17.png";
import img18 from "../../assets/18.png";

export default function ImageLevel({ nivel }) {
  var imagem;
  if (nivel >= 0 && nivel < 5) {
    imagem = img0;
  }
  if (nivel >= 5 && nivel < 10) {
    imagem = img1;
  }
  if (nivel >= 10 && nivel < 15) {
    imagem = img2;
  }
  if (nivel >= 15 && nivel < 20) {
    imagem = img3;
  }
  if (nivel >= 20 && nivel < 25) {
    imagem = img4;
  }
  if (nivel >= 25 && nivel < 30) {
    imagem = img5;
  }
  if (nivel >= 30 && nivel < 35) {
    imagem = img6;
  }
  if (nivel >= 35 && nivel < 40) {
    imagem = img7;
  }
  if (nivel >= 40 && nivel < 45) {
    imagem = img8;
  }
  if (nivel >= 45 && nivel < 50) {
    imagem = img9;
  }
  if (nivel >= 50 && nivel < 55) {
    imagem = img10;
  }
  if (nivel >= 55 && nivel < 60) {
    imagem = img11;
  }
  if (nivel >= 60 && nivel < 65) {
    imagem = img12;
  }
  if (nivel >= 65 && nivel < 70) {
    imagem = img13;
  }
  if (nivel >= 70 && nivel < 75) {
    imagem = img14;
  }
  if (nivel >= 75 && nivel < 80) {
    imagem = img15;
  }
  if (nivel >= 80 && nivel < 85) {
    imagem = img16;
  }
  if (nivel >= 85 && nivel < 90) {
    imagem = img17;
  }
  if (nivel >= 90 && nivel <= 100) {
    imagem = img18;
  }

  return (
    <div>
      <img src={imagem} />
    </div>
  );
}
