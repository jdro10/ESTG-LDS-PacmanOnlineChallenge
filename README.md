# PacmanOnlineChallenge

<div align="center">
<h1 >PacmanOnlineChallenge </h1></div>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pacman Online Challenge será um jogo para PC, que está atualmente a ser desenvolvido para a unidade curricular "Laboratório de Desenvolvimento de Software". 
O jogo a ser desenvolvido terá por base o tão conhecido Pacman, desenvolvido pela Nanco, portanto toda a mecânica, lógica e regras serão as mesmas. O objetivo, não só, é  desenvolver o mesmo jogo de raiz em modo singleplayer, mas também levar o mesmo <b>um passo a frente, mais competitivo e mais apelativo de jogar ao implementar um sistema multiplayer</b> em que é possível jogar contra adversários humanos.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A nossa visão que fundamenta uma maior competitividade neste jogo, baseia-se no facto,  tal como referido anteriormente, de ser possível jogar contra humanos, também haverá desafios diários em que os jogadores podem participar e terão direito a diversas recompensas, por fim haverá um sistema de ranking relacionado com as partidas singleplayer, multiplayer ou ligado às recompensas diárias.</p>

## 💻Stack

- [.Net](https://dotnet.microsoft.com/)
- [React](https://reactjs.org)
- [Pygame](https://www.pygame.org/)
- [mongoDB](https://www.mongodb.com/)

<h3>Backend<h3>
<p>Pasta que contém todo o código relativo ao backend, contendo a REST API e a parte correspondente ao multiplayer.<p>
<h3>Frontend<h3>
<p>Pasta com todo o código do frontend.<p>
<h3>Game<h3>
<p>Pasta com código relativo ao jogo singleplayer.<p>

## Requisitos para correr o projeto:

- Ter o .NET instalado;
- Ter o python e pygame instalados;
- Ter o npm instalado;

## Como correr o projeto:

- Dentro da pasta Backend/API:
	- dotnet build;
	- dotnet run;
	- No browser https://localhost:5001 - desativar o certificado;
- Dentro da pasta Backend/Multiplayer:
	- dotnet build;
	- dotnet run;
- Dentro da pasta Frontend/Frontend:
	- npm install;
	- npm start;
- Dentro da pasta Game:
	- py Login.py