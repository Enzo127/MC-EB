#Class responsible for determining the valid moves at the current state
#import os.path
class Game_State():
    def __init__(self,color):           #Cuando creo el juego, debo guardar el color con el que se jugara la partida
        self.turn = color
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
    
    best_col = {-5:0,-4:0,-3:0,-2:0,-1:0       ,0:0 ,1:0 ,2:0 ,3:1 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0 ,9:0 ,10:0 ,11:0 ,12:0 ,13:0 ,14:0 ,15:0      ,16:0,17:0,18:0,19:0,20:0}
    q_quantity_row_tactical      = 0
    q_quantity_row_upgrade_mia   = 0
    q_quantity_row_upgrade_rival = 0    #Reinas mias en la de upgrade rival
    Q_quantity_row_upgrade_rival = 0    #Reinas rvales en su fila de upgrade

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
            self.turn = not self.turn
            
        
        if self.turn:
            piece_moves = {"H": knight_moves, "B": bishop_moves,"R": rook_moves,"P": pawn_moves,"Q": queen_moves,"K": king_moves}
        else:
            piece_moves = {"h": knight_moves, "b": bishop_moves,"r": rook_moves,"p": pawn_moves,"q": queen_moves,"k": king_moves}


        for r in range(len(self.board)):                                                        #numero de filas
            for c in range(len(self.board[r])):                                                 #numero de columnas para una fila dada
                piece = self.board[r][c][0]                                                     #Leo y guardo el contenido del casillero
                if piece != " ":                                                                #Si el casillero esta vacio, lo desestimo
                    if (self.turn and piece.isupper()) or (not self.turn and piece.islower()):  #
                        self.move_Functions[piece](r ,c ,piece_moves[piece] ,change, 0)            #LLamo a la funcion correspondiente // el ultimo termino solo sirve como extra (se aplica cuando llamas a la reina)

        #Vuelvo el color a la normalidad
        if change == 1:                                  
            self.turn = not self.turn

        queen_moves = self.queen_Nomenclature_Captures(queen_moves)

        moves = [knight_moves, bishop_moves, rook_moves, pawn_moves, queen_moves, king_moves]
        return moves


    #reajusto la nomenclatura en los movimientos de captura de la reina, ya que al llamar a las funciones "getBishopMoves" y "getRookMoves", se asignaban las letras incorrectas
    #Arregla la nomenclatura de la lista que tiene los movimientos con captura de la reina
    def queen_Nomenclature_Captures(self, queen_moves):
        for movement in queen_moves[0]:                
            letter = movement[3][1]
            if self.turn:
                movement[3] = "Q"+letter
            else:
                movement[3] = "q"+letter

        return queen_moves


#Get all the pawn moves for the pawn locatd at row, col and add these moves to the list
#Me parece que seria mas eficiente hacer una clase "pieza" y dentro de esa clase o como herencia poner todas las piezas
#Metiendo ademas los distintos tipos de movimiento como metodos, pero que se yo, fijate

