from flask import Flask, render_template as render, request
import json
import os.path


app = Flask(__name__)

# Variable para conocer si empezó a jugar primero la maquina o el usuario
# True , Empezó primero la maquina
# False, empezó jugando primero el usuario
# firstMachine = True
# dataGAMES = {}
# pathFileGAMES = "games.json"

# dataGAMES['xbbbxboox']='positive'
# dataGAMES['bbbbxboox']='negative'
# dataGAMES['xbbbxboob']='positive'


# FUNCION EN DESARROLLO...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Devolverá la poscicion de la jugada que debe realizar la maquina
@app.route('/machine_next_play', methods = ['POST'])
def playMachine():  # Recibe el estado del tablero del juego actual de tictactoe 
    request_front_end = request.get_json()
    current_play = request_front_end['state_current_play']
    first_machine = request_front_end['first_machine']
    return (current_play + ' | ' +first_machine)

if __name__== '__main__':
    app.run(debug=True)

    # File = getFile(pathFileGAMES)#Archivo JSON de las jugadas aprendidas
    # for keysData in File.keys():#Recorre las claves
    #     if File.get(keysData) == "positive":
    #         print("Si!!!!!")    



def exists_file_to_save(path_file_on_save_games):
    # Verifica si el archivo en el cual se desea guardar jugadas
    if os.path.exists(path_file_on_save_games): 
        return True    
    return False


# Obtiene todo el contenido del archivo <.json>. 
# Devuelve un json
def getFile(rutaFile):
    with open(rutaFile) as file:
        data = json.load(file)
    return data             
    
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
def currentBoardIsContent(currentBoard, evaluationBoard):    
    is_current = True
    for positionBoard in range(9):
        if firstMachine and (currentBoard[positionBoard] != 'b'):
            if currentBoard[positionBoard] != (evaluationBoard[positionBoard]):
                is_current = False
                return is_current
        elif (firstMachine == False) and (currentBoard[positionBoard] != 'b'):
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
def next_play(current_board, evaluation_board):
    if currentBoardIsContent(current_board, evaluation_board):
        return 0
        
    else:
        return 0 #SALIDA EN DESARROLLO...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# sii = True if (1 in [2,3,1]) else False
# print(sii)   




# print(boxesMarkedWith("xbbbxboox","x"))
#print(getFile(pathFileGAMES).keys())
# print(currentBoardIsContent( 'xbbbbbobb','xbbbxboox'))
# print(currentBoardIsContent( 'xbbbbboxb','xbbbxboox'))
# print(currentBoardIsContent( 'obbbbbxbb','xbbbxboox'))
# print(currentBoardIsContent( 'obbbbbxob','xbbbxboox'))

# print(intersection_positions( [1,2,3,4],[2,4,3]))


