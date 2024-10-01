def compute_sum_to_n(n):
    """
    Computes the sum of all non-negative integers up to and including the specified value n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The sum of all non-negative integers from 0 to n.

    Raises:
        AssertionError: If n is not a non-negative integer.
    """

    # Assertions
    assert isinstance(n, int), "Input must be an integer."
    assert n >= 0, "Input must be a non-negative integer."

    # Compute the sum
    return n * (n + 1) // 2