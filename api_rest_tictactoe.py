from flask import Flask, render_template as render, request, session
import json
import random
import os.path

app = Flask(__name__)

class Game:
    # Variable para conocer si maquina juega con "x" u "o"
# True , Maquina juega con x
# False, Maquina juega con o
    firstMachine = True
    dataGAMES = {}
    pathFileGAMES = "games.json"

    # Obtiene todo el contenido del archivo <.json>. 
    # Devuelve un json
    def getFile(rutaFile):
        with open(rutaFile) as file:
            data = json.load(file)
        return data       

    def exists_file_to_save(path_file_on_save_games):
        # Verifica si el archivo en el cual se desea guardar jugadas existe
        if os.path.exists(path_file_on_save_games): 
            return True    
        return False 
    
    def write_on_file_plays(date_games_to_save, path_file_on_save_games):
        with open(path_file_on_save_games, 'w') as file:
            json.dump(date_games_to_save, file, indent=4)

    #Recibe un tablero del estado del juego, 
    # y devuelve un array con las posiciones que están marcadas con un simbolo, 
    # ya sea <x> o <o>
    def boxesMarkedWith(board,symbol):  
        markeredPositions=[]
        for positionBoard in range(9):
            if board[positionBoard] == symbol:
                markeredPositions.append(positionBoard)    
        return markeredPositions

    # Verifica si el estado actual del juego está contenido en un estado ganador de la base de datos.
    # Devuelve un Booleano
    def currentBoardIsContent(currentBoard, evaluationBoard, first_machine):    
        is_current = True
        for positionBoard in range(9):
            if first_machine and (currentBoard[positionBoard] != 'b'):
                if currentBoard[positionBoard] != (evaluationBoard[positionBoard]):
                    is_current = False
                    return is_current
            elif (first_machine == False) and (currentBoard[positionBoard] != 'b'):
                if currentBoard[positionBoard] == (evaluationBoard[positionBoard]):
                    is_current = False
                    return is_current
        return is_current

    # Encuentra el conjunto intersección de dos arrays
    # Devuelve el conjunto de posiciones que puede tomar la maquina
    def intersection_positions(array_positions_evaluation_board, array_positions_current_board):
        array_positions = array_positions_evaluation_board[:] #Clonamos el array que tiene mas posiciones; el de mayor longitud
        for i in range(0, len(array_positions_current_board)):
            print(array_positions_current_board[i])
            if (array_positions_current_board[i] in array_positions_evaluation_board):
                array_positions.remove(array_positions_current_board[i])
        
        return array_positions


    # Devuelve la posición de la jugada a realizar
    def next_play(possibles_played):           
        while True:  
            possible_position = random.randint(0, 8)   
            if  possible_position in possibles_played:
                return possible_position                    
        return 0
    
    def next_played_random(current_play):           
        while True:  
            possible_position = random.randint(0, 8)   
            if  current_play[possible_position] == 'b':
                return possible_position                    
        return 0

# -----------------------------------------------------------------------------------------------------
# APRENDE NUEVA JUGADA
# Agrega una nueva jugada al JSON que contiene las jugadas aprendidas
@app.route('/learn_play', methods = ['POST'])
def learn_new_play():
    new_play_to_add = request.get_json()

    key_to_add = ""
    value_to_add = "positive"
    # obtiene la clave y el valor del JSON recibido
    for key_play in new_play_to_add.keys():
        key_to_add = key_play
        value_to_add = new_play_to_add[key_to_add]
    
    try:
        json_all_plays_learned = Game.getFile(Game.pathFileGAMES)    #Trae todas las jugadas aprendidas
        json_all_plays_learned[key_to_add] # Antes de agregar la jugada, verifica si la jugada ya está aprendida
        # Si la jugada no está aprendida, procede a añadirla
    except KeyError:
        json_all_plays_learned[key_to_add] = value_to_add
        Game.write_on_file_plays(json_all_plays_learned, Game.pathFileGAMES)
        return 'La jugada ha sido aprendida'
    # Si no puede traer todas las jugadas aprendidas es porque no ha aprendido alguna jugada
    # Por tanto se procede a agregar la nueva jugada 
    except FileNotFoundError:
        Game.dataGAMES[key_to_add] = value_to_add
        Game.write_on_file_plays(Game.dataGAMES, Game.pathFileGAMES)
        return 'La jugada ha sido aprendida'

    return 'La jugada ya estaba aprendida'


# FUNCION EN DESARROLLO...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Devolverá la poscicion de la jugada que debe realizar la maquina
@app.route('/machine_next_play', methods = ['POST'])
def playMachine():  # Recibe el estado del tablero del juego actual de tictactoe 
                    # y un booblean que indica True si la maquina empezó a jugar primero

    request_front_end = request.get_json()
    current_play = request_front_end['state_current_play']
    first_machine = request_front_end['first_machine']
    #Obtiene todas las jugadas aprendidas, en formato json
    json_data_games = Game.getFile(Game.pathFileGAMES)

    #JUGAR A BLOQUEAR
    for possible_played in json_data_games.keys():
        # Verifica si el estado actual del juego está contenido en un juego ganador y si este es NEGATIVO
        #De ser asi, se procede a bloquear las jugadas del usuario
        if Game.currentBoardIsContent(current_play, possible_played, first_machine) and (json_data_games[possible_played] == "negative"):
            if first_machine: #Si es True, maquina está jugando con x             
                array_intersection_possible_played = (Game.intersection_positions(Game.boxesMarkedWith( possible_played, 'o'), Game.boxesMarkedWith( current_play, 'o')))
                return str(Game.next_play(array_intersection_possible_played))
            else: #Maquina está jugando con o
                array_intersection_possible_played = (Game.intersection_positions(Game.boxesMarkedWith( possible_played, 'x'), Game.boxesMarkedWith( current_play, 'x')))
                return str(Game.next_play(array_intersection_possible_played))  

    #JUGAR A GANAR
    for possible_played in json_data_games.keys():
        # Verifica si el estado actual del juego está contenido en un juego ganador y si este es positivo
        if Game.currentBoardIsContent(current_play, possible_played, first_machine) and (json_data_games[possible_played] == "positive"):
            if first_machine: #Si es True, maquina está jugando con x             
                array_intersection_possible_played = (Game.intersection_positions(Game.boxesMarkedWith( possible_played, 'x'), Game.boxesMarkedWith( current_play, 'x')))
                return str(Game.next_play(array_intersection_possible_played))
            else: #Maquina está jugando con o
                array_intersection_possible_played = (Game.intersection_positions(Game.boxesMarkedWith( possible_played, 'o'), Game.boxesMarkedWith( current_play, 'o')))
                return str(Game.next_play(array_intersection_possible_played))            
        
    # Si no reconoce el estado actual del juego en la Base de Datos, 
    # entonces realizará un movimiento random    
    return ('No sé esa jugada, pos hagamos esta : '+ str(Game.next_played_random(current_play)))


if __name__== '__main__':
    app.run(debug=True)

# print(boxesMarkedWith("xbbbxboox","x"))
#print(getFile(pathFileGAMES).keys())
# print(currentBoardIsContent( 'xbbbbbobb','xbbbxboox'))
# print(currentBoardIsContent( 'xbbbbboxb','xbbbxboox'))
# print(currentBoardIsContent( 'obbbbbxbb','xbbbxboox'))
# print(currentBoardIsContent( 'obbbbbxob','xbbbxboox'))

# print(intersection_positions( [1,2,3,4],[2,4,3]))


