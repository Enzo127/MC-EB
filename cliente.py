'''
El cliente establece la conexion con el server via websocket y responde a los eventos que este envie, si le llega el evento "your_turn", envia la data del turno al archivo
bot y espera el movimiento con el que responder al server (este programa es un dummy que no procesa data alguna).
'''
import asyncio
import websockets
import json
import time
import bot
from bot import bot_work, limpiar

board = [                                                                                      
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]



msg_accept = '''{
"action": "accept_challenge", 
"data": { 
"board_id": "2d348323-2e79-4961-ac36-1b000e8c42a5" 
}
}
'''
p_msg_accept = json.loads(msg_accept)


msg_move = '''{
"action": "move",
"data": {
"board_id": "2d348323-2e79-4961-ac36-1b000e8c42a5",
"turn_token": "e40573bb-138f-4171-a200-66258f546755",
"from_row": 12,
"from_col": 0,
"to_row": 11,
"to_col": 0
}
}'''
p_msg_move = json.loads(msg_move)


async def conexion(): 
    #URL 
    url_base = "ws://megachess.herokuapp.com/service?authtoken="
    #Mete un print que le diga al usuario que ponga su token o enter para el mio por defecto
    #Ingresar token o usar el mio por defecto
    #token = input('Enter token: ')
    #if (len(token) < 1): token = '34c0015f-0ec5-4599-9b27-c9253497533d'
    token='3981ee15-5df7-4633-bf31-7bb921534ecb'
    url_jugador = url_base + token        
    
    async with websockets.connect(url_jugador) as socketa:
        print ("Conectando a {}".format(url_jugador))
        await eventos(socketa)                                                  #Se ejecuta por siempre el verificador de eventos
        print ("FIN")                                                           #Si por algun motivo terminara la funcion "eventos", pasarias por aca y terminaria la ejecucion

#Podes armar una funcion por aca como en el ej de prueba, a la cual le pasas el websocket y el mensaje a enviar y esta lo envia (esa funcion es await, asique hasta el mejor que cedas ahi)


async def eventos(socketa):  
    while True:
        response = await socketa.recv()
        data = json.loads(response)

        #EVENTO: Lista de jugadores online actualizada
        if data['event'] == 'update_user_list':
            print("Actualizar lista")
            players = data["data"]["users_list"]
            print (players)
            print ()

        #EVENTO: Fin de la partida
        if data['event'] == 'gameover':
            
            print("\nFIN DE LA PARTIDA\n")    
            i=0
            for r in range(len(board)):
                for c in range(len(board[r])):
                    board[r][c] = data["data"]["board"][i]
                    i=i+1
            for line in board:
                print(line)
            print("Identificador de partida:",data["data"]["board_id"])
            print("Jugador blanco: " , data["data"]["white_username"] , data["data"]["white_score"])
            print("Jugador negro : " , data["data"]["black_username"] , data["data"]["black_score"])
            try:    
                limpiar(data["data"]["board_id"])    #Al terminar la partida, cierro el objeto game con el board_id correspondiente
                
            except:       #Este except esta solo porque cuando juego contra mi mismo, al terminar la partida, intento limpiar el objeto 2 veces y eso me da error
                pass      

        #EVENTO: Solicitud de movimiento (continuacion o inicio de partida)
        if data['event'] == 'your_turn':            
            #1) Actualizacion de campos
            p_msg_move["data"]["turn_token"] = data["data"]["turn_token"]       #Actualizacion de turn token (debe actualizarse en cada turno)
            p_msg_move["data"]["board_id"]   = data["data"]["board_id"]         #Actualizacion de board_id   (Si posteriormente creo una sola vez el objeto partida, este paso es necesario realizarlo una sola vez(igual que con el color))
            
            
            #2) LLamo a la logica de la IA para que me devuelva el mejor movimiento para el estado actual del tablero
            move_choice = bot_work(data["data"])
            #await asyncio.sleep(2)
            print("Move:",move_choice)

            #3) Conformacion de la respuesta
            p_msg_move["data"]["from_row"] = move_choice[0][0]                  #Start_SQ
            p_msg_move["data"]["from_col"] = move_choice[0][1]
            p_msg_move["data"]["to_row"]   = move_choice[1][0]                  #End_SQ
            p_msg_move["data"]["to_col"]   = move_choice[1][1]
            
            #4) Envio de la respuesta en formato JSON
            msg_move = json.dumps(p_msg_move)
            await socketa.send(msg_move)        #esto deberia estar en una funcion aparte, mira la guia

        #EVENTO: Solicitud de partida recibida
        if data['event'] == 'ask_challenge':
            if data["data"]["username"] == "Julieta":
                pass
            else:
                print("New challenger: {} has arrived".format(data["data"]["username"]))    #Desafiante

                #Proba esto despues, la pagina no envia el campo "message"
                '''if len(data["data"]["message"]) > 0:
                    print (data["data"]["message"])
                '''
                #h=1
                #if h==2:

                
                confirmacion = input("Aceptar desafio? (y/n)")
                if confirmacion == "y":                                                     #Desafio aceptado
                    p_msg_accept["data"]["board_id"] = data["data"]["board_id"]             #Actualizo el mensaje de aceptacion con el board_id correspondiente
                    enviar_aceptacion =  json.dumps(p_msg_accept)                           #Convierto el diccionario python a string JSON
                    await socketa.send(enviar_aceptacion)                                   #Envio el msj de aceptacion via websocket

                else:
                    print("Invitacion de {} rechazada".format(data["data"]["username"]))    #Desafio rechazado
                        
if __name__ == '__main__':
    #LLama a conexion

    asyncio.run(conexion())
