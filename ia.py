####-------------------------------------------------------Variables-------------------------------------------------------####
'''
En este arreglo voy a ir guardando todos los posibles movimientos que puedo realizar:
Cada posicion del arreglo almacena todos los movimientos validos de mis piezas a ese lugar
El movimiento se almacena en forma de una lista con el siguiente contenido: [piece ,tipo ,i ,captura]
Donde:
    _piece   = pieza con la que me puedo mover a ese casillero
    _tipo    = si el movimiento es de captura (tipo = 0) o si es un movimiento a espacio libre (tipo = 1)
    _i       = orden del movimiento dentro de la lista de mis posibles movimientos
    _captura = este valor lo tengo solo para movimientos de tipo=0, es un string con 2 caracteres, el primero indica mi pieza y el segundo la pieza que capture
               ej:  qK ------>Yo como jugador negro, puedo concretar la captura de un rey rival si me muevo a este casillero

El objetivo de mapear este arreglo con todos mis posibles movimientos es para posteriormente volverlo a recorrer pero ahora analizando los movimientos que podria realizar mi rival
en la jugada posterior a la mia, con este metodo logro:
1) Analizar si mis movimientos de captura (tipo=0) son limpios o si el rival me puede recapturar la pieza...si se da que me puede recapturar, analizo el resultado neto de la 
   captura -------------> (valor_mi_pieza - valor_pieza_capturada) ------> Si el resultado es >0 fue un buen movimiento (mientras mas >0, mejor es el movimiento)

2) Analizar si los movimientos a espacios libres (tipo=1) son buenos o si al moverme a ese espacio me expongo a una captura.
'''
tablero = [
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]]

#Asigno valores a mis piezas y a las del rival
valores_mios  = {"P":10 ,"H":50, "B":40,"R":60,"Q":70,"K":5,        #Los valores de peones y reinas los calculo con funciones arriba, debido a que sus valores dependen del estado del tablero (No hace falta que esten aca, nunca los buscas aca)
                 "p":10 ,"h":50, "b":40,"r":60,"q":70,"k":5}      

valores_rival = {"p":10,"h":40,"b":50,"r":70,"q":80,"k":300,
                 "P":10,"H":40,"B":50,"R":70,"Q":80,"K":300}

#A los peones les incremento el valor respecto a que tan cerca de coronar estan
valor_peon_white = {13:10, 12:25 ,11:30 ,10:35 ,9:75 ,8:90}         #row=8 ----> Coronacion
valor_peon_black = {2:10  ,3:25  ,4:30  ,5:35  ,6:75 ,7:90}         #row=7 ----> Coronacion




#Esta funcion me da el valor del movimiento de un peon, el cual aumenta mientras mas cerca de coronar este
def peon(fila, color):
    if color == True:
        return valor_peon_white[fila]
    else:
        return valor_peon_black[fila]

#Actualiza el valor de las reinas dependiendo de la cantidad de estas que controle
def reina(cantidad, color):
    valor = 80 - cantidad * 5

    if valor < 0:
        valor = 30

    if color == True:
        valores_mios["Q"] = valor
    else:
        valores_mios["q"] = valor



####-------------------------------------------------------Fin Variables-------------------------------------------------------####

