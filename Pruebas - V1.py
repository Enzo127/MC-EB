import asyncio
import websockets
import json
import tablero
import random
import copy

turno = '''{
"event": "your_turn", 
"data": 
{
"board_id": "7d9d90e6-d6ca-443d-9106-86a022337758", 
"turn_token": "0a6c0b38-90d1-40bd-b4e0-1c5528d2de57", 
"username": "Ulrazen", 
"actual_turn": "white", 
"board":      "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR",
"board_test": "rrhhbbqqkkbbhhrrrrhhbbqqkkbbHhrrpppppppppppppppppppppppppppppppp                                                                                                                                PHQBHPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQQQBBHHRR", 
"testing_1":  "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppp ppppppppppppppp                                                                                 P                          P     PPPPP  PP           PPPPPP PPPqPPPPP PP  PPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR",
"testing_2":  "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                b     Q    r                                h        K          R B                      PP P     qPPPPPP  P PPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR",
"move_left": 199, 
"opponent_username": "EnzoC"}
}'''




x = json.loads(turno)
actual = x["data"]["board_test"]
print(x["data"])

def peon_rival(fila, color):  
    if color == "white":
        return valor_peon_black[fila]
    else:
        return valor_peon_white[fila]

#Esta funcion me da el valor del movimiento de un peon, el cual aumenta mientras mas cerca de coronar este
#esto deberia ser un metodo de la clase pieza o peon
def peon_propio(fila, color):
    if color == "white":
        return valor_peon_white[fila]
    else:
        return valor_peon_black[fila]

#Actualiza el valor de las reinas dependiendo de la cantidad de estas que controle
#esto deberia ser un metodo de la clase pieza o reina
def reina(cantidad, color):
    valor = 90-cantidad*5
    
    if valor < 0:
        valor = 20
    
    print("Valor de la reina:",valor)
    if color == "white":
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

#Asigno valores a mis piezas y a las del rival
valores_mios  = {"P":10 ,"H":1, "B":40,"R":60,"Q":70,"K":200,        #Los valores de peones y reinas los calculo con funciones arriba, debido a que sus valores dependen del estado del tablero (No hace falta que esten aca, nunca los buscas aca)
                 "p":10 ,"h":1, "b":40,"r":60,"q":70,"k":200}      

valores_rival = {"p":10,"h":40,"b":60,"r":70,"q":150,"k":200,
                 "P":10,"H":40,"B":60,"R":70,"Q":150,"K":200}

valor_peon_white = {13:10, 12:20 ,11:30 ,10:50 ,9:80,8:90}        #row=8 ----> Coronacion
valor_peon_black = {2:10  ,3:20  ,4:30  ,5:50  ,6:80,7:100}        #row=7 ----> Coronacion

best_col = {0:9 ,1:9 ,2:3 ,3:3 ,4:8 ,5:8 ,6:8 ,7:1 ,8:1 ,9:1 ,10:1 ,11:5 ,12:5 ,13:5 ,14:9 ,15:9}

#Peones cambian su valor dependiendo de la fila en la que se encuentran, las reinas varian su valor dependiendo de la cantidad de estas que tenga
color = "whit"
game = tablero.game("white" == "whie")
game.Actualizar(actual)

