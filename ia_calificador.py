'''
Almacena todas las funciones y herramientas para calificar los movimientos en el paso 2) de la ia.
'''
#-----------------------------------------------------------------------Settings---------------------------------------------------------------------------------

valores_rival = {"h":5 ,"b":6 ,"r":7 ,"q":8 ,"k":9,           #Los valores de "p" y "P" los asignamos con el diccionario "valor_peon"
                 "H":5 ,"B":6 ,"R":7 ,"Q":8 ,"K":9}    

valores_mios  = {"p":1 ,"h":5,"b":6 ,"r":7 ,"q":0 ,"k":90,    #Los valores de "p" y "P" los asignamos con el diccionario "valor_peon"
                 "P":1 ,"H":5,"B":6 ,"R":7 ,"Q":0 ,"K":90}  


piece_number={"P":0 ,"H":1 ,"B":2 ,"R":3 ,"K":4 ,"Q":5,       #Relacion entre int y string
              "p":0 ,"h":1 ,"b":2 ,"r":3 ,"k":4 ,"q":5}

#A los peones les incremento el valor respecto a que tan cerca de coronar estan
valor_peon = {13:0 ,12:1 ,11:2 ,10:3 ,9:4 ,8:5,         #row=8 ----> Coronacion (los peones nunca van a valer 5, porque en 5 coronan y como reinas valen 8)
              2: 0 ,3: 1 ,4: 2 ,5: 3 ,6:4 ,7:5}         #row=7 ----> Coronacion


#-----------------------------------------------------------------------Funciones--------------------------------------------------------------------------------

def analisis_capturas_limpias(lista_capturas_limpias):

    for movement in lista_capturas_limpias:
        if movement[3][1] == "P" or movement[3][1] == "p":
            movement[2] =  valor_peon[movement[1][0]]    #tambien tendrias que analizar en la suma la pieza con que te lo capturas, ya que si podes capturar por ej una reina infiltrada, es mejor hacerlo con un peon que con un rey
   
        else:
            movement[2] =  valores_rival[movement[3][1]]

    return lista_capturas_limpias

#busco si la posicion inicial de la pieza que puede hacer una captura limpia esta siendo atacada por el rival..si es asi y tengo una captura limpia contra ella, contraataco
def extra_capturas_limpias   (lista_capturas_rival, moves_analysis):
    
    for move_selected in moves_analysis:
        start_sq = move_selected[0]     #tuple con sq inicial

        for movement in lista_capturas_rival:
            if movement[1] == start_sq:
                move_selected[2] = move_selected[2] + 10  

                #break               #No estoy seguro que este bien esto, pero capaz no es tan importante tampoco y te ahorras mucho tiempo

    
    for move_mio in moves_analysis:
        x = (move_mio[0], move_mio[1])

        for move_rival in lista_capturas_rival:
            y = (move_rival[1],move_rival[0])

            if x == y:
                move_mio[2] = move_mio[2] + 100
 
    return moves_analysis

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def analisis_capturas_rival_retirada(lista_capturas_rival, moves, board_eventos ,valor_row_strategy, moves_analysis):
    tipo = 1                                        #Voy a analizar mis movimientos a espacios vacios (retirada)

    for move_capture in lista_capturas_rival:       #Con el movimiento de captura del rival, busco mi pieza y los movimientos posibles de ella
        piece = piece_number[move_capture[3][1]]    #move_capture[3][1] es el string identificador de la pieza que me puede comer
        if piece ==5:                               #las retiradas solo las analizo para reinas
            start_sq = move_capture[1]

            for movement in moves[piece][tipo]:
                if start_sq == movement[0]:
                    end_sq = movement[1]
                    end_row = end_sq[0]
                    if (board_eventos[end_sq[0]][end_sq[1]] == "+" or board_eventos[end_sq[0]][end_sq[1]] == " ") and  6 <= end_row <=9:
                        
                        if start_sq[0] == end_row:                                                  #esto es clave para movimientos de retirada en la misma fila(si estas en row tactical y te queres mover a otra columna dentro de la misma fila, antes te va a decir que ya tenes una reina ahi)
                            valor_row_strategy[end_row] = valor_row_strategy[end_row] +1
                            movement[2] =  valor_row_strategy[end_row] * 100
                            valor_row_strategy[end_row] = valor_row_strategy[end_row] -1

                        else:
                            movement[2] =  valor_row_strategy[end_row] * 100
                        

                        move_save = [start_sq ,end_sq ,movement[2]]
                        repeated = moves_analysis.count(move_save)

                        if movement[2] > 0 and repeated == 0:
                            
                            moves_analysis.append(move_save)

    return moves_analysis


def analisis_capturas_rival_contraataque(lista_capturas_rival, lista_capturas_sucias, moves_analysis):

    for move_capture in lista_capturas_rival:
        start_sq = move_capture[1]

        for movement in lista_capturas_sucias:
            if start_sq == movement[0]:
                end_sq = movement[1]
                
                if movement[3][1] == "p" or movement[3][1] == "P":
                    movement[2] = valor_peon[end_sq[0]] - valores_mios[movement[3][0]]
                else:
                    movement[2] = valores_rival[movement[3][1]] - valores_mios[movement[3][0]]

                move_save = [start_sq ,end_sq ,movement[2]]
                repeated = moves_analysis.count(move_save)

                if repeated == 0:                       # si no haces esto, pasa que cuando te pueden capturar con 2 piezas, sumas los mismos movimientos 2 veces, podes solucionarlo con esto o retocando la logica del for
                            
                    moves_analysis.append(move_save)

    return moves_analysis

def move_strategic(moves , board_eventos ,game ,moves_analysis):
    #si llegue aca, ya se que tengo al menos una reina propia en row_upgrade
    piece = 5
    tipo  = 1

    for movement in moves[piece][tipo]:
        start_sq  = movement[0]
        start_row = start_sq[0]
        end_sq    = movement[1]
        end_row   = end_sq[0]

        if 6 <= end_row <= 9 and start_row == game.row_upgrade_mia:  
            if game.qm_quantity_row_upgrade_mia >= 1 and (board_eventos[end_sq[0]][end_sq[1]] == "+" or board_eventos[end_sq[0]][end_sq[1]] == " ") and end_row == game.row_upgrade_rival:

                movement[2] = game.valor_row_strategy[end_row] * 100    #POR ACA HAY UN PROBLEMITA, NO ESTAS VERIFICANDO LA CANTIDAD DE REINAS QUE TENGO (CON MOVEMENT[2]>0, ENTONCES SEGUIR MOVIENDO SIN QUE TE IMPORTE NADA)
                move_save = [start_sq ,end_sq ,movement[2]]
                moves_analysis.append(move_save)
            elif game.qm_quantity_row_upgrade_mia >= 2 and (board_eventos[end_sq[0]][end_sq[1]] == "+" or board_eventos[end_sq[0]][end_sq[1]] == " ") and start_row != end_row:

                movement[2] = game.valor_row_strategy[end_row] * 100
                move_save = [start_sq ,end_sq ,movement[2]]
                moves_analysis.append(move_save)
            
    return moves_analysis