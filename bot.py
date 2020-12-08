'''
Es el vinculo entre el cliente, el objeto y la ia:

_Busca o crea un objeto game para cada juego en ejecucion
_Pide al objeto correspondiente toda la data necesaria para la eleccion del mejor movimiento en el turno actual
_Luego, transfiere la data obtenida al planificador de la ia para que este califique los movimientos segun su estrategia
_Finalmente, de los movimientos calificados busco cual es el que tiene mayor puntaje y se lo envio al cliente

En definitiva: Esta seccion del programa tiene como input el estado antes de que tenga que mover y entrega como output el mejor movimiento posible para responder al server
'''

import tablero
import ia_planificador

juegos_Ejecutandose = {}            #Diccionario que juega los juegos corriendose actualmente (cada juego es un objeto), identifico cada juego mediante "board_id" 

#-----------------------------------------------------------BOT--------------------------------------------------------------------------------#
def bot_work(datos_partida):   
    #1) Accedo al juego en cuestion mediante la id unica de cada partida (si no existe, lo creo)
    juego_actual = juegos_Ejecutandose.get(datos_partida["board_id"])
    if juego_actual is None:    
        juego_actual = crear_juego(datos_partida["board_id"], datos_partida["actual_turn"])     #Para crear una partida necesito el board_id y el color con el que voy a jugar
        
    #Esto solo se ejecuta cuando estoy jugando contra mi mismo
    #Tengo un solo objeto creado por partida y varios atributos dependen del color, por lo que al jugar contra mi mismo, debo reescribir los atributos que dependen del color
    if datos_partida["username"] == datos_partida ["opponent_username"]:   
        restart_atributes(datos_partida["actual_turn"] ,juego_actual)


    #2)Actualizar el tablero
    juego_actual.Actualizar(datos_partida["board"])

    #3)Actualizar estado de columnas
    juego_actual.columna_Rating()

    #4)Obtencion de movimientos propios y del rival
    moves       = []                                               #Reseteo las listas con los posibles movimientos mios y del rival
    moves_enemy = []

    change=0                                                       #Obtengo una lista con todos los movimientos validos posibles que puedo realizar
    moves       = juego_actual.get_All_Possible_Moves(change)      #change=0 ----> Me devuelve una lista con mis movimientos validos posibles           (para el estado actual del tablero)
            
    change=1                                                       #Obtengo una lista con todos los movimientos validos posibles del rival
    moves_enemy = juego_actual.get_All_Possible_Moves(change)      #change=1 ----> Me devuelve una lista con los movimientos validos posibles del rival (para el estado actual del tablero)
    
    #5)Calificar los movimientos obtenidos
    moves_analized = ia_planificador.inicio(moves, moves_enemy, juego_actual)     #Asigno un valor a cada movimiento
    juego_actual.queens_Quantity = 0                                             #reseteo el nro de reinas luego de evaluar los movimientos
    
    #6)Obtencion del mejor movimiento respecto a la calificacion otorgada 
    return comparacion(moves_analized)

#----------------------------------------------------------------FIN BOT----------------------------------------------------------------------------#
#-----------------------------------------------------------FUNCIONES DEl BOT-----------------------------------------------------------------------#
# Crea para cada "board_id" un objeto "game"
def crear_juego(id_nueva, color):
    print ("Inicia el juego")
    print("id_game: {}".format(id_nueva))
    number = tablero.game(color == "white")             #Si coincide, crea el juego como blancas (True = white); en caso contrario como negras (False = Black)
    juegos_Ejecutandose.update({id_nueva:number})       #Asigna el id como identificador del nuevo juego creado
    return juegos_Ejecutandose.get(id_nueva)            #Devuelve el juego recien creado

# Verifica el valor asignado por la ia a cada movimiento y elige el de mayor valor
def comparacion(moves):
    comparacion = None
    best_move = []
    for movimiento_final in moves:
        if comparacion is None:
            comparacion = movimiento_final[2]
            best_move = movimiento_final

        elif movimiento_final[2] > comparacion:
            comparacion = movimiento_final[2]
            best_move = movimiento_final
    
    return best_move

# Elimina el respectivo objeto juego mediante su id (una vez que el juego ha terminado)
def limpiar(id_vieja):
    juegos_Ejecutandose.pop(id_vieja)

# Cambia los atributos inicializados en el objeto a los del color contrario (sirve para jugar contra mi mismo usnado el mismo objeto)
def restart_atributes(turno, juego_actual):
    if turno == "white":
        juego_actual.color = True
        juego_actual.seteo_Inicial(True)
    else:
        juego_actual.color = False
        juego_actual.seteo_Inicial(False)