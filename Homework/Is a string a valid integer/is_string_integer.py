def is_string_integer(char: str) -> bool:
    """
    Checks if a given single character string represents a valid integer in base 10.

    Args:
    char (str): The character to be checked. Should be a single character string.

    Returns:
    bool: True if the character is a valid integer in base 10, False otherwise.

    Raises:
    AssertionError: If the input is not a single character string.
    """
    # Assertion to check if the input is a single character string
    assert isinstance(char, str), "Input must be a string."
    assert len(char) == 1, "Input must be a single character."

    return char.isdigit()
