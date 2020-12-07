import ia_funcionalidades

def inicio(moves, moves_enemy, game):   #es un desperdicio pasar el game completo de momento
    #1) Generar board de eventos    
    board_eventos = ia_funcionalidades.analizador_casilleros(moves, moves_enemy, True)

    #2) Buscar los eventos $, & y ? y guardar el casillero en que se encuentran
    lista_desordenada = ia_funcionalidades.eventos(board_eventos)

    #3) Buscar los movimientos validos que tienen como endRow el casillero del evento
    #Capturas limpias mias ($)
    lista_capturas_limpias = []
    lista_capturas_limpias = ia_funcionalidades.finder(moves, lista_desordenada[0],lista_capturas_limpias, True)
    lista_capturas_limpias = ia_funcionalidades.finder(moves, lista_desordenada[1],lista_capturas_limpias, False)

    #Capturas del rival  (&)    #estos son mas faciles de encontrar
    lista_capturas_rival = []
    tipo=0
    for piece in range(6):
        for movement in moves_enemy[piece][tipo]:
            if movement != []:
                lista_capturas_rival.append(movement)

    print("aca",lista_capturas_rival)

    #Capturas sucias mias (?)
    lista_capturas_sucias = []
    lista_capturas_sucias = ia_funcionalidades.finder(moves, lista_desordenada[2],lista_capturas_sucias, False) #si usas break perdes un par de terminos, pero capaz no es mala (analiza la primera pieza que pueda capturar..es incompleto pero capaz rinde, pensalo)..o na

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #4)                                                                     Verificar que camino tomar 
    moves_analysis = []
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # a) Capturas limpias                       ($)
    if lista_capturas_limpias != []:
        if len(lista_capturas_limpias) > 1:
            moves_analysis = ia_funcionalidades.analisis_capturas_limpias(lista_capturas_limpias)
            moves_analysis = ia_funcionalidades.extra_capturas_limpias   ( lista_capturas_rival ,moves_analysis)

            return moves_analysis


    # b) Capturas rival                         (&)    
    elif lista_capturas_rival != []:
        #moves_analysis = ia_funcionalidades.analisis_capturas_rival_contraataque (lista_capturas_rival, lista_capturas_sucias)
        print(game.valor_row_strategy)
        

        moves_analysis = ia_funcionalidades.analisis_capturas_rival_retirada     (lista_capturas_rival, moves, board_eventos ,game.valor_row_strategy ,moves_analysis)
        
        return moves_analysis
        

    # c) Movimientos estrategicos de reinas     (moves[5][1][1] a espacios con evento "+" o " ")



    # d) Avance de peones
    else:
        moves_analysis = peon_avance(moves, game)
        return moves_analysis


    # e) Capturas sucias                        (?) Esto toma mayor relevancia cuando quedan solo 30 movimientos (evoluciona a importancia nivel c)







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






