from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import scipy.stats


@flojoy(node_type="default")
def ANDERSON(
    default: OrderedPair | Matrix,
    dist: str = "norm",
) -> OrderedPair | Matrix | Scalar:
    """The ANDERSON node is based on a numpy or scipy function.
    The description of that function is as follows:

            Anderson-Darling test for data coming from a particular distribution.

            The Anderson-Darling test tests the null hypothesis that a sample is
            drawn from a population that follows a particular distribution.
            For the Anderson-Darling test, the critical values depend on
            which distribution is being tested against.  This function works
            for normal, exponential, logistic, or Gumbel (Extreme Value
            Type I) distributions.

    Parameters
    ----------
    x : array_like
            Array of sample data.
    dist : {'norm', 'expon', 'logistic', 'gumbel', 'gumbel_l', 'gumbel_r', 'extreme1'}, optional
            The type of distribution to test against.  The default is 'norm'.
            The names 'extreme1', 'gumbel_l' and 'gumbel' are synonyms for the
            same distribution.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        m=scipy.stats.anderson(
            x=default.y,
            dist=dist,
        )
    )

    return result
