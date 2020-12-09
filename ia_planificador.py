'''
Este programa es el vinculo entre la data recibida por "bot" y las 2 partes de la estrategia para elegir los mejores movimientos (es la columna vertebral de la ia).

La estrategia de la ia se compone de 2 partes:
1) Con mis movimientos y los del rival ---> Mapeo todos los casilleros del tablero con los eventos posibles (capturas mias, capturas del rival, casilleros en mi control, etc.)
2) Establecer una prioridas sobre que eventos son mas importantes que otros y calificar los movimientos que corresponden a tal evento.

Para el paso 1) se importa "ia_board_eventos"
Para el paso 2) se importa "ia_calificador"

En definitiva: Recibe la data del estado actual del game y debe devolver una lista con los mejores movimientos calificados.
'''

from ia_board_eventos import analizador_eventos, eventos
import ia_calificador

def inicio(moves, moves_enemy, game):   
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------(1) Mapeo de eventos----------------------------------------------------------------------------------                                                                    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #i)   Generar board de eventos    
    board_eventos     = analizador_eventos(moves, moves_enemy, game.color ,game.board)    

    #ii)  Buscar los eventos $, & y ? y guardar el casillero en que se encuentran
    lista_desordenada = eventos(board_eventos)

    #iii) Buscar los movimientos validos que tienen como endRow el casillero del evento
    lista_capturas_limpias = []                                                                 #Capturas limpias mias ($)
    lista_capturas_limpias = finder(moves, lista_desordenada[0],lista_capturas_limpias)


    lista_capturas_rival = []                                                                   #Capturas del rival  (&)    
    tipo=0
    for piece in range(6):
        for movement in moves_enemy[piece][tipo]:
            if movement != []:
                lista_capturas_rival.append(movement)


    lista_capturas_sucias = []                                                                  #Capturas sucias mias (?)
    lista_capturas_sucias = finder(moves, lista_desordenada[1],lista_capturas_sucias) 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------(2) Calificador de movimientos------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    moves_analysis = []
    # i) Capturas limpias                       ($)
    if lista_capturas_limpias != []: 
        
        if len(lista_capturas_limpias) > 1:
            moves_analysis = ia_calificador.analisis_capturas_limpias(lista_capturas_limpias ,moves_analysis)
            moves_analysis = ia_calificador.extra_capturas_limpias   (lista_capturas_rival ,moves_analysis)

            print("Respondo con captura limpia")
            return moves_analysis

        else:
            print("Respondo con captura limpia")
            return lista_capturas_limpias
    
    # ii) Reina infiltrada al ataque            (?) Esto toma mayor relevancia cuando quedan solo 30 movimientos (evoluciona a importancia nivel c)
    if lista_capturas_sucias != []:
        moves_analysis = ia_calificador.reina_infiltrada(lista_capturas_sucias ,game.retaguardia_rival ,moves_analysis, True)

        if moves_analysis != []:
            print("respondo atacando su retaguardia")
            return moves_analysis

    # iii) Capturas rival                         (&)    
    if lista_capturas_rival != []:

        #a) Respuesta coontraatacando (apto para todas las piezas) (recordar que esta es una captura en la que expongo a mi pieza a ser recapturada)
        moves_analysis = ia_calificador.analisis_capturas_rival_contraataque (lista_capturas_rival, lista_capturas_sucias ,moves_analysis)
        if moves_analysis != []:
            print("Respondo con contraataque")
            return moves_analysis

        #b) Respuesta infiltrando una reina mia en su retaguardia
        moves_analysis = ia_calificador.reina_infiltrada(lista_capturas_sucias ,game.retaguardia_rival ,moves_analysis, False)

        if moves_analysis != []:
            print("respondo atacando su retaguardia")
            return moves_analysis

        #c) Respuesta moviendose a row estrategica (solo apto para reinas)
        moves_analysis = ia_calificador.analisis_capturas_rival_retirada    (lista_capturas_rival, moves, board_eventos ,game.qq_row_strategy ,game.valor_row_strategy ,moves_analysis)
        if moves_analysis != []:
            print("Respondo con retirada a row estrategica")
            return moves_analysis
    
    # iii) Movimientos estrategicos de reinas     (moves[5][1][1] a espacios con evento "+" o " ")
    row_upgrade = game.row_strategy["upgrade_mia"]
    queens_in_row_upgrade_mia = game.qq_row_strategy[row_upgrade]
    data_row_upgrade = [row_upgrade ,queens_in_row_upgrade_mia]

    if game.queens_Quantity >= 2 or queens_in_row_upgrade_mia >= 1:        #or game.qm_row_upgrade>1
        
        piece = 5
        tipo  = 1
        moves_analysis = ia_calificador.move_strategic(moves[piece][tipo] ,board_eventos ,data_row_upgrade ,game.qq_row_strategy ,game.valor_row_strategy, game.retaguardia_mia ,moves_analysis) #----------->EN VEZ DE PASAR TODOS LOS MOVES, PODRIAS PASAR moves[5][1]

        if moves_analysis != []:
            print("Respondo con un movimiento estrategico")
            return moves_analysis
    
    # iv) Avance de peones
    if moves_analysis == [] and lista_capturas_limpias == []:
        moves_analysis = peon_avance(moves, game)
        print("Respondo con avance de peones")
        return moves_analysis


#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def peon_avance (moves, game):
    piece = 0
    tipo  = 1
    moves_selected = []

    #esto se reescribe siempre, lo podrias intentar meter en game, asi no lo reescribis en cada llamada a esta funcion
    if game.color == True:
        valor_peon = {13:10, 12:25 ,11:30 ,10:35 ,9:75 ,8:90}         #row=8 ----> Coronacion

    else:
        valor_peon = {2:10  ,3:25  ,4:30  ,5:35  ,6:75 ,7:90}         #row=7 ----> Coronacion


    for movement in moves[piece][tipo]:
        movement[2] = valor_peon[movement[1][0]] + game.best_col[movement[1][1]]  #para probar, saque movement[2] de la suma(no acarreo valores pasados, fijate si lo queres asi)
        moves_selected.append(movement)
                       
    return moves_selected


def finder(moves, buscado, encontrado):       #si multiple=True , esa pieza puede hacer mas de una captura
    tipo=0                                              #si multiple=False, esa pieza tiene una sola captura, por lo que se corta la iteracion y pasamos a otra
    for buscar in buscado:
        for piece in range(6):
            for movement in moves[piece][tipo]:
                if  movement[1] == buscar:
                    encontrado.append(movement)

    return encontrado



