'''
Almacena todas las funciones y herramientas para calificar los movimientos en el paso 2) de la ia.
'''
#Dependiendo la fila, las capturas tienen un mayor valor agregado
row_clean_capture_white = {0:8 ,1:8 ,2:8 ,3:1 ,4:2 ,5:3 ,6:3 ,7:7 ,8:7 ,9:4 ,10:5 ,11:6 ,12:6 ,13:9 ,14:9 ,15:9}  
row_clean_capture_black = {0:9 ,1:9 ,2:9 ,3:6 ,4:6 ,5:5 ,6:4 ,7:7 ,8:7 ,9:3 ,10:3 ,11:1 ,12:2 ,13:8 ,14:8 ,15:8}

valores_rival = {"h":5 ,"b":6 ,"r":7 ,"q":8 ,"k":9,           #Los valores de "p" y "P" los asignamos con el diccionario "valor_peon"
                 "H":5 ,"B":6 ,"R":7 ,"Q":8 ,"K":9}    

valores_mios  = {"p":1 ,"q":7 ,"b":5 ,"h":3 ,"r":7 ,"k":9,    #Los valores de "p" y "P" los asignamos con el diccionario "valor_peon"
                 "P":1 ,"Q":7 ,"B":5 ,"H":3 ,"R":7 ,"K":9}  


piece_number={"P":0 ,"H":1 ,"B":2 ,"R":3 ,"K":4 ,"Q":5,       #Relacion entre int y string
              "p":0 ,"h":1 ,"b":2 ,"r":3 ,"k":4 ,"q":5}

#A los peones les incremento el valor respecto a que tan cerca de coronar estan
valor_peon = {13:0 ,12:1 ,11:2 ,10:3 ,9:4 ,8:5,         #row=8 ----> Coronacion (los peones nunca van a valer 5, porque en 5 coronan y como reinas valen 8)
              2: 0 ,3: 1 ,4: 2 ,5: 3 ,6:4 ,7:5}         #row=7 ----> Coronacion


#Actualiza el valor de mis reinas, mientras mas reinas tengo menor es su valor
def queen_value(queens_quantity):
    valor = 10 - queens_quantity
    if valor <= 0:
        valor = 2
    valores_mios["q"] = valor
    valores_mios["Q"] = valor


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

#Si tengo una pieza bajo ataque y esa pieza se puede mover a un casillero sin eventos peligrosos, se mueve esquivando el ataque
#La retirada esta habilitada para todas las piezas excepto el caballo y alfil (piece=1 and piece=2)
def capturas_rival_retirada(lista_capturas_rival, moves, board_eventos ,qq_row_strategy ,valor_row_strategy  ,moves_analysis):
    tipo = 1                                        #Voy a analizar mis movimientos a espacios vacios (retirada)
    for move_capture in lista_capturas_rival:       #Con el movimiento de captura del rival, busco mi pieza y los movimientos posibles de ella
        start_sq = move_capture[1]
        piece_str = move_capture[3][1]
        piece_int = piece_number[piece_str]    #move_capture[3][1] es el string identificador de la pieza que me puede comer
        
        for movement in moves[piece_int][tipo]:
            if start_sq == movement[0]:
                end_sq = movement[1]
                start_row = start_sq[0]
                end_row = end_sq[0]
                end_col = end_sq[1]

                #Peones
                if piece_int == 0 and ((start_row>4 and piece_str.islower()) or (start_row<11 and piece_str.isupper())) and (board_eventos[end_row][end_col]==" " or board_eventos[end_row][end_col]=="+") :
                    movement[2] = movement[2] + valor_peon[end_row]
                    move_save = [start_sq ,end_sq ,movement[2]]
                    moves_analysis.append(move_save)
                #Torres y reyes 
                if  2 < piece_int < 5 and (board_eventos[end_row][end_col]==" " or board_eventos[end_row][end_col]=="+"):
                    movement[2] = movement[2] + valores_mios[move_capture[3][1]]
                    move_save = [start_sq ,end_sq ,movement[2]]
                    moves_analysis.append(move_save)
                #Reinas
                if piece_int ==5:                   #Logica de reinas
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

