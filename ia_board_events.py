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


De la combinacion de eventos simples, resultan los siguentes eventos compuestos (. = combinacion):

+.-  == #  ----> El casillero esta vacio y tanto yo como el rival tenemos movimientos hacia ese casillero (casillero neutro)
x.-  == ?  ----> El casillero esta controlado por el rival, yo tengo un movimiento de captura hacia el, pero el rival me puede recapturar la pieza (captura sucia)

Si al final de todo el mapeo, tengo eventos "x" sin que se hayan conbinado, significa que son capturas limpias (puedo capturar una pieza rival sin la posibilidad de ser recapturado).
x ----fin mapeo-----> Captura limpia
'''

def event_maker(moves ,moves_enemy ,color ,board_game):
    board_event = [                                                                                      
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

    #Mapeo con mis piezas
    board_event = move_not_capture_pawn   (color, board_event ,board_game, True)      #Mapeo los casilleros controlados por mis peones(aunque no puedan moverse, pero los defienden)
    board_event = move_not_capture_mine   (moves, board_event)                        #Mapeo mis movimientos con las demas piezas (excepto peon) a espacios libres (tipo=1)
    board_event = move_with_capture_mine  (moves, board_event)                        #Mapeo mis movimientos con captura                                           (tipo=0)

    #Mapeo con las piezas del rival
    board_event = move_not_capture_pawn   (not color, board_event ,board_game, False) #Mapeo los casilleros controlados por peones rivales(aunque no puedan moverse, pero los defienden)
    board_event = move_not_capture_enemy (moves_enemy, board_event)                   #Mapeo los movimientos del rival a espacios libres                           (tipo=1)
    board_event = move_with_capture_enemy(moves_enemy, board_event)                   #Mapeo los movimientos del rival con captura                                 (tipo=0)
    
    #print()
    #for line in board_event:                                     
    #    print(line)
    #print()

    return board_event

#Los peones controlan casilleros a los que no pueden moverse EXCEPTO que sea con una captura
#Con esta funcion marco con +p todos los casilleros VACIOS que controlan mis peones
def move_not_capture_pawn(color, board_event ,board_game, mine):    #con mine = True analizo los casilleros controlados por mis peones
    if mine:                                                        #con mine = False, analizo los casilleros controlados por los peones del rival (mas complejo porque es en el turno sgte)
        event_change = {" ":"+"   ,"+":"+"}
    else:
        event_change = {" ":"-"   ,"+":"#"   ,"x":"?"     ,"#":"#"      ,"?":"?"     ,"-":"-"}  #Conviene hacerlo con un diccionario aca, sino usaria muchos if

    for r in range(16):
        for c in range(16):
            if color and board_game[r][c] == "P":

                if c+1<=15 and (board_game[r-1][c+1] == " " or (not mine and board_game[r-1][c+1].isupper())):
                    event_before          = board_event[r-1][c+1]
                    board_event[r-1][c+1] = event_change[event_before]

                if c-1>=0 and  (board_game[r-1][c-1] == " " or (not mine and board_game[r-1][c-1].isupper())):
                    event_before          = board_event[r-1][c-1]
                    board_event[r-1][c-1] = event_change[event_before]

            elif not color and board_game[r][c] == "p":

                if c+1<=15 and (board_game[r+1][c+1] == " " or (not mine and board_game[r+1][c+1].islower())):
                    event_before          = board_event[r+1][c+1]
                    board_event[r+1][c+1] = event_change[event_before]


                if c-1>=0 and (board_game[r+1][c-1] == " "  or (not mine and board_game[r+1][c-1].islower())):
                    event_before          = board_event[r+1][c-1]
                    board_event[r+1][c-1] = event_change[event_before]
    
    return board_event

def move_not_capture_mine(moves, board_event):    
    tipo = 1                                                  #Movimientos a espacios libres    
      
    for piece in range(1,6):                                      
        for movement in moves[piece][tipo]:
            end = movement[1]   
            board_event[end[0]][end[1]] = "+"

    return board_event

def move_with_capture_mine(moves, board_event):               #El orden en que corren los if es FUNDAMENTAL 
    for piece in range(6):
        for movement in moves[piece][0]:
            end = movement[1]

            if board_event[end[0]][end[1]] == "x":     #Esta seccion NO la podes hacer con diccionarios, porque el orden de los if importa (y los diccionarios son arreglos desordenados)
                board_event[end[0]][end[1]] = "x"


            if board_event[end[0]][end[1]] == " ":                      
                board_event[end[0]][end[1]] = "x"
    return board_event


def move_not_capture_enemy(moves_enemy, board_event):
    for piece in range(1,6):
        for movement in moves_enemy[piece][1]:
            end = movement[1]

            if board_event[end[0]][end[1]] == " ":                            
                board_event[end[0]][end[1]] = "-"

            if board_event[end[0]][end[1]] == "+":          
                board_event[end[0]][end[1]] = "#"

            if board_event[end[0]][end[1]] == "x":                         
                board_event[end[0]][end[1]] = "?"
    return board_event

def move_with_capture_enemy(moves_enemy, board_event):
    for piece in range(6):
        for movement in moves_enemy[piece][0]:
            end = movement[1]

            if board_event[end[0]][end[1]] == "&":  
                board_event[end[0]][end[1]] = "&"    

            #if board_event[end[0]][end[1]] == "+":                           
            #    board_event[end[0]][end[1]] = "!"         #esto nunca va a ocurrir, voy a tener que analizar % sacando la pieza, si otra pieza mia cubre ese lugar con +, entonces evoluciono a !

            if board_event[end[0]][end[1]] == " ":                          
                board_event[end[0]][end[1]] = "&"

    return board_event


#Obtengo la posicion (row, col) de los eventos de captura limpia ($ = no me puede recapturar) y los eventos de captura sucia (? = me puede recapturar)
def event_search(board_event):
    search = {"x":0 ,"?":1}
    tipo_evento = [[],[]]
    
    for r in range(16):
        for c in range(16):
            
            event = search.get(board_event[r][c])
            if event != None:
                tipo_evento[event].append((r,c))

    return tipo_evento




