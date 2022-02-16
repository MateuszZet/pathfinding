from unittest import TestCase

from main import create_matrix, testing_paths, find_path
import numpy as np

test_matrix = [[1, 0, 1, 1],
               [1, 1, 0, 0],
               [1, 1, 0, 1],
               [1, 1, 1, 1]]


class Test(TestCase):
    def test_create_matrix(self):
        self.assertEqual(type(create_matrix(4, 4)), np.ndarray)

    def test2_create_matrix(self):
        self.assertEqual(create_matrix(4, 4).size, 16)

    def test3_create_matrix(self):
        self.assertEqual(create_matrix(4, 4).size, 16)

    def test4_create_matrix(self):
        self.assertEqual(create_matrix(4, 4).shape, (4, 4))

    def test5_create_matrix(self):
        self.assertEqual(create_matrix(3, 5).shape, (5, 3))

    def test_find_path(self):
        self.assertEqual(find_path(test_matrix, 0, 0, 3, 3), [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)])

    def test_find_path2(self):
        self.assertEqual(find_path(test_matrix, 0, 0, 3, 3, True), [(0, 0), (1, 1), (1, 2), (2, 3), (3, 3)])

    def test_testing_paths(self):
        self.assertEqual(type(testing_paths(0, 0)), int)

    def test2_testing_paths(self):
        self.assertEqual(type(testing_paths(10, 10)), int)

    def test3_testing_paths(self):
        self.assertEqual(type(testing_paths(0, 0, diagonals=True)), int)

    def test3_testing_paths(self):
        self.assertEqual(type(testing_paths(0, 0, diagonals=False)), int)