#Esta funcion recibe toda la data (movimientos posibles mios, los del rival, la cantidad de reinas, mejores columnas para mover peones) y asigna un valor a cada movimiento
def bot_inteligence(moves_propios, moves_enemy, queens_quantity, color, best_col, juego_actual):  #arregla los argumentos, estas pasando juego_actual, que tiene todo lo demas adentro
  
    reina(queens_quantity, color)
    print(queens_quantity)

    moves_propios = moves_pawn_free   (moves_propios, queens_quantity, color, best_col)
    moves_propios = moves_queen_free    (moves_propios, juego_actual)
    moves_propios = moves_propios_capture(moves_propios, color)

    moves_propios = moves_queen_capture (moves_propios, juego_actual)

    moves_propios = moves_enemy_free          (moves_propios, moves_enemy)
    moves_propios = moves_enemy_capture       (moves_propios, moves_enemy)   
    #moves_enemy_piece_ataqued (moves_propios, moves_enemy)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #FALTA UN EVENTO IMPORTANTE: SI EL RIVAL PUEDE COMERME UNA PIEZA Y ESA PIEZA PUEDE ATACARLA ANTES, SERIA BUENO QUE LO HAGA
    #PARA RESOLVERLO, NECESITAS---> pieza_que_me_pueden_capturar = moves_enemy[piece][0][movement][3][1] (con esto pasarias que pieza es la del rival)
    #con esa letra, deberia ir a un diccionario que tenga valores entre el 0 y 5 (igual que piece)
    #Tambien necesitas -----------> posicion_pieza_que_me_pueden_capturar = moves_enemy[piece][0][movement][1] (este seria el tuple al que me moveria para capturar == la posicion inicial de mi pieza)
    #finalmente, entro a -------->  moves_propios[dict[pieza_que_me_pueden_capturar]][for entre 0 y 1(tenes que verificar que no este vacio esto creo)][movement][0] == posicion_pieza_que_me_pueden_capturar
    #si ocurre igualdad, tenes que terminar con---> moves_propios[dict[pieza_que_me_pueden_capturar]][for entre 0 y 1(tenes que verificar que no este vacio esto creo)][movement][2] = moves_propios[dict[pieza_que_me_pueden_capturar]][for entre 0 y 1(tenes que verificar que no este vacio esto creo)][movement][2]  + un valor agregado
    for piece_enemy in range(6):
        for movement in moves_enemy[piece_enemy][0]:
            start_sq = movement[0]
            end_sq   = movement[1]
            for my_piece in range(6):
                for movemento in moves_propios[my_piece][0]:
                    if end_sq == movemento[0] and start_sq == movemento[1]:
                        movemento[2] = movemento[2] + valores_rival[movemento[3][1]] * 10 + valores_mios[movemento[3][0]] * 10 + 2000
 
    #esto deberia ser una funcion
    for x in range (16):
        for y in range (16):
            tablero[x][y] = []

    return moves_propios




def moves_pawn_free   (moves_propios, queens_quantity, color, best_col):
    piece = 3
    tipo  = 1
    i     = 0

    for movement in moves_propios[piece][tipo]:
        tablero[movement[1][0]][movement[1][1]].append([piece,tipo,i])  
        i=i+1
            
        if queens_quantity < 14:
            movement[2] = movement[2] + peon(movement[1][0], color) + best_col[movement[1][1]] + 450

        else:
            movement[2] = movement[2] + peon(movement[1][0], color) + best_col[movement[1][1]] + 50
                        
    return moves_propios                
    
def moves_queen_free  (moves_propios, juego_actual):
    piece = 5
    tipo  = 1
    i     = 0

    for movement in moves_propios[piece][tipo]:
        tablero[movement[1][0]][movement[1][1]].append([piece,tipo,i])  
        i=i+1

        #Logica de reinas
        '''
        Moverte con una reina desde la fila de coronacion propia a la fila tactica(la fila anterior a la coronacion) tiene un valor agregado
        Condiciones: _La pieza a evaluar es una reina en la fila de coronacion propia
                     _Tengo al menos 2 reinas en la fila de coronacion propia (asi no la dejo libre para ser ocupada por el rival)
                     _En la fila tactica no hay ni una reina propia 
        '''
        #movement[1][0] = endRow
        #movement[1][1] = endCol
        if (juego_actual.qm_quantity_row_upgrade_mia > 1)    and (juego_actual.qm_quantity_row_tactical == 0) and (movement[1][0] == juego_actual.row_tactical) and (movement[0][0] == juego_actual.row_upgrade_mia):
            movement[2] = movement[2] + 1000
                        
        '''
        Moverte con una reina desde la fila de coronacion propia a la fila de coronacion del rival(la fila posterior a la coronacion propia) tiene un valor agregado
        Condiciones:_La pieza a evaluar es una reina en la fila de coronacion propia
                    _El rival no tiene reinas suyas en su fila de coronacion (que me puedan recapturar si me muevo ahi)
                    _Yo no tengo otra reina su fila de coronacion (con una es suficiente)
        '''
        if (juego_actual.qm_quantity_row_upgrade_rival == 0) and (juego_actual.qr_quantity_row_upgrade_rival == 0) and (movement[1][0] == juego_actual.row_upgrade_rival) and (movement[0][0] == juego_actual.row_upgrade_mia):
            movement[2] = movement[2] + 10000



    
    return moves_propios

