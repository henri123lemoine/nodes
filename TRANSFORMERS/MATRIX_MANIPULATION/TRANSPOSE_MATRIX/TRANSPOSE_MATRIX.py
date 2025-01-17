from numpy import transpose
from flojoy import flojoy, Matrix


@flojoy
def TRANSPOSE_MATRIX(default: Matrix) -> Matrix:
    """The TRANSPOSE_MATRIX node takes an input 2D matrix and transposes it.

    Inputs
    ------
    a : Matrix
        The input matrix to be transposed

    Returns
    -------
    Matrix
        The transposed matrix
    """

    return Matrix(m=transpose(default.m, (1, 0)))
