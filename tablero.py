#Class responsible for determining the valid moves at the current state
#import os.path
class game():
    def __init__(self,turn):           #Cuando creo el juego, debo guardar el color con el que se jugara la partida
        self.color = turn
        self.move_Functions = {"P": self.get_Pawn_Moves, "R": self.get_Rook_Moves, "H":self.get_Knight_Moves, "B": self.get_Bishop_Moves,"Q": self.get_Queen_Moves,"K": self.get_King_Moves,
                               "p": self.get_Pawn_Moves, "r": self.get_Rook_Moves, "h":self.get_Knight_Moves, "b": self.get_Bishop_Moves,"q": self.get_Queen_Moves,"k": self.get_King_Moves}
                               
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
    qm_quantity_row_tactical      = 0
    qm_quantity_row_upgrade_mia   = 0
    qm_quantity_row_upgrade_rival = 0    #Reinas mias en la de upgrade rival
    qr_quantity_row_upgrade_rival = 0    #Reinas rvales en su fila de upgrade

    row_upgrade_mia   = 0
    row_upgrade_rival = 0
    row_tactical      = 0
    reina_mia         = 0
    reina_rival       = 0
    valor_row_strategy = {7:3 ,8:2 ,9:1 ,6:1}

    #Actualizar con el estado actual del tablero
    def Actualizar (self, refresh):
        i=0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.board[r][c] = refresh[i]
                i=i+1

    #All moves without considering cheks
    def get_All_Possible_Moves(self,change):    
        pawn_moves   = [[],[]]                   #pawn_moves[0] = Capture piece    //  pawn_moves[1] = Move to blank space
        rook_moves   = [[],[]]                    
        bishop_moves = [[],[]]
        queen_moves  = [[],[]]                    #OPTIMIZA ESTO, HACELO CON UN FOR O ALGO ASI, QUE SE YO
        knight_moves = [[],[]]
        king_moves   = [[],[]]
         
        
        #Ahora obtenemos las capturas de las piezas negras sobre piezas negras(o viceversa)(recaptura por si las blancas toman esa pieza) y a lugares vacios (para evitar movernos a ellos).
        #Si nos fijamos en la funcion de peones, NO vamos a obtener los movimientos a lugares libres, pero eso es una VENTAJA, ya que los peones solo pueden capturar hacia los costados (y esos si los guardamos).
        if change == 1:                                  
            self.color = not self.color
            
        
        if self.color:
            piece_moves = {"H": knight_moves, "B": bishop_moves,"R": rook_moves,"P": pawn_moves,"Q": queen_moves,"K": king_moves}
        else:
            piece_moves = {"h": knight_moves, "b": bishop_moves,"r": rook_moves,"p": pawn_moves,"q": queen_moves,"k": king_moves}


        for r in range(len(self.board)):                                                        #numero de filas
            for c in range(len(self.board[r])):                                                 #numero de columnas para una fila dada
                piece = self.board[r][c][0]                                                     #Leo y guardo el contenido del casillero
                if piece != " ":                                                                #Si el casillero esta vacio, lo desestimo
                    if (self.color and piece.isupper()) or (not self.color and piece.islower()):  #
                        self.move_Functions[piece](r ,c ,piece_moves[piece] ,change)            #LLamo a la funcion correspondiente // el ultimo termino solo sirve como extra (se aplica cuando llamas a la reina)

        #Vuelvo el color a la normalidad
        if change == 1:                                  
            self.color = not self.color

        queen_moves = self.queen_Nomenclature_Captures(queen_moves)

        #moves = [knight_moves, bishop_moves, rook_moves, pawn_moves, king_moves, queen_moves]
        moves = [pawn_moves,knight_moves, bishop_moves, rook_moves,  king_moves, queen_moves]
        return moves


    #reajusto la nomenclatura en los movimientos de captura de la reina, ya que al llamar a las funciones "getBishopMoves" y "getRookMoves", se asignaban las letras incorrectas
    #Arregla la nomenclatura de la lista que tiene los movimientos con captura de la reina
    def queen_Nomenclature_Captures(self, queen_moves):
        for movement in queen_moves[0]:                
            letter = movement[3][1]
            if self.color:
                movement[3] = "Q"+letter
            else:
                movement[3] = "q"+letter

        return queen_moves


