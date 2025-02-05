"""Module for generating an array of random numbers"""
import secrets

def random_array(arr):
    """Function for generating an array of random numbers"""
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
