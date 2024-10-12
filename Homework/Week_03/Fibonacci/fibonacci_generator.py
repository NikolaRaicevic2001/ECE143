def fibonacci(n):
    ''' 
    This script contains a generator function to compute the first n Fibonacci numbers. The Fibonacci sequence is defined recursively as:
    F[n] = F[n-1] + F[n-2] with initial values F[0] = 1 and F[1] = 1.

    The generator will produce Fibonacci numbers up to the n-th term.

    Args:
        n (int): a number of Fibonacci numbers to be generated.
    Returns:
        list: a list of n Fibonacci numbers.
    Raises:
        AssertionError: If value n is not an integer or not a positive number or a zero.

    '''

    # Input Validation
    assert isinstance(n, int) and n > 0, "Input must be a positive integer."

    # Fibonacci Sequence    
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
if __name__ == "__main__":
    # Test cases to validate the functionality
    print(list(fibonacci(1)))
    print(list(fibonacci(2)))
    print(list(fibonacci(5)))
    print(list(fibonacci(10)))

    assert list(fibonacci(1)) == [1], "Test case for n=1 failed."
    assert list(fibonacci(2)) == [1, 1], "Test case for n=2 failed."
    assert list(fibonacci(5)) == [1, 1, 2, 3, 5], "Test case for n=5 failed."
    assert list(fibonacci(10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], "Test case for n=10 failed."
    print("All test cases passed!")