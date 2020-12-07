
def analizador_casilleros(moves,moves_enemy,color):
    board = [                                                                                      
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]

    board = move_sin_captura(moves, color, board)
    board = move_con_captura(moves, board)
    board = moves_enemy_sin_captura(moves_enemy, board)
    board = moves_enemy_con_captura(moves_enemy, board)
    board = evolucion(board)

    for line in board:
        print(line)

    return board



def move_sin_captura(moves, color, board):
    for piece in range(6):
        for movement in moves[piece][1]:
            if piece == 0:  #esto deberia ser una funcion
                start = movement[0]
                if color:                                       #esto esta mal
                    try:                                        #tenes que consultar si el espacio esta vacio antes de escribir +p, ya que puede estar ocupado por una pieza mia 
                        board[start[0]-1][start[1]+1] = "+p"    #(en si, no es un problema grave, no me puedo mover a ese + porque no va a estar en los movimientos posibles, pero el concepto de ilustracion esta mal)
                    except:
                        pass
                    try:    
                        board[start[0]-1][start[1]-1] = "+p"
                    except:
                        pass
                if not color:
                    try:
                        board[start[0]+1][start[1]+1] = "+p"
                    except:
                        pass
                    try:
                        board[start[0]+1][start[1]-1] = "+p"
                    except:
                        pass
            else:
                end = movement[1]
                board[end[0]][end[1]] = "+"
    return board

def move_con_captura(moves, board):
    for piece in range(6):
        for movement in moves[piece][0]:
            end = movement[1]

            if board[end[0]][end[1]] == "x":   
                board[end[0]][end[1]] = "xx"

            if board[end[0]][end[1]] == "+p":                        
                board[end[0]][end[1]] = "x"


            if board[end[0]][end[1]] == "xx":                        
                pass

            if board[end[0]][end[1]] == " ":                      #ESTO ES IMPORTANTISIMO QUE ESTE EN ULTIMA POSICION
                board[end[0]][end[1]] = "x"
    return board

def moves_enemy_sin_captura(moves_enemy, board):
    for piece in range(6):
        for movement in moves_enemy[piece][1]:
            end = movement[1]

            if board[end[0]][end[1]] == " ":  
                if piece == 0:                          
                    board[end[0]][end[1]] = "-p"
                else:                           
                    board[end[0]][end[1]] = "-"

            if board[end[0]][end[1]] == "+" or board[end[0]][end[1]] == "+p":      
                   
                board[end[0]][end[1]] = "#"

            if board[end[0]][end[1]] == "x" or board[end[0]][end[1]] == "xx":                         
                board[end[0]][end[1]] = "?"
    return board

def moves_enemy_con_captura(moves_enemy, board):
    for piece in range(6):
        for movement in moves_enemy[piece][0]:
            end = movement[1]

            if board[end[0]][end[1]] == "%":  
                board[end[0]][end[1]] = "%%"    

            if board[end[0]][end[1]] == "-p":                           
                board[end[0]][end[1]] = "%"

            if board[end[0]][end[1]] == "+":                           
                board[end[0]][end[1]] = "!"         #esto nunca va a ocurrir, voy a tener que analizar % sacando la pieza, si otra pieza mia cubre ese lugar con +, entonces evoluciono a !


            if board[end[0]][end[1]] == "%%":     
                pass

            if board[end[0]][end[1]] == " ":                          
                board[end[0]][end[1]] = "%"

    return board

#Esto tiene algun sentido aparte del visual???
def evolucion(board):                   #esto es optimizable, (podrias poner un continue despues de que se cumpla cada evento)
    for r in range(16): 
        for c in range(16):             #deberias poner continue si se da la condicion, asi no repetis tantas comparaciones..(pero la verdadera papa seria usar diccionario creo)
            
            if board[r][c] == "x":
                board[r][c] = "$"
                continue

            if board[r][c] == "xx":
                board[r][c] = "$$"
                continue

            if board[r][c] == "%":
                board[r][c] = "&"
                continue

            if board[r][c] == "%%":
                board[r][c] = "&&"
                continue

            if board[r][c] == "-p":
                board[r][c] = "-"
                continue

            if board[r][c] == "+p":
                board[r][c] = "+"
                continue

    return board

