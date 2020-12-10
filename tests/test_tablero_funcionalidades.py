import unittest
import tablero

#AAA Rule: Arrange, Act, Assert
class test_tablero_funcionalidades(unittest.TestCase):
    '''
    En este test probamos los metodos "actualizar" y "seteo_inicial" del objeto "tablero"
    '''

    #Comprobar si se rellena el tablero de forma correcta con el metodo "actualizar"
    def test_actualizar(self):
        #Arrange
        funcionalidades = tablero.Game(True)
        board_test = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        board_test_expected = [
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
        funcionalidades.actualizar(board_test)
        #Assert
        self.assertEqual (funcionalidades.board, board_test_expected)


    #Creo un juego como blancas, llamo a la funcion de seteo inicial de variables y compruebo al menos 2 elementos
    def test_inicializar_blancas(self):
        funcionalidades   = tablero.Game(True)                #Juego creado como jugador blanco
        valor_row_strategy = {8:4 ,9:1 ,10:3    ,7:5 ,5:2}
        reina_mia         = "Q"

        funcionalidades.seteo_inicial(True)

        self.assertEqual (funcionalidades.valor_row_strategy  , valor_row_strategy)
        self.assertEqual (funcionalidades.reina_mia        , reina_mia)

    #Creo un juego como negras, llamo a la funcion de seteo inicial de variables y compruebo al menos 2 elementos
    def test_inicializar_negras(self):
        funcionalidades   = tablero.Game(False)               #Juego creado como jugador negro
        row_strategy       = {"upgrade_mia":7 ,"upgrade_rival":8 ,"peones_rival":10 ,"peones_mios_1":6 ,"peones_mios_2":5}
        reina_rival       = "Q"

        funcionalidades.seteo_inicial(False)

        self.assertEqual (funcionalidades.row_strategy    , row_strategy)
        self.assertEqual (funcionalidades.reina_rival     , reina_rival)


    #Verifico que la funcion "best_col" cuente bien la cantidad de reinas propias y del rival en filas estrategicas
    def test_row_stretegy_as_white(self):
        funcionalidades = tablero.Game(True)     #analizo la posicion como jugador blanco
        funcionalidades.seteo_inicial(True)          
        funcionalidades.board = [
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'R', 'H', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['Q', 'Q', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],       #peones rival
            [' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' '],       
            [' ', ' ', ' ', 'Q', 'Q', ' ', ' ', 'q', ' ', ' ', 'q', ' ', ' ', ' ', 'q', ' '],       #coronacion negras
            [' ', 'Q', ' ', ' ', 'Q', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' '],       #coronacion blancas
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],       #peones 1
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],       #peones 2
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        funcionalidades.queens_in_row_strategy()

        self.assertTrue(funcionalidades.qq_row_strategy[8]  ==  4 )                  #Hay 4 Q en la fila de upgrade propia
        self.assertTrue(funcionalidades.qq_row_strategy[9]  ==  0 )                  #Hay 0 Q en la fila de peones 1
        self.assertTrue(funcionalidades.qq_row_strategy[10] ==  1 )                  #Hay 1 Q en la fila de peones 2
        self.assertTrue(funcionalidades.qq_row_strategy[7]  ==  2 )                  #Hay 2 Q en la fila de upgrade rival
        self.assertTrue(funcionalidades.qq_row_strategy[5]  ==  3 )                  #Hay 3 Q en la fila de peones del rival
        
