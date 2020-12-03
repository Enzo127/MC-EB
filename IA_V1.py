import ChessEngine_V1
import copy
#Aca vas a tener que crear otro objeto en lo posible

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
    #if cantidad < 4:                    #Capeo valores
    #    cantidad=4
    #elif cantidad > 10:
    #    cantidad=10

    #valor = valor_reina[cantidad]
    #valor = 10-cantidad*5
    valor = 80 - cantidad * 5
    if valor < 0:
        valor = 30
    if color == True:
        valores_mios["Q"] = valor
    else:
        valores_mios["q"] = valor

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
juegos_Ejecutandose = {}
#Asigno valores a mis piezas y a las del rival
valores_mios  = {"P":10 ,"H":50, "B":40,"R":60,"Q":70,"K":5,        #Los valores de peones y reinas los calculo con funciones arriba, debido a que sus valores dependen del estado del tablero (No hace falta que esten aca, nunca los buscas aca)
                 "p":10 ,"h":50, "b":40,"r":60,"q":70,"k":5}      

valores_rival = {"p":10,"h":40,"b":50,"r":70,"q":80,"k":300,
                 "P":10,"H":40,"B":50,"R":70,"Q":80,"K":300}

valor_peon_white = {13:10, 12:15 ,11:20 ,10:25 ,9:80 ,8:90}         #row=8 ----> Coronacion
valor_peon_black = {2:10  ,3:15  ,4:20  ,5:25  ,6:80 ,7:90}         #row=7 ----> Coronacion


#best_col_0 = {0:9 ,1:9 ,2:3 ,3:3 ,4:8 ,5:8 ,6:8 ,7:0 ,8:0 ,9:0 ,10:0 ,11:5 ,12:5 ,13:5 ,14:8 ,15:8}
#best_col_1 = {0:0 ,1:13 ,2:14 ,3:15 ,4:16 ,5:12 ,6:11 ,7:10 ,8:9 ,9:8 ,10:7 ,11:6 ,12:5 ,13:4 ,14:3 ,15:2}
#Peones cambian su valor dependiendo de la fila en la que se encuentran, las reinas varian su valor dependiendo de la cantidad de estas que tenga

#A esto hay que retocarlo y dejarlo mas flaco
def bot_inteligence(moves, moves_enemy, queens_quantity, color, game_Actual):  
    #ESTO PUEDE OCUPAR MUCHO TIEMPO, HAY MUCHISIMAS FORMAS DE HACER ESTA COPIA DE LA LISTA, ALGUNAS CUESTAN FRACCIONES DE SEG Y OTRAS LLEGAN A TOMAR MUCHO MAS, INVESTIGALO
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
                    #Logica de peones: Mientras mas cerca de la coronacion este, mas valioso es el movimiento
                    '''
                    if piece == 3:
                        if (queens_quantity < 10) and color:
                            movement[2] = movement[2] + peon_propio(movement[1][0], color) + best_col_0[movement[1][1]] + 450
                        elif (queens_quantity < 10) and not color:
                            movement[2] = movement[2] + peon_propio(movement[1][0], color) + best_col_1[movement[1][1]] + 450
                        else:
                            movement[2] = movement[2] + peon_propio(movement[1][0], color) + best_col_0[movement[1][1]] + 50
                        #movement[2] = movement[2] + peon_propio(movement[1][0], color) + best_col[movement[1][1]] + 100  #esto es provisorio, pero la idea es que, si tenes pocas reinas, conviene mucho seguir coronando para controlar el centro
                    '''
                    if piece == 3:
                        if (queens_quantity < 14) and color:
                            movement[2] = movement[2] + peon_propio(movement[1][0], color) + game_Actual.best_col[movement[1][1]] + 450
                        elif (queens_quantity < 14) and not color:
                            movement[2] = movement[2] + peon_propio(movement[1][0], color) + game_Actual.best_col[movement[1][1]] + 450
                        else:
                            movement[2] = movement[2] + peon_propio(movement[1][0], color) + game_Actual.best_col[movement[1][1]] + 50
                        #movement[2] = movement[2] + peon_propio(movement[1][0], color) + best_col[movement[1][1]] + 100  #esto es provisorio, pero la idea es que, si tenes pocas reinas, conviene mucho seguir coronando para controlar el centro




                    if piece == 5:
                        movement[2] = movement[2] + 10
                    if piece == 2:
                        movement[2] = movement[2] + 1
                    #Logica de reinas: Si se puede mover hacia la fila de coronacion contraria, es un movimiento valioso
                    '''
                    elif piece == 4:    #esto lo podria hacer una funcion, de la misma forma en que lo haces arriba con el peon // CLAVE 
                        
                        if color == True:
                            best_row = 7       #La fila 7 es la mejor posicion para las reinas blancas (fila de coronacion del rival)
                            alternative_row = 6
                        else:
                            best_row = 8       #La fila 8 es la mejor posicion para las reinas negras (fila de coronacion del rival)
                            alternative_row = 9
                        
                        if queens_quantity < 8 :
                            if (movement[1][0] == best_row) and (movement[0][0] != best_row) and (movement[0][0] != alternative_row):      #movement[1] = end_sq    // movement[1][0] = fila del end_sq
                                movement[2] = movement[2] + 1000               #Si la fila a la que moveria es la de coronacion rival, añado puntos de valor (este tiene que ser mayor que los movimientos de tus peones(es mas valiosos controlar la fila de coronacion rival que coronar peones propios))
                            elif (movement[1][0] == alternative_row) and (movement[0][0] != best_row) and (movement[0][0] != alternative_row):
                                movement[2] = movement[2] + 100
                    '''    
                    i=i+1


    #Esta podria ser otra funcion, en la cual pasas 
    for piece in range(6):
        for tipo in range(2):
            if tipo ==0:
                #Movimientos del rival con captura
                for movemento in moves_enemy[piece][tipo]:
                    if len(tablero[movemento[1][0]][movemento[1][1]]) != 0:            
                        for capture_move in tablero[movemento[1][0]][movemento[1][1]]:                           
                            if len(capture_move) == 4: #la lista tiene 5 posiciones SOLO si ya se ha analizado la recaptura por parte del rival                            
                                moves[capture_move[0]][capture_move[1]][capture_move[2]][2] = moves[capture_move[0]][capture_move[1]][capture_move[2]][2] - valores_mios[moves[capture_move[0]][capture_move[1]][capture_move[2]][3][0]] * 10                           
                                capture_move.append("visado")       #Esto sirve para no restar 2 veces el valor de una captura(la pieza aunque me la puedan capturar varias piezas, la capturan una sola vez)            
            else:
                #Movimientos del rival a espacios vacios
                for movemento in moves_enemy[piece][tipo]:
                    if len(tablero[movemento[1][0]][movemento[1][1]]) != 0:             
                        for bad_move in tablero[movemento[1][0]][movemento[1][1]]:
                            if bad_move[0] == 3:
                                pass
                            else:
                                moves[bad_move[0]][bad_move[1]][bad_move[2]][2] = moves[bad_move[0]][bad_move[1]][bad_move[2]][2] - 10000         #Moverte a un espacio vacio y que te capturen es un movimiento PESIMO, por lo que restando 1000 nos aseguramos de que no sea elegido
    
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

