import logging
import os
import unittest
import os
import numpy as np
from imresize import imresize
import numpy as np

"""
Some basic tests for stl_tools
"""

logging.basicConfig(level=logging.DEBUG)


class Test_imresize(unittest.TestCase):

    def test_rgb(self):
        """ Tests imresize function
        """
        A = np.random.randn(100, 100, 3)
        B = imresize(A, (50, 100))
        m, n, c = B.shape
        assert m == 50
        assert n == 100
        assert c == 3

    def test_int_size(self):
        """ Tests imresize function
        """
        A = np.random.randn(100, 100)
        m, n = imresize(A, 2).shape
        assert m == 200
        assert n == 200

    def test_float_size(self):
        """ Tests imresize function
        """
        A = np.random.randn(100, 100)
        m, n = imresize(A, 0.5).shape
        assert m == 50
        assert n == 50

    def test_imresize(self):
        """ Tests imresize function
        """
        A = np.random.randn(100, 100)
        m, n = imresize(A, (50, 200)).shape
        assert m == 50
        assert n == 200

    def test_imresize_reversed(self):
        """ Tests imresize function
        """
        A = imresize(np.random.randn(100, 100), (100, 100))
        B = imresize(A, (200, 200))
        C = imresize(B, (100, 100))

        residual = np.linalg.norm(A - C) / np.linalg.norm(A)
        assert residual < 0.1

if __name__ == '__main__':
    unittest.main()
