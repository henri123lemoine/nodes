import numpy as np
from flojoy import Matrix


def test_SHUFFLE_MATRIX(mock_flojoy_decorator):
    import SHUFFLE_MATRIX

    np.random.seed(40)

    x = np.array([[5,6,3], [3,2,4], [1,1,1]])

    inputMatrix = Matrix(m=x)

    result = np.random.permutation(x)

    np.random.seed(40)

    shuffledX = SHUFFLE_MATRIX.SHUFFLE_MATRIX(inputMatrix)

    assert np.array_equal(shuffledX.m, result)