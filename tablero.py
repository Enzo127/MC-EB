'''
Contiene el objeto game, se crea y almacena un game por cada partida en juego.

Clase responsable de:   

_Establecer las variables unicas de cada color (Por ej: La fila de coronacion del jugador blanco r=8 y del negro es r=7)
_Determinar todos los movimientos validos propios y almacenarlos de forma ordenada para el board actual
_Determinar todos los movimientos validos del rival posterior a mi posible movimiento (incluyendo recapturas) y almacenarlos de forma ordenada para el board actual
_Añadir un valor agregado a las mejores columnas para el avance de los peones (para ayudar a la IA en la tarea de calificar el mejor movimiento)
'''
class game():
    def __init__(self,turn):           #Cuando creo el juego, debo guardar el color con el que se jugara la partida
        self.color = turn
        self.move_Functions = {"P": self.get_Pawn_Moves, "R": self.get_Rook_Moves, "H":self.get_Knight_Moves, "B": self.get_Bishop_Moves,"Q": self.get_Queen_Moves,"K": self.get_King_Moves,
                               "p": self.get_Pawn_Moves, "r": self.get_Rook_Moves, "h":self.get_Knight_Moves, "b": self.get_Bishop_Moves,"q": self.get_Queen_Moves,"k": self.get_King_Moves}

        if self.color:                      #Valores de atributos para jugador blanco
            self.reina_mia          = "Q"
            self.reina_rival        = "q"

            self.row_strategy       = {"upgrade_mia":8 ,"upgrade_rival":7 ,"peones_rival":5 ,"peones_mios_1":9 ,"peones_mios_2":10}
            self.qq_row_strategy    = {8:0 ,9:0 ,10:0    ,7:0 ,5:0}   #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
            self.valor_row_strategy = {8:3 ,9:1 ,10:2    ,7:5 ,5:4}
            self.retaguardia_rival  = [0, 1]
            self.retaguardia_mia    = [14,15]
        else:                               #Valores de atributos para jugador negro
            self.reina_mia          = "q"
            self.reina_rival        = "Q"

            self.row_strategy       = {"upgrade_mia":7 ,"upgrade_rival":8 ,"peones_rival":10 ,"peones_mios_1":6 ,"peones_mios_2":5}
            self.qq_row_strategy    = {7:0 ,6:0 ,5:0    ,8:0 ,10:0} #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
            self.valor_row_strategy = {7:3 ,6:1 ,5:2    ,8:5 ,10:4}
            self.retaguardia_rival  = [14, 15]
            self.retaguardia_mia  = [0, 1]
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
    
    queens_Quantity = 0            
    
    best_col = {0:0 ,1:0 ,2:0 ,3:1 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0 ,9:0 ,10:0 ,11:0 ,12:0 ,13:0 ,14:0 ,15:0 }

    qm_quantity_row_tactical        = 0
    qm_quantity_row_tactical_rival  = 0
    qm_quantity_row_upgrade_mia     = 0
    qm_quantity_row_upgrade_rival   = 0    #Reinas mias en la de upgrade rival

    qr_quantity_row_upgrade_rival   = 0    #Reinas rvales en su fila de upgrade

    

    #Actualizar con el estado actual del tablero
    def Actualizar (self, refresh):
        i=0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.board[r][c] = refresh[i]
                i=i+1

        for row in self.board:
            print(row)

    '''
    Obtengo todos los movimientos validos de las piezas (con change=0 obtengo mis movimientos y con change=1 los del rival + las posibles recapturas)
    El resultado de la funcion es una lista ordenada de la sgte forma:
    
    all_moves[piece][type][move]     con:   

    _0 <= piece <= 5   (Todos los movimientos de un tipo de pieza se almancenan en la misma sublista)  
    _0 <= type <= 1    (type = movimientos de captura     ||   type = movimientos a espacios vacios)
    _move es otra lista que contiene informacion referente al movimiento ---> sq_start, sq_end, valor(empieza en 0, la ia ingresa el resultado del analisis aca) y 
     si el movimiento es de captura añadimos un string identificador de captura   ej: pQ  --------> como jugador negro, puedo comer con un peon una reina blanca del rival
    '''
    def get_All_Possible_Moves(self,change):    
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
                        self.move_Functions[piece](r ,c ,piece_moves[piece] ,change)                  #LLamo a la funcion correspondiente 

        #Vuelvo el color a la normalidad
        if change == 1:                                  
            self.color = not self.color

        queen_moves = self.queen_Nomenclature_Captures(queen_moves)

        moves = [pawn_moves,knight_moves, bishop_moves, rook_moves,  king_moves, queen_moves]
        return moves


    #reajusto la nomenclatura en los movimientos de captura de la reina, ya que al llamar a las funciones "getBishopMoves" y "getRookMoves", se asignaban las letras de captura "b" o "r"
    #Arregla la nomenclatura de la lista que tiene los movimientos con captura de la reina
    def queen_Nomenclature_Captures(self, queen_moves):
        for movement in queen_moves[0]:                
            letter = movement[3][1]
            if self.color:
                movement[3] = "Q"+letter
            else:
                movement[3] = "q"+letter

        return queen_moves


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Movimienentos de piezas--------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #Movimientos del peon
    def get_Pawn_Moves(self,r,c,pawn_moves,change): 
        if self.color:    #Logica de peon blanco
            if self.board[r-1][c] == " " and change==0:                 #Verifico si puedo avanzar 1 casillero  
                if (r == 13 or r ==12) and self.board[r-2][c] == " ":   #Avance de a 2
                    pawn_moves[1].append([(r,c),(r-2,c),0])
                else:
                    pawn_moves[1].append([(r,c),(r-1,c),0])             #Guardo el movimiento de 1 avance SOLO si no puedo avanzar de a 2

            if c-1 >= 0: #Capturas a la izquierda
                if change ==1:                        #Casilleros que cubre con captura el peon rival
                    pawn_moves[1].append([(r,c),(r-1,c-1), 0, "P"+self.board[r-1][c-1][0]])

                if self.board[r-1][c-1][0].islower(): #Captura de pieza enemiga
                    pawn_moves[0].append([(r,c),(r-1,c-1), 0, "P"+self.board[r-1][c-1][0]])


            if c+1 <= 15: #Capturas a la derecha
                if change ==1:                         #Casilleros que cubre con captura el peon rival (incluida sus piezas para recaptura)
                    pawn_moves[1].append([(r,c),(r-1,c+1), 0, "P"+self.board[r-1][c+1][0]])

                if self.board[r-1][c+1][0].islower():                   #Captura de pieza enemiga
                    pawn_moves[0].append([(r,c),(r-1,c+1), 0, "P"+self.board[r-1][c+1][0]])


        else:       #Logica de peon negro
            if self.board[r+1][c] == " " and change==0:                 #Verifico si puedo avanzar 1 casillero  
                if (r == 2 or r ==3) and self.board[r+2][c] == " ":     #Avance de a 2
                    pawn_moves[1].append([(r,c),(r+2,c),0])
                else:
                    pawn_moves[1].append([(r,c),(r+1,c),0])             #Guardo el movimiento de 1 avance SOLO si no puedo avanzar de a 2

            if c-1 >= 0: #Capturas a la izquierda
                if change ==1:                        #Casilleros que cubre con captura el peon rival (incluida sus piezas para recaptura)
                    pawn_moves[1].append([(r,c),(r+1,c-1), 0, "p"+self.board[r+1][c-1][0]])

                if self.board[r+1][c-1][0].isupper(): #Captura de pieza enemiga
                    pawn_moves[0].append([(r,c),(r+1,c-1), 0, "p"+self.board[r+1][c-1][0]])

            if c+1 <= 15: #Capturas a la derecha
                if change ==1:
                    pawn_moves[1].append([(r,c),(r+1,c+1), 0, "p"+self.board[r+1][c+1][0]])

                if self.board[r+1][c+1][0].isupper(): #Captura de pieza enemiga
                    pawn_moves[0].append([(r,c),(r+1,c+1), 0, "p"+self.board[r+1][c+1][0]])

    #Movimientos del alfil
    def get_Bishop_Moves(self,r,c,bishop_moves,change):
        directions = ((-1,-1),(-1,1),(1,-1),(1,1))
        extra = 0
        for d in directions:
            for i in range(1,16):                                                              #El alfil se puede mover un maximo de 15 casilleros
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if (0 <= endRow < 16) and (0 <= endCol < 16):                                  #Limites del tablero
                    
                    endPiece = self.board[endRow][endCol]                   
                    if endPiece == " ":                                                        #Lugar vacio es valido
                        bishop_moves[1].append([(r,c),(endRow,endCol),extra])                  #Movimientos a espacios libres [1]

                    
                    elif endPiece.islower() and self.color:                                    #Captura de pieza enemiga
                        bishop_moves[0].append([(r,c),(endRow,endCol), extra, "B"+endPiece])   #Movimientos de captura [0]
                        break

                    elif endPiece.isupper() and not self.color:                                #Captura de pieza enemiga
                        bishop_moves[0].append([(r,c),(endRow,endCol), extra, "b"+endPiece])
                        break
                    
                    #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                    elif change==1:  
                        bishop_moves = analisis_rival(bishop_moves,endPiece, self.color, r,c,endRow,endCol)
                        break                    
                    
                    
                    
                    else:   #Al llegar aca, significa que hay una pieza rival, por lo que termino la iteracion
                        break
                else:       #Al llegar aca, significa que llegue al limite del tablero, por lo que termino la iteracion
                    break

    #Movimientos de la torre
    def get_Rook_Moves(self,r,c,rook_moves,change):
        directions = ((-1,0),(0,-1),(1,0),(0,1))                                            #Direcciones de movimiento posible con la torre
        for d in directions:
            for i in range(1,16):
                endRow = r + d[0] * i
                endCol = c + d[1] * i

                if (0 <= endRow < 16) and (0 <= endCol < 16):                               #Limites del tablero
                    endPiece = self.board[endRow][endCol]
                    if endPiece == " ":                                                     #Lugar vacio es valido
                        rook_moves[1].append([(r,c),(endRow,endCol),0])

                    elif endPiece.islower() and self.color:                                 #Captura de pieza enemiga
                        rook_moves[0].append([(r,c),(endRow,endCol), 0, "R"+endPiece])
                        break
                        
                    elif endPiece.isupper() and not self.color:                             #Captura de pieza enemiga
                        rook_moves[0].append([(r,c),(endRow,endCol), 0, "r"+endPiece])
                        break

                    #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                    elif change==1:  
                        rook_moves = analisis_rival(rook_moves,endPiece, self.color, r,c,endRow,endCol)
                        break

                    else:   #Al llegar aca, significa que hay una pieza rival, por lo que termino la iteracion
                        break
                else:       #Al llegar aca, significa que llegue al limite del tablero, por lo que termino la iteracion
                    break

    #Movimientos de la reina, sus movimientos se pueden conformar con los del alfil y la torre
    def get_Queen_Moves(self,r,c,queen_moves,change):
        if change==0:
            self.queens_Quantity=self.queens_Quantity+1     #Contador de numero de reinas propias para el turno actual
        
        self.get_Rook_Moves(r,c,queen_moves,change)              
        self.get_Bishop_Moves(r,c,queen_moves,change)

    #Movimientos del caballero
    def get_Knight_Moves(self,r,c,knight_moves,change):
        directions = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))  #Todas las posibles di

        for m in directions:
            endRow = r + m[0]
            endCol = c + m[1]
            if (0 <= endRow < 16) and (0 <= endCol < 16):                       #Limites del tablero
                endPiece = self.board[endRow][endCol]
                #Movimientos a espacios libres
                if endPiece==" ":                                               #Lugar vacio es valido
                    knight_moves[1].append([(r,c),(endRow,endCol),0])

                #Movimientos con captura
                elif endPiece.islower() and self.color:  
                    knight_moves[0].append([(r,c),(endRow,endCol), 0, "H"+endPiece])

                elif endPiece.isupper() and not self.color:
                    knight_moves[0].append([(r,c),(endRow,endCol), 0, "h"+endPiece])
                    
                #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                elif change==1:  
                    knight_moves = analisis_rival(knight_moves,endPiece, self.color, r,c,endRow,endCol)

    #Movimientos del rey
    def get_King_Moves(self,r,c,king_moves,change): 
        directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

        for i in range(8):
            endRow = r + directions[i][0]
            endCol = c + directions[i][1]
            if (0 <= endRow < 16) and (0 <= endCol < 16):
                endPiece = self.board[endRow][endCol]
                if endPiece==" ":                                        #Lugar vacio es valido
                    king_moves[1].append([(r,c),(endRow,endCol),0])

                if endPiece.islower() and self.color:  
                    king_moves[0].append([(r,c),(endRow,endCol), 0, "K"+endPiece])

                elif endPiece.isupper() and not self.color:
                    king_moves[0].append([(r,c),(endRow,endCol), 0, "k"+endPiece])

                #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                elif change==1:  
                    king_moves = analisis_rival(king_moves,endPiece, self.color, r,c,endRow,endCol)
                

    #Esto solo se ejecuta cuando juego contra mi mismo, es la misma asignacion de atributos que dependen del color que hay en el __init__
    def seteo_Inicial(self, color):
        if color:                                   #Valores de atributos para jugador blanco
            self.reina_mia          = "Q"
            self.reina_rival        = "q"

            self.row_strategy       = {"upgrade_mia":8 ,"upgrade_rival":7 ,"peones_rival":5 ,"peones_mios_1":9 ,"peones_mios_2":10}
            self.qq_row_strategy    = {8:0 ,9:0 ,10:0    ,7:0 ,5:0}   #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
            self.valor_row_strategy = {8:3 ,9:1 ,10:2    ,7:5 ,5:4}

        else:                                       #Valores de atributos para jugador negro
            self.reina_mia          = "q"
            self.reina_rival        = "Q"

            self.row_strategy       = {"upgrade_mia":7 ,"upgrade_rival":8 ,"peones_rival":10 ,"peones_mios_1":6 ,"peones_mios_2":5}
            self.qq_row_strategy    = {7:0 ,6:0 ,5:0    ,8:0 ,10:0} #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
            self.valor_row_strategy = {7:3 ,6:1 ,5:2    ,8:5 ,10:4}

    '''
    El objetivo de la funcion es evaluar que columna es mejor para empezar a mover un nuevo peon: La mejor columna es en la cual el peon se puede coronar mas rapido, sin
    exponerse a ser capturado por reinas rivales O si se expone, tiene que ser defendido por reinas propias.

    Esto lo logra mediante 2 acciones:
    _Contar la cantidad de reinas propias y del rival en 3 filas estrategicas: fila de coronacion propia(row_upgrade), fila de coronacion del rival(row_upgrade_rival) 
    y fila previa a la coronacion propia (row_tactical).

    _Mientras se analizan las 3 filas, se van asignando valores a las columnas dependiendo la posicion de las reinas.
    '''

    #ESTAS 3 DEBERIAN SEPARARSE EN 3 FUNCIONES MAS PEQUEÑAS
    #ESTAS 3 DEBERIAN SEPARARSE EN 3 FUNCIONES MAS PEQUEÑAS
    
    def columna_Rating(self):
        #Esto se tiene que resetear todos los turnos
        for row in self.qq_row_strategy:
            self.qq_row_strategy[row] = 0

        self.qr_quantity_row_upgrade_rival   = 0    #Reinas rvales en su fila de upgrade   // qr = queen rival
        self.best_col = {0:0 ,1:1 ,2:0 ,3:0 ,4:5 ,5:0 ,6:0 ,7:0 ,8:0 ,9:0 ,10:0 ,11:0 ,12:0 ,13:0 ,14:0 ,15:0 }
        

        #1) Analisis: Cantidad de reinas mias en row_peones_mios_1 y row_peones_mios_2
        row = self.row_strategy["peones_mios_1"]
        for col in range(16):
            if (self.reina_mia == self.board[row][col]):
                self.qq_row_strategy[row] = self.qq_row_strategy[row] + 1
                self.best_col[col] = self.best_col[col] - 20                    #Si tengo una reina en la fila de tactica, no conviene mover el peon que esta detras de ella (ya que los bloquea mi propia pieza)
                                                                                #Conviene mas mover peones de otra columna para coronarlos
        row = self.row_strategy["peones_mios_2"]
        for col in range(16):
            if (self.reina_mia == self.board[row][col]):
                self.qq_row_strategy[row] = self.qq_row_strategy[row] + 1
                self.best_col[col] = self.best_col[col] - 20                    #Si tengo una reina en la fila de tactica, no conviene mover el peon que esta detras de ella (ya que los bloquea mi propia pieza)
                                                                                #Conviene mas mover peones de otra columna para coronarlos

        #2) Analisis: Cantidad de reinas mias en row upgrade y la columna en que se encuentra
        row          = self.row_strategy["upgrade_mia"]
        row_peones_1 = self.row_strategy["peones_mios_1"]
        row_peones_2 = self.row_strategy["peones_mios_2"]

        for col in range(16):
            if self.reina_mia == self.board[row][col]:
                self.qq_row_strategy[row] = self.qq_row_strategy[row] + 1
                self.best_col[col] = self.best_col[col] - 20                    #Si tengo una reina en la fila de coronacion, no conviene mover el peon que esta detras de ella (ya que los bloquea mi propia pieza)
                                                                                #Conviene mas mover peones de otra columna para coronarlos
                
                if self.qq_row_strategy[row_peones_1] == 0 and self.qq_row_strategy[row_peones_2]: #Si no tengo reinas propias en row_tactical, avanzar peones en la columna al lado de una reina que tengas en row_upgrade
                    if col+1 <= 15:
                        self.best_col[col+1] = self.best_col[col+1] + 5    
                    if col-1 >= 0:             
                        self.best_col[col-1] = self.best_col[col-1] + 5

                else:
                    if col+2 <= 15:
                        self.best_col[col+2] = self.best_col[col+2] + 8
                        self.best_col[col+1] = self.best_col[col+1] + 1
                    if col-2 >= 0: 
                        self.best_col[col-2] = self.best_col[col-2] + 8
                        self.best_col[col-1] = self.best_col[col-1] + 1

        #3) Analisis: Cantidad de reinas rivales en su upgrade, cantidad de reinas propias en su upgrade y la columna en la que se encuentra la reina del rival (si las hay)
        row  = self.row_strategy["upgrade_rival"]
        for col in range(16):
            if self.reina_mia == self.board[row][col]:                     #verifico si tengo reinas propias en la fila de upgrade rival
                self.qq_row_strategy[row] = self.qq_row_strategy[row] + 1                     

            if self.reina_rival == self.board[row][col]:                   #verifico si el rival tiene reinas propias en su row upgrade   (ESTO HACE FALTA????)
                self.qr_quantity_row_upgrade_rival = self.qr_quantity_row_upgrade_rival + 1   
         
                self.best_col[col]   = self.best_col[col]   - 9                   #Mover un peon en una columna en la cual hay una reina rival en row_upgrade_rival no es una buena idea
                for i in range(1,4):

                    if col+i <= 15:
                        self.best_col[col+i] = self.best_col[col+i] + (i*3-9)     #Evaluo negativamente a las columnas alrededor de una reina rival en row_upgrade_rival (es donde principalmente se suelen encontrar)

                    if col-i >= 0:
                        self.best_col[col-i] = self.best_col[col-i] + (i*3-9)     
        
        
        #4) Analisis: Cantidad de reinas propias en row tactical rival  
        row  = self.row_strategy["peones_rival"]           
        for col in range(16):
            if self.reina_mia == self.board[row][col]:
                self.qq_row_strategy[row] = self.qq_row_strategy[row] + 1


        #CUANDO TENGAS TIEMPO, OPTIMIZA ESTO CON UNA FUNCION Y UN FOR, CHEQUEA EL METODO ITEMS DE LOS DICCIONARIOS, POR AHI VA LA MANO
        #Actualizo valor de row_upgrade_rival
        #2do edit: lo mejor seria hacer el fixed value en cada uno de los pasos de arriba (ya tenes el row declarado arriba)

        #self.row_strategy       = {"upgrade_mia":8 ,"upgrade_rival":7 ,"peones_rival":5 ,"peones_mios_1":9 ,"peones_mios_2":10}
        #self.qq_row_strategy    = {8:0 ,9:0 ,10:0    ,7:0 ,5:0}   #Filas estrategicas y la cantidad de reinas propias en ellas (qq = queens quantity)
        '''
        fixed_value = self.valor_row_strategy[self.row_upgrade_rival] - self.qm_quantity_row_upgrade_rival
        self.valor_row_strategy[self.row_upgrade_rival] = fixed_value

        #Actualizo valor de row_tactical
        fixed_value = self.valor_row_strategy[self.row_tactical] - self.qm_quantity_row_tactical
        self.valor_row_strategy[self.row_tactical] = fixed_value

        #Actualizo valor de row_upgrade_mia
        fixed_value = self.valor_row_strategy[self.row_upgrade_mia] - self.qm_quantity_row_upgrade_mia   
        self.valor_row_strategy[self.row_upgrade_mia] = fixed_value

        #Actualizo valor de row_tactical_rival
        fixed_value = self.valor_row_strategy[self.row_tactical_rival] - self.qm_quantity_row_tactical_rival  
        self.valor_row_strategy[self.row_tactical_rival] = fixed_value
        '''
        

#Almacena los movimientos con captura validos del rival
def analisis_rival(piece_moves ,endPiece ,color ,r ,c ,endRow ,endCol):
    if endPiece.islower() and not color:
        piece_moves[1].append([(r,c),(endRow,endCol), 0])   #Necesito el 3er termino? Total, no califico lo que el rival podria hacer
        return piece_moves

    elif endPiece.isupper() and color:
        piece_moves[1].append([(r,c),(endRow,endCol), 0])
        return piece_moves

    return piece_moves


