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

        funcionalidades.seteo_Inicial(True)

        self.assertEqual (funcionalidades.row_upgrade_mia  , row_upgrade_mia)
        self.assertEqual (funcionalidades.reina_mia        , reina_mia)

    #Creo un juego como negras, llamo a la funcion de seteo inicial de variables y compruebo al menos 2 elementos
    def test_inicializar_negras(self):
        funcionalidades = tablero.game(False)               #Juego creado como jugador negro
        row_tactical      = 6
        reina_rival       = "Q"

        funcionalidades.seteo_Inicial(False)

        self.assertEqual (funcionalidades.row_tactical    , row_tactical)
        self.assertEqual (funcionalidades.reina_rival     , reina_rival)


    #Para un tablero con reinas propias y rivales verifico si las columnas que deberian priorizarse son las mejor evaluadas
    #ESTE TEST CAPAZ QUE ES DIFICL DE ENTENDER PARA OTRA PERSONA, PODRIAS HACER UN GLOSARIO
    def test_best_col(self):
        funcionalidades = tablero.game(False)     #analizo la posicion como jugador negro
        funcionalidades.seteo_Inicial(False)          
        funcionalidades.board = [
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'R', 'H', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', ' '],       #tactical negras
            [' ', ' ', 'q', 'q', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', 'q', ' ', ' '],       #coronacion negras
            [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', 'Q', ' ', 'Q', ' ', ' ', ' ', ' '],       #coronacion blancas
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],       #tactical blancas
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        funcionalidades.columna_Rating()
        x = funcionalidades.best_col                    #Lo guardo en otra variable para llamarlo mas facilment
        
        #print()
        #for i in x:
        #    print(i,  x[i])

        self.assertTrue(x[1]  > x[0])
        self.assertTrue(x[15] > x[13])
        self.assertTrue(x[15] > x[14])
        self.assertTrue(x[14] > x[12])
        self.assertTrue(x[6] == x[8])
        self.assertTrue(x[3]  < x[4])
        self.assertTrue(x[1]  > x[15])          #Esto es asi porque a la col 1 le suma la col 2 y 3...mientras que a la col 15 le suma solo la col 13

    
    
    #Verifico que la funcion "best_col" cuente bien la cantidad de reinas propias y del rival en filas estrategicas
    def test_filas_estrategicas(self):
        funcionalidades = tablero.game(True)     #analizo la posicion como jugador blanco
        funcionalidades.seteo_Inicial(True)          
        funcionalidades.board = [
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'R', 'H', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' '],       #tactical negras
            [' ', ' ', ' ', 'Q', 'Q', ' ', ' ', 'q', ' ', ' ', 'q', ' ', ' ', ' ', 'q', ' '],       #coronacion negras
            [' ', 'Q', ' ', ' ', 'Q', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' '],       #coronacion blancas
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],       #tactical blancas
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        funcionalidades.columna_Rating()

        self.assertTrue(funcionalidades.qm_quantity_row_tactical      ==  0 )       #No puse ni una reina propia en row_tactical de las blancas
        self.assertTrue(funcionalidades.qm_quantity_row_upgrade_mia   ==  4 )       #Hay 4 Q en la fila de coronacion blanca
        self.assertTrue(funcionalidades.qm_quantity_row_upgrade_rival ==  2 )       #Hay 2 Q en la fila de coronacion negra
        self.assertTrue(funcionalidades.qr_quantity_row_upgrade_rival ==  3 )       #Hay 3 q en la fila de coronacion de las negras

