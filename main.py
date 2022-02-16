from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import numpy as np

'''
Function for creating random matrix of 0 and 1 of specific size
return: numpy.ndarray
'''

def create_matrix(x, y):
    matrix = np.random.randint(low=0, high=2, size=(y, x))
    return matrix


def find_path(matrix, start_x, start_y, stop_x, stop_y, diagonals=False, info=False):
    # create a grid
    grid = Grid(matrix=matrix)

    # create a start and end cell
    start = grid.node(start_x, start_y)
    end = grid.node(stop_x, stop_y)

    if diagonals:
        # create finder
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    else:
        finder = AStarFinder()

    # use finder
    path, runs = finder.find_path(start, end, grid)

    if not info:
        pass
    else:
        print('RUNS: ' + str(runs))
        print('PATH: ' + str(path))

    return path


'''
Function to test how many randomly generated square matrices with path from 
point (0,0) - right top corner to (x,x) - left bottom corner 
exists

param attempts: int - on how many randomly generated matrixes try to find path
param matrix_size: int - matrix size 5 is for example 5x5
diagonals: boolean - by default diagonal paths are disabled
return: int - length of list with existing paths for specified number of runs

'''


def testing_paths(attempts, matrix_size, diagonals=False):
    paths_list = []

    for i in range(0, attempts):
        matrix = create_matrix(matrix_size, matrix_size)
        path = find_path(matrix, 0, 0, matrix_size - 1, matrix_size - 1, diagonals)
        paths_list.append(path)

    # paths_list2 = [x for x in paths_list if x != []]
    paths_list2 = list(filter(None, paths_list))

    # print(paths_list)
    # print(paths_list2)

    return len(paths_list2)


'''
Pathfinding

0 in grid is obstacle
1 in grid is NOT obstacle

'''


# It is list of lists
matrix = [[1, 0, 1, 1],
          [1, 1, 0, 0],
          [1, 1, 0, 1],
          [1, 1, 1, 1]]

#This are numpy.ndarray
rand_matrix = create_matrix(4, 4)
rand_matrix2 = create_matrix(5, 3)
rand_matrix3 = create_matrix(3, 5)

print(matrix)
print('\n')
print(rand_matrix)
print('\n')
print(rand_matrix2)
print('\n')
print(rand_matrix3)
print('\n')

print('\nFinding path from point (0,0) to (3,3) on the same grid without and with diagonals:\n')
path1 = find_path(matrix, 0, 0, 3, 3, diagonals=False, info=True)
path2 = find_path(matrix, 0, 0, 3, 3, diagonals=True, info=True)

print('\n Running testing_paths... \n')
number_of_existing_paths = testing_paths(0, 10, diagonals=False)
print(number_of_existing_paths)
