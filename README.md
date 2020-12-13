[![Build Status](https://travis-ci.com/Enzo127/MC-EB.svg?token=Nx3isxfu7pDpvqBeY9pq&branch=main)](https://travis-ci.com/Enzo127/MC-EB) [![Coverage Status](https://coveralls.io/repos/github/Enzo127/MC-EB/badge.svg?branch=main&service=github)](https://coveralls.io/github/Enzo127/MC-EB?branch=main)


## About:
MegaChess es un juego por código donde los participantes, mediante inteligencia artificial, deben competir. Este juego guarda un parecido al Ajedrez. 

El servidor se encarga de crear las partidas y torneos, controlar los turnos de los jugadores y la validación de las movidas. 

Este ajedrez en particular se trata de un tablero de 16 x 16, que contiene 64 piezas por color (4 piezas donde había 1 pieza original en el tablero de 8 x 8).

Gameover
Cuando se concluyen cuando alguna de las siguientes condiciones es cierta:
Todos las movida indicadas en move_left, la partida finaliza.  
Un jugador tiene menos de -500 puntos
Un jugador se queda sin piezas


Puntajes

Esta variante del ajedrez no se basa en el jaque, sino en los puntos. Cada pieza tiene un valor:

   Pawn: 10
   Horse: 30
   Bishop: 40
   Rook: 60
   Queen: 5
   King: 100

Si un jugador mueve con éxito una pieza, sumará el valor de la pieza movida.
Si un jugador come una pieza del oponente, entonces sumará el valor de la pieza del oponente multiplicado por 10.
Si un jugador realiza una movida incorrecta o pierde el turno, entonces restará 20 puntos.

Promote
En este ajedrez en particular, los peones coronan (promote) en el centro del tablero, convirtiéndose en Damas automáticamente.

Cada promote da 500 puntos