#Get all the pawn moves for the pawn locatd at row, col and add these moves to the list
#Me parece que seria mas eficiente hacer una clase "pieza" y dentro de esa clase o como herencia poner todas las piezas
#Metiendo ademas los distintos tipos de movimiento como metodos, pero que se yo, fijate

#Aca investiga, serie bueno crear una clase pieza, tal que todas las sgtes funciones sean metodos de pieza y que pieza herede game
    def get_Pawn_Moves(self,r,c,pawn_moves,change): 
        if self.color:    #deberias pasar otro parametro = color, capaz mas arriba, pero aca verificas(una sola vez hace falta verificar, hacelo con un if y un flag)
            if self.board[r-1][c] == " " and change==0: #1 square pawn advance  
                if (r == 13 or r ==12) and self.board[r-2][c] == " ": #2 square pawn advance
                    pawn_moves[1].append([(r,c),(r-2,c),0])
                else:
                    pawn_moves[1].append([(r,c),(r-1,c),0])             #Guardo el movimiento de 1 avance SOLO si no puedo avanzar de a 2

            if c-1 >= 0: #captures to the left
                if change ==1:
                    pawn_moves[1].append([(r,c),(r-1,c-1), 0, "P"+self.board[r-1][c-1][0]])

                if self.board[r-1][c-1][0].islower(): #enemy piece to capture
                    pawn_moves[0].append([(r,c),(r-1,c-1), 0, "P"+self.board[r-1][c-1][0]])


            if c+1 <= 15: #captures to the right
                if change ==1:
                    pawn_moves[1].append([(r,c),(r-1,c+1), 0, "P"+self.board[r-1][c+1][0]])

                if self.board[r-1][c+1][0].islower(): #enemy piece to capture
                    pawn_moves[0].append([(r,c),(r-1,c+1), 0, "P"+self.board[r-1][c+1][0]])




        else:
            if self.board[r+1][c] == " " and change==0: #1 square pawn advance 
                
                if (r == 2 or r ==3) and self.board[r+2][c] == " ": #2 square pawn advance

                    pawn_moves[1].append([(r,c),(r+2,c),0])
                else:
                    pawn_moves[1].append([(r,c),(r+1,c),0])           #Guardo el movimiento de 1 avance SOLO si no puedo avanzar de a 2

            if c-1 >= 0: #captures to the left
                if change ==1:
                    pawn_moves[1].append([(r,c),(r+1,c-1), 0, "p"+self.board[r+1][c-1][0]])

                if self.board[r+1][c-1][0].isupper(): #enemy piece to capture
                    pawn_moves[0].append([(r,c),(r+1,c-1), 0, "p"+self.board[r+1][c-1][0]])

            if c+1 <= 15: #captures to the right
                if change ==1:
                    pawn_moves[1].append([(r,c),(r+1,c+1), 0, "p"+self.board[r+1][c+1][0]])

                if self.board[r+1][c+1][0].isupper(): #enemy piece to capture
                    pawn_moves[0].append([(r,c),(r+1,c+1), 0, "p"+self.board[r+1][c+1][0]])


    def get_Bishop_Moves(self,r,c,bishop_moves,change):
        directions = ((-1,-1),(-1,1),(1,-1),(1,1))
        extra = 0
        for d in directions:
            for i in range(1,16):        #bishops can move max of 7 squares
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if (0 <= endRow < 16) and (0 <= endCol < 16): #on board
                    
                    endPiece = self.board[endRow][endCol]                   
                    if endPiece == " ": #empty space valid
                        bishop_moves[1].append([(r,c),(endRow,endCol),extra])


                    elif endPiece.islower() and self.color: #enemy piece valid
                        bishop_moves[0].append([(r,c),(endRow,endCol), extra, "B"+endPiece])
                        break

                    elif endPiece.isupper() and not self.color: #enemy piece valid
                        bishop_moves[0].append([(r,c),(endRow,endCol), extra, "b"+endPiece])
                        break
                    
                    #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                    elif change==1:  
                        bishop_moves = analisis_rival(bishop_moves,endPiece, self.color, r,c,endRow,endCol)
                        break                    
                    
                    
                    
                    else:   #friendly piece invalid
                        break
                else:       #off board
                    break


    def get_Rook_Moves(self,r,c,rook_moves,change):
        directions = ((-1,0),(0,-1),(1,0),(0,1))
        extra=0
        for d in directions:
            for i in range(1,16):
                endRow = r + d[0] * i
                endCol = c + d[1] * i

                if (0 <= endRow < 16) and (0 <= endCol < 16): #on board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == " ": #empty space valid
                        rook_moves[1].append([(r,c),(endRow,endCol),extra])

                    elif endPiece.islower() and self.color: #enemy piece valid
                        rook_moves[0].append([(r,c),(endRow,endCol), extra, "R"+endPiece])
                        break
                        
                    elif endPiece.isupper() and not self.color: #enemy piece valid
                        rook_moves[0].append([(r,c),(endRow,endCol), extra, "r"+endPiece])
                        break

                    #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                    elif change==1:  
                        rook_moves = analisis_rival(rook_moves,endPiece, self.color, r,c,endRow,endCol)
                        break

                    else:   #friendly piece invalid
                        break
                else:       #off board
                    break


    def get_Queen_Moves(self,r,c,queen_moves,change):
        if change==0:
            self.queens_Quantity=self.queens_Quantity+1     #Contador de numero de reinas para el tablero actual
        
        self.get_Rook_Moves(r,c,queen_moves,change)              
        self.get_Bishop_Moves(r,c,queen_moves,change)


    def get_Knight_Moves(self,r,c,knight_moves,change):
        directions = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))

        for m in directions:
            endRow = r + m[0]
            endCol = c + m[1]
            if (0 <= endRow < 16) and (0 <= endCol < 16):
                endPiece = self.board[endRow][endCol]
                if endPiece==" ":                                        #not an ally piece (empty or enemy piece)
                    knight_moves[1].append([(r,c),(endRow,endCol),0])

                elif endPiece.islower() and self.color:  
                    knight_moves[0].append([(r,c),(endRow,endCol), 0, "H"+endPiece])

                elif endPiece.isupper() and not self.color:
                    knight_moves[0].append([(r,c),(endRow,endCol), 0, "h"+endPiece])
                    
                #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                elif change==1:  
                    knight_moves = analisis_rival(knight_moves,endPiece, self.color, r,c,endRow,endCol)


    def get_King_Moves(self,r,c,king_moves,change): 
        directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

        for i in range(8):
            endRow = r + directions[i][0]
            endCol = c + directions[i][1]
            if (0 <= endRow < 16) and (0 <= endCol < 16):
                endPiece = self.board[endRow][endCol]
                if endPiece==" ":                                        #not an ally piece (empty or enemy piece)
                    king_moves[1].append([(r,c),(endRow,endCol),0])

                if endPiece.islower() and self.color:  
                    king_moves[0].append([(r,c),(endRow,endCol), 0, "K"+endPiece])

                elif endPiece.isupper() and not self.color:
                    king_moves[0].append([(r,c),(endRow,endCol), 0, "k"+endPiece])

                #Cuando change==1, debo verificar que piezas el rival puede defender ante capturas mias (analizo si el rival puede recapturar sus piezas)
                elif change==1:  
                    king_moves = analisis_rival(king_moves,endPiece, self.color, r,c,endRow,endCol)
                

    #Estas variables se inicial por defecto para las piezas blancas, pero si me tocan negras, las cambio por las correctas
    def seteo_Inicial(self, color):
        if color:
            self.row_upgrade_mia    = 8
            self.row_upgrade_rival  = 7
            self.row_tactical       = 9
            self.reina_mia          = "Q"
            self.reina_rival        = "q"
            self.valor_row_strategy = {7:3 ,8:2 ,9:1 ,6:1}   #deberian bajar su valor, dependiendo la cantidad de reinas en la fila (-1 por cada reina, capeado a 0)

        else:
            self.row_upgrade_mia    = 7
            self.row_upgrade_rival  = 8
            self.row_tactical       = 6
            self.reina_mia          = "q"
            self.reina_rival        = "Q"
            self.valor_row_strategy = {8:3 ,7:2 ,6:1 ,9:1}
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
    #ESTAS 3 DEBERIAN SEPARARSE EN 3 FUNCIONES MAS PEQUEÑAS
    #ESTAS 3 DEBERIAN SEPARARSE EN 3 FUNCIONES MAS PEQUEÑAS
    
    #este sistema de asignacion de puntos es medio malo, creo que analizar los eventos de cada columna es MUCHISIMO mejor
    def columna_Rating(self):
        #Esto se tiene que resetear todos los turnos
        self.best_col = {0:0 ,1:0 ,2:0 ,3:0 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0 ,9:0 ,10:0 ,11:0 ,12:0 ,13:0 ,14:0 ,15:0 }
        self.qm_quantity_row_tactical      = 0
        self.qm_quantity_row_upgrade_mia   = 0   
        self.qm_quantity_row_upgrade_rival = 0    #Reinas mias en la de upgrade rival    // qm = queen mia
        self.qr_quantity_row_upgrade_rival = 0    #Reinas rvales en su fila de upgrade   // qr = queen rival


        #ESTAS 3 DEBERIAN SEPARARSE EN 3 FUNCIONES MAS PEQUEÑAS

        #1) Analisis: Cantidad de reinas mias en row tactical
        for col in range(len(self.board[self.row_tactical])):
            if self.reina_mia == self.board[self.row_tactical][col]:
                self.qm_quantity_row_tactical = self.qm_quantity_row_tactical + 1

                self.best_col[col] = self.best_col[col] - 20                    #Si tengo una reina en la fila de tactica, no conviene mover el peon que esta detras de ella (ya que los bloquea mi propia pieza)
                                                                                #Conviene mas mover peones de otra columna para coronarlos


        #2) Analisis: Cantidad de reinas mias en row upgrade y la columna en que se encuentra
        for col in range(len(self.board[self.row_upgrade_mia])):
            if self.reina_mia == self.board[self.row_upgrade_mia][col]:
                self.qm_quantity_row_upgrade_mia = self.qm_quantity_row_upgrade_mia + 1

                self.best_col[col] = self.best_col[col] - 20                    #Si tengo una reina en la fila de coronacion, no conviene mover el peon que esta detras de ella (ya que los bloquea mi propia pieza)
                                                                                #Conviene mas mover peones de otra columna para coronarlos

                if self.qm_quantity_row_tactical == 0:                           #Si no tengo reinas propias en row_tactical, avanzar peones en la columna al lado de una reina que tengas en row_upgrade
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
        for col in range(len(self.board[self.row_upgrade_rival])):
            if self.reina_mia == self.board[self.row_upgrade_rival][col]:
                self.qm_quantity_row_upgrade_rival = self.qm_quantity_row_upgrade_rival + 1   #verifico si tengo reinas propias en la fila de upgrade rival
            if self.reina_rival == self.board[self.row_upgrade_rival][col]:
                self.qr_quantity_row_upgrade_rival = self.qr_quantity_row_upgrade_rival + 1   #verifico si tengo reinas propias en la fila de upgrade rival
         
                self.best_col[col]   = self.best_col[col]   - 9                   #Mover un peon en una columna en la cual hay una reina rival en row_upgrade_rival no es una buena idea
                for i in range(1,4):

                    if col+i <= 15:
                        self.best_col[col+i] = self.best_col[col+i] + (i*3-9)     #Evaluo mal a las columnas alrededor de una reina rival en row_upgrade_rival (es donde principalmente se suelen encontrar)

                    if col-i >= 0:
                        self.best_col[col-i] = self.best_col[col-i] + (i*3-9)     
        

                
 
def analisis_rival(piece_moves ,endPiece ,color ,r ,c ,endRow ,endCol):
    if endPiece.islower() and not color:
        piece_moves[1].append([(r,c),(endRow,endCol), 0, "defiende su pieza"])
        return piece_moves

    elif endPiece.isupper() and color:
        piece_moves[1].append([(r,c),(endRow,endCol), 0, "defiende su pieza"])
        return piece_moves

    return piece_moves