def comparacion(moves):
    comparacion = None
    
    best_move = []
    for piece in range(6):
        for tipo in range(2):
            for movimiento_final in moves[piece][tipo]:
                if comparacion is None:
                    comparacion = movimiento_final[2]
                    best_move = movimiento_final

                elif movimiento_final[2] > comparacion:
                    comparacion = movimiento_final[2]
                    best_move = movimiento_final
    
    return best_move

def limpiar(id_vieja):
    juegos_Ejecutandose.pop(id_vieja)


#def bot_work(juego_actual, refresh, turno):
def bot_work(id_Actual, refresh, turno):    
    moves   = []
    moves_enemy = []

    #Recibir id_game, verificar si el juego existe (en un dicionario por ej, con key=id_game), si no existe, crearlo
    #1) Accedo al juego en cuestion mediante la id unica de cada partida (Aca hay un errorcito groso que sucede cuando jugas contra vos mismo (creas el juego y asignas un color, pero los 2 accedemos con el mismo color))
    #para solucionar el bug cuando jugas contra vos mismo, deberias verificar username == opponent_username, Si es asi, cambia el color por cada jugada 
    juego_actual = juegos_Ejecutandose.get(id_Actual)
    if juego_actual is None:
        print ("Inicia el juego")
        print("id_game: {}".format(id_Actual))
        number = ChessEngine_V1.Game_State(turno)
        juegos_Ejecutandose.update({id_Actual:number})
        juego_actual = juegos_Ejecutandose.get(id_Actual)
    
    #2)Actualizar el tablero
    juego_actual.Actualizar(refresh)

    #2.5)Actualizar estado columnas
    juego_actual.columna_Rating()

    #3)Obtencion de movimientos propios y del rival
    change=0                                                       #Obtengo una lista con todos los movimientos validos posibles que puedo realizar
    moves       = juego_actual.get_All_Possible_Moves(change)      #change=0 ----> Me devuelve una lista con mis movimientos validos posibles           (para el estado actual del tablero)
            
    change=1                                                       #Obtengo una lista con todos los movimientos validos posibles del rival
    moves_enemy = juego_actual.get_All_Possible_Moves(change)      #change=1 ----> Me devuelve una lista con los movimientos validos posibles del rival (para el estado actual del tablero)
    
    #4)Calificar los movimientos obtenidos
    moves_analized = bot_inteligence(moves, moves_enemy, juego_actual.queens_Quantity, turno, juego_actual)       #Asigno un valor a cada movimiento
    juego_actual.queens_Quantity = 0                                                                #reseteo el nro de reinas luego de evaluar los movimientos
    
    #5)Obtencion del mejor movimiento respecto a la calificacion otorgada 
    return comparacion(moves_analized)



                
