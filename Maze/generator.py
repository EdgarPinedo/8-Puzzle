
from random import randint
from main import Grid_Position

def initialState():
    rows = randint(2, 500)
    columns = randint(2, 500)
    startingPosition = target = Grid_Position(0, 0)

    while startingPosition == target:
        startingPosition = Grid_Position(randint(0, rows - 1), randint(0, columns - 1))
        target = Grid_Position(randint(0, rows - 1), randint(0, columns - 1))
    
    maze = []
    for row in range(rows):
        maze.append([])
        for column in range(columns):
            currentPos = Grid_Position(row, column)
            state
            if startingPosition == currentPos or target == currentPos:
                state = 1
            else:
                state = randint(0, 1)
            maze[row].append(state)
    

