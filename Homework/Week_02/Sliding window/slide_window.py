def slide_window(x, width, increment):
    """
    Generates a sequence of overlapping sublists (sliding windows) from the input list.
    
    Each window has a specified width and slides through the input list with a specified increment.
    The function truncates the output if the window extends beyond the length of the input list.
    
    Args:
        x (list): The input list to generate sliding windows from.
        width (int): The width of each sliding window (number of elements in each sublist).
        increment (int): The increment by which the window moves after each step.
        
    Returns:
        list: A list of sublists (sliding windows) extracted from the input list.
        
    Raises:
        AssertionError: If the input is not a list or if the width and increment are not positive integers.

    Example:
        >>> slide_window(list(range(15)), 5, 2)
        [[0, 1, 2, 3, 4],
         [2, 3, 4, 5, 6],
         [4, 5, 6, 7, 8],
         [6, 7, 8, 9, 10],
         [8, 9, 10, 11, 12],
         [10, 11, 12, 13, 14]]

        >>> slide_window(list(range(18)), 5, 2)
        [[0, 1, 2, 3, 4],
         [2, 3, 4, 5, 6],
         [4, 5, 6, 7, 8],
         [6, 7, 8, 9, 10],
         [8, 9, 10, 11, 12],
         [10, 11, 12, 13, 14],
         [12, 13, 14, 15, 16]]
    """
    
    # Input validation
    assert isinstance(x, list), "Input x must be a list"
    assert isinstance(width, int) and width > 0, "Width must be a positive integer"
    assert isinstance(increment, int) and increment > 0, "Increment must be a positive integer"
    
    # Initialize the list to hold sliding windows
    result = []
    
    # Iterate through the list using the sliding window logic
    for i in range(0, len(x) - width + 1, increment):
        result.append(x[i:i + width])
    
    return result

# Example usage and test cases
print(slide_window(list(range(15)), 5, 2))  # Expected: [[0, 1, 2, 3, 4], [2, 3, 4, 5, 6], [4, 5, 6, 7, 8], [6, 7, 8, 9, 10], [8, 9, 10, 11, 12], [10, 11, 12, 13, 14]]
print(slide_window(list(range(18)), 7, 2))  # Expected: [[0, 1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11, 12], [8, 9, 10, 11, 12, 13, 14], [10, 11, 12, 13, 14, 15, 16]]
