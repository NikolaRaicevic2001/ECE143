def compute_average_word_length(instring, unique=False):
    """
    Compute the average length of the words in the input string.

    This function calculates the average word length of all words in `instring`.
    If `unique=True`, it only considers each unique word once when calculating the
    average. The function is case-sensitive, so "the" and "The" are considered different
    words if `unique=True`.

    Args:
        instring (str): The input string containing words.
        unique (bool): If True, duplicate words are only counted once. Defaults to False.

    Returns:
        float: The average word length (including or excluding duplicates depending on `unique`).

    Raises:
        AssertionError: If `instring` is not a string or `unique` is not a boolean.
        AssertionError: If the input string contains no words.
    
    Example:
        >>> text = '''Mary had a little lamb
        its fleece was white as snow
        and everywhere that Mary went
        the lamb was sure to go'''
        
        >>> compute_average_word_length(text, unique=False)
        3.8181818181818183
        
        >>> compute_average_word_length(text, unique=True)
        3.8421052631578947
    """
    # Input validation
    assert isinstance(instring, str), "Input must be a string"
    assert isinstance(unique, bool), "Unique flag must be a boolean"

    # Split the input string into words
    words = instring.split()
    
    # Handle the 'unique' flag
    if unique:
        words = list(set(words))  # Remove duplicates

    # Ensure there are words to process
    assert len(words) > 0, "The input string contains no words"

    # Compute the total length of all words
    total_length = sum(len(word) for word in words)
    
    # Calculate the average word length
    average_length = total_length / len(words)
    
    return average_length

if __name__ == "__main__":
    # Example usage:
    input_text = '''Mary had a little lamb
    its fleece was white as snow
    and everywhere that Mary went
    the lamb was sure to go'''

    # Without unique words
    print(compute_average_word_length(input_text, unique=False))  # With duplicates

    # With unique words
    print(compute_average_word_length(input_text, unique=True))   # Without duplicates