from solver import Solver

class DFS(Solver):
    def __init__(self, initial_state):
        super(DFS, self).__init__(initial_state)
        self.reached = False
        self.frontier = []

    def solve(self, recursive):
        if recursive == True:
            self.__recursiveDFS(self.initial_state)
        else:
            self.__iterativeDFS()
        
    def __recursiveDFS(self, board):
        self.explored_nodes.add(tuple(board.state))
        if board.goal_test():
            self.reached = True
            self.set_solution(board)

        if self.reached == False:
            for neighbor in board.neighbors():
                if tuple(neighbor.state) not in self.explored_nodes:
                    self.__recursiveDFS(neighbor)
                    self.max_depth = max(self.max_depth, neighbor.depth)
    
    def __iterativeDFS(self):
        self.frontier.append(self.initial_state)
        while self.frontier:
            board = self.frontier.pop()
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                break
            for neighbor in board.neighbors()[::-1]:
                if tuple(neighbor.state) not in self.explored_nodes:
                    self.frontier.append(neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)

