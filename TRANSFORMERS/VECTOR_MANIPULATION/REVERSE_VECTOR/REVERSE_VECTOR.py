import numpy as np
from flojoy import flojoy, Vector

@flojoy
def REVERSE_VECTOR(
    default: Vector,
) -> Vector:
    """The REVERSE_VECTOR node returns the input vector where
    the elements are in the reverse order

    Inputs
    ------
    v : Vector
        The input vector

    Returns
    -------
    Vector
        Reversed input vector
    """

    return Vector(v=np.flip(default.v))
