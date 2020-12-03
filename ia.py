import copy

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
Arreglo = [
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


####-------------------------------------------------------Fin Variables-------------------------------------------------------####



#Esta funcion recibe toda la data (movimientos posibles mios, los del rival, la cantidad de reinas, mejores columnas para mover peones) y asigna un valor a cada movimiento
def bot_inteligence(moves, moves_enemy, queens_quantity, color, game_Actual):  
    tablero = copy.deepcopy(Arreglo)               #Cada vez que llamo a esta funcion, empiezo trabajando con un arreglo limpio
    reina(queens_quantity, color)
    
    for piece in range(6):
        for tipo in range(2):
            i=0
            #ANALIZO MOVIMIENTOS CON CAPTURAS
            if tipo==0:                 #Logica para capturas
                #Mis Movimientos
                for movement in moves[piece][tipo]:      
                    tablero[movement[1][0]][movement[1][1]].append([piece,tipo,i,movement[3]])      #Como aca analizo capturas, tambien debo agregar el termino movement[3] // ej: Rr: Mi torre captura torre rival
                    
                    if movement[3][1] == "P" or movement[3][1] == "p":
                        movement[2] = movement[2] + peon_rival(movement[1][0], color) * 10
                    
                    else:
                        movement[2] = movement[2] + valores_rival[movement[3][1]] * 10                               #movement[3][0] = la pieza con la que yo capture // movement[3][1] la pieza que capture
                    i=i+1

            #ANALIZO MOVIMIENTOS A ESPACIOS LIBRES
            if tipo==1:                 #Logica para movimientos a espacios vacios
                #ANALIZO MIS MOVIMIENTOS
                for movement in moves[piece][tipo]:               
                    tablero[movement[1][0]][movement[1][1]].append([piece,tipo,i])  #agrego al tablero una lista con [pieza a la que me refiero][tipo: 0=movimiento con captura / 1=movimiento a espacio vacio][lugar en la lista "moves"]
                    #Logica de peones: Mientras mas cerca de la coronacion este, mas valor agregado tiene el movimiento

                    if piece == 3:
                        if queens_quantity < 14:
                            movement[2] = movement[2] + peon_propio(movement[1][0], color) + game_Actual.best_col[movement[1][1]] + 450

                        else:
                            movement[2] = movement[2] + peon_propio(movement[1][0], color) + game_Actual.best_col[movement[1][1]] + 50
                        
                    i=i+1

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Esta podria ser otra funcion, en la cual pasas 
    for piece in range(6):
        for tipo in range(2):
            if tipo ==0:
                #Movimientos del rival con captura
                for movemento in moves_enemy[piece][tipo]:
                    if len(tablero[movemento[1][0]][movemento[1][1]]) != 0:            
                        for capture_move in tablero[movemento[1][0]][movemento[1][1]]:                           
                            if len(capture_move) == 4: #la lista tiene 5 posiciones SOLO si ya se ha analizado la recaptura por parte del rival     

                                #aca es donde podrias agregar una logica de que si la pieza que te pueden capturar es una reina, esta se vuelva a row_tactica o uno de esos lugares

                                moves[capture_move[0]][capture_move[1]][capture_move[2]][2] = moves[capture_move[0]][capture_move[1]][capture_move[2]][2] - valores_mios[moves[capture_move[0]][capture_move[1]][capture_move[2]][3][0]] * 10                           
                                capture_move.append("visado")       #Esto sirve para no restar 2 veces el valor de una captura(la pieza aunque me la puedan capturar varias piezas, la capturan una sola vez)            
            else:   #tipo==1
                #Movimientos del rival a espacios vacios
                for movemento in moves_enemy[piece][tipo]:
                    if len(tablero[movemento[1][0]][movemento[1][1]]) != 0:             
                        for bad_move in tablero[movemento[1][0]][movemento[1][1]]:
                            if bad_move[0] == 3:    #lo que digo aca es: si me pueden capturar al peon que estoy moviendo, no hay drama, hay otra logica que se ocupa de analizar eso
                                pass
                            else:
                                moves[bad_move[0]][bad_move[1]][bad_move[2]][2] = moves[bad_move[0]][bad_move[1]][bad_move[2]][2] - 10000         #Moverte a un espacio vacio y que te capturen es un movimiento PESIMO, por lo que restando 10000 nos aseguramos de que no sea elegido
    
    #FALTA UN EVENTO IMPORTANTE: SI EL RIVAL PUEDE COMERME UNA PIEZA Y ESA PIEZA PUEDE ATACARLA ANTES, SERIA BUENO QUE LO HAGA
    #PARA RESOLVERLO, NECESITAS---> pieza_que_me_pueden_capturar = moves_enemy[piece][0][movement][3][1] (con esto pasarias que pieza es la del rival)
    #con esa letra, deberia ir a un diccionario que tenga valores entre el 0 y 5 (igual que piece)
    #Tambien necesitas -----------> posicion_pieza_que_me_pueden_capturar = moves_enemy[piece][0][movement][1] (este seria el tuple al que me moveria para capturar == la posicion inicial de mi pieza)
    #finalmente, entro a -------->  moves[dict[pieza_que_me_pueden_capturar]][for entre 0 y 1(tenes que verificar que no este vacio esto creo)][movement][0] == posicion_pieza_que_me_pueden_capturar
    #si ocurre igualdad, tenes que terminar con---> moves[dict[pieza_que_me_pueden_capturar]][for entre 0 y 1(tenes que verificar que no este vacio esto creo)][movement][2] = moves[dict[pieza_que_me_pueden_capturar]][for entre 0 y 1(tenes que verificar que no este vacio esto creo)][movement][2]  + un valor agregado
    for piece_enemy in range(6):
        for movement in moves_enemy[piece_enemy][0]:
            start_sq = movement[0]
            end_sq   = movement[1]
            for my_piece in range(6):
                for movemento in moves[my_piece][0]:
                    if end_sq == movemento[0] and start_sq == movemento[1]:
                        movemento[2] = movemento[2] + valores_rival[movemento[3][1]] * 10 + valores_mios[movemento[3][0]] * 10 + 2000
 
    return moves




#Esta funcion evalua el valor de los peones rivales para la captura
#esto deberia ser un metodo de la clase pieza o peon
def peon_rival(fila, color):  
    if color == True:
        return valor_peon_black[fila]
    else:
        return valor_peon_white[fila]

#Esta funcion me da el valor del movimiento de un peon, el cual aumenta mientras mas cerca de coronar este
#esto deberia ser un metodo de la clase pieza o peon
def peon_propio(fila, color):
    if color == True:
        return valor_peon_white[fila]
    else:
        return valor_peon_black[fila]

#Actualiza el valor de las reinas dependiendo de la cantidad de estas que controle
#esto deberia ser un metodo de la clase pieza o reina
def reina(cantidad, color):

    valor = 120 - cantidad * 5
    if valor < 0:
        valor = 30
    if color == True:
        valores_mios["Q"] = valor
    else:
        valores_mios["q"] = valor