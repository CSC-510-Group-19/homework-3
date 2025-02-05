""" Document contains one function, random_array, which returns a a randomly generated array """
import secrets

def random_array(arr):
    """ random_array takes an array object and returns a random array.

    Parameters
    ----------
    arr : array
        an array of objects acting as placeholders for random generated values.

    Returns
    -------
    arr : array
        an array with random values.
    """

    for i in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