#El rival me puede capturar una pieza, respondo contraatacando(y me expongo a que me recapturar) solo si el valor de mi pieza es menor que el de la pieza rival
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

                if movement[2] >= 0:
                    move_save = [start_sq ,end_sq ,movement[2]]
                    repeated = moves_analysis.count(move_save)
                    if repeated == 0: 
                                
                        moves_analysis.append(move_save)
    return moves_analysis

#Muevo las reinas de mi casilla de upgrade o de la retaguardia a filas estrategicas en las que apliquen mayor presion
def move_strategic(moves ,board_eventos ,data_row_upgrade ,qq_row_strategy ,valor_row_strategy ,row_strategy ,retaguardia_mia ,moves_analysis):
    for movement in moves:
        start_sq  = movement[0]
        end_sq    = movement[1]

        start_row = start_sq[0]
        end_row   = end_sq[0]
        end_col   = end_sq[1]

        result = qq_row_strategy.get(end_row)
        if result is None:  #Si es None, significa que la fila destino no es estrategica
            continue
        if (start_row == data_row_upgrade[0] and end_row != start_row) or start_row==retaguardia_mia[0] or start_row==retaguardia_mia[1]:
            if  board_eventos[end_row][end_col] == "+" or board_eventos[end_row][end_col] == " ":

                #Si tengo una sola reina en upgrade, verifico si me puedo mover a la fila de upgrade rival, sino paso y sigo juntando mas reinas en mi row de upgrade
                if data_row_upgrade[1] == 1 and qq_row_strategy[end_row] == 0:
                    movement[2] = valor_row_strategy[end_row] - valor_row_strategy[data_row_upgrade[0]]     #este resultado solo va a ser positivo para la row_upgrade_rival
                    if movement[2] > 0:
                        move_save = [start_sq ,end_sq ,movement[2]] 
                        moves_analysis.append(move_save)
                
                #Si tengo mas de 1 reina en row upgrade, las empiezo a distribuir dependiendo las filas que tengan menos reinas y mas valor estrategico
                elif data_row_upgrade[1] >= 2 and qq_row_strategy[end_row] == 0:
                    movement[2] = valor_row_strategy[end_row]
                    move_save = [start_sq ,end_sq ,movement[2]] 
                    moves_analysis.append(move_save)

                #Si acumulo varias reinas en mi fila de upgrade, conviene moverlas a la fila de upgrade rival para meter presion
                elif end_row == row_strategy["upgrade_rival"] and  (qq_row_strategy[row_strategy["upgrade_mia"]] > qq_row_strategy[row_strategy["upgrade_rival"]] + 1):
                    movement[2] = valor_row_strategy[end_row]
                    move_save = [start_sq ,end_sq ,movement[2]] 
                    moves_analysis.append(move_save)

    return moves_analysis

#Tengo una pieza en la retaguardia rival, añado el valor de la pieza rival a cada movimiento
def piece_infiltrated(lista_capturas_sucias ,retaguardia_rival ,moves_analysis):   
    for movement in lista_capturas_sucias:
        start_sq = movement[0]
        end_sq   = movement[1]
        start_row = movement[0][0]
        end_row   = movement[1][0]

        x = retaguardia_rival.count(start_row)      #solo para start_row y end_row que se ubican ambas en la retaguardia rival
        y = retaguardia_rival.count(end_row)

        if x!=0 and y!=0:
            movement[2] = valores_rival[movement[3][1]]
            move_save = [start_sq ,end_sq ,movement[2]]
            moves_analysis.append(move_save)
    return moves_analysis

#Priprizo las columnas 6 y 7, para asi liberar las reinas de la retaguardia
def opening_white(moves ,row_strategy ,modifier): #Con modifier establezco que columna tiene mas prioridad entre la 6 y la 7
    moves_selected = []
    for movement in moves:
        col     = movement[0][1]
        end_row = movement[1][0]
        if   col == 6 + modifier:
            movement[2] = 2 + (10 - abs(row_strategy["upgrade_mia"] - end_row)) * 10
            moves_selected.append(movement)

        elif col == 7 - modifier:
            movement[2] = 1 + (10 - abs(row_strategy["upgrade_mia"] - end_row)) * 10
            moves_selected.append(movement)
    return moves_selected


def opening_black_complex (moves ,move_opening):
    moves_selected = []
    for movement in moves:
        end_sq = movement[1]
        if len(move_opening) > 0   and  end_sq == move_opening[0]:
            moves_selected.append(movement)
            move_opening.pop(0)
            return moves_selected
    return moves_selected
    

