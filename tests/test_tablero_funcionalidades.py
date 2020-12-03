import unittest
import tablero

#AAA Rule: Arrange, Act, Assert
class test_tablero_funcionalidades(unittest.TestCase):
    '''
    En este test probamos los metodos "Actualizar" y "seteo_Inicial" del objeto "tablero"
    '''

    #Comprobar si se rellena el tablero de forma correcta con el metodo "Actualizar"
    def test_Actualizar(self):
        #Arrange
        funcionalidades = tablero.game(True)
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
        funcionalidades.Actualizar(board_test)
        #Assert
        self.assertEqual (funcionalidades.board, board_test_expected)


    #Creo un juego como blancas, llamo a la funcion de seteo inicial de variables y compruebo al menos 2 elementos
    def test_inicializar_blancas(self):
        funcionalidades = tablero.game(True)                #Juego creado como jugador blanco
        row_upgrade_mia   = 8
        reina_mia         = "Q"

        funcionalidades.seteo_Inicial()

        self.assertEqual (funcionalidades.row_upgrade_mia  , row_upgrade_mia)
        self.assertEqual (funcionalidades.reina_mia        , reina_mia)

    #Creo un juego como negras, llamo a la funcion de seteo inicial de variables y compruebo al menos 2 elementos
    def test_inicializar_negras(self):
        funcionalidades = tablero.game(False)               #Juego creado como jugador negro
        row_tactical      = 6
        reina_rival       = "Q"

        funcionalidades.seteo_Inicial()

        self.assertEqual (funcionalidades.row_tactical    , row_tactical)
        self.assertEqual (funcionalidades.reina_rival     , reina_rival)