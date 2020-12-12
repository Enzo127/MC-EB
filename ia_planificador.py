'''
Este programa es el vinculo entre la data recibida por "bot" y las 2 partes de la estrategia para elegir los mejores movimientos (es la columna vertebral de la ia).

La estrategia de la ia se compone de 2 partes:
1) Con mis movimientos y los del rival ---> Mapeo todos los casilleros del tablero con los eventos posibles (capturas mias, capturas del rival, casilleros en mi control, etc.)
2) Establecer una prioridas sobre que eventos son mas importantes que otros y calificar los movimientos que corresponden a tal evento.

Para el paso 1) se importa "ia_board_eventos"
Para el paso 2) se importa "ia_calificador"

En definitiva: Recibe la data del estado actual del Game y debe devolver una lista con los mejores movimientos calificados.
'''

from ia_board_events import event_maker, event_search
import ia_calificador

def analisis_ia(moves, moves_enemy, Game):   
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------(1) Mapeo de eventos----------------------------------------------------------------------------------                                                                    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #i)   Generar board de eventos    
    board_eventos     = event_maker(moves, moves_enemy, Game.color ,Game.board)    

    #ii)  Buscar los eventos x, & y ? y guardar el casillero en que se encuentran
    lista_desordenada = event_search(board_eventos)

    #iii) Buscar los movimientos validos que tienen como endRow el casillero del evento
    lista_capturas_limpias = []                                                                 #Capturas limpias mias ($)
    lista_capturas_limpias = finder(moves, lista_desordenada[0],lista_capturas_limpias)

    lista_capturas_rival = []                                                                   #Capturas del rival  (&)
    lista_capturas_rival = finder_rival(moves_enemy , lista_capturas_rival)    

    lista_capturas_sucias = []                                                                  #Capturas sucias mias (?)
    lista_capturas_sucias = finder(moves, lista_desordenada[1],lista_capturas_sucias) 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------(2) Calificador de movimientos------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Los siguientes eventos estan ordenados por prioridad y el que ocurra primero es el que responde


    ia_calificador.queen_value(Game.queens_quantity)    #Actualizo el valor de mis reinas, dependiendo de la cantidad que disponga (mientras mayor cantidad, menos valor)
    moves_analysis = []
    # i) Capturas limpias                          ($)  #Las capturas limpias tienen maxima prioridad (capturas sin que me puedan recapturar)
    if lista_capturas_limpias != []: 
        
        if len(lista_capturas_limpias) > 1:             #Solo realizamos calificacion entre capturas limpias cuando hay mas de una (si solo hay una, realizar ese movimiento)
            lista_capturas_limpias = ia_calificador.capturas_limpias(lista_capturas_limpias)      #Añado el valor de la pieza capturadas a cada movimiento
            return lista_capturas_limpias

        else:                                            #Si tengo un solo movimiento en la lista de capturas limpias, no hace falta analizar comparaciones
            return lista_capturas_limpias
    

    # ii) Pieza infiltrada al ataque               (?) 
    #Tengo una pieza en la retaguardia rival con capturas sucias (es bueno que coma, porque las piezas en la retaguardia suelen ser valiosas)
    if lista_capturas_sucias != []:
        moves_analysis = ia_calificador.queen_infiltrated(lista_capturas_sucias ,Game.retaguardia_rival ,moves_analysis)
        if moves_analysis != []:
            return moves_analysis


    # iii) Capturas rival                         (&)    
    if lista_capturas_rival != []:
        #a) Respuesta coontraatacando (apto para todas las piezas) (esta es una captura sucia, en la que expongo a mi pieza a ser recapturada)
        print("respondo contraatacando")
        moves_analysis = ia_calificador.capturas_rival_contraataque (lista_capturas_rival, lista_capturas_sucias ,moves_analysis)
        if moves_analysis != []:
            return moves_analysis


        #b) Respuesta moviendose a row estrategica (solo apto para reinas) (modificado para todas las piezas)
        print("respondo con retirada")
        moves_analysis = ia_calificador.capturas_rival_retirada    (lista_capturas_rival, moves, board_eventos ,Game.qq_row_strategy ,Game.valor_row_strategy ,moves_analysis)
        if moves_analysis != []:
            return moves_analysis
    

    # iv) Movimientos estrategicos de reinas     (moves[5][1][1] a espacios con evento "+" o " ")
    row_upgrade = Game.row_strategy["upgrade_mia"]
    queens_in_row_upgrade_mia = Game.qq_row_strategy[row_upgrade]
    data_row_upgrade = [row_upgrade ,queens_in_row_upgrade_mia]

    if Game.queens_quantity >= 2 or queens_in_row_upgrade_mia >= 1:  #Solo los considero si tengo cierta cantidad de reinas y si alguna se encuentra en mi fila de upgrade
        piece = 5   #reina
        tipo  = 1   #movimiento a espacio libre
        moves_analysis = ia_calificador.move_strategic(moves[piece][tipo] ,board_eventos ,data_row_upgrade ,Game.qq_row_strategy ,Game.valor_row_strategy ,Game.row_strategy ,Game.retaguardia_mia ,moves_analysis) #----------->EN VEZ DE PASAR TODOS LOS MOVES, PODRIAS PASAR moves[5][1]

        if moves_analysis != []:
            return moves_analysis
    


    # v) Avance de peones                         #Si todas las condiciones superiores no se cumplen ---> Mover peones
    if moves_analysis == [] and lista_capturas_limpias == []:
        #Analisis de apertura
        #Analisis de apertura blanco  ------> Hay una apertura que es la mas eficiente de todas y las blancas parten con la ventaja de poder desarrollarla primero
        if Game.flag_apertura and Game.color:
            moves_analysis = ia_calificador.opening_white (moves[0][1], Game.row_strategy ,0)

        #Analsis de apertura negro    ------> Busco la mejor respuesta al 1er movimiento blanco para poder conquistar el centro lo mas rapido posible
        elif Game.flag_apertura and not Game.color:
            if Game.flag_first_move:               #Si soy el jugador negro y es mi 1er movimiento, tengo que elegir (una sola vez) cual es la mejor apertura
                Game.strategy = ia_calificador.opening_selector  (Game.board)   #Guardo en el objeto cual es la estrategia de apertura que voy a seguir
                Game.flag_first_move = False       #No volver a realizarlo el proximo turno

            if Game.strategy ==0:
                moves_analysis = ia_calificador.opening_black_complex (moves[0][1] ,Game.move_opening)  #Apertura complicada que responde a la mejor apertura blanca

            elif Game.strategy == 1:
                moves_analysis = ia_calificador.opening_white (moves[0][1], Game.row_strategy ,1)       #Respuesta a apertura blanca un poco mas debil

            elif Game.strategy == 2:
                moves_analysis = ia_calificador.opening_white (moves[0][1], Game.row_strategy ,0)       #Mejor estrategia de apertura posible (solo si el rival hizo su primer movimiento con un peon distito)
        
        if moves_analysis != []:    
            return moves_analysis


        Game.flag_apertura = False    #Si no hubo movimientos de apertura validos, pasamos a la ultima estrategia de peones

        #Analisis de movimientos con peones fuera de apertura
        moves_analysis = ia_calificador.peon_avance(moves[0][1], Game ,board_eventos)      #moves[0][1]----> movimientos de peones (moves[0]) y solo movimientos a espacios blancos (tipo=1)
        return moves_analysis
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Buscadores de movimientos respecto a los eventos encontrados
def finder(moves, buscado, encontrado):       
    tipo=0                                             
    for buscar in buscado:
        for piece in range(6):
            for movement in moves[piece][tipo]:
                if  movement[1] == buscar:
                    encontrado.append(movement)

    return encontrado


def finder_rival(moves_enemy ,lista_capturas_rival):
    tipo=0
    for piece in range(6):
        for movement in moves_enemy[piece][tipo]:
            if movement != []:
                lista_capturas_rival.append(movement)

    return lista_capturas_rival