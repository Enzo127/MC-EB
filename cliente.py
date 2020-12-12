'''
El cliente establece la conexion con el server via websocket y responde a los eventos que este envie, si le llega el evento "your_turn", envia la data del turno al archivo
bot y espera el movimiento con el que responder al server (este programa es un dummy que no procesa data alguna).

No hay test de este archivo de programa debido a que no hay logica alguna (que pueda fallar) en esta seccion del programa.
'''
import asyncio
import websockets
import json
from bot import bot_work, limpiar

board_end_game = [                                                                                            
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

async def send(websocket, action, data):    #Termina de conformar el mensaje y lo envia via el websocket antes creado
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    await websocket.send(message)


async def conexion(): 
    print("Ingrese su token o presione 'Enter' para usar el usuario 'EnzoC':")
    url_base = "ws://megachess.herokuapp.com/service?authtoken="                   #URL 
    token = input('Enter token: ')                                                 #Ingresar token o usar el mio por defecto
    if (len(token) < 1): token = '3981ee15-5df7-4633-bf31-7bb921534ecb'            
    url_jugador = url_base + token        
    
    async with websockets.connect(url_jugador) as websocket:
        print ("Conectando a {}".format(url_jugador))
        await eventos(websocket)                                                  #Se ejecuta por siempre el verificador de eventos


async def eventos(websocket):  
    while True:
        response = await websocket.recv()
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
            for r in range(16):
                print
                for c in range(16):
                    board_end_game [r][c] = data["data"]["board"][i]
                    i=i+1

            for line in board_end_game :
                print(line)

            print("Identificador de partida:",data["data"]["board_id"])
            print("Jugador blanco: " , data["data"]["white_username"] , data["data"]["white_score"])
            print("Jugador negro : " , data["data"]["black_username"] , data["data"]["black_score"])
            try:    
                limpiar(data["data"]["board_id"])    #Al terminar la partida, elimino el objeto game con el board_id correspondiente
                
            except:       #Este except esta solo porque cuando juego contra mi mismo, al terminar la partida, intento limpiar el objeto 2 veces y eso me da error
                pass      


        #EVENTO: Error encontrado
        if data['event'] == 'response_error':
            print(data["data"])


        #EVENTO: Solicitud de movimiento (continuacion o inicio de partida)
        if data['event'] == 'your_turn':            
            #1) LLamo a la logica de la IA para que me devuelva el mejor movimiento para el estado actual del tablero
            move_choice = bot_work(data["data"])

            #2) Conformacion de la respuesta y llamado a la funcion que la envia al server
            await send(websocket , 'move' ,
            {   'board_id'  : data['data']['board_id'],
                'turn_token': data['data']['turn_token'],
                'from_row'  : move_choice[0][0],                 #Start_SQ
                'from_col'  : move_choice[0][1],                 
                'to_row'    : move_choice[1][0],                 #End_SQ
                'to_col'    : move_choice[1][1]                
            })


        #EVENTO: Solicitud de partida recibida
        if data['event'] == 'ask_challenge':
            print("New challenger: {} has arrived".format(data["data"]["username"]))    #Jugador desafiante

            confirmacion = input("Aceptar desafio? (y/n)")
            if confirmacion == "y":                                                     #Desafio aceptado
                await send(websocket, 'accept_challenge',                               #Envio el "action" correspondiente, junto con el board_id para que inicie la partida
                {'board_id' : data["data"]["board_id"]}
                )
                
            else:
                print("Invitacion de {} rechazada".format(data["data"]["username"]))    #Desafio rechazado
                        
if __name__ == '__main__':

    asyncio.run(conexion())     #LLama a conexion
