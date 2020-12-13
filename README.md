## Badges:
[![Build Status](https://travis-ci.com/Enzo127/MC-EB.svg?token=Nx3isxfu7pDpvqBeY9pq&branch=main)](https://travis-ci.com/Enzo127/MC-EB) [![Coverage Status](https://coveralls.io/repos/github/Enzo127/MC-EB/badge.svg?branch=main&service=github)](https://coveralls.io/github/Enzo127/MC-EB?branch=main)

## Languages and Utilities:
<img align="left" alt="Python 3" width="26px" src="https://user-images.githubusercontent.com/66569117/102001075-8a868a00-3ccc-11eb-8e1e-4b48be386518.png" />
<img align="left" alt="Travis ci" width="26px"src="https://user-images.githubusercontent.com/66569117/102001248-8eb3a700-3cce-11eb-9ced-d93d508b9395.png" />
<img align="left" alt="Coveralls" width="26px"src="https://user-images.githubusercontent.com/66569117/102001268-eeaa4d80-3cce-11eb-9c42-e8acdbe96141.png" />
<img align="left" alt="Visual Studio Code" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png" />
<img align="left" alt="Git" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png" />
<img align="left" alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" /> 
<br />

## Mi estrategia:
Cada turno almaceno todos los movimientos validos mios y del rival y en base a eso genero un board con los eventos posibles en cada casillero:
 - Capturas limpias mias (x) (capturas en las que el rival no puede recapturarme)
 - Capturas sucias mias (?) (capturas en las que el rival me puede recapturas) 
 - Capturas del rival (&)
 - Casilleros vacios pero controlados por mis piezas (+)
 - Casilleros vacios pero controlados por piezas rivales (-)

Luego, evaluo los movimientos posibles y elijo el mejor considerando lo que podria hacer el rival el proximo turno.

### Archivos de programa:
 - cliente: Se conecta al server via websocket con mi usuario, recibe los eventos de este y responde con las acciones correspondientes.
 - tablero: Objeto vinculado a cada partida en juego.
 - bot: Tiene como input el estado actual de un juego y como output el mejor movimiento en respuesta.
 - ia: Se encarga de generar los eventos posibles y evaluar los movimientos.

## Acerca del juego:
MegaChess es un juego por código donde los participantes, mediante inteligencia artificial, deben competir. Este juego guarda un parecido al Ajedrez. 

El servidor se encarga de crear las partidas y torneos, controlar los turnos de los jugadores y la validación de las movidas. 

Este ajedrez en particular se trata de un tablero de 16 x 16, que contiene 64 piezas por color (4 piezas donde había 1 pieza original en el tablero de 8 x 8).

### Gameover:
Cuando se concluyen cuando alguna de las siguientes condiciones es cierta:

 - Todos las movida indicadas en move_left, la partida finaliza.  
 - Un jugador tiene menos de -500 puntos
 - Un jugador se queda sin piezas


### Puntajes:
Esta variante del ajedrez no se basa en el jaque, sino en los puntos. Cada pieza tiene un valor:

  - Pawn: 10
  - Horse: 30
  - Bishop: 40
  - Rook: 60
  - Queen: 5
  - King: 100


Si un jugador mueve con éxito una pieza, sumará el valor de la pieza movida.

Si un jugador come una pieza del oponente, entonces sumará el valor de la pieza del oponente multiplicado por 10.

Si un jugador realiza una movida incorrecta o pierde el turno, entonces restará 20 puntos.

### Promote:
En este ajedrez en particular, los peones coronan (promote) en el centro del tablero, convirtiéndose en Damas automáticamente.

Cada promote da 500 puntos

## Autor:
* **Enzo Crespillo**    [enzo__127@hotmail.com]()
