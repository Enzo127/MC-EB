'''
------------------------------------------------------------------------------LOGICA DEL MAPEO---------------------------------------------------------------------------

Antes de empezar: Cuando hablo de mis movimientos son posibilidades instantaneas, mientras que los movimientos del rival son posibilidades despues del mio, 
por lo que hay que considerar que el rival se podria mover hacia sus propias piezas (yo podria capturar su pieza y el recapturar).

Los eventos simples posibles son:
" " = El casillero esta vacio y no hay movimientos hacia el por mi o por el rival
+   = El casillero esta vacio, pero tengo movimientos validos hacia ellos 
-   = El casillero esta vacio, pero el rival tiene movimientos validos hacia ellos
x   = El casillero esta ocupado por una pieza rival y tengo un movimiento de captura hacia el
&   = El casillero esta ocupado por mi y el rival tiene un movimiento de captura hacia el
+p  = Los peones solo controlan los casilleros adyacentes hacia el centro (tengo que hacer la diferenciacion porque el peon no se puede mover ahi excepto que sea una captura)

De la combinacion de eventos simples, resultan los siguentes eventos compuestos (. = combinacion):

x.x  == xx ----> El casillero esta ocupado por una pieza rival y tengo 2 o mas movimientos de captura hacia el
&.&  == && ----> El casillero esta ocupado por mi y el rival tiene 2 o mas movimientos de captura hacia el

+.-  == #  ----> El casillero esta vacio y tanto yo como el rival tenemos movimientos hacia ese casillero (casillero neutro)
x.-  == ?  ----> El casillero esta controlado por el rival, yo tengo un movimiento de captura hacia el, pero el rival me puede recapturar la pieza (captura sucia)

Luego de mapear con todos mis movimientos y los del rival, hay ciertos eventos que evolucionan:
x  => $ -------> Puedo capturar una pieza y no ser recapturado (captura limpia)
'''

def analizador_eventos(moves ,moves_enemy ,color):
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

    board = move_sin_captura(moves, color, board)           #Mapeo mis movimientos a espacios libres (tipo=1)
    board = move_con_captura(moves, board)                  #Mapeo mis movimientos con captura       (tipo=0)
    board = moves_enemy_sin_captura(moves_enemy, board)     #Mapeo los movimientos del rival a espacios libres (tipo=1)
    board = moves_enemy_con_captura(moves_enemy, board)     #Mapeo los movimientos del rival con captura        (tipo=0)
    board = evolucion(board)                                #Posterior al mapeo, upgradeo ciertos eventos

    #for line in board:                                     #Visualizacion para testeo
    #    print(line)
    return board

def move_sin_captura(moves, color, board):
    tipo = 1                #Movimientos a espacios libres
    for piece in range(6):
        for movement in moves[piece][tipo]:
            if piece == 0:  
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

def move_con_captura(moves, board):               #El orden en que corren los if es FUNDAMENTAL 
    for piece in range(6):
        for movement in moves[piece][0]:
            end = movement[1]

            if board[end[0]][end[1]] == "x":     #Esta seccion NO la podes hacer con diccionarios, porque el orden de los if importa (y los diccionarios son arreglos desordenados)
                board[end[0]][end[1]] = "xx"

            if board[end[0]][end[1]] == "+p":                        
                board[end[0]][end[1]] = "x"

            if board[end[0]][end[1]] == "xx":                        
                pass

            if board[end[0]][end[1]] == " ":                      
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

            if board[end[0]][end[1]] == "&":  
                board[end[0]][end[1]] = "&&"    

            if board[end[0]][end[1]] == "-p":                           
                board[end[0]][end[1]] = "&"

            #if board[end[0]][end[1]] == "+":                           
            #    board[end[0]][end[1]] = "!"         #esto nunca va a ocurrir, voy a tener que analizar % sacando la pieza, si otra pieza mia cubre ese lugar con +, entonces evoluciono a !


            if board[end[0]][end[1]] == "&&":     
                pass

            if board[end[0]][end[1]] == " ":                          
                board[end[0]][end[1]] = "&"

    return board

#Posterior a mapear board_eventos con los movimientos posibles, algunos eventos upgradean
def evolucion(board):                   
    upgrade = {"x":"$" ,"xx":"$$" ,"-p":"-" ,"+p":"+"}
    
    for r in range(16): 
        for c in range(16):        
            
            event = upgrade.get(board[r][c])
            if event != None:
                board[r][c] = event

    return board


#Obtengo la posicion (row, col) de los eventos 
def eventos(board):
    search = {"$$":0 ,"$":1 ,"?":2}
    tipo_evento = [[],[],[]]
    
    for r in range(16):
        for c in range(16):
            
            event = search.get(board[r][c])
            if event != None:
                tipo_evento[event].append((r,c))

    return tipo_evento




