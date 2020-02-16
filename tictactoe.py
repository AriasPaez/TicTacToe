import json
import os.path

dataGAMES = {}
pathFileGAMES = "games.json"
# Variable para conocer si empezó a jugar primero la maquina o el usuario
# True , Empezó primero la maquina
# False, empezó jugando primero el usuario
firstMachine= False

dataGAMES['xbbbxboox']='positive'
dataGAMES['bbbbxboox']='negative'
dataGAMES['xbbbxboob']='positive'

# Verifica si el archivo en el cual se desea guardar jugadas
if os.path.exists(pathFileGAMES): 
    print("Existe")
else:
    print("NO!!!!!!!!!! Existe")  

# Obtiene todo el contenido del archivo <.json>. 
# Devuelve un json
def getFile(rutaFile):
    with open(rutaFile) as file:
        data = json.load(file)
    return data             
    

with open('games.json', 'w') as file:
    json.dump(dataGAMES, file, indent=4)

# FUNCION EN DESARROLLO...
# Devolverá la poscicion de la jugada que debe realizar la maquina
def playMachine(stateTable):  #Estado del tablero 
    File = getFile(pathFileGAMES)#Archivo JSON de las jugadas
    for keysData in File.keys():#Recorre las claves
        if File.get(keysData) == "positive":
            print("Si!!!!!")    

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
                print(positionBoard)
                print(currentBoard[positionBoard] ,' - ', (evaluationBoard[positionBoard]))
                is_current = False
                return is_current
        elif (firstMachine == False) and (currentBoard[positionBoard] != 'b'):
            if currentBoard[positionBoard] == (evaluationBoard[positionBoard]):
                is_current = False
                return is_current
    return is_current
            




# print(boxesMarkedWith("xbbbxboox","x"))
#print(getFile(pathFileGAMES).keys())
# print(currentBoardIsContent( 'xbbbbbobb','xbbbxboox'))
# print(currentBoardIsContent( 'xbbbbboxb','xbbbxboox'))
print(currentBoardIsContent( 'obbbbbxbb','xbbbxboox'))
print(currentBoardIsContent( 'obbbbbxob','xbbbxboox'))
