from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import scipy.stats


@flojoy(node_type="default")
def SIGMACLIP(
    default: OrderedPair | Matrix,
    low: float = 4.0,
    high: float = 4.0,
) -> OrderedPair | Matrix | Scalar:
    """The SIGMACLIP node is based on a numpy or scipy function.
    The description of that function is as follows:

            Perform iterative sigma-clipping of array elements.

            Starting from the full sample, all elements outside the critical range are
            removed, i.e. all elements of the input array `c` that satisfy either of
    the following conditions::

            c < mean(c) - std(c)*low
            c > mean(c) + std(c)*high

            The iteration continues with the updated sample until no
            elements are outside the (updated) range.

    Parameters
    ----------
    a : array_like
            Data array, will be raveled if not 1-D.
    low : float, optional
            Lower bound factor of sigma clipping. Default is 4.
    high : float, optional
            Upper bound factor of sigma clipping. Default is 4.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        m=scipy.stats.sigmaclip(
            a=default.y,
            low=low,
            high=high,
        )
    )

    return result
