from flojoy import flojoy, Vector, Matrix


@flojoy
def MATRIX_2_VECTOR(default: Matrix) -> Vector:
    """The MATRIX_2_VECTOR node takes a matrix and flatten it into vector type data.

    Inputs
    ------
    default: Matrix
        The input matrix that will be transformed into vector data type.

    Returns
    -------
    Vector
        Vector that is flatten from input matrix.
    """
    rVector = default.m.flatten()

    return Vector(v=rVector)
