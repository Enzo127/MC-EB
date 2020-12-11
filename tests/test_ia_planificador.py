import unittest
import tablero
from ia_planificador import analisis_ia

class test_ia_planificador(unittest.TestCase):
    # i) Evaluo una situacion en la que tengo multiples capturas limpias y evaluo cual de las capturas limpias que puedo hacer es la mejor
    '''
    def test_captura_limpia_multiple(self):
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
        moves_expected = [[(6, 5), (4, 7), 29, 'Bp'], [(6, 5), (5, 4), 40, 'Bp'], [(6, 5), (7, 6), 85, 'Bq'], [(9, 8), (7, 6), 86, 'Qq'], [(14, 6), (7, 6), 86, 'Qq'], [(14, 10), (13, 9), 104, 'Br'], [(14, 8), (13, 9), 98, 'Kr'], [(14, 9), (13, 9), 98, 'Kr']]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)

    '''
    # i) Evaluo una situacion en la que tengo solo una captura limpia
    def test_captura_limpia_unica(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(False)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', ' ', 'p', 'p', 'p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(7, 5), (7, 10), 0, 'qQ']]
        
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

    '''
    # iv) Tengo una reina en el centro y la puedo mover a una fila mas activa
    def test_move_strategic(self):          
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', ' ', 'p', 'p', ' ', 'p', 'p', 'p', 'p', 'p', ' ', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' '],#peon rival        r=5        4ta
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#upgrade_rival     r=7        1ra
            [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#upgrade           r=8        2da
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#peon mio          r=10       3ra
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        Game_test.queens_in_row_strategy()                      #actualiza la cantidad de reinas estrategicas ----> Totalmente necesario en esta funcion

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(8, 5), (7, 5), 1], [(8, 5), (7, 4), 1], [(8, 5), (7, 6), 1]]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)

    
    # v) Avance de peones blancos
    def test_peon_avance_blanco(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            [' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', 'p', 'p', 'p', 'p', 'p', ' ', 'p', 'p', 'p', 'p', ' ', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', 'P', ' ', 'P', 'b', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'P', 'P', ' ', 'P', 'P', 'P', 'P', ' ', 'P', ' ', ' ', 'P', 'P', 'P', 'P'],
            [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(9, 0), (8, 0), -500], [(10, 3), (9, 3), -600], [(10, 8), (9, 8), -500], [(10, 10), (9, 10), -500], [(12, 1), (11, 1), 211], [(12, 1), (10, 1), 301], [(12, 2), (11, 2), -780], [(12, 2), (10, 2), -690], [(12, 4), (11, 4), -780], [(12, 4), (10, 4), -690], [(12, 5), (11, 5), -799], [(12, 5), (10, 5), -700], [(12, 6), (11, 6), -1799], [(12, 6), (10, 6), -500], [(12, 7), (11, 7), -1789], [(12, 7), (10, 7), -500], [(12, 9), (11, 9), -799], [(12, 9), (10, 9), -699], [(12, 12), (11, 12), 2000], [(12, 12), (10, 12), -1700], [(12, 13), (11, 13), -790], [(12, 13), (10, 13), -700], [(12, 14), (11, 14), -1790], [(12, 14), (10, 14), -1700], [(12, 15), (11, 15), -1790], [(12, 15), (10, 15), -500], [(13, 3), (12, 3), -10880], [(13, 3), (11, 3), -10790], [(13, 8), (12, 8), -20880], [(13, 8), (11, 8), -20790], [(13, 10), (12, 10), -11889], [(13, 10), (11, 10), 2000], [(13, 11), (12, 11), -11879], [(13, 11), (11, 11), -11789]]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    # v) Avance de peones negros
    def test_peon_avance_negro(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(False)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', ' ', 'p', 'p', ' ', 'p', 'p', 'p', 'p', 'p', ' ', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        Game_test.first_move = False
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(2, 4), (3, 4), -10880], [(2, 4), (4, 4), -10790], [(2, 7), (3, 7), -10889], [(2, 7), (4, 7), -10799], [(2, 13), (3, 13), -10890], [(3, 0), (4, 0), 201], [(3, 0), (5, 0), 300], [(3, 1), (4, 1), -790], [(3, 1), (5, 1), -500], [(3, 2), (4, 2), -790], [(3, 2), (5, 2), -700], [(3, 3), (4, 3), 211], [(3, 3), (5, 3), 301], [(3, 5), (4, 5), -789], [(3, 5), (5, 5), -699], [(3, 6), (4, 6), 211], [(3, 6), (5, 6), 301], [(3, 8), (4, 8), -1789], [(3, 8), (5, 8), -500], [(3, 9), (4, 9), -11799], [(3, 9), (5, 9), -500], [(3, 10), (4, 10), -2790], [(3, 10), (5, 10), -500], [(3, 11), (4, 11), -799], [(3, 11), (5, 11), -700], [(3, 12), (4, 12), -780], [(3, 12), (5, 12), -690], [(3, 14), (4, 14), -780], [(3, 14), (5, 14), -690], [(3, 15), (4, 15), -790], [(3, 15), (5, 15), -700], [(4, 13), (5, 13), -700], [(5, 7), (6, 7), -500], [(6, 4), (7, 4), -500]]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
    
    # v) Peones negros buscando presionar piezas rivales (deberian valorarse mas los mov de peones que posteriormente van a atacar a Q en row=5 y R en row=6)
    def test_peon_avance_negro_presion(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(False)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', ' ', 'p', 'p', ' ', 'p', 'p', 'p', 'p', 'p', ' ', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' '],
            [' ', ' ', 'Q', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        Game_test.first_move = False
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(2, 4), (3, 4), -1897], [(2, 4), (4, 4), -1798], [(2, 7), (3, 7), -11890], [(2, 13), (3, 13), -10890], [(3, 0), (4, 0), -2799], [(3, 0), (5, 0), -500], [(3, 1), (4, 1), 2000], [(3, 1), (5, 1), -500], [(3, 2), (4, 2), -11799], [(3,3), (4, 3), 2000], [(3, 3), (5, 3), -500], [(3, 5), (4, 5), -11790], [(3, 6), (4, 6), 221], [(3, 6), (5, 6), 311], [(3, 8), (4, 8), -10798], [(3, 8), (5, 8), -10699], [(3, 9), (4, 9), -790], [(3, 9), (5, 9), 2000], [(3, 10), (4, 10), -790], [(3, 10), (5, 10), -700], [(3, 11), (4, 11), -790], [(3, 11), (5, 11), -700], [(3, 12), (4, 12), -780], [(3, 12), (5, 12), -690], [(3, 14), (4, 14), -780], [(3, 14), (5, 14), -690], [(3, 15), (4, 15), -790], [(3, 15), (5, 15), -700], [(4, 7), (5, 7), -500], [(4, 13), (5, 13), -700], [(5, 5), (6, 5), -500]]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)


    # v) Primer turno como negro (respondo en la columna totalmente opuesta a la que se mueva el blanco) (solo si el rival empezo moviendose 2 casilleros)
    def test_first_move_black(self):
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
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
       
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(3, 0), (4, 0), 210], [(3, 0), (5, 0), 300], [(3, 1), (4, 1), 210], [(3, 1), (5, 1), 300], [(3, 2), (4, 2), 210], [(3, 2), (5, 2), 300], [(3, 3), (4, 3), 210], [(3, 3), (5, 3), 300], [(3, 4), (4, 4), 210], [(3, 4), (5, 4), 300], [(3, 5), (4, 5), 210], [(3, 5), (5, 5), 300], [(3, 6), (4, 6), 210], [(3, 6), (5, 6), 300], [(3, 7), (4, 7), 210], [(3, 7), (5, 7), 300], [(3, 8), (4, 8), 210], [(3, 8), (5, 8), 300], [(3, 9), (4, 9), 210], [(3, 9), (5, 9), 1300], [(3, 10), (4, 10), 210], [(3, 10), (5, 10), 300], [(3, 11), (4, 11), 210], [(3, 11), (5, 11), 300], [(3, 12), (4, 12), 210], [(3, 12), (5, 12), 300], [(3, 13), (4, 13), 210], [(3, 13), (5, 13), 300], [(3, 14), (4, 14), 210], [(3, 14), (5, 14), 300], [(3, 15), (4, 15), 210], [(3, 15), (5, 15), 300]]
        
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)

        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)