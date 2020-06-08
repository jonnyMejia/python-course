from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci(n):
    """This a function recursive

    Args:
        n (int): Is a positive int.

    Raises:
        TypeError: n must be a positive int
        ValueError: n must be a positive int

    Returns:
        int: Return a positive integer
    """
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

