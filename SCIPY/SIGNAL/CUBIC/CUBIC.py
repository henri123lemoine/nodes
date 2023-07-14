from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import scipy.signal


@flojoy(node_type="default")
def CUBIC(
    default: OrderedPair | Matrix,
) -> OrderedPair | Matrix | Scalar:
    """The CUBIC node is based on a numpy or scipy function.
    The description of that function is as follows:

            A cubic B-spline.

            This is a special case of `bspline`, and equivalent to ``bspline(x, 3)``.

    Parameters
    ----------
    x : array_like
            a knot vector

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        m=scipy.signal.cubic(
            x=default.y,
        )
    )

    return result
