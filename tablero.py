'''
Contiene el objeto game, se crea y almacena un game por cada partida en juego.

Clase responsable de:   

_Establecer las variables unicas de cada color (Por ej: La fila de coronacion del jugador blanco r=8 y del negro es r=7)
_Determinar todos los movimientos validos propios y almacenarlos de forma ordenada para el board actual
_Determinar todos los movimientos validos del rival posterior a mi posible movimiento (incluyendo recapturas) y almacenarlos de forma ordenada para el board actual
_Guardar los movimientos y darmelos en listas ordenadas respecto a si los movimientos son con captura o si son a espacios libres.
'''

class Game():       
    def __init__(self,turn):           #Cuando creo el juego, debo guardar el color con el que se jugara la partida
        self.color = turn              

        #Diccionario para llamar a los metodos de movimientos de piezas
        self.move_functions = {"P": self.get_pawn_moves, "R": self.get_rook_moves, "H":self.get_knight_moves, "B": self.get_bishop_moves,"Q": self.get_queen_moves,"K": self.get_king_moves,
                               "p": self.get_pawn_moves, "r": self.get_rook_moves, "h":self.get_knight_moves, "b": self.get_bishop_moves,"q": self.get_queen_moves,"k": self.get_king_moves}
        
        
        #color = True ---> white  ||  color = False ---> black
        if self.color:                      #Valores de atributos para jugador blanco  //cambiar el nombre de color
            self.reina_mia          = "Q"
            self.reina_rival        = "q"
            self.row_strategy       = {"upgrade_mia":8 ,"upgrade_rival":7 ,"peones_rival":5}
            self.qq_row_strategy    = {8:0 ,7:0 ,5:0}   #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
            self.valor_row_strategy = {8:2 ,7:3 ,5:1}   #Valor de las filas estrategicas (la fila de upgrade rival es la mas valiosa, despues mi fila de upgrade y por ultimo la de peones rival)
            self.retaguardia_rival  = [0, 1]
            self.retaguardia_mia    = [14,15]
            
        else:                               #Valores de atributos para jugador negro
            self.reina_mia          = "q"
            self.reina_rival        = "Q"
            self.row_strategy       = {"upgrade_mia":7 ,"upgrade_rival":8 ,"peones_rival":10}
            self.qq_row_strategy    = {7:0 ,8:0 ,10:0} #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
            self.valor_row_strategy = {7:2 ,8:3 ,10:1} #Valor de las filas estrategicas (la fila de upgrade rival es la mas valiosa, despues mi fila de upgrade y por ultimo la de peones rival)
            self.retaguardia_rival  = [14, 15]
            self.retaguardia_mia    = [0, 1]

            self.strategy           = 2                #Este valor puede varias entre 0 y 2, elige la estrategia de apertura como negras en la IA (por default la estrategia 2)
            self.move_opening       = [(5,5) ,(5,6) ,(6,6) ,(5,7) ,(6,7) ,(5,8) ,(4,6) ,(5,6) ,(4,7) ,(5,7) ,(6,5) ,(6,8)]  #Primeros 12 mejores movimientos para la estrategia 0

    #Atributos comunes a los 2 colores
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
    
    queens_quantity = 0            #Sirve para determinar el valor de las reinas mias
    
    flag_apertura      = True      #Identifican si el objeto game se encuentra en los movimientos iniciales de apertura (se usa en ia_planificador)
    flag_first_move    = True
    


    #actualizar con el estado actual del tablero
    def actualizar (self, refresh):                     
        i=0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.board[r][c] = refresh[i]
                i=i+1

    '''
    Obtengo todos los movimientos validos de las piezas (con change=0 obtengo mis movimientos y con change=1 los del rival + las posibles recapturas)
    El resultado de la funcion es una lista ordenada de la sgte forma:
    
    all_moves[piece][type][move]     con:   

    _0 <= piece <= 5   (Todos los movimientos de un tipo de pieza se almancenan en la misma sublista)  
    _0 <= type <= 1    (type = movimientos de captura     ||   type = movimientos a espacios vacios)
    _move es otra lista que contiene informacion referente al movimiento ---> sq_start, sq_end, valor(empieza en 0, la ia ingresa el resultado del analisis aca) y 
     si el movimiento es de captura añadimos un string identificador de captura   ej: pQ  --------> como jugador negro, puedo comer con un peon una reina blanca del rival
    '''
    def get_all_possible_moves(self,change):    
        pawn_moves   = [[],[]]                   #Los movimientos con captura se almacenan en moves[0] y los movimientos a espacios libres en moves[1]
        rook_moves   = [[],[]]                    
        bishop_moves = [[],[]]
        queen_moves  = [[],[]]                    
        knight_moves = [[],[]]
        king_moves   = [[],[]]
         
        #Con change obtenemos los movimientos validos posibles del rival luego de mi turno (incluyendo las posibles recapturas de sus piezas)
        
        if change == 1:                                  #Si change=1, analizo con el color del rival
            self.color = not self.color
            
        
        if self.color:
            piece_moves = {"H": knight_moves, "B": bishop_moves,"R": rook_moves,"P": pawn_moves,"Q": queen_moves,"K": king_moves}
        else:
            piece_moves = {"h": knight_moves, "b": bishop_moves,"r": rook_moves,"p": pawn_moves,"q": queen_moves,"k": king_moves}


        for r in range(len(self.board)):                                                              #numero de filas
            for c in range(len(self.board[r])):                                                       #numero de columnas para una fila dada
                piece = self.board[r][c][0]                                                           #Leo y guardo el contenido del casillero
                if piece != " ":                                                                      #Si el casillero esta vacio, lo desestimo
                    if (self.color and piece.isupper()) or (not self.color and piece.islower()):  
                        self.move_functions[piece](r ,c ,piece_moves[piece] ,change)                  #LLamo a la funcion correspondiente (con esto me ahorro hacer multiples if para cada pieza)

        #Vuelvo el color a la normalidad
        if change == 1:                                  
            self.color = not self.color

        queen_moves = self.queen_nomenclature_captures(queen_moves)

        moves = [pawn_moves,knight_moves, bishop_moves, rook_moves,  king_moves, queen_moves]
        return moves


    #reajusto la nomenclatura en los movimientos de captura de la reina, ya que al llamar a las funciones "getBishopMoves" y "getRookMoves", se asignaban las letras de captura "b" o "r"
    #Arregla la nomenclatura de la lista que tiene los movimientos con captura de la reina
    def queen_nomenclature_captures(self, queen_moves):         #PASAR queen_moves[0] en vez de las 2 listas
        for movement in queen_moves[0]:                
            letter = movement[3][1]
            if self.color:
                movement[3] = "Q"+letter
            else:
                movement[3] = "q"+letter
        return queen_moves


    '''
    Elementos que guardo de un movimiento (move):
    move[0] = start_sq
    move[1] = end_sq
    move[2] = valor (en esta seccion es simplemente inicializado en 0, la seccion de la IA actualiza este valor)

    move[3] = este termino esta solo para movimientos de captura, es un string de 2 elementos que indica con que pieza capture a una pieza rival
    ej: "pQ  --------> como jugador negro, puedo comer con un peon una reina blanca del rival"
    '''
    #Guardo los movimientos validos de peones
    def get_pawn_moves(self,r,c,pawn_moves,change):                 
        if self.color:    #Logica de peon blanco                    
            if self.board[r-1][c] == " " and change==0:    #Verifico si puedo avanzar 1 casillero (change =0 porque no me interesa guardar los movimientos a espacios vacios de los peones rivales)        
                pawn_moves[1].append([(r,c),(r-1,c),0])                 #Avance de a 1 casillero
                if (r == 13 or r ==12) and self.board[r-2][c] == " ":   #Avance de a 2 casilleros
                    pawn_moves[1].append([(r,c),(r-2,c),0])                                     #lo guardo como movimiento a espacio libre ----> pawn_moves[1]
                
            if c-1 >= 0: #Capturas a la izquierda
                if self.board[r-1][c-1][0].islower(): #Captura de pieza enemiga
                    pawn_moves[0].append([(r,c),(r-1,c-1), 0, "P"+self.board[r-1][c-1][0]])     #lo guardo como movimiento de captura --->pawn_moves[0]

            if c+1 <= 15: #Capturas a la derecha
                if self.board[r-1][c+1][0].islower():                   #Captura de pieza enemiga
                    pawn_moves[0].append([(r,c),(r-1,c+1), 0, "P"+self.board[r-1][c+1][0]])

        else:       #Logica de peon negro
            if self.board[r+1][c] == " " and change==0:                 #Verifico si puedo avanzar 1 casillero  
                pawn_moves[1].append([(r,c),(r+1,c),0])                 #Avance de a 1 casillero
                if (r == 2 or r ==3) and self.board[r+2][c] == " ":     #Avance de a 2 casilleros
                    pawn_moves[1].append([(r,c),(r+2,c),0])

                    
            if c-1 >= 0: #Capturas a la izquierda
                if self.board[r+1][c-1][0].isupper(): #Captura de pieza enemiga
                    pawn_moves[0].append([(r,c),(r+1,c-1), 0, "p"+self.board[r+1][c-1][0]])

            if c+1 <= 15: #Capturas a la derecha
                if self.board[r+1][c+1][0].isupper(): #Captura de pieza enemiga
                    pawn_moves[0].append([(r,c),(r+1,c+1), 0, "p"+self.board[r+1][c+1][0]])


    #Movimientos del alfil
    def get_bishop_moves(self,r,c,bishop_moves,change):
        directions = ((-1,-1),(-1,1),(1,-1),(1,1))

        for d in directions:
            for i in range(1,16):                                                              #El alfil se puede mover un maximo de 15 casilleros
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if (0 <= end_row < 16) and (0 <= end_col < 16):                                  #Limites del tablero
                    
                    end_piece = self.board[end_row][end_col]                   
                    if end_piece == " ":                                                        #Lugar vacio es valido
                        bishop_moves[1].append([(r,c),(end_row,end_col),0])                      #Movimientos a espacios libres [1]

                    
                    elif end_piece.islower() and self.color:                                    #Captura de pieza enemiga
                        bishop_moves[0].append([(r,c),(end_row,end_col), 0, "B"+end_piece])       #Movimientos de captura [0]
                        break

                    elif end_piece.isupper() and not self.color:                                #Captura de pieza enemiga
                        bishop_moves[0].append([(r,c),(end_row,end_col), 0, "b"+end_piece])
                        break
                    
                    #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                    elif change==1:  
                        bishop_moves = analisis_rival(bishop_moves,end_piece, self.color, r,c,end_row,end_col)
                        break                    
                    
                    else:   #Al llegar aca, significa que hay una pieza mia, por lo que termino la iteracion
                        break
                else:       #Al llegar aca, significa que llegue al limite del tablero, por lo que termino la iteracion
                    break

    #Movimientos de la torre
    def get_rook_moves(self,r,c,rook_moves,change):
        directions = ((-1,0),(0,-1),(1,0),(0,1))                                            #Direcciones de movimiento posible con la torre
        for d in directions:
            for i in range(1,16):
                end_row = r + d[0] * i
                end_col = c + d[1] * i

                if (0 <= end_row < 16) and (0 <= end_col < 16):                               #Limites del tablero
                    end_piece = self.board[end_row][end_col]
                    if end_piece == " ":                                                     #Lugar vacio es valido
                        rook_moves[1].append([(r,c),(end_row,end_col),0])

                    elif end_piece.islower() and self.color:                                 #Captura de pieza enemiga
                        rook_moves[0].append([(r,c),(end_row,end_col), 0, "R"+end_piece])
                        break
                        
                    elif end_piece.isupper() and not self.color:                             #Captura de pieza enemiga
                        rook_moves[0].append([(r,c),(end_row,end_col), 0, "r"+end_piece])
                        break

                    #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                    elif change==1:  
                        rook_moves = analisis_rival(rook_moves,end_piece, self.color, r,c,end_row,end_col)
                        break

                    else:   #Al llegar aca, significa que hay una pieza mia, por lo que termino la iteracion
                        break
                else:       #Al llegar aca, significa que llegue al limite del tablero, por lo que termino la iteracion
                    break

    #Movimientos de la reina, sus movimientos se pueden conformar con los del alfil y la torre
    def get_queen_moves(self,r,c,queen_moves,change):
        if change==0:
            self.queens_quantity=self.queens_quantity+1     #Contador de numero de reinas propias para el turno actual
        
        self.get_rook_moves(r,c,queen_moves,change)              
        self.get_bishop_moves(r,c,queen_moves,change)

    #Movimientos del caballero
    def get_knight_moves(self,r,c,knight_moves,change):
        directions = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))  #Todas las posibles di

        for m in directions:
            end_row = r + m[0]
            end_col = c + m[1]
            if (0 <= end_row < 16) and (0 <= end_col < 16):                       #Limites del tablero
                end_piece = self.board[end_row][end_col]
                #Movimientos a espacios libres
                if end_piece==" ":                                               #Lugar vacio es valido
                    knight_moves[1].append([(r,c),(end_row,end_col),0])

                #Movimientos con captura
                elif end_piece.islower() and self.color:  
                    knight_moves[0].append([(r,c),(end_row,end_col), 0, "H"+end_piece])

                elif end_piece.isupper() and not self.color:
                    knight_moves[0].append([(r,c),(end_row,end_col), 0, "h"+end_piece])
                    
                #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                elif change==1:  
                    knight_moves = analisis_rival(knight_moves,end_piece, self.color, r,c,end_row,end_col)

    #Movimientos del rey
    def get_king_moves(self,r,c,king_moves,change): 
        directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

        for i in range(8):
            end_row = r + directions[i][0]
            end_col = c + directions[i][1]
            if (0 <= end_row < 16) and (0 <= end_col < 16):
                end_piece = self.board[end_row][end_col]
                if end_piece==" ":                                        #Lugar vacio es valido
                    king_moves[1].append([(r,c),(end_row,end_col),0])

                if end_piece.islower() and self.color:  
                    king_moves[0].append([(r,c),(end_row,end_col), 0, "K"+end_piece])

                elif end_piece.isupper() and not self.color:
                    king_moves[0].append([(r,c),(end_row,end_col), 0, "k"+end_piece])

                #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                elif change==1:  
                    king_moves = analisis_rival(king_moves,end_piece, self.color, r,c,end_row,end_col)
                

    #Esto solo se ejecuta cuando juego contra mi mismo, es la misma asignacion de atributos que dependen del color que hay en el __init__
    def seteo_inicial(self, color):
        if color:                      #Valores de atributos para jugador blanco  //cambiar el nombre de color
            self.reina_mia          = "Q"
            self.reina_rival        = "q"
            self.row_strategy       = {"upgrade_mia":8 ,"upgrade_rival":7 ,"peones_rival":5}
            self.qq_row_strategy    = {8:0 ,7:0 ,5:0}   #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
            self.valor_row_strategy = {8:2 ,7:3 ,5:1}   #Valor de las filas
            self.retaguardia_rival  = [0, 1]
            self.retaguardia_mia    = [14,15]
            
        else:                               #Valores de atributos para jugador negro
            self.reina_mia          = "q"
            self.reina_rival        = "Q"
            self.row_strategy       = {"upgrade_mia":7 ,"upgrade_rival":8 ,"peones_rival":10}
            self.qq_row_strategy    = {7:0 ,8:0 ,10:0} #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
            self.valor_row_strategy = {7:2 ,8:3 ,10:1}
            self.retaguardia_rival  = [14, 15]
            self.retaguardia_mia    = [0, 1]

            self.strategy           = 2                #Este valor puede varias entre 0 y 2, elige la estrategia de apertura como negras en la IA (por default la estrategia 2)
            self.move_opening       = [(5,5) ,(5,6) ,(6,6) ,(5,7) ,(6,7) ,(5,8) ,(4,6) ,(5,6) ,(4,7) ,(5,7) ,(6,5) ,(6,8)]  #Primeros 12 mejores movimientos para la estrategia 0


    '''
    _Contar la cantidad de reinas propias en 3 filas estrategicas: fila de coronacion propia(row_upgrade), fila de coronacion del rival(row_upgrade_rival) 
    y fila de peones debiles del rival (por lo general el rival se mueve de a 2 casilleros con los peones y estos quedan expuestos).
    '''
    def queens_in_row_strategy(self):    
        for row in self.qq_row_strategy:            #Esto se tiene que resetear todos los turnos
            self.qq_row_strategy[row] = 0
        
        #1) Analisis: Cantidad de reinas mias en row upgrade
        row = self.row_strategy["upgrade_mia"]
        for col in range(16):
            if self.reina_mia == self.board[row][col]:
                self.qq_row_strategy[row] = self.qq_row_strategy[row] + 1

        #2) Analisis: Cantidad de reinas propias en row upgrade rival
        row  = self.row_strategy["upgrade_rival"]
        for col in range(16):
            if self.reina_mia == self.board[row][col]:                     #verifico si tengo reinas propias en la fila de upgrade rival
                self.qq_row_strategy[row] = self.qq_row_strategy[row] + 1                     

        #3) Analisis: Cantidad de reinas propias en la row de peones debiles del rival 
        row  = self.row_strategy["peones_rival"]           
        for col in range(16):
            if self.reina_mia == self.board[row][col]:
                self.qq_row_strategy[row] = self.qq_row_strategy[row] + 1


#Almacena los movimientos con captura validos del rival
def analisis_rival(piece_moves ,end_piece ,color ,r ,c ,end_row ,end_col):
    if end_piece.islower() and not color:
        piece_moves[1].append([(r,c),(end_row,end_col), 0])   #Necesito el 3er termino? Total, no califico lo que el rival podria hacer
        return piece_moves

    elif end_piece.isupper() and color:
        piece_moves[1].append([(r,c),(end_row,end_col), 0])
        return piece_moves

    return piece_moves