def moves_propios_capture(moves_propios, color):
    tipo = 0
    for piece in range(5):
        i=0
        for movement in moves_propios[piece][tipo]:
            tablero[movement[1][0]][movement[1][1]].append([piece,tipo,i,movement[3]])  
            i=i+1
            
            if movement[3][1] == "P" or movement[3][1] == "p":
                movement[2] = movement[2] + peon(movement[1][0], not color) * 10
                    
            else:
                movement[2] = movement[2] + valores_rival[movement[3][1]] * 10 

    return moves_propios

def moves_queen_capture  (moves_propios, juego_actual):
    piece = 5
    tipo  = 0
    i     = 0

    for movement in moves_propios[piece][tipo]:
        tablero[movement[1][0]][movement[1][1]].append([piece,tipo,i,movement[3]])  
        i=i+1
        #movement[1][0]
        #aca tendrias que armar una logica para agregar a movement[2]

        movement[2] = movement[2] + valores_rival[movement[3][1]] * 10
    
    return moves_propios


#esto solo lo aplico para mis reinas, ya que no me interesa si el rival me puede comer peones (hice una logica para protejerlos) y las demas piezas mias no deberian moverse a lugares libres
def moves_enemy_free          (moves_propios, moves_enemy):
    tipo=1
    for piece in range(6):
        for movement in moves_enemy[piece][tipo]:
            if len(tablero[movement[1][0]][movement[1][1]]) != 0: 
                for bad_move in tablero[movement[1][0]][movement[1][1]]:
                    if bad_move[0] == 5:                               #solo analizo a las reinas propias que le rival me pueda capturar en movimientos de retirada
                        moves_propios[bad_move[0]][bad_move[1]][bad_move[2]][2] = moves_propios[bad_move[0]][bad_move[1]][bad_move[2]][2] - 10000
    return moves_propios

#Esto aplica para todas las piezas MENOS la reina (ella se maneja aparte)
def moves_enemy_capture       (moves_propios, moves_enemy):
    tipo=0
    for piece in range(6):
        for movement in moves_enemy[piece][tipo]:
            if len(tablero[movement[1][0]][movement[1][1]]) != 0:            
                for capture_move in tablero[movement[1][0]][movement[1][1]]:                           
                    if len(capture_move) == 4: #la lista tiene 5 posiciones SOLO si ya se ha analizado la recaptura por parte del rival

                        moves_propios[capture_move[0]][capture_move[1]][capture_move[2]][2] = moves_propios[capture_move[0]][capture_move[1]][capture_move[2]][2] - valores_mios[moves_propios[capture_move[0]][capture_move[1]][capture_move[2]][3][0]] * 10                           
                        capture_move.append("visado")       #Esto sirve para no restar 2 veces el valor de una captura(la pieza aunque me la puedan capturar varias piezas, la capturan una sola vez)   
    return moves_propios


#def moves_enemy_piece_ataqued (moves_propios, moves_enemy):

'''
    for piece_enemy in range(6):
        for movement in moves_enemy[piece_enemy][0]:
            start_sq = movement[0]
            end_sq   = movement[1]
            for my_piece in range(6):
                for movemento in moves_propios[my_piece][0]:
                    if end_sq == movemento[0] and start_sq == movemento[1]:
                        movemento[2] = movemento[2] + valores_rival[movemento[3][1]] * 10 + valores_mios[movemento[3][0]] * 10 + 2000

'''