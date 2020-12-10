'''
Almacena todas las funciones y herramientas para calificar los movimientos en el paso 2) de la ia.
'''
#-----------------------------------------------------------------------Settings---------------------------------------------------------------------------------
row_clean_capture_white = {0:9 ,1:9 ,2:9    ,3:1 ,4:2 ,5:3 ,6:3 ,7:7 ,8:7 ,9:4 ,10:5     ,11:6 ,12:6        ,13:8 ,14:8 ,15:8}
row_clean_capture_black = {0:8 ,1:8 ,2:8    ,3:6 ,4:6 ,5:5 ,6:4 ,7:7 ,8:7 ,9:3 ,10:3     ,11:1 ,12:2        ,13:9 ,14:9 ,15:9}

valores_rival = {"h":5 ,"b":6 ,"r":7 ,"q":8 ,"k":9,           #Los valores de "p" y "P" los asignamos con el diccionario "valor_peon"
                 "H":5 ,"B":6 ,"R":7 ,"Q":8 ,"K":9}    

valores_mios  = {"p":1 ,"q":2 ,"b":3 ,"h":4 ,"r":5 ,"k":9,    #Los valores de "p" y "P" los asignamos con el diccionario "valor_peon"
                 "P":1 ,"Q":2 ,"B":3 ,"H":4 ,"R":5 ,"K":9}  


piece_number={"P":0 ,"H":1 ,"B":2 ,"R":3 ,"K":4 ,"Q":5,       #Relacion entre int y string
              "p":0 ,"h":1 ,"b":2 ,"r":3 ,"k":4 ,"q":5}

#A los peones les incremento el valor respecto a que tan cerca de coronar estan
valor_peon = {13:0 ,12:1 ,11:2 ,10:3 ,9:4 ,8:5,         #row=8 ----> Coronacion (los peones nunca van a valer 5, porque en 5 coronan y como reinas valen 8)
              2: 0 ,3: 1 ,4: 2 ,5: 3 ,6:4 ,7:5}         #row=7 ----> Coronacion


#-----------------------------------------------------------------------Funciones--------------------------------------------------------------------------------
#Añade un valor a la captura dependiendo la pieza rival (realizar una captura limpia sobre un rey es mas valioso que sobre un alfil)
def capturas_limpias(lista_capturas_limpias):  
    for movement in lista_capturas_limpias:
        end_row     = movement[1][0]
        piece_mine  = movement[3][0]
        piece_rival = movement[3][1]

        if piece_mine.isupper():
            movement[2] = row_clean_capture_white[end_row] * 10
        else:
            movement[2] = row_clean_capture_black[end_row] * 10

        if movement[3][1] == "P" or movement[3][1] == "p":  #Para los peones asigno un valor dependiendo la fila en que esten (mas cerca de coronar es mas valioso)
            movement[2] = movement[2] + valor_peon[movement[1][0]] + (10-valores_mios[piece_mine])     #tambien tendrias que analizar en la suma la pieza con que te lo capturas, ya que si podes capturar por ej una reina infiltrada, es mejor hacerlo con un peon que con un rey

        else:
            movement[2] = movement[2] + valores_rival[piece_rival] + (10-valores_mios[piece_mine])     #Las demas piezas tienen valores fijos

    return lista_capturas_limpias


'''
#Analizo si hay una pieza enemiga atacando a mi pieza que dispone de una captura limpia y si ocurre, añado (+1) (añade +1 por CADA pieza rival que la ataque)
def extra_capturas_limpias   (lista_capturas_rival, lista_capturas_limpias):   
                                                                
    for move_selected in lista_capturas_limpias:            
        start_sq_mine = move_selected[0]     #tuple con sq inicial
        end_sq_mine   = move_selected[1]

        for movement in lista_capturas_rival:
            start_sq_rival = movement[0]
            end_sq_rival   = movement[1]

            if start_sq_mine == end_sq_rival and end_sq_mine  ==  start_sq_rival:   #Si mi captura limpia tiene como objetivo una pieza rival que me esta atacando ------> +10 de valor agregado
                move_selected[2] = move_selected[2] + 2000 

            elif start_sq_mine == end_sq_rival:               #Si el start_sq de mi pieza == al end_sq de una captura rival, entonces me conviene moverme con esta pieza para que no me capture
                move_selected[2] = move_selected[2] + 1000     #Condicion valida -----> +1 de valor agregado



    return lista_capturas_limpias
'''


