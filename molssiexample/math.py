"""
A file for executing math functions.
"""

from typing import Union
import numpy as np


def pi(n: Union[int, float] = 1e4) -> float:
    """
    This function computes the value of Pi.

    Parameters
    ----------
    n : Union[int, float], optional
       Number of points to generate.

    Returns
    -------
    pi : float
        The computed value of Pi.

    """
    return 4 * np.mean(np.linalg.norm(np.random.rand(int(n), 2), axis=-1) < 1)


print("pi ", pi(1e6))


def euler(n=10):
    """
    This function computes the value of :math:`e` via a Taylor series expansion.

    .. math::

        e = 1 + \\sum_n^\\infty \\frac{1}{n!}

    Parameters
    ----------
    n : int
        The order of Taylor expansion.

    Returns
    -------
    e_value : float
        The computed value of Euler's number.

    """
    if n < 0:
        raise ValueError("Only positive integers are allowed")

    etaylor = 0.0
    
    for x in range(0, n + 1):
        etaylor += 1 / fact(x)

    return etaylor


def fact(n):
    fact = 1

    for x in range(1, n + 1):
        fact *= x
    return fact


#print ("The e is : ",end="")
#for x in range(0,10+1):
#    print (x, euler(x))

#print ("The fact is : ",end="")
#for x in range(0,10+1):
#        print (x, fact(x))

#print ("noarg ", euler())