#Busco que peon movio el rival blanco y en base a eso, elijo que estrategia de apertura sigo como jugador negro
def opening_selector(board):
    if board[10][6]   != " ":
        selector = 0
        return selector
    elif board[10][5] != " ":
        selector = 1
        return selector
    else:
        selector = 2
        return selector


#Evalua los mejores movimientos de los peones
def peon_avance (moves, Game ,board_eventos):
    moves_selected = []
    upgrade_in = {4:100 ,3:200 ,2:300 ,1:400 ,0:1000}

    for movement in moves:
        end_row   = movement[1][0]
        col = movement[0][1]                        #start_col = end_col SIEMPRE para movimientos que no son de captura
        
        if board_eventos[end_row][col] == "-":      #Si avanzo, el rival tiene una captura limpia sobre mi pieza (califico muy mal el movimiento y sigo al proximo)
            movement[2] = -10000       
            #Lo guardo de todos modos, porque aunque el rival haya ahogado mis movimientos (peor de los casos), conviene seguir avanzando la linea de peones y liberar mis piezas en retaguardia    
            moves_selected.append(movement)         
            continue

        #Si el peon puede avanzar para PRESIONAR CON CAPTURA en el proximo turno a una pieza rival SIN exponerse, es un excelente movimiento
        if board_eventos[end_row][col] != "-":      #solo ocurre si ---> " ", "+" o "#"
            if Game.color:       #Jugador blanco
                if  col < 15 and Game.board[end_row-1][col+1].islower():    #captura posible hacia la DERECHA en el proximo turno
                    movement[2] = movement [2] + 2000
                elif col > 0 and Game.board[end_row-1][col-1].islower():    #captura posible hacia la IZQUIERDA en el proximo turno

                    movement[2] = movement [2] + 2000
            else:                #Jugador negro
                if   col < 15 and Game.board[end_row+1][col+1].isupper():   #captura posible hacia la DERECHA en el proximo turno          
                    movement[2] = movement [2] + 2000
                elif col > 0 and Game.board[end_row+1][col-1].isupper():    #captura posible hacia la IZQUIERDA en el proximo turno
                    movement[2] = movement [2] + 2000

        if movement[2] > 0:                 #Si se cumplio la condicion superior, continuo al sgte movimiento
            moves_selected.append(movement)
            continue   

        if (col == 6 or col == 7):          #Priorizo mover los peones de la columna 6 y 7, asi puedo liberar las 4 reinas de la retaguardia
            movement[2] = movement[2] + 2000
                                    
        rows_to_upgrade = abs(Game.row_strategy["upgrade_mia"] - end_row)  #Es mejor mover un peon que esta cerca de la coronacion
        movement[2] = movement[2] + upgrade_in[rows_to_upgrade]
        
        if Game.color:
            for i in range(16):     
                if Game.board[end_row - i][col] != " ":                 #Si hay casilleros ocupados por otras piezas delante del peon, no es bueno moverse en esta columna
                    movement[2] = movement[2] - 10000
                if board_eventos[end_row - i][col] == "-":
                    movement[2] = movement[2] - 1000
                if board_eventos[end_row - i][col] == "+":
                    movement[2] = movement [2] + 10
                if board_eventos[end_row - i][col] == "#":
                    movement[2] = movement [2] + 1
                if end_row - i == Game.row_strategy["upgrade_mia"]:     #si por ultimo evalue la fila de upgrade, terminar la iteracion
                    break
        else:
            for i in range(16):     
                if Game.board[end_row + i][col] != " ":                 #Si hay casilleros ocupados por otras piezas delante del peon, no es bueno moverse en esta columna
                    movement[2] = movement[2] - 10000
                if board_eventos[end_row + i][col] == "-":
                    movement[2] = movement[2] - 1000
                if board_eventos[end_row + i][col] == "+":
                    movement[2] = movement [2] + 10
                if board_eventos[end_row + i][col] == "#":
                    movement[2] = movement [2] + 1
                if end_row + i == Game.row_strategy["upgrade_mia"]:     #si por ultimo evalue la fila de upgrade, terminar la iteracion
                    break
            
        moves_selected.append(movement)
                       
    return moves_selected

