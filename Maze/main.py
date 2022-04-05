from collections import deque
import pprint
from random import randint

# Generate 
def initialState():
    rows = randint(20, 50)
    columns = randint(20, 150)
    startingPosition = target = Grid_Position(0, 0)

    while startingPosition == target:
        startingPosition = Grid_Position(randint(0, rows - 1), randint(0, columns - 1))
        target = Grid_Position(randint(0, rows - 1), randint(0, columns - 1))
    
    maze = []
    for row in range(rows):
        maze.append([])
        for column in range(columns):
            currentPos = Grid_Position(row, column)
            state = 1
            if startingPosition == currentPos or target == currentPos:
                state = 1
            else:
                state = randint(0, 1)
            maze[row].append(state)
    
    return maze, startingPosition, target

# to keep track of the blocks of maze
class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def inside(self, rows, columns):
        return 0 <= self.x and self.x < rows and 0 <= self.y and self.y < columns
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# each block will have its own position and cost of steps taken
class Node:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost
    
def recoverThePath(previousBlock, dest: Grid_Position, start: Grid_Position):
    path = []
    while dest != Grid_Position(-1, -1):
        path.append(dest)
        dest = previousBlock[dest.x][dest.y]
    path.reverse()
    return path

#BFS algo for the maze
def bfs(Grid, dest: Grid_Position, start: Grid_Position):
    # to get neighbours of current node
    adj_cell_x = [-1, +0, +0, +1]
    adj_cell_y = [+0, -1, +1, +0]
    rows, columns = (len(Grid), len(Grid[0])) # n for rows, m for columns
    visited_blocks = [[False for i in range(columns)]
                for j in range(rows)]
                
    previousBlock = [[Grid_Position(-1, -1) for i in range(columns)]
                for j in range(rows)]
    visited_blocks[start.x][start.y] = True
    queue = deque()
    sol = Node(start, 0)
    queue.append(sol)

    movements = 4
    cost = 0
    while queue:
        current_block = queue.popleft()  # Dequeue the front cell
        current_pos = current_block.pos
        cost = cost + 1
        
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Algorithm used = BFS")
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return recoverThePath(previousBlock, dest, start), current_block.cost # build the path

        for i in range(movements):
            newX = current_pos.x + adj_cell_x[i]
            newY = current_pos.y + adj_cell_y[i]
            newPosition = Grid_Position(newX, newY)
            if newPosition.inside(rows, columns) == True and Grid[newX][newY] == 1 and not visited_blocks[newX][newY]:
                nextCell = Node(newPosition, current_block.cost + 1)
                visited_blocks[newX][newY] = True
                previousBlock[newX][newY] = current_pos    
                queue.append(nextCell)
    return [], -1

#Iterative DFS algo for the maze
def iterativeDfs(Grid, dest: Grid_Position, start: Grid_Position):
    adj_cell_x = [+1, +0, +0, -1]
    adj_cell_y = [+0, +1, -1, +0]
    rows, columns = (len(Grid), len(Grid[0]))
    visited_blocks = [[False for i in range(columns)]
               for j in range(rows)]
    
    previousBlock = [[Grid_Position(-1, -1) for i in range(columns)]
                for j in range(rows)]
    visited_blocks[start.x][start.y] = True
    stack = deque()
    sol = Node(start, 0)
    stack.append(sol)

    movements = 4
    cost = 0
    while stack:
        current_block = stack.pop()
        current_pos = current_block.pos
        cost = cost + 1

        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Algorithm used = Iterative DFS")
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return recoverThePath(previousBlock, dest, start), current_block.cost
     
        for i in range(movements):
            newX = current_pos.x + adj_cell_x[i]
            newY = current_pos.y + adj_cell_y[i]
            newPosition = Grid_Position(newX, newY)
            if newPosition.inside(rows, columns) == True and Grid[newX][newY] == 1 and not visited_blocks[newX][newY]:
                nextCell = Node(newPosition, current_block.cost + 1)
                visited_blocks[newX][newY] = True
                previousBlock[newX][newY] = current_pos    
                stack.append(nextCell)
    return [], -1


# Recursive DFS algo for the maze
def solve(Grid, dest: Grid_Position, currentBlock: Grid_Position, visitedBlock, previousBlock, cost : int):    
    visitedBlock[currentBlock.x][currentBlock.y] = True

    if dest == currentBlock:
        return previousBlock, cost

    adj_cell_x = [+1, +0, +0, -1]
    adj_cell_y = [+0, +1, -1, +0]
    rows, columns = (len(Grid), len(Grid[0]))

    movements = 4
    for i in range(movements):
        newX = currentBlock.x + adj_cell_x[i]
        newY = currentBlock.y + adj_cell_y[i]
        nextBlock = Grid_Position(newX, newY)

        if (nextBlock.inside(rows, columns) == True) and (Grid[newX][newY] == 1) and (not visitedBlock[newX][newY]):
            previousBlock[newX][newY] = currentBlock

            previousBlockCopy, costCopy = solve(Grid, dest, nextBlock, visitedBlock, previousBlock, cost + 1)
            if previousBlockCopy != None:
                return previousBlockCopy, costCopy
    return None, None

def recursiveDfs(Maze, dest: Grid_Position, start: Grid_Position):
    rows, columns = (len(Maze), len(Maze[0]))
    visitedBlock = [[False for i in range(columns)]
                for j in range(rows)]
                
    previousBlock = [[Grid_Position(-1, -1) for i in range(columns)]
                for j in range(rows)]
    
    previousBlock, cost = solve(Maze, dest, start, visitedBlock, previousBlock, 0)

    if previousBlock != None:
        print("Algorithm used = Recursive DFS")
        print("Path found!!")
        print("Total nodes visited = ", cost)
        return recoverThePath(previousBlock, dest, start), cost

    return [], -1
    
    


def main():
    noPath = True
    while noPath == True:
        maze, starting_position, destination = initialState()
        # print(maze)

        # maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #         [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        #         [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        #         [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        #         [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
        #         [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        #         [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        #         [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        #         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        #         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        #         [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # destination = Grid_Position(10, 0)
        # starting_position = Grid_Position(4, 11)

        # path, res = iterativeDfs(maze, destination, starting_position)
        path, res = recursiveDfs(maze, destination, starting_position)

        if res != -1:
            for row in range(len(maze)):
                for column in range(len(maze[0])):
                    # print(row, column)
                    currentCell = Grid_Position(row, column)
                    character = '.'
                    if currentCell == starting_position:
                        character = 'S'
                    elif currentCell == destination:
                        character = 'D'
                    elif maze[row][column] == 0:
                        character = '▀'
                    print(character, end = "")
                print()

            print("\n\nPath: ")
            for cell in path:
                print(f'[{cell.x}, {cell.y}]')
            print("Shortest path steps =", res)
            noPath = False
        else:
            print("Path does not exit")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("main start\n")
    main()