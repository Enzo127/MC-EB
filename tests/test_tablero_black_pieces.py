import unittest
import tablero

class test_tablero_black_pieces(unittest.TestCase):
    '''
    Inicio el test como jugador negro y coloco piezas de forma estrategica en el tablero para analizar situaciones criticas y ver si las funciones que invocan responden 
    de la manera esperada, las piezas a analizar (fila, columna) son:

     PIEZAS     |  Test 1   |   Test 2   |  Test 3
    ---------------------------------------------------
    -Peones     |  (3,2)    |  (6,13)    |    (3,15)
    -Caballos   |  (9,1)    |  (5,5)     |    
    -Alfil      |  (6,1)    |  (11,8)    |   
    -Torre      |  (8,0)    |  (13,15)   |   
    -Reina      |  (4,2)    |  (12,14)   |    
    -Rey        |  (4,0)    |  (12,9)    |    

    Edit: Las piezas se han agrupado un poco para considerar principalmente situaciones criticas y no analizar de mas movimientos a espacios vacios (que son los mas comunes)

    '''
    def setUp(self):
        self.game_TEST = tablero.game(False)
        self.moves = [[],[]]
        self.game_TEST.board = [
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'R', 'H', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', ' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['k', 'B', 'q', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' '],
            ['Q', ' ', ' ', ' ', ' ', 'h', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', 'K', ' ', ' ', ' '],
            ['r', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'h', ' ', ' ', ' ', 'r', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'k', 'P', 'P', 'P', 'P', 'q', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'r'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]


    ####                            PIEZAS NEGRAS                            ####

    #TEST PAWNS
    def test_Pawn_black_1(self):
        #Test 1
        move_capture = [[(3, 2), (4, 1), 0, 'pB'], [(3, 2), (4, 3), 0, 'pK']]
        move_free    = [ ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Pawn_Moves(3, 2, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Pawn_black_2(self):
        #Test 2
        move_capture = [[(6, 13), (7, 12), 0, 'pK']]
        move_free    = [[(6, 13), (7, 13), 0] ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Pawn_Moves(6, 13, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Pawn_black_3(self):
        #Test 2
        move_capture = []
        move_free    = [[(3, 15), (5, 15), 0] ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Pawn_Moves(3, 15, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    #TEST KNIGHTS
    def test_Knight_black_1(self):
        #Test 1
        move_capture = [ [(9, 1), (8, 3), 0, 'hB'] ]
        move_free    = [ [(9, 1), (7, 0), 0], [(9, 1), (7, 2), 0], [(9, 1), (10, 3), 0], [(9, 1), (11, 0), 0], [(9, 1), (11, 2), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Knight_Moves(9, 1, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Knight_black_2(self):
        #Test 2
        move_capture = [[(5, 5), (4, 3), 0, 'hK'], [(5, 5), (7, 6), 0, 'hQ'] ]
        move_free    = [[(5, 5), (4, 7), 0], [(5, 5), (6, 3), 0], [(5, 5), (6, 7), 0], [(5, 5), (7, 4), 0] ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Knight_Moves(5, 5, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)


    #TEST BISHOP 
    def test_Bishop_black_1(self):
        move_capture = [[(6, 1), (5, 0), 0, 'bQ'], [(6, 1), (4, 3), 0, 'bK'], [(6, 1), (8, 3), 0, 'bB']]
        move_free    = [[(6, 1), (5, 2), 0], [(6, 1), (7, 0), 0], [(6, 1), (7, 2), 0] ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Bishop_Moves(6, 1, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Bishop_black_2(self):
        #Test 2
        move_capture = [[(11, 8), (9, 6), 0, 'bH'], [(11, 8), (7, 12), 0, 'bK'], [(11, 8), (12, 7), 0, 'bP'] ]
        move_free    = [[(11, 8), (10, 7), 0], [(11, 8), (10, 9), 0], [(11, 8), (9, 10), 0], [(11, 8), (8, 11), 0] ]
        actual_move  = [move_capture ,move_free]
        
        self.game_TEST.get_Bishop_Moves(11, 8, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)


    #TEST ROOK
    def test_Rook_black_1(self):
        #Test 1
        move_capture = [[(8, 0), (5, 0), 0, 'rQ'], [(8, 0), (8, 3), 0, 'rB'] ]
        move_free    = [[(8, 0), (7, 0), 0], [(8, 0), (6, 0), 0], [(8, 0), (9, 0), 0], [(8, 0), (10, 0), 0], [(8, 0), (11, 0), 0], [(8, 0), (8, 1), 0], [(8, 0), (8, 2), 0] ]
        actual_move  = [move_capture ,move_free]
    
        self.game_TEST.get_Rook_Moves(8, 0, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Rook_black_2(self):
        #Test 2
        move_capture = [[(13, 15), (12, 15), 0, 'rP'], [(13, 15), (13, 14), 0, 'rP'], [(13, 15), (14, 15), 0, 'rR'] ]
        move_free    = [ ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Rook_Moves(13, 15, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)


    #TEST QUEEN
    #Este test tiene una particularidad, recorda que el metodo "get_Queen_Moves" esta conformado por los metodos "get_Bishop_Moves" y "get_Rook_Moves"
    #Hay que llamar al metodo "queen_Nomenclature_Captures" para colocar la nomenclatura correcta a la lista de los movimientos de la reina
    def test_Queen_black_1(self):
        #Test 1
        move_capture = [[(4, 2), (4, 1), 0, 'qB'], [(4, 2), (12, 2), 0, 'qP'], [(4, 2), (4, 3), 0, 'qK'], [(4, 2), (12, 10), 0, 'qP'] ]
        move_free    = [[(4, 2), (5, 2), 0], [(4, 2), (6, 2), 0], [(4, 2), (7, 2), 0], [(4, 2), (8, 2), 0], [(4, 2), (9, 2), 0], [(4, 2), (10, 2), 0], [(4, 2), (11, 2), 0], [(4, 2), (3, 1), 0], [(4, 2), (5, 1), 0], [(4, 2), (6, 0), 0], [(4, 2), (5, 3), 0], [(4, 2), (6, 4), 0], [(4, 2), (7, 5), 0], [(4, 2), (8, 6), 0], [(4, 2), (9, 7), 0], [(4, 2), (10, 8), 0], [(4, 2), (11, 9), 0] ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Queen_Moves(4, 2, self.moves, 0, 0)
        self.game_TEST.queen_Nomenclature_Captures(self.moves)

        self.assertEqual(self.moves, actual_move)

    def test_Queen_black_2(self):
        #Test 2
        move_capture = [[(12, 14), (12, 13), 0, 'qP'], [(12, 14), (13, 14), 0, 'qP'], [(12, 14), (12, 15), 0, 'qP'], [(12, 14), (13, 13), 0, 'qP'] ]
        move_free    = [[(12, 14), (11, 14), 0], [(12, 14), (10, 14), 0], [(12, 14), (9, 14), 0], [(12, 14), (8, 14), 0], [(12, 14), (7, 14), 0], [(12, 14), (6, 14), 0], [(12, 14), (5, 14), 0], [(12, 14), (4, 14), 0], [(12, 14), (11, 13), 0], [(12, 14), (10, 12), 0], [(12, 14), (9, 11), 0], [(12, 14), (8, 10), 0], [(12, 14), (7, 9), 0], [(12, 14), (6, 8), 0], [(12, 14), (5, 7), 0], [(12, 14), (4, 6), 0], [(12, 14), (11, 15), 0] ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Queen_Moves(12, 14, self.moves, 0, 0)
        self.game_TEST.queen_Nomenclature_Captures(self.moves)

        self.assertEqual(self.moves, actual_move)


    #TEST KING
    def test_King_black_1(self):
        #Test 1
        move_capture = [[(4, 0), (4, 1), 0, 'kB'], [(4, 0), (5, 0), 0, 'kQ'] ]
        move_free    = [[(4, 0), (3, 1), 0], [(4, 0), (5, 1), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_King_Moves(4, 0, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_King_black_2(self):
        #Test 2
        move_capture = [[(12, 9), (12, 8), 0, 'kP'], [(12, 9), (12, 10), 0, 'kP'], [(12, 9), (13, 8), 0, 'kP'], [(12, 9), (13, 9), 0, 'kP'], [(12, 9), (13, 10), 0, 'kP'] ]
        move_free    = [[(12, 9), (11, 9), 0], [(12, 9), (11, 10), 0] ]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_King_Moves(12, 9, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)