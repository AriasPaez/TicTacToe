from flask import Flask, render_template as render, request, session, jsonify, Markup, flash
import json
import random
import os.path

app = Flask(__name__)
app.secret_key = 'no se la digas a nadie'

board = [['', ''] for _ in range(9)]
board.append(True)

class Game:
    dataGAMES = {}
    pathFileGAMES = "games.json"    
    def clear_board(board, color):
        for n in range(len(board) - 1):
            board[n][1] = Markup('style="border: 1 solid' + color +
                                ';" disabled')
    def is_winner(board):
        array_exit = []

        #----------0 1 2 -----------#
        row = board[0][0] + board[1][0] + board[2][0]
        if row.count('x') == 3:
            Game.clear_board(board, 'red')
            array_exit.append(True)
            array_exit.append('red')
            return array_exit
        elif row.count('o') == 3:
            Game.clear_board(board, 'green')
            array_exit.append(True)
            array_exit.append('green')
            return array_exit

        #----------3 4 5 -----------#
        row = board[3][0] + board[4][0] + board[5][0]
        if row.count('x') == 3:
            Game.clear_board(board, 'red')
            array_exit.append(True)
            array_exit.append('red')
            return array_exit
        elif row.count('o') == 3:
            Game.clear_board(board, 'green')
            array_exit.append(True)
            array_exit.append('green')
            return array_exit

        #----------6 7 8 -----------#
        row = board[6][0] + board[7][0] + board[8][0]
        if row.count('x') == 3:
            Game.clear_board(board, 'red')
            array_exit.append(True)
            array_exit.append('red')
            return array_exit
        elif row.count('o') == 3:
            Game.clear_board(board, 'green')
            array_exit.append(True)
            array_exit.append('green')
            return array_exit
        
        #----------0 3 6 -----------#
        row = board[0][0] + board[3][0] + board[6][0]
        if row.count('x') == 3:
            Game.clear_board(board, 'red')
            array_exit.append(True)
            array_exit.append('red')
            return array_exit
        elif row.count('o') == 3:
            Game.clear_board(board, 'green')
            array_exit.append(True)
            array_exit.append('green')
            return array_exit

        #----------1 4 7 -----------#
        row = board[1][0] + board[4][0] + board[7][0]
        if row.count('x') == 3:
            Game.clear_board(board, 'red')
            array_exit.append(True)
            array_exit.append('red')
            return array_exit
        elif row.count('o') == 3:
            Game.clear_board(board, 'green')
            array_exit.append(True)
            array_exit.append('green')
            return array_exit

        #----------2 5 8 -----------#
        row = board[2][0] + board[5][0] + board[8][0]
        if row.count('x') == 3:
            Game.clear_board(board, 'red')
            array_exit.append(True)
            array_exit.append('red')
            return array_exit
        elif row.count('o') == 3:
            Game.clear_board(board, 'green')
            array_exit.append(True)
            array_exit.append('green')
            return array_exit

        #----------0 4 8 -----------#
        row = board[0][0] + board[4][0] + board[8][0]
        if row.count('x') == 3:
            Game.clear_board(board, 'red')
            array_exit.append(True)
            array_exit.append('red')
            return array_exit
        elif row.count('o') == 3:
            Game.clear_board(board, 'green')
            array_exit.append(True)
            array_exit.append('green')
            return array_exit

        #----------2 4 6 -----------#
        row = board[2][0] + board[4][0] + board[6][0]
        if row.count('x') == 3:
            Game.clear_board(board, 'red')
            array_exit.append(True)
            array_exit.append('red')
            return array_exit
        elif row.count('o') == 3:
            Game.clear_board(board, 'green')
            array_exit.append(True)
            array_exit.append('green')
            return array_exit

            
        # if len(''.join(map(lambda l: l[0], board[:-1]))) > 8:
        #     Game.clear_board(board, 'yellow')
        #     array_exit.append(False)
        #     array_exit.append('yellow')
        #     return array_exit

        if board[0][0] == 'b' or board[1][0] == 'b' or board[2][0] == 'b' or board[3][0] == 'b' or board[4][0] == 'b' or board[5][0] == 'b' or board[6][0] == 'b' or board[7][0] == 'b' or board[8][0] == 'b':
            array_exit.append(False)
            array_exit.append('')
            
            return array_exit
        else:
            # Game.clear_board(board, 'yellow')
            array_exit.append(False)
            array_exit.append('')
            return array_exit
        


        
    def to_format_JSON_LEARN(array_board,who_win):
        new_board = ''
        for i in range(9):
            if array_board[i][0] == '':
                array_board[i][0]='b'            
            new_board += array_board[i][0]        
        # board_dic = {'first_machine':str(array_board[-1]), 'state_current_play':str(new_board)}    
        board_dic = {str(new_board):str(who_win)}    
        # return jsonify("state_current_play:"+str(new_board)+",first_machine:"+str(array_board[-1]))
        return (board_dic)
        
    def to_format_JSON(array_board):
        new_board = ''
        for i in range(9):
            if array_board[i][0] == '':
                array_board[i][0]='b'            
            new_board += array_board[i][0]        
        board_dic = {'first_machine':str(array_board[-1]), 'state_current_play':str(new_board)}    
        # return jsonify("state_current_play:"+str(new_board)+",first_machine:"+str(array_board[-1]))
        return (board_dic)


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
    
    # Devuelve una jugada random.
    def next_played_random(current_play):           
        while True:  
            possible_position = random.randint(0, 8)   
            if  current_play[possible_position] == 'b':
                return possible_position                    
        return 0
    
        # FUNCION EN DESARROLLO...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Devolverá la poscicion de la jugada que debe realizar la maquina
    # @app.route('/machine_next_play', methods = ['POST'])
    def playMachine(request_front_end):  
        # Recibe el estado del tablero del juego actual de tictactoe 
        # y un booblean que indica True si la maquina empezó a jugar primero
        # request_front_end = request.get_json()
        first_machine = request_front_end['first_machine']
        current_play = request_front_end['state_current_play']
        
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
        return str(Game.next_played_random(current_play))
    # APRENDE NUEVA JUGADA
    # Agrega una nueva jugada al JSON que contiene las jugadas aprendidas
    
    def learn_new_play(new_play_to_add,who_win):
        # new_play_to_add = request.get_json()
        key_to_add = ""
        if who_win == 'red':
            value_to_add = "positive"
        elif who_win == 'green':
            value_to_add = "negative"
        # obtiene la clave y el valor del JSON recibido
        for key_play in new_play_to_add.keys():
            key_to_add = key_play
            # value_to_add = new_play_to_add[key_to_add]        
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



