import unittest
import tablero
from ia_planificador import analisis_ia

class test_ia_planificador(unittest.TestCase):
    # i) Evaluo cual de las capturas limpias que puedo hacer es la mejor
    def test_captura_limpia(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', ' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'q', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_All_Possible_Moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_All_Possible_Moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(6, 5), (5, 4), 123, 'Bp'], [(6, 5), (7, 6), 128, 'Bq'], [(9, 8), (7, 6), 128, 'Qq'], [(14, 6), (7, 6), 118, 'Qq'], [(14, 10), (13, 9), 118, 'Bq'], [(14, 8), (13, 9), 118, 'Kq'], [(14, 9), (13, 9), 118, 'Kq']]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    '''
    # ii) Tengo una reina en la retaguardia rival con capturas sucias (es bueno que coma, porque las piezas en la retaguardia son valiosos, mientras que la reina solo vale 5 puntos)
    def test_queen_infiltrated_true(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],       #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k'],
            ['P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'q', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_All_Possible_Moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_All_Possible_Moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)



    # iii) a) Respondo a las amenazas del rival contraatacando (valido para todas mis piezas)
    def test_capturas_rival_contraataque(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],       #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k'],
            ['P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'q', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_All_Possible_Moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_All_Possible_Moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)



    # iii) b) Una reina propia se puede infiltrar en las filas de retaguardia del rival con una captura sucia (posibilidad de que la recapturen)
    def test_queen_infiltrated_false(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],       #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k'],
            ['P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'q', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_All_Possible_Moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_All_Possible_Moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    # iii) c) El rival me puede capturar una reina, pero yo me muevo a fila estrategica para esquivar el ataque
    def test_capturas_rival_retirada (self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],       #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k'],
            ['P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'q', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_All_Possible_Moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_All_Possible_Moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    # iv) Tengo una reina en el centro y la puedo mover a una fila mas activa
    def test_move_strategic(self):          
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],       #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k'],
            ['P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'q', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_All_Possible_Moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_All_Possible_Moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    # v) Avance de peones
    def test_peon_avance(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],       #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k'],
            ['P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'q', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_All_Possible_Moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_All_Possible_Moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
    '''