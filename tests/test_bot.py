import unittest
import bot
import tablero

class test_tablero_black_pieces(unittest.TestCase):
    #Empiezo todos los tests con 2 juegos creados de antemano
    def setUp(self):
        #1er juego 
        self.id_prueba_1    = "sfjijoisjef283749"
        color_prueba_1      = "white"
        bot.crear_juego(self.id_prueba_1, color_prueba_1)

        #2do juego 
        self.id_prueba_2    = "384f98428m4823489"
        color_prueba_2      = "black"
        bot.crear_juego(self.id_prueba_2, color_prueba_2)


    #Creo otro juego y compruebo: que se creo con el color correcto, que hay un total de 3 juegos corriendo (los 2 del setUp y este) y que los 3 juegos corresponden a objetos distintos
    def test_crear_juego(self):
        #3er juego 
        id_prueba_3        = "923rfj23j'3939sf3"
        color_prueba_3     = "black"
        c = bot.crear_juego(id_prueba_3, color_prueba_3)
        self.assertEqual(c.color, False )                    #Comprobacion de color

        a = bot.juegos_Ejecutandose[self.id_prueba_1]
        b = bot.juegos_Ejecutandose[self.id_prueba_2]

        self.assertEqual(len(bot.juegos_Ejecutandose), 3)   #Comprobar cantidad de juegos almacenados
        self.assertTrue(a != b != c)                        #Comprobar que los juegos son distintos


    #LLamo a limpiar con un id del setUp y compruebo como antes esa key antes estaba y luego es removida
    def test_eliminar_juego(self):
        self.assertIsNotNone(bot.juegos_Ejecutandose.get(self.id_prueba_1))
        bot.limpiar(self.id_prueba_1)
        self.assertIsNone(bot.juegos_Ejecutandose.get(self.id_prueba_1))

    #Genero una lista con todos los movimientos posibles tipica, y evaluo si la funcion comparacion me devuelve el mejor movimiento posible
    def test_comparacion(self):
        moves_test = [[[[(1, 12), (0, 10), 586, 'Hb'], [(1, 12), (0, 14), 686, 'Hr'], [(1, 12), (2, 10), 86, 'Hp'], [(1, 12), (2, 14), 86, 'Hp'], [(1, 12), (3, 11), 186, 'Hp'], [(1, 12), (3, 13), 186, 'Hp'], [(14, 13), (12, 14), 1500, 'Hq']], []],[[], []], [[[(1, 11), (0, 11), -299, 'Rb'], [(1, 11), (1, 10), -299, 'Rb'], [(1, 11), (2, 11), -799, 'Rp']], []], [[[(13, 1), (12, 0), 3000, 'Pk'], [(13, 8), (12, 9), 3000, 'Pk'], [(13, 10), (12, 9), 3000, 'Pk'], [(13, 13), (12, 14), 2250, 'Pq'], [(13, 15), (12, 14), 2250, 'Pq']], [[(12, 1), (10, 1), 500], [(12, 2), (10, 2), 500], [(12, 3), (10, 3), 500], [(12, 4), (10, 4), 500], [(12, 5), (10, 5), 500], [(12, 6), (10, 6), 500], [(12, 7), (10, 7), 500], [(12, 8), (10, 8), 500], [(12, 10), (10, 10), 500], [(12, 11), (10, 11), 500], [(12, 12), (10, 12), -9500], [(12, 13), (10, 13), 500], [(12, 15), (10, 15), 500]]], [[], []], [[], []]]
        
        best_move_test = bot.comparacion (moves_test)
        best_move_correcto = [(13, 1), (12, 0), 3000, 'Pk']

        self.assertEqual(best_move_test, best_move_correcto)


  