def capturas_rival_retirada(lista_capturas_rival, moves, board_eventos ,qq_row_strategy ,valor_row_strategy, moves_analysis):
    tipo = 1                                        #Voy a analizar mis movimientos a espacios vacios (retirada)
    
    for move_capture in lista_capturas_rival:       #Con el movimiento de captura del rival, busco mi pieza y los movimientos posibles de ella
        piece = piece_number[move_capture[3][1]]    #move_capture[3][1] es el string identificador de la pieza que me puede comer
        if piece ==5:                               #las retiradas solo las analizo para reinas
            start_sq = move_capture[1]
            for movement in moves[piece][tipo]:
                if start_sq == movement[0]:
                    end_sq = movement[1]
                    end_row = end_sq[0]

                    if start_sq[0] == end_row:      #Consulto si la pieza quedaria en la misma fila (importante para elegir la fila estrategica de retirada)
                        move_in_same_row = 1
                    else:
                        move_in_same_row = 0

                    quantity = qq_row_strategy.get(end_row)         #Verifico que end_row esta dentro de las row_stretegy y que no haya mas de una reina propia en esa fila   
                    if quantity != None:
                        quantity = quantity -move_in_same_row
                    
                    if (board_eventos[end_sq[0]][end_sq[1]] == "+" or board_eventos[end_sq[0]][end_sq[1]] == " ") and  quantity == 0:
                        
                        movement[2] = valor_row_strategy[end_row] 
                        
                        move_save = [start_sq ,end_sq ,movement[2]]
                        repeated = moves_analysis.count(move_save)

                        if movement[2] > 0 and repeated == 0:
                            
                            moves_analysis.append(move_save)

    return moves_analysis


def capturas_rival_contraataque(lista_capturas_rival, lista_capturas_sucias, moves_analysis):
    for move_capture in lista_capturas_rival:
        start_sq = move_capture[1]

        for movement in lista_capturas_sucias:
            if start_sq == movement[0]:
                end_sq = movement[1]
                
                if movement[3][1] == "p" or movement[3][1] == "P":
                    movement[2] = valor_peon[end_sq[0]] - valores_mios[movement[3][0]]
                else:
                    movement[2] = valores_rival[movement[3][1]] - valores_mios[movement[3][0]]

                if movement[2] > 0:
                    move_save = [start_sq ,end_sq ,movement[2]]
                    repeated = moves_analysis.count(move_save)

                    if repeated == 0:                       # si no haces esto, pasa que cuando te pueden capturar con 2 piezas, sumas los mismos movimientos 2 veces, podes solucionarlo con esto o retocando la logica del for
                                
                        moves_analysis.append(move_save)

    return moves_analysis

def move_strategic(moves ,board_eventos ,data_row_upgrade ,qq_row_strategy ,valor_row_strategy, retaguardia_mia ,moves_analysis):

    for movement in moves:
        start_sq  = movement[0]
        end_sq    = movement[1]

        start_row = start_sq[0]
        end_row   = end_sq[0]
        #print("LLEGUE ACA?")
        #if (start_row == data_row_upgrade[0] and end_row != start_row):
        if (start_row == data_row_upgrade[0] and end_row != start_row) or start_row==retaguardia_mia[0] or start_row==retaguardia_mia[1]:
            
            if  board_eventos[end_sq[0]][end_sq[1]] == "+" or board_eventos[end_sq[0]][end_sq[1]] == " ":
                
                result = qq_row_strategy.get(end_row)
                if result is None or result >= 1:
                    continue
                
                if data_row_upgrade[1] ==1:
                    movement[2] = valor_row_strategy[end_row] - valor_row_strategy[data_row_upgrade[0]]
                    if movement[2] > 0:
                        move_save = [start_sq ,end_sq ,movement[2]]
                        moves_analysis.append(move_save)
                else:
                    movement[2] = valor_row_strategy[end_row]
                    move_save = [start_sq ,end_sq ,movement[2]]
                    moves_analysis.append(move_save)

    return moves_analysis


def queen_infiltrated(lista_capturas_sucias ,retaguardia_rival ,moves_analysis, infiltracion):   #Si infiltracion=True, consulto solo por reinas infiltradas, si es False, consulto por reinas que se puedan infiltrar
    x = 1

    for movement in lista_capturas_sucias:
        start_sq = movement[0]
        end_sq   = movement[1]

        start_row = movement[0][0]
        end_row   = movement[1][0]

        if infiltracion:
            x = retaguardia_rival.count(start_row)
        y = retaguardia_rival.count(end_row)

        if x!=0 and y!=0:
            movement[2] = valores_rival[movement[3][1]]
            move_save = [start_sq ,end_sq ,movement[2]]
            moves_analysis.append(move_save)

    return moves_analysis



def peon_avance (moves, game):
    piece = 0
    tipo  = 1
    moves_selected = []

    #esto se reescribe siempre, lo podrias intentar meter en game, asi no lo reescribis en cada llamada a esta funcion
    if game.color == True:
        valor_peon = {13:10, 12:25 ,11:30 ,10:35 ,9:75 ,8:90}         #row=8 ----> Coronacion

    else:
        valor_peon = {2:10  ,3:25  ,4:30  ,5:35  ,6:75 ,7:90}         #row=7 ----> Coronacion


    for movement in moves[piece][tipo]:
        movement[2] = valor_peon[movement[1][0]] + game.best_col[movement[1][1]]  #para probar, saque movement[2] de la suma(no acarreo valores pasados, fijate si lo queres asi)
        moves_selected.append(movement)
                       
    return moves_selected