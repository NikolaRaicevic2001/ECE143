import itertools

def get_power_of3(n):
    """
    Constructs a given number using the set of weights {1, 3, 9, 27}
    with addition and subtraction operations, and returns the combination
    of coefficients as a 4-element list. Each coefficient represents whether
    to subtract (-1), omit (0), or add (1) the corresponding weight.

    Args:
        n (int): The target integer to represent, between 1 and 40 (inclusive).

    Returns:
        list: A 4-element list of integers, where each element is -1, 0, or 1, representing
        how each weight is used to construct the number. For example, [1, 0, 1, 0] means:
        1*1 + 0*3 + 1*9 + 0*27 = 10.

    Raises:
        AssertionError: If `n` is not an integer or if `n` is not within the range 1-40.

    Example:
        >>> get_power_of3(8)
        [1, 0, -1, 0]
        
        >>> get_power_of3(10)
        [1, 0, 1, 0]
    """
    # Input validation
    assert isinstance(n, int), "Input must be an integer"
    assert 1 <= n <= 40, "Input must be between 1 and 40 inclusive"
    
    weights = [1, 3, 9, 27]
    
    # Generate all combinations of coefficients (-1, 0, 1)
    for combination in itertools.product([-1, 0, 1], repeat=4):
        # Calculate the number represented by this combination
        total = sum(c * w for c, w in zip(combination, weights))
        
        if total == n:
            return list(combination)
    
    # If no combination is found
    raise ValueError(f"Unable to represent the number {n} using the set {weights}")

if __name__ == "__main__":
    # Example usage and test cases
    print(get_power_of3(8))   # Example output: [1, 0, -1, 0] because 1*1 + 0*3 + -1*9 + 0*27 = 8
    print(get_power_of3(10))  # Example output: [1, 0, 1, 0] because 1*1 + 0*3 + 9*1 + 0*27 = 10