game.board = [
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'R', 'H', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', ' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['k', 'B', 'q', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' '],
            ['Q', ' ', ' ', ' ', ' ', 'h', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', 'K', ' ', ' ', ' '],
            ['r', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'h', ' ', ' ', ' ', 'r', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'k', 'P', 'P', 'P', 'P', 'q', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'r'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]


for line in game.board:
    print(line)


change=0
moves = game.get_All_Possible_Moves(change)
change=1
moves_enemy = game.get_All_Possible_Moves(change)

empieza=1
#Almaceno los movimientos PROPIOS posibles
if empieza ==1:
    #ESTO PUEDE OCUPAR MUCHO TIEMPO, HAY MUCHISIMAS FORMAS DE HACER ESTA COPIA DE LA LISTA, ALGUNAS CUESTAN FRACCIONES DE SEG Y OTRAS LLEGAN A TOMAR MUCHO MAS, INVESTIGALO
    tablero = copy.deepcopy(Arreglo)               #Cada vez que llamo a esta funcion, empiezo trabajando con un arreglo limpio
    reina(game.queens_Quantity, color)
    for piece in range(6):
        for tipo in range(2):
            i=0
            #ANALIZO MOVIMIENTOS CON CAPTURAS
            if tipo==0:                 #Logica para capturas
                #Mis Movimientos
                for movement in moves[piece][tipo]:      
                    tablero[movement[1][0]][movement[1][1]].append([piece,tipo,i,movement[3]])      #Como aca analizo capturas, tambien debo agregar el termino movement[3] // ej: Rr: Mi torre captura torre rival
                    
                    if movement[3][1] == "P" or movement[3][1] == "p":
                        movement[2] = peon_rival(movement[1][0], color) * 10
                    
                    else:
                        movement[2] = valores_rival[movement[3][1]] * 10                               #movement[3][0] = la pieza con la que yo capture // movement[3][1] la pieza que capture

                    i=i+1
                #Movimientos del rival
                #for movemento in moves_enemy[piece][tipo]:
                #    if len(tablero[movemento[1][0]][movemento[1][1]]) != 0:            
                #        for capture_move in tablero[movemento[1][0]][movemento[1][1]]:                           
                #            if len(capture_move) == 4: #la lista tiene 5 posiciones SOLO si ya se ha analizado la recaptura por parte del rival                            
                #                moves[capture_move[0]][capture_move[1]][capture_move[2]][2] = moves[capture_move[0]][capture_move[1]][capture_move[2]][2] - valores_mios[moves[capture_move[0]][capture_move[1]][capture_move[2]][3][0]] * 15 +1                            
                #                capture_move.append("visado")       #Esto sirve para no restar 2 veces el valor de una captura(la pieza aunque me la puedan capturar varias piezas, la capturan una sola vez)
            i=0 #innecesario
            #ANALIZO MOVIMIENTOS A ESPACIOS LIBRES
            if tipo==1:                 #Logica para movimientos a espacios vacios
                #ANALIZO MIS MOVIMIENTOS
                for movement in moves[piece][tipo]:               
                    tablero[movement[1][0]][movement[1][1]].append([piece,tipo,i])  #agrego al tablero una lista con [pieza a la que me refiero][tipo: 0=movimiento con captura / 1=movimiento a espacio vacio][lugar en la lista "moves"]
                    #Logica de peones: Mientras mas cerca de la coronacion este, mas valioso es el movimiento
                    if piece == 3:
                        if game.queens_Quantity < 8:
                            movement[2] = movement[2]+450   #esto es provisorio, pero la idea es que, si tenes pocas reinas, conviene mucho seguir coronando para controlar el centro
                        movement[2] = movement[2] + peon_propio(movement[1][0], color)
            
                    #Logica de reinas: Si se puede mover hacia la fila de coronacion contraria, es un movimiento valioso
                    elif piece == 4:    #esto lo podria hacer una funcion, de la misma forma en que lo haces arriba con el peon // CLAVE 
                        
                        if color == "white":
                            best_row = 7       #La fila 7 es la mejor posicion para las reinas blancas (fila de coronacion del rival)
                            alternative_row = 6
                        else:
                            best_row = 8       #La fila 8 es la mejor posicion para las reinas negras (fila de coronacion del rival)
                            alternative_row = 9
                        
                        if game.queens_Quantity < 8 :
                            if (movement[1][0] == best_row) and (movement[0][0] != best_row) and (movement[0][0] != alternative_row):      #movement[1] = end_sq    // movement[1][0] = fila del end_sq
                                movement[2] = movement[2] + 1000               #Si la fila a la que moveria es la de coronacion rival, añado puntos de valor (este tiene que ser mayor que los movimientos de tus peones(es mas valiosos controlar la fila de coronacion rival que coronar peones propios))
                            elif (movement[1][0] == alternative_row) and (movement[0][0] != best_row) and (movement[0][0] != alternative_row):
                                movement[2] = movement[2] + 500

                    #else:   #Esta linea mepa que no deberia ir (la papa seria que solo los peones y reinas hagas movimientos a espacios libres para tactica, las demas piezas solo deberian capturar en lo posible(AL MENOS COMO PRIMER BOSQUEJO DE IA))
                    #    if color == "white":
                    #        movement[2] = movement[2] + valores_white[valor_pieza[piece]]                        #Guardo el valor del movimiento en movement                    //ESTA LINEA ESTA A MODO DE PRUEBA, ESTA INCOMPLETA
                    #    else:
                    #        movement[2] = movement[2] + valores_black[valor_pieza[piece]]      
                    i=i+1

                #ANALIZO LOS MOVIMIENTOS DEL RIVAL
                #for movemento in moves_enemy[piece][tipo]:
                #    if len(tablero[movemento[1][0]][movemento[1][1]]) != 0:             
                #        for bad_move in tablero[movemento[1][0]][movemento[1][1]]:
                #            moves[bad_move[0]][bad_move[1]][bad_move[2]][2] = moves[bad_move[0]][bad_move[1]][bad_move[2]][2] -10000         #Moverte a un espacio vacio y que te capturen es un movimiento PESIMO, por lo que restando 1000 nos aseguramos de que no sea elegido
           


    for piece in range(6):
        for tipo in range(2):
#Movimientos del rival
            if tipo == 0:
                for movemento in moves_enemy[piece][tipo]:
                    if len(tablero[movemento[1][0]][movemento[1][1]]) != 0:            
                        for capture_move in tablero[movemento[1][0]][movemento[1][1]]:                           
                            if len(capture_move) == 4: #la lista tiene 5 posiciones SOLO si ya se ha analizado la recaptura por parte del rival                            
                                moves[capture_move[0]][capture_move[1]][capture_move[2]][2] = moves[capture_move[0]][capture_move[1]][capture_move[2]][2] - valores_mios[moves[capture_move[0]][capture_move[1]][capture_move[2]][3][0]] * 15 +1                            
                                capture_move.append("visado")       #Esto sirve para no restar 2 veces el valor de una captura(la pieza aunque me la puedan capturar varias piezas, la capturan una sola vez)            
            else:
                for movemento in moves_enemy[piece][tipo]:
                    if len(tablero[movemento[1][0]][movemento[1][1]]) != 0:             
                        for bad_move in tablero[movemento[1][0]][movemento[1][1]]:
                            moves[bad_move[0]][bad_move[1]][bad_move[2]][2] = moves[bad_move[0]][bad_move[1]][bad_move[2]][2] -10000         #Moverte a un espacio vacio y que te capturen es un movimiento PESIMO, por lo que restando 1000 nos aseguramos de que no sea elegido
    '''
    for piece_enemy in range(6):
        for movement in moves_enemy[piece_enemy][0]:
            start_sq = movement[0]
            for my_piece in range(6):
                for movemento in moves[my_piece][0]:
                    if start_sq == movemento[0]:
                        movemento[2] = movemento[2] + valores_rival[movemento[3][1]] * 5
    '''

#game.turn = False
#moves_enemy = game.get_All_Possible_Moves(0)

for piece in range(6):
    for movement in moves_enemy[piece][0]:
        end_sq = movement[1]
        start_sq = movement[0]
        for my_piece in range(6):
            for movemento in moves[my_piece][0]:
                if end_sq==movemento[0] and start_sq==movemento[1]:
                    movemento[2] = movemento[2] + valores_rival[movemento[3][1]] * 5
                    
i=0
comparacion = 10
best_move = []
for piece in range(6):
    for tipo in range(2):
        for movimiento_final in moves[piece][tipo]:
            if movimiento_final[2] > comparacion:
                comparacion = movimiento_final[2]
                best_move = movimiento_final
print()
print(best_move)


'''
print("captures knight:",moves[0][0])
print("captures knight:",len(moves[0][0]))
print()
print("free space knight:",moves[0][1])
print("free space knight:",len(moves[0][1]))
print()
'''
print("captures bishop:",moves[1][0])
print("captures: bishop",len(moves[1][0]))
print()
print("free space bishop:",moves[1][1])
print("free space bishop:",len(moves[1][1]))
print()
'''
print("captures Rook:",moves[2][0])
print("captures Rook:",len(moves[2][0]))
print()
print("free space Rook:",moves[2][1])
print("free space Rook:",len(moves[2][1]))
print()

print("captures pawn:",moves[3][0])
print("captures pawn:",len(moves[3][0]))
print()
print("free space pawn:",moves[3][1])
print("free space pawn:",len(moves[3][1]))

print()
print("captures queen:",moves[4][0])
print("captures queen:",len(moves[4][0]))

print()
print("free space queen:",moves[4][1])
print("free space queen:",len(moves[4][1]))

print()
print("captures King:",moves[5][0])
print("captures King:",len(moves[5][0]))
print()
print("free space King:",moves[5][1])
print("free space King:",len(moves[5][1]))

print(moves)
print(len(moves))
'''
#for line in game.board:
#    print(line)