#Aca investiga, serie bueno crear una clase pieza, tal que todas las sgtes funciones sean metodos de pieza y que pieza herede game
    def get_Pawn_Moves(self,r,c,pawn_moves,change,extra): 
        if self.turn:    #deberias pasar otro parametro = color, capaz mas arriba, pero aca verificas(una sola vez hace falta verificar, hacelo con un if y un flag)
            if self.board[r-1][c] == " " and change==0: #1 square pawn advance  
                if (r == 13 or r ==12) and self.board[r-2][c] == " ": #2 square pawn advance
                    pawn_moves[1].append([(r,c),(r-2,c),0])
                else:
                    pawn_moves[1].append([(r,c),(r-1,c),0])             #Guardo el movimiento de 1 avance SOLO si no puedo avanzar de a 2

            if c-1 >= 0: #captures to the left
                if self.board[r-1][c-1][0].islower() or (self.board[r-1][c-1][0].isupper() and change==1): #enemy piece to capture
                    pawn_moves[0].append([(r,c),(r-1,c-1), 0, "P"+self.board[r-1][c-1][0]])
            if c+1 <= 15: #captures to the right
                if self.board[r-1][c+1][0].islower() or (self.board[r-1][c+1][0].isupper() and change==1): #enemy piece to capture
                    pawn_moves[0].append([(r,c),(r-1,c+1), 0, "P"+self.board[r-1][c+1][0]])

        else:
            if self.board[r+1][c] == " " and change==0: #1 square pawn advance 
                
                if (r == 2 or r ==3) and self.board[r+2][c] == " ": #2 square pawn advance

                    pawn_moves[1].append([(r,c),(r+2,c),0])
                else:
                    pawn_moves[1].append([(r,c),(r+1,c),0])           #Guardo el movimiento de 1 avance SOLO si no puedo avanzar de a 2

            if c-1 >= 0: #captures to the left
                if self.board[r+1][c-1][0].isupper() or (self.board[r+1][c-1][0].islower() and change==1): #enemy piece to capture
                    pawn_moves[0].append([(r,c),(r+1,c-1), 0, "p"+self.board[r+1][c-1][0]])
            if c+1 <= 15: #captures to the right
                if self.board[r+1][c+1][0].isupper() or (self.board[r+1][c+1][0].islower() and change==1): #enemy piece to capture
                    pawn_moves[0].append([(r,c),(r+1,c+1), 0, "p"+self.board[r+1][c+1][0]])


    def get_Rook_Moves(self,r,c,rook_moves,change,extra):
        directions = ((-1,0),(0,-1),(1,0),(0,1))
        #OPTIMIZAR
        extra=0
        if self.turn:
            color = "white"
        else:
            color = "black"

        for d in directions:
            for i in range(1,16):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if (0 <= endRow < 16) and (0 <= endCol < 16): #on board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == " ": #empty space valid
                        rook_moves[1].append([(r,c),(endRow,endCol),extra])
                        
                    elif (endPiece[0].islower() and color=="white") or (endPiece[0].isupper() and change==1): #enemy piece valid
                        rook_moves[0].append([(r,c),(endRow,endCol), extra, "R"+endPiece[0]])
                        break

                    elif (endPiece[0].isupper() and color=="black") or (endPiece[0].islower() and change==1): #enemy piece valid
                        rook_moves[0].append([(r,c),(endRow,endCol), extra, "r"+endPiece[0]])
                        break

                    else:   #friendly piece invalid
                        break
                else:       #off board
                    break

    def get_Bishop_Moves(self,r,c,bishop_moves,change,queen_call):
        directions = ((-1,-1),(-1,1),(1,-1),(1,1))
        if self.turn:
            color = "white"
        else:
            color = "black"

        if self.turn:
            row_upgrade_mia   = 8
            row_upgrade_rival = 7
            row_tactical      = 9

        if not self.turn:
            row_upgrade_mia   = 7
            row_upgrade_rival = 8
            row_tactical      = 6

        for d in directions:
            for i in range(1,16):        #bishops can move max of 7 squares
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if (0 <= endRow < 16) and (0 <= endCol < 16): #on board
                    extra = 0
                    if queen_call != 0:        

                        if (self.q_quantity_row_upgrade_mia > 1)    and (self.q_quantity_row_tactical == 0) and (endRow == row_tactical) and (r == row_upgrade_mia):
                            extra = extra + 1000
                        if (self.q_quantity_row_upgrade_rival == 0) and (self.Q_quantity_row_upgrade_rival == 0) and (endRow == row_upgrade_rival) and (r == row_upgrade_mia):
                            extra = extra + 10000


                    endPiece = self.board[endRow][endCol]                   
                    if endPiece == " ": #empty space valid
                        bishop_moves[1].append([(r,c),(endRow,endCol),extra])


                    elif (endPiece[0].islower() and color=="white") or (endPiece[0].isupper() and change==1): #enemy piece valid
                        bishop_moves[0].append([(r,c),(endRow,endCol), extra, "B"+endPiece[0]])
                        break

                    elif (endPiece[0].isupper() and color=="black") or (endPiece[0].islower() and change==1): #enemy piece valid
                        bishop_moves[0].append([(r,c),(endRow,endCol), extra, "b"+endPiece[0]])
                        break
                    else:   #friendly piece invalid
                        break
                else:       #off board
                    break

    def get_Queen_Moves(self,r,c,queen_moves,change,extra):
        extra = 1
        if change==0:
            self.queens_Quantity=self.queens_Quantity+1
            #Analisis tactico
            if self.turn:
                #row_upgrade_mia   = 8
                row_upgrade_rival = 7
                row_tactical      = 9

            if not self.turn:
                #row_upgrade_mia   = 7
                row_upgrade_rival = 8
                row_tactical      = 6

            if (self.q_quantity_row_upgrade_mia > 1)    and (self.q_quantity_row_tactical == 0) and (r == row_tactical):
                extra = extra + 1000
            if (self.q_quantity_row_upgrade_rival == 0) and (self.Q_quantity_row_upgrade_rival == 0) and (r == row_upgrade_rival):
                extra = extra + 10000
        
        self.get_Rook_Moves(r,c,queen_moves,change,extra)              
        self.get_Bishop_Moves(r,c,queen_moves,change,extra)

    def get_Knight_Moves(self,r,c,knight_moves,change,extra):
        directions = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))
        if self.turn:
            color = "white"
        else:
            color = "black"
        for m in directions:
            endRow = r + m[0]
            endCol = c + m[1]
            if (0 <= endRow < 16) and (0 <= endCol < 16):
                endPiece = self.board[endRow][endCol]
                if endPiece[0]==" ":                                        #not an ally piece (empty or enemy piece)
                    knight_moves[1].append([(r,c),(endRow,endCol),0])

                elif (endPiece[0].islower() and color=="white") or (endPiece[0].isupper() and change==1):  
                    knight_moves[0].append([(r,c),(endRow,endCol), 0, "H"+endPiece[0]])

                elif (endPiece[0].isupper() and color=="black") or (endPiece[0].islower() and change==1):
                    knight_moves[0].append([(r,c),(endRow,endCol), 0, "h"+endPiece[0]])
                    
    def get_King_Moves(self,r,c,king_moves,change,extra): 
        directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        if self.turn:
            color = "white"
        else:
            color = "black"
        for i in range(8):
            endRow = r + directions[i][0]
            endCol = c + directions[i][1]
            if (0 <= endRow < 16) and (0 <= endCol < 16):
                endPiece = self.board[endRow][endCol]
                if endPiece[0]==" ":                                        #not an ally piece (empty or enemy piece)
                    king_moves[1].append([(r,c),(endRow,endCol),0])

                if (endPiece[0].islower() and color=="white") or (endPiece[0].isupper() and change==1):  
                    king_moves[0].append([(r,c),(endRow,endCol), 0, "K"+endPiece[0]])

                elif (endPiece[0].isupper() and color=="black") or (endPiece[0].islower() and change==1):
                    king_moves[0].append([(r,c),(endRow,endCol), 0, "k"+endPiece[0]])


    def columna_Rating(self):

        #Este seteo se deberia hacer una sola vez en la partida, lo podrias meter en el init
        if self.turn:
            row_upgrade_mia   = 8
            row_upgrade_rival = 7
            row_tactical      = 9
            reina_mia         = "Q"
            reina_rival       = "q"

        else:
            row_upgrade_mia   = 7
            row_upgrade_rival = 8
            row_tactical      = 6
            reina_mia         = "q"
            reina_rival       = "Q"

        #Esto se tiene que resetear todos los turnos
        self.best_col = {-5:-10,-4:-10,-3:-10,-2:-10,-1:-10       ,0:0 ,1:0 ,2:0 ,3:1 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0 ,9:0 ,10:0 ,11:0 ,12:0 ,13:0 ,14:0 ,15:0      ,16:-10,17:-10,18:-10,19:-10,20:-10}
        self.q_quantity_row_tactical      = 0
        self.q_quantity_row_upgrade_mia   = 0
        self.q_quantity_row_upgrade_rival = 0    #Reinas mias en la de upgrade rival
        self.Q_quantity_row_upgrade_rival = 0    #Reinas rvales en su fila de upgrade

        #1) Analisis: Cantidad de reinas mias en row tactical
        for col in range(len(self.board[row_tactical])):
            if reina_mia == self.board[row_tactical][col]:
                self.q_quantity_row_tactical = self.q_quantity_row_tactical + 1

        #2) Analisis: Cantidad de reinas mias en row upgrade y la columna en que se encuentra
        for col in range(len(self.board[row_upgrade_mia])):
            if reina_mia == self.board[row_upgrade_mia][col]:
                self.q_quantity_row_upgrade_mia = self.q_quantity_row_upgrade_mia + 1

                if self.q_quantity_row_tactical == 0:                           #Lo que quisiste decir aca es: Si no tengo reinas propias en row_tactical, avanza peones en la columna al lado de una reina que tengas en row_upgrade
                    self.best_col[col+1] = self.best_col[col+1] + 5             #El problema es que esta suma la hace siempre, NO referida a si tenes una reina en row_upgrade
                    self.best_col[col-1] = self.best_col[col-1] + 5

                else:
                    self.best_col[col+2] = self.best_col[col+2] + 8
                    self.best_col[col-2] = self.best_col[col-2] + 8

        #3) Analisis: Cantidad de reinas rivales en su upgrade, cantidad de reinas propias en su upgrade y la columna en la que se encuentra la reina del rival (si las hay)
        for col in range(len(self.board[row_upgrade_rival])):
            if reina_mia == self.board[row_upgrade_rival][col]:
                self.q_quantity_row_upgrade_rival = self.q_quantity_row_upgrade_rival + 1   #verifico si tengo reinas propias en la fila de upgrade rival
            if reina_rival == self.board[row_upgrade_rival][col]:
                self.Q_quantity_row_upgrade_rival = self.Q_quantity_row_upgrade_rival + 1   #verifico si tengo reinas propias en la fila de upgrade rival

            if reina_rival == self.board[row_upgrade_rival][col]:
                
                self.best_col[col]   = self.best_col[col]   - 4 
                self.best_col[col+1] = self.best_col[col+1] - 3 
                self.best_col[col-1] = self.best_col[col+1] - 3 
                self.best_col[col+2] = self.best_col[col+2] - 2 
                self.best_col[col-2] = self.best_col[col-2] - 2 
                self.best_col[col+3] = self.best_col[col+3] - 1 
                self.best_col[col-3] = self.best_col[col-3] - 1 
                self.best_col[col+4] = self.best_col[col+4] + 1 
                self.best_col[col-4] = self.best_col[col-4] + 1 
                
        
