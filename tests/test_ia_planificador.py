import unittest
import tablero
from ia_planificador import analisis_ia

class test_ia_planificador(unittest.TestCase):
    # i) Evaluo cual de las capturas limpias que puedo hacer es la mejor
    def test_captura_limpia(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', ' ', 'p', ' ', ' ', ' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],   #En este escenario, lo que me gustaria es comer la torre que amenaza mi rey en la retaguarda
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],   #con la pieza de menor valor posible
            [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'r', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(6, 5), (4, 7), 29, 'Bp'], [(6, 5), (5, 4), 40, 'Bp'], [(6, 5), (7, 6), 85, 'Bq'], [(9, 8), (7, 6), 86, 'Qq'], [(14, 6), (7, 6), 86, 'Qq'], [(14, 10), (13, 9), 94, 'Br'], [(14, 8), (13, 9), 88, 'Kr'], [(14, 9), (13, 9), 88, 'Kr']]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    
    # ii) Tengo una reina en la retaguardia rival con capturas sucias (es bueno que coma, porque las piezas en la retaguardia son valiosos, mientras que la reina solo vale 5 puntos)
    def test_queen_infiltrated_true(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(False)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'],
            ['P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P'], #Tengo 2 reinas infiltradas en row=14, evaluo los puntajes de lo que comen
            ['R', 'R', 'q', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', ' ', 'q', 'H', 'H', 'R', 'R'], #El mejor evaluado tiene que ser el que captura a la pieza mas valiosa (en este caso el K)
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', ' ', 'H', 'R', 'R']] #en este caso, la mejor captura es con q desde (14,11) a K en (14,9)
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(14, 2), (14, 1), 7], [(14, 2), (14, 3), 5], [(14, 11), (14, 9), 9], [(14, 11), (14, 12), 5], [(14, 2), (15, 1), 7], [(14, 2), (15, 2), 5], [(14, 2), (15, 3), 5], [(14, 11), (15, 10), 6], [(14, 11), (15, 11), 6]]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    '''
    # iii) a) Respondo a las amenazas del rival contraatacando (valido para todas mis piezas)
    def test_capturas_rival_contraataque(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
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
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = []
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    
    # iii) b) Una reina propia se puede infiltrar en las filas de retaguardia del rival con una captura sucia (posibilidad de que la recapturen)
    def test_queen_infiltrated_false(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
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
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    # iii) c) El rival me puede capturar una reina, pero yo me muevo a fila estrategica para esquivar el ataque
    def test_capturas_rival_retirada (self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
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
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    # iv) Tengo una reina en el centro y la puedo mover a una fila mas activa
    def test_move_strategic(self):          
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
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
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    # v) Avance de peones
    def test_peon_avance(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
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
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = 
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
    '''