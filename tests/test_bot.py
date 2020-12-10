import unittest
import bot
import tablero

class test_bot(unittest.TestCase):
    #Empiezo todos los tests con 2 juegos creados de antemano
    def setUp(self):
        self.id_prueba_1    = "sfjijoisjef283749"               #1er juego 
        color_prueba_1      = "white"
        bot.crear_juego(self.id_prueba_1, color_prueba_1)

        self.id_prueba_2    = "384f98428m4823489"               #2do juego 
        color_prueba_2      = "black"
        bot.crear_juego(self.id_prueba_2, color_prueba_2)


    #Creo otro juego y compruebo: que se creo con el color correcto, que hay un total de 3 juegos corriendo (los 2 del setUp y este) y que los 3 juegos corresponden a objetos distintos
    def test_crear_juego(self):
        #3er juego 
        id_prueba_3        = "923rfj23j'3939sf3"
        color_prueba_3     = "black"
        c = bot.crear_juego(id_prueba_3, color_prueba_3)
        self.assertEqual(c.color, False )                    #Comprobacion de color

        a = bot.juegos_ejecutandose[self.id_prueba_1]
        b = bot.juegos_ejecutandose[self.id_prueba_2]
        
        self.assertEqual(len(bot.juegos_ejecutandose), 3)   #Comprobar cantidad de juegos almacenados
        self.assertTrue(a != b != c)                         #Comprobar que los juegos son distintos


    #LLamo a limpiar con un id del setUp y compruebo como antes esa key antes estaba y luego es removida
    def test_eliminar_juego(self):
        
        self.assertIsNotNone(bot.juegos_ejecutandose.get(self.id_prueba_1))
        bot.limpiar(self.id_prueba_1)
        self.assertIsNone(bot.juegos_ejecutandose.get(self.id_prueba_1))


    #Genero una lista con todos los movimientos posibles tipica, y evaluo si la funcion comparacion me devuelve el mejor movimiento posible
    def test_comparacion(self):
        moves_test = [[(1, 12), (0, 10), 586, 'Hb'], [(1, 12), (0, 14), 686, 'Hr'], [(1, 12), (2, 10), 86, 'Hp'], [(1, 12), (2, 14), 86, 'Hp'], [(1, 12), (3, 11), 186, 'Hp'], [(1, 12), (3, 13), 186, 'Hp'], [(14, 13), (12, 14), 1500, 'Hq'],[(1, 11), (0, 11), -299, 'Rb'], [(1, 11), (1, 10), -299, 'Rb'], [(1, 11), (2, 11), -799, 'Rp'], [(13, 1), (12, 0), 3000, 'Pk'], [(13, 8), (12, 9), 3000, 'Pk'], [(13, 10), (12, 9), 3000, 'Pk'], [(13, 13), (12, 14), 2250, 'Pq'], [(13, 15), (12, 14), 2250, 'Pq'],[(12, 1), (10, 1), 500], [(12, 2), (10, 2), 500], [(12, 3), (10, 3), 500], [(12, 4), (10, 4), 500], [(12, 5), (10, 5), 500], [(12, 6), (10, 6), 500], [(12, 7), (10, 7), 500], [(12, 8), (10, 8), 500], [(12, 10), (10, 10), 500], [(12, 11), (10, 11), 500], [(12, 12), (10, 12), -9500], [(12, 13), (10, 13), 500], [(12, 15), (10, 15), 500]]
        
        best_move_test = bot.comparacion (moves_test)
        best_move_correcto = [(13, 1), (12, 0), 3000, 'Pk']

        self.assertEqual(best_move_test, best_move_correcto)


    
    #Recibo la "data" de un evento "your_turn" tipico y debo responder: creando un nuevo juego y devolviendo un movimiento
    def test_bot_work_new_game(self):
        data = {
        'board_id': '329f0cc1-e50f-4d53-b565-05f8f5380983', 
        'turn_token': '9a7073f6-24ac-4216-8c21-9de70500a47c', 
        'username': 'EnzoC', 
        'actual_turn': 'black', 
        'board': 'rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppp p ppppppppp       ppppppppp                  q  pp              q              q             Q          QQ                  P     q P     q   P  P P    P P q     PP P   P             P          Q  BBHHRR     BQQKqBBHHRR', 
        'move_left': 55, 
        'opponent_username': 'Ulrazen'}
        
        move_expected = [(15, 9), (15, 8), 9]
        move = bot.bot_work(data)
        
        self.assertEqual(move, move_expected)
        self.assertEqual(len(bot.juegos_ejecutandose), 3)                               #Comprobar cantidad de juegos almacenados (deberian estar los 2 del setUp y el nuevo de este test)
        bot.limpiar('329f0cc1-e50f-4d53-b565-05f8f5380983')
        self.assertEqual(len(bot.juegos_ejecutandose), 2)                               #Elimine el juego que habia creado en este test (para que no haya conflicto con los demas test y para probar bot.limpiar)
        

    #Partida almacenada contra mi mismo (el objeto fue iniciado como "white" pero ahora debo responderme con las negras usando el mismo objeto)
    def test_bot_work_myself(self):
        data = {
        'board_id': 'sfjijoisjef283749',                       #game inicializado como white en el setUp
        'turn_token': '9a7073f6-24ac-4216-8c21-9de70500a47c', 
        'username': 'EnzoC',                                   #username == opponent_username
        'actual_turn': 'black',                                #Turno actual "black" 
        'board': '   h b  Q bbhhrr   b    kkbbhhrr         ppppppp                                                        p                                                      b             b                                        PPPPPPPPPP     B QKKBBHHRR     Q QKKBBHHRR', 
        'move_left': 50, 
        'opponent_username': 'EnzoC'}
        
        move_expected = [(1, 8), (0, 8), 89 ,'kQ']   
        move = bot.bot_work(data)
        
        self.assertEqual(move, move_expected)
        self.assertEqual(len(bot.juegos_ejecutandose), 2)   #Tienen estar solo los 2 juegos del setUp (accedo a un game ya creado)

    
    #Testeo mas especificamente "restart_atributes"   (Solo se ejecuta cuando juego contra mi mismo)
    def test_restart_atributes(self):
        game = bot.juegos_ejecutandose[self.id_prueba_2]    #Juego inicializado como "black"
        
        self.assertEqual(game.color, False)                                             #Compruebo al menos 2 atributos antes del reset
        self.assertEqual(game.valor_row_strategy, {7:3 ,6:1 ,5:2    ,8:5 ,10:4})

        bot.restart_atributes("white", game)
        self.assertEqual(game.color, True)                                              #Compruebo que los atributos han cambiado luego del rest
        self.assertEqual(game.valor_row_strategy, {8:3 ,9:1 ,10:2    ,7:5 ,5:4})
        

    