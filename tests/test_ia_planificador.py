import unittest
import tablero
from ia_planificador import analisis_ia
from bot import comparacion

'''
Doy un tablero con un escenario, luego comparo para ese tablero los movimientos evaluados con los que responde la IA 
y el mejor movimiento (el que esta evaluado con el mayor puntaje)
'''

class test_ia_planificador(unittest.TestCase):
    # i) Evaluo una situacion en la que tengo multiples capturas limpias y evaluo cual de las capturas limpias que puedo hacer es la mejor
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
        moves_expected = [[(6, 5), (4, 7), 27, 'Bp'], [(6, 5), (5, 4), 38, 'Bp'], [(6, 5), (7, 6), 83, 'Bq'], [(9, 8), (7, 6), 84, 'Qq'], [(14, 6), (7, 6), 84, 'Qq'], [(14, 10), (13, 9), 102, 'Br'], [(14, 8), (13, 9), 98, 'Kr'], [(14, 9), (13, 9), 98, 'Kr']]
        best_move_expected = [(14, 10), (13, 9), 102, 'Br']
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)

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
        best_move_expected = [(7, 5), (7, 10), 0, 'qQ']
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)

    # ii) Tengo una reina en la retaguardia rival con capturas sucias (es bueno que coma, porque las piezas en la retaguardia son valiosos, mientras que la reina solo vale 5 puntos)
    def test_queen_infiltrated(self):
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
        best_move_expected = [(14, 11), (14, 9), 9]
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)

    
    # iii) a) Respondo a las amenazas del rival contraatacando (valido para todas mis piezas)
    def test_capturas_rival_contraataque(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', ' ', 'p', 'p', 'p', 'Q', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', ' ', ' ', 'p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(2, 10), (1, 9), 4], [(2, 10), (1, 10), 1], [(2, 10), (1, 11), 1], [(9, 7), (8, 6), 7], [(9, 7), (8, 8), 8], [(14, 6), (8, 6), 3]]
        best_move_expected = [(9, 7), (8, 8), 8]
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)
 
    # iii) b) El rival me puede capturar una pieza, pero yo me muevo a un casillero sin peligro para esquivar el ataque (fundamental para que no me capturen los reyes)
    def test_capturas_rival_retirada_piezas_valiosas (self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', 'K', ' ', ' ', ' '],#La reina enemiga ataca 3 piezas mias, las 3 deberian responder con retirada
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#siendo mas valioso el movimiento de la pieza mia que mas puntos valga
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', ' ', 'K', ' ', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(8, 12), (7, 12), 9], [(8, 12), (7, 13), 9], [(8, 12), (8, 13), 9], [(8, 12), (9, 12), 9], [(8, 12), (9, 13), 9], [(7, 9), (6, 9), 7], [(7, 9), (5, 9), 7], [(7, 9), (7, 8), 7], [(7, 9), (7, 7), 7], [(7, 9), (7, 6), 7], [(7, 9), (7, 5), 7], [(7, 9), (7, 4), 7], [(7, 9), (7, 3), 7], [(7, 9), (7, 2), 7], [(7, 9), (7, 1), 7], [(7, 9), (7, 0), 7], [(7, 9), (10, 9), 7], [(7, 9), (11, 9), 7], [(7, 9), (7, 12), 7], [(7, 9), (7, 13), 7], [(7, 9), (7, 14), 7], [(7, 9), (7, 15), 7], [(10, 8), (9, 8), 4]]
        best_move_expected = [(8, 12), (7, 12), 9]
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)


    # iii) b) El rival me puede capturar una reina con peones, pero yo me muevo a fila estrategica para esquivar el ataque
    def test_capturas_rival_retirada_reinas (self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(False)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', ' ', ' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#coronacion negra
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#coronacion blanca (fila ya ocupada con una reina, asique no deberia retirarme ahi)
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#Esta reina va a retirarse(la ataca una pieza de bajo valor) a un casillero seguro, dentro de una
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#fila estrategica en la que no tenga mas de una reina(asi controlo diferentes filas estrategicas)
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        Game_test.queens_in_row_strategy()

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(10, 6), (7, 6), 2], [(10, 6), (10, 5), 1], [(10, 6), (10, 4), 1], [(10, 6), (10, 3), 1], [(10, 6), (10, 2), 1], [(10, 6), (10, 1), 1], [(10, 6), (10, 0), 1], [(10, 6), (10, 7), 1], [(10, 6), (10, 9), 1], [(10, 6), (10, 10), 1], [(10, 6), (10, 11), 1], [(10, 6), (10, 12), 1], [(10, 6), (10, 13), 1], [(10, 6), (10, 14), 1], [(10, 6), (10, 15), 1], [(10, 6), (7, 3), 2], [(10, 6), (7, 9), 2]]
        best_move_expected = [(10, 6), (7, 6), 2]
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)


    # iv) Caso 1: Tengo una reina en mi fila de coronacion y la puedo mover a la fila de coronacion rival SIN que la capturen
    def test_move_strategic_caso_1(self):          
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
        best_move_expected = [(8, 5), (7, 5), 1]
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)
    
    
    # iv) Caso 2: Tengo mas de 1 reina en row upgrade, las puedo distribuir a otras filas dependiendo cuales tienen menos reinas y mayor valor estrategico
    def test_move_strategic_caso_2(self):          
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', ' ', ' ', 'p', 'p', 'p', ' ', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'Q', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #Una de estas 2 reinas deberia moverse a la fila 5 (fila de peones debiles del rival)
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        Game_test.queens_in_row_strategy()                      #actualiza la cantidad de reinas estrategicas ----> Totalmente necesario en esta funcion

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(8, 6), (5, 3), 1], [(8, 6), (5, 9), 1], [(8, 7), (5, 7), 1], [(8, 7), (5, 10), 1]]
        best_move_expected = [(8, 6), (5, 3), 1]
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)

    # iv) Caso 3: Tengo reinas en las 3 filas estrategicas, pero estoy juntando demasiadas en mi row de upgrade, si se cumple 
    #             si se cumple-----> cantidad de reinas+1 en row upgrade mia > cantidad de reinas en row upgrade rival  -----> Mover una reina de mi fila de upgrade a la rival
    def test_move_strategic_caso_3(self):          
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', ' ', ' ', 'p', 'p', 'p', ' ', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'Q', 'Q', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        Game_test.queens_in_row_strategy()                      #actualiza la cantidad de reinas estrategicas ----> Totalmente necesario en esta funcion

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(8, 6), (7, 5), 3], [(8, 6), (7, 7), 3], [(8, 7), (7, 7), 3], [(8, 7), (7, 8), 3], [(8, 8), (7, 8), 3], [(8, 8), (7, 7), 3], [(8, 8), (7, 9), 3]]
        best_move_expected = [(8, 6), (7, 5), 3]
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)

    # v) Apertura de peones blanca
    def test_peon_apertura_blanca(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(True)         #color  (True = white) (False = black)
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
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#La apertura mas fuerte de las blancas es empujar rapido los peones de la columna 6 y 7
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#y liberar las reinas que estan detras
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        Game_test.flag_apertura = True     #Escenario en el que ya hice los movimientos de apertura

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(12, 6), (11, 6), 72], [(12, 6), (10, 6), 82], [(12, 7), (11, 7), 71], [(12, 7), (10, 7), 81]]
        best_move_expected = [(12, 6), (10, 6), 82]
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)

    # v) Apertura numero 1 de negras (Game.strategy = 2)
    def test_peon_apertura_negra_1(self):
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
            ['P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#El rival negro inicio con una mala apertura, yo como jugador negro aprovecho y empujo los
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#peones de la columna 6 y 7
            [' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        Game_test.flag_apertura    = True     #Escenario en el que ya hice los movimientos de apertura
        Game_test.flag_first_move  = True

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(3, 6), (4, 6), 72], [(3, 6), (5, 6), 82], [(3, 7), (4, 7), 71], [(3, 7), (5, 7), 81]]
        best_move_expected = [(3, 6), (5, 6), 82]

        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test) #LLamo a la funcion con los imputs declarados y obtengo el resultado
        best_move_result = comparacion(moves_result)

        self.assertEqual(moves_result ,moves_expected)              #Comparacion entre resultado esperado y obtenido
        self.assertEqual(best_move_result ,best_move_expected)

    # v) Apertura numero 2 de negras (Game.strategy = 1)
    def test_peon_apertura_negra_2(self):
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
            [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #Esta es una variacion de la apertura blanca fuerte, pero liberando las reinas de la retaguardia
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], #por la columna 5 y 6, en vez de por la 6 y 7...como negro, respondo moviendo primero el peon
            ['P', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], #mas cercano de la columna 7 y despues de la columna 6
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        Game_test.flag_apertura    = True     #Escenario en el que ya hice los movimientos de apertura
        Game_test.flag_first_move  = True

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(3, 6), (4, 6), 71], [(3, 6), (5, 6), 81], [(3, 7), (4, 7), 72], [(3, 7), (5, 7), 82]]
        best_move_expected = [(3, 7), (5, 7), 82]   
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)
    
    # v) Apertura numero 3 de negras (Game.strategy = 0)
    def test_peon_apertura_negra_3(self):
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

        Game_test.flag_apertura    = True     #Escenario en el que ya hice los movimientos de apertura
        Game_test.flag_first_move  = True
        test_move_opening          = [(5,5) ,(5,6) ,(6,6) ,(5,7) ,(6,7) ,(5,8) ,(4,6) ,(5,6) ,(4,7) ,(5,7) ,(6,5) ,(6,8)]  #estrategia de apertura 

        self.assertEqual(Game_test.move_opening ,test_move_opening)

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(3, 5), (5, 5), 0]]
        best_move_expected = [(3, 5), (5, 5), 0]    #Respondo siguiendo los movimientos en orden de "test_move_opening"
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)
        test_move_opening.pop(0)
        self.assertEqual(Game_test.move_opening ,test_move_opening)


    # v) Apertura numero 3 de negras terminada (ya hice todos los movimientos posibles o el rival rompio mi estrategia) y debo continuar con el movimiento de peones normal
    def test_peon_apertura_negra_3_broke(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(False)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', ' ', ' ', ' ', ' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'p', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        Game_test.flag_apertura    = True     #Escenario en el que ya hice los movimientos de apertura
        Game_test.flag_first_move  = False
        Game_test.strategy         = 0

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(2, 5), (3, 5), -9870], [(2, 5), (4, 5), -9780], [(2, 6), (3, 6), -7870], [(2, 6), (4, 6), -7780], [(2, 7), (3, 7), -7860], [(2, 7), (4, 7), -7770], [(2, 8), (3, 8), 140], [(2, 8), (4, 8), 230], [(3, 0), (4, 0), 210], [(3, 0), (5, 0), 300], [(3, 1), (4, 1), 210], [(3, 1), (5, 1), 300], [(3, 2), (4, 2), 210], [(3, 2), (5, 2), 300], [(3, 3), (4, 3), 210], [(3, 3), (5, 3), 300], [(3, 4), (4, 4), 220], [(3, 4), (5, 4), 310], [(3, 9), (4, 9), 230], [(3, 9), (5, 9), 320], [(3, 10), (4, 10), 220], [(3, 10), (5, 10), 310], [(3, 11), (4, 11), 220], [(3, 11), (5, 11), 310], [(3, 12), (4, 12), 220], [(3, 12), (5, 12), 310], [(3, 13), (4, 13), 220], [(3, 13), (5, 13), 310], [(3, 14), (4, 14), 220], [(3, 14), (5, 14), 310], [(3, 15), (4, 15), 220], [(3, 15), (5, 15), 310], [(5, 5), (6, 5), 410], [(6, 6), (7, 6), 3000]]
        best_move_expected = [(6, 6), (7, 6), 3000]     #Peon de columna 6 (de las mejores columnas) cercano a coronacion
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)
        self.assertEqual(Game_test.flag_apertura ,False)  #Habia empezado en True, pero al ver que no podia seguir con la apertura, la logica lo cambia a False y continua 
                                                          #con el movimiento de peones de la funcion "peon_avance"
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
            [' ', 'P', 'P', ' ', 'P', 'P', ' ', ' ', ' ', 'P', ' ', ' ', 'P', 'P', 'P', 'P'],
            [' ', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        Game_test.flag_apertura = False     #Escenario en el que ya hice los movimientos de apertura

        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(9, 0), (8, 0), -10000], [(10, 3), (9, 3), -600], [(10, 8), (9, 8), -10000], [(10, 10), (9, 10), -599], [(12, 1), (11, 1), 211], [(12, 1), (10, 1), 301], [(12, 2), (11, 2), -780], [(12, 2), (10, 2), -690], [(12, 4), (11, 4), -780], [(12, 4), (10, 4), -690], [(12, 5), (11, 5), -799], [(12, 5), (10, 5), -700], [(12, 9), (11, 9), -779], [(12, 9), (10, 9), -689], [(12, 12), (11, 12), 2000], [(12, 12), (10, 12), -1700], [(12, 13), (11, 13), -790], [(12, 13), (10, 13), -700], [(12, 14), (11, 14), -1790], [(12, 14), (10, 14), -1700], [(12, 15), (11, 15), -1790], [(12, 15), (10, 15), -10000], [(13, 3), (12, 3), -10880], [(13, 3), (11, 3), -10790], [(13, 8), (12, 8), -20880], [(13, 8), (11, 8), -20790], [(13, 10), (12, 10), -10888], [(13, 10), (11, 10), 2000], [(13, 11), (12, 11), -10878], [(13, 11), (11, 11), -10788]]
        best_move_expected = [(12, 12), (11, 12), 2000] #Moverme con el peon a atacar el alfil
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)
    
    # v) Avance de peones negros
    def test_peon_avance_negro(self):
        #Declaro todos los datos de entrada a la funcion a testear
        Game_test = tablero.Game(False)         #color  (True = white) (False = black)
        Game_test.board = [                    #Necesito un board distinto para cada test
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', ' ', 'p', ' ', ' ', 'p', 'p', 'p', 'p', 'p', ' ', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'p', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]

        Game_test.flag_apertura = False
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(2, 4), (3, 4), -10880], [(2, 4), (4, 4), -10790], [(2, 6), (3, 6), -7888], [(2, 6), (4, 6), -7789], [(2, 7), (3, 7), -7888], [(2, 7), (4, 7), -7798], [(2, 13), (3, 13), -10890], [(3, 0), (4, 0), 210], [(3, 0), (5, 0), 300], [(3, 1), (4, 1), 210], [(3, 1), (5, 1), 300], [(3, 2), (4, 2), 210], [(3, 2), (5, 2), 300], [(3, 3), (4, 3), 220], [(3, 3), (5, 3), 310], [(3, 5), (4, 5), 211], [(3, 5), (5, 5), 311], [(3, 8), (4, 8), -1789], [(3, 8), (5, 8), -10000], [(3, 9), (4, 9), -11799], [(3, 9), (5, 9), -10000], [(3, 10), (4, 10), -2790], [(3, 10), (5, 10), -10000], [(3, 11), (4, 11), -799], [(3, 11), (5, 11), -700], [(3, 12), (4, 12), -780], [(3, 12), (5, 12), -690], [(3, 14), (4, 14), -780],[(3, 14), (5, 14), -690], [(3, 15), (4, 15), -790], [(3, 15), (5, 15), -700], [(4, 13), (5, 13), -700], [(5, 6), (6, 6), 2401], [(5, 7), (6, 7), 2401], [(6, 4), (7, 4), -10000]]
        best_move_expected = [(5, 6), (6, 6), 2401] 
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result   = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)

    # v) El rival blanco me esta presionando, mis peones deben moverse al centro por las lineas mas seguras (en este caso la 6, aunque este atacada, el casillero donde pueden capturar esta defendido)
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

        Game_test.flag_apertura = False
        
        change=0                                                       
        moves       = Game_test.get_all_possible_moves(change)              
        change=1                                                       
        moves_enemy = Game_test.get_all_possible_moves(change) 

        #Declaro el resultado esperado
        moves_expected = [[(2, 4), (3, 4), -1897], [(2, 4), (4, 4), -1798], [(2, 7), (3, 7), -9890], [(2, 13), (3, 13), -10890], [(3, 0), (4, 0), -2799], [(3, 0), (5, 0), -10000], [(3, 1), (4, 1), 2000], [(3, 1), (5, 1), -10000], [(3, 2), (4, 2), -11799], [(3, 3), (4, 3), 2000], [(3, 3), (5, 3), -10000], [(3, 5), (4, 5), -11790], [(3, 6), (4, 6), 2221], [(3, 6), (5, 6), 2311], [(3, 8), (4, 8), -10798], [(3, 8), (5, 8), -10699], [(3, 9), (4, 9), -790], [(3, 9), (5, 9), 2000], [(3, 10), (4, 10), -790], [(3, 10), (5, 10), -700], [(3, 11), (4, 11), -790], [(3, 11), (5, 11), -700], [(3, 12), (4, 12), -780], [(3, 12), (5, 12), -690], [(3, 14), (4, 14), -780], [(3, 14), (5, 14), -690], [(3, 15), (4, 15), -790], [(3, 15),(5, 15), -700], [(4, 7), (5, 7), -10000], [(4, 13), (5, 13), -700], [(5, 5), (6, 5), -10000]]
        best_move_expected = [(3, 6), (5, 6), 2311] #El peon es de la col 6 y tiene un camino sin piezas delante ni piezas rivales que lo puedan capturar de forma limpia (en el casillero donde lo pueden atacar, esta defendido por un peon mio)              
        #LLamo a la funcion con los imputs declarados y obtengo el resultado
        moves_result     = analisis_ia(moves ,moves_enemy ,Game_test)
        best_move_result = comparacion(moves_result)
        #Comparacion entre resultado esperado y obtenido
        self.assertEqual(moves_result ,moves_expected)
        self.assertEqual(best_move_result ,best_move_expected)

