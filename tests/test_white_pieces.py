import unittest
import ChessEngine_V1

#AAA Rule: Arrange, Act, Assert
class Test_Engine(unittest.TestCase):
    def setUp(self):
        self.game_TEST = ChessEngine_V1.Game_State(True)
        self.moves = [[],[]]
        self.game_TEST.board = [
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'R', 'H', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K'],
            ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'r', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', 'R', ' ', ' ', ' ', ' ', ' ', ' '],
            ['H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', 'k', ' ', 'k', ' ', ' ', 'q', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

    #Comprobacion de color
    def test_turn(self):
        self.assertEqual(self.game_TEST.turn, True)

    ####                            PIEZAS BLANCAS                            ####

    #TEST PAWNS
    def test_Pawn_White_1(self):
        #Test 1
        move_capture = [[(12, 10),(11, 9),0,"Pk"] ,[(12, 10),(11, 11),0,"Pk"] ]
        move_free    = [[(12, 10),(10, 10),0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Pawn_Moves(12, 10, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Pawn_White_2(self):
        #Test 2
        move_capture = [[(12, 15),(11, 14),0,"Pq"]]
        move_free    = [[(12, 15),(11, 15),0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Pawn_Moves(12, 15, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)


    #TEST KNIGHTS
    def test_Knight_White_1(self):
        #Test 1
        move_capture = [[(1, 12), (0, 10), 0, 'Hb'], [(1, 12), (0, 14), 0, 'Hr'], [(1, 12), (2, 10), 0, 'Hp'], [(1, 12), (2, 14), 0, 'Hp'], [(1, 12), (3, 11), 0, 'Hp'], [(1, 12), (3, 13), 0, 'Hp']]
        move_free    = []
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Knight_Moves(1, 12, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Knight_White_2(self):
        #Test 2
        move_capture = [ [(8, 0), (6, 1), 0, 'Hr'] ]
        move_free    = [ [(8, 0), (9, 2), 0], [(8, 0), (10, 1), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Knight_Moves(8, 0, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)


    #TEST BISHOP 
    def test_Bishop_White_1(self):
        """
        metele comentario de lo que representa el actual move
        """
        move_capture = [[(7, 2), (6, 1), 0, 'Br'], [(7, 2), (3, 6), 0, 'Bp']]
        move_free    = [[(7, 2), (6, 3), 0], [(7, 2), (5, 4), 0], [(7, 2), (4, 5), 0], [(7, 2), (8, 1), 0], [(7, 2), (9, 0), 0], [(7, 2), (8, 3), 0], [(7, 2), (9, 4), 0], [(7, 2), (10, 5), 0], [(7, 2), (11, 6), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Bishop_Moves(7, 2, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Bishop_White_2(self):
        #Test 2
        move_capture = [[(7, 8), (3, 4), 0, 'Bp'], [(7, 8), (3, 12), 0, 'Bp']]
        move_free    = [[(7, 8), (6, 7), 0], [(7, 8), (5, 6), 0], [(7, 8), (4, 5), 0], [(7, 8), (6, 9), 0], [(7, 8), (5, 10), 0], [(7, 8), (4, 11), 0], [(7, 8), (8, 7), 0], [(7, 8), (9, 6), 0], [(7, 8), (10, 5), 0], [(7, 8), (11, 4), 0], [(7, 8), (8, 9), 0], [(7, 8), (9, 10), 0], [(7, 8), (10, 11), 0], [(7, 8), (11, 12), 0]]
        actual_move  = [move_capture ,move_free]
        
        self.game_TEST.get_Bishop_Moves(7, 8, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)


    #TEST ROOK
    def test_Rook_White_1(self):
        #Test 1
        move_capture = [[(1, 11), (0, 11), 0, 'Rb'], [(1, 11), (1, 10), 0, 'Rb'], [(1, 11), (2, 11), 0, 'Rp']]
        move_free    = []
        actual_move  = [move_capture ,move_free]
    
        self.game_TEST.get_Rook_Moves(1, 11, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_Rook_White_2(self):
        #Test 2
        move_capture = [[(7, 9), (3, 9), 0, 'Rp'], [(7, 9), (11, 9), 0, 'Rk']]
        move_free    = [[(7, 9), (6, 9), 0], [(7, 9), (5, 9), 0], [(7, 9), (4, 9), 0], [(7, 9), (8, 9), 0], [(7, 9), (9, 9), 0], [(7, 9), (10, 9), 0], [(7, 9), (7, 10), 0], [(7, 9), (7, 11), 0], [(7, 9), (7, 12), 0], [(7, 9), (7, 13), 0], [(7, 9), (7,14), 0], [(7, 9), (7, 15), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Rook_Moves(7, 9, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)


    #TEST QUEEN
    #Este test tiene una particularidad, recorda que el metodo "get_Queen_Moves" esta conformado por los metodos "get_Bishop_Moves" y "get_Rook_Moves"
    #Hay que llamar al metodo "queen_Nomenclature_Captures" para colocar la nomenclatura correcta a la lista de los movimientos de la reina
    def test_Queen_White_1(self):
        #Test 1
        move_capture = [[(5, 0), (3, 0), 0, 'Qp'], [(5, 0), (6, 0), 0, 'Qp'], [(5, 0), (3, 2), 0, 'Qp'], [(5, 0), (6, 1), 0, 'Qr']]
        move_free    = [[(5, 0), (4, 0), 0], [(5, 0), (5, 1), 0], [(5, 0), (5, 2), 0], [(5, 0), (5, 3), 0], [(5, 0), (5, 4), 0], [(5, 0), (5, 5), 0], [(5, 0), (5, 6), 0], [(5, 0), (5, 7), 0], [(5, 0), (5, 8), 0], [(5, 0), (5, 9), 0], [(5, 0), (5, 10), 0], [(5, 0), (5, 11), 0], [(5, 0), (5, 12), 0], [(5, 0), (5, 13), 0], [(5, 0), (5, 14), 0], [(5, 0), (5, 15), 0], [(5, 0), (4, 1), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Queen_Moves(5, 0, self.moves, 0, 0)
        self.game_TEST.queen_Nomenclature_Captures(self.moves)

        self.assertEqual(self.moves, actual_move)

    def test_Queen_White_2(self):
        #Test 2
        move_capture = [[(11, 7), (3, 7), 0, 'Qp'], [(11, 7), (11, 9), 0, 'Qk'], [(11, 7), (3, 15), 0, 'Qp']]
        move_free    = [[(11, 7), (10, 7), 0], [(11, 7), (9, 7), 0], [(11, 7), (8, 7), 0], [(11, 7), (7, 7), 0], [(11, 7), (6, 7), 0], [(11, 7), (5, 7), 0], [(11, 7), (4, 7), 0], [(11, 7), (11, 6), 0], [(11, 7), (11, 5), 0], [(11, 7), (11, 4), 0], [(11, 7), (11, 3), 0], [(11, 7), (11, 2), 0], [(11, 7), (11, 1), 0], [(11, 7), (11, 0), 0], [(11, 7), (11, 8), 0], [(11, 7), (10, 6), 0], [(11, 7), (9, 5), 0], [(11, 7), (8, 4), 0], [(11, 7), (7, 3), 0], [(11, 7), (10, 8), 0], [(11, 7), (9, 9), 0], [(11, 7), (8, 10), 0], [(11, 7), (7, 11), 0], [(11, 7), (6, 12), 0], [(11, 7), (5, 13), 0], [(11, 7), (4, 14), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_Queen_Moves(11, 7, self.moves, 0, 0)
        self.game_TEST.queen_Nomenclature_Captures(self.moves)

        self.assertEqual(self.moves, actual_move)


    #TEST KING
    def test_King_White_1(self):
        #Test 1
        move_capture = [[(6, 2), (6, 1), 0, 'Kr']]
        move_free    = [[(6, 2), (5, 1), 0], [(6, 2), (5, 2), 0], [(6, 2), (5, 3), 0], [(6, 2), (6, 3), 0], [(6, 2), (7, 1), 0], [(6, 2), (7, 3), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_King_Moves(6, 2, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    def test_King_White_2(self):
        #Test 2
        move_capture = [[(4, 15), (3, 14), 0, 'Kp'], [(4, 15), (3, 15), 0, 'Kp']]
        move_free    = [[(4, 15), (4, 14), 0], [(4, 15), (5, 14), 0], [(4, 15), (5, 15), 0]]
        actual_move  = [move_capture ,move_free]

        self.game_TEST.get_King_Moves(4, 15, self.moves, 0, 0)
        self.assertEqual(self.moves, actual_move)

    #Comprobar si se rellena el tablero de forma correcta
    def test_Actualizar(self):
        #Arrange
        board_test = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        board_test_result = [
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        #Act
        self.game_TEST.Actualizar(board_test)
        #Assert
        self.assertEqual (self.game_TEST.board, board_test_result)



if __name__ == "__main__":
    unittest.main()

