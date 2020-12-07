#Detallar los alcances de este programa (a bot le llega el estado de una partida y tiene que discernir que juego es, si tiene que crearlo y pedir
# a distintos programas todo lo necesario para devolver el mejor movimiento)
import tablero
import ia_organizador

#Diccionario que juega los juegos corriendose actualmente (cada juego es un objeto), identifico cada juego mediante "board_id" 
juegos_Ejecutandose = {}

#-----------------------------------------------------------BOT--------------------------------------------------------------------------------#
#Esta funcion tiene como input el estado antes de que tenga que mover y entrega como output el mejor movimiento posible para responder al server
def bot_work(datos_partida):   
    #1) Accedo al juego en cuestion mediante la id unica de cada partida (si no existe, lo creo)
    juego_actual = juegos_Ejecutandose.get(datos_partida["board_id"])
    if juego_actual is None:    
        juego_actual = crear_juego(datos_partida["board_id"], datos_partida["actual_turn"])     #Para crear una partida necesito el board_id y el color con el que voy a jugar
        juego_actual.seteo_Inicial(datos_partida["actual_turn"] == "white")                     #Al crear un nuevo juego, debo setear ciertos valores dependiendo de si me tocaron blancas o negras
  
    #Esto solo se ejecuta cuando estoy jugando contra mi mismo
    #Tengo un solo objeto creado por partida e inicializado con un color, pero al jugar contra mi mismo, debo ir alternando el color dependiendo de que turno sea
    if datos_partida["username"] == datos_partida ["opponent_username"]:   
                            
        if datos_partida["actual_turn"] == "white":
            juego_actual.color = True
            juego_actual.seteo_Inicial(True)
        else:
            juego_actual.color = False
            juego_actual.seteo_Inicial(False)

    print(juego_actual.color)


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
    moves_analized = ia_organizador.inicio(moves, moves_enemy, juego_actual)     #Asigno un valor a cada movimiento....(estas pasando juego y 2 atributos de este, podes hacerlo asi para mas orden, pero en is, pasando el objeto ya estas pasando los demas datos)
    juego_actual.queens_Quantity = 0                                                                                          #reseteo el nro de reinas luego de evaluar los movimientos
    
    #6)Obtencion del mejor movimiento respecto a la calificacion otorgada 
    return comparacion(moves_analized)

#----------------------------------------------------------------FIN BOT----------------------------------------------------------------------------#
#-----------------------------------------------------------FUNCIONES DEl BOT-----------------------------------------------------------------------#
# Funcion que crea para cada "board_id" un objeto "game"
def crear_juego(id_nueva, color):
    print ("Inicia el juego")
    print("id_game: {}".format(id_nueva))
    number = tablero.game(color == "white")             #Si coincide, crea el juego como blancas (True = white); en caso contrario como negras (False = Black)
    juegos_Ejecutandose.update({id_nueva:number})       #Asigna el id como identificador del nuevo juego creado
    return juegos_Ejecutandose.get(id_nueva)            #Devuelve el juego recien creado

# Funcion que verifica el valor asignado por la ia a cada movimiento y elige el de mayor valor
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

# Funcion que elimina el objeto juego mediante su id (una vez que el juego ha terminado)
def limpiar(id_vieja):
    juegos_Ejecutandose.pop(id_vieja)
