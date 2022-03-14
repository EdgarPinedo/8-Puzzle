#import resource
import sys
import numpy as np

from bfs import BFS
from board import Board

def main():
    p = input("Ingresa el estado inicial: ") 
    tablero = Board(np.array(eval(p)))
    s = BFS(tablero)
    s.solve()

    print('\nCamino a la meta: ' + str(s.path) + '\n')
    print('Costo del camino: ' + str(len(s.path)) + '\n')
    print('Nodos expandidos: ' + str(s.nodes_expanded) + '\n')
    print('Nodos explorados: ' + str(len(s.explored_nodes)) + '\n')
    print('Profundidad de búsqueda: ' + str(s.solution.depth) + '\n')
    print('Profundidad máxima de búsqueda: ' + str(s.max_depth) + '\n')

if __name__ == "__main__":
    main()