def eventos(board):
    tipos = [[],[],[]]
    for r in range(16):
        for c in range(16):
            if board[r][c] == "$$":
                tipos[0].append((r,c))
                continue

            if board[r][c] == "$":
                tipos[1].append((r,c))
                continue

            if board[r][c] == "?":
                tipos[2].append((r,c))
                continue
    
    return tipos

def finder(moves, buscado, encontrado, multiple):       #si multiple=True , esa pieza puede hacer mas de una captura
    tipo=0                                              #si multiple=False, esa pieza tiene una sola captura, por lo que se corta la iteracion y pasamos a otra
    x=False
    for buscar in buscado:
        for piece in range(6):
            for movement in moves[piece][tipo]:
                if  movement[1] == buscar:
                    encontrado.append(movement)

                    if multiple:
                        x=True
                        break
            if x:
                x=False
                break
    return encontrado



#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------PARCHE-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

valores_rival = {"h":5,"b":6 ,"r":7 ,"q":8 ,"k":9,    #Los valores de "p" y "P" los asisnamos con el diccionario que esta debajo
                 "H":5,"B":6 ,"R":7 ,"Q":8 ,"K":9}    

piece_number={"P":0 ,"H":1 ,"B":2 ,"R":3 ,"K":4 ,"Q":5,
              "p":0 ,"h":1 ,"b":2 ,"r":3 ,"k":4 ,"q":5}

#A los peones les incremento el valor respecto a que tan cerca de coronar estan
valor_peon_white = {13:0 ,12:1 ,11:2 ,10:3 ,9:4 ,8:5}         #row=8 ----> Coronacion (los peones nunca van a valer 5, porque en 5 coronan y como reinas valen 8)
valor_peon_black = {2: 0 ,3: 1 ,4: 2 ,5: 3 ,6:4 ,7:5}         #row=7 ----> Coronacion


#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

def analisis_capturas_limpias(lista_capturas_limpias):

    for movement in lista_capturas_limpias:
        if movement[3][1] == "P":
            movement[2] =  valor_peon_white[movement[1][0]]    #movement[2] +

        elif movement[3][1] == "p":
            movement[2] =  valor_peon_black[movement[1][0]]     #tambien tendrias que analizar en la suma la pieza con que te lo capturas, ya que si podes capturar por ej una reina infiltrada, es mejor hacerlo con un peon que con un rey

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


'''
def analisis_capturas_rival_contraataque(lista_capturas_rival, lista_capturas_sucias):
    moves_analysis = []
    for move_capture in lista_capturas_rival:
        start_sq = move_capture[1]

        for movement in lista_capturas_rival:
            if start_sq == movement[0]:
                end_sq = movement[1]

                movement[2] = movement[2] + valor_pieza_rival - valor_pieza_mia

                moves_analysis.append([start_sq, end_sq, movement[2]])

    return moves_analysis
'''

def analisis_capturas_rival_retirada(lista_capturas_rival, moves, board_eventos ,valor_row_strategy, moves_analysis):

    tipo = 1                                        #Voy a analizar mis movimientos a espacios vacios (retirada)

    for move_capture in lista_capturas_rival:       #Con el movimiento de captura del rival, busco mi pieza y los movimientos posibles de ella
        piece = piece_number[move_capture[3][1]]    #move_capture[3][1] es el string identificador de la pieza que me puede comer
        start_sq = move_capture[1]

        for movement in moves[piece][tipo]:
            if start_sq == movement[0]:
                end_sq = movement[1]
                if board_eventos[end_sq[0]][end_sq[1]] == "+" or board_eventos[end_sq[0]][end_sq[1]] == " ":
                    if piece == 5:
                        row = end_sq[0]
                        if 6 <= row <= 9:
                            movement[2] = movement[2] + valor_row_strategy[row] * 100
                            moves_analysis.append([start_sq ,end_sq ,movement[2]])


    return moves_analysis



    