# -----------------------------------------------------------------------------------------------------
#@app.route('/index/<int:n>')
@app.route('/<int:n>')
def board_triky(n):
    ch = 'x'
    if board[-1]:
        ch = 'o'
    board[n][0] = ch
    board[n][1] = 'disabled'
    for i in range(9):
        if board[i][0] == 'b':
            board[i][0]=''  
    Game.is_winner(board)
    # YELLOW EN CASO DE EMPATE; ROJO SI GANA MAQUINA; VERDE SI GANA USUARIO
    if Game.is_winner(board)[0]:# and (Game.is_winner(board)[1] != 'yellow'):

        new_board_format = Game.to_format_JSON_LEARN(board,Game.is_winner(board)[1])
        print(new_board_format)
        print(Game.learn_new_play(new_board_format,Game.is_winner(board)[1]))
        for i in range(9):
                if board[i][0] == 'b':
                    board[i][0]='' 
        flash("Congratulations, You Win!")
        return render('index.html', board=board)         
    else:
        new_board_format = Game.to_format_JSON(board)
        
        if 'b' in new_board_format['state_current_play']:
            
            machine_of_play = Game.playMachine(new_board_format)
            board[int(machine_of_play)][0] = 'x'
            board[int(machine_of_play)][1] = 'disabled'
             
        if Game.is_winner(board)[0]:
            new_board_format = Game.to_format_JSON_LEARN(board,Game.is_winner(board)[1])
            print(new_board_format)
            print(Game.learn_new_play(new_board_format,Game.is_winner(board)[1]))
            for i in range(9):
                if board[i][0] == 'b':
                    board[i][0]='' 
            flash("I'm Sorry,You Lost! ")       
            return render('index.html', board=board)
        else:
            Tied = True
            for i in range(9):
                if board[i][0] == 'b':
                    Tied = False
                    board[i][0]='' 
            if Tied:
                flash("Tied Game! ")
                return render('index.html', board=board)
            else:
                flash("Keep playing! ")
                return render('index.html', board=board)
            


#@app.route('/index/r')
@app.route('/r')
def reset():
    for n in range(len(board) - 1):
        board[n] = ['', '']
    return render('index.html', board=board)
    

@app.route('/')
def page_home():
    return render('index.html', board=board)


if __name__== '__main__':
    app.run(host = "0.0.0.0",  debug=True)

