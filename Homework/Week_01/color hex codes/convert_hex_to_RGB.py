def convert_hex_to_RGB(hex_codes):
    """
    Converts a list of hex color codes into a list of RGB-tuples.

    Args:
    hex_codes(list of str): The list of color hex-codes. Should include "#" followed by 6 hexadecimal digits (e.g., ['#FFAABB']).

    Returns:
    list of tuple: Returns a list of tuples, each containing three elements corresponding to respective R, G, or B color (e.g., [(255, 170, 187)]).

    Raises:
    AssertionError: If the input is not a list of valid hex color strings.
    """

    # Assertions
    assert isinstance(hex_codes, list), "Input must be a list."
    for hex_code in hex_codes:
        assert isinstance(hex_code, str), "Each hex code must be a string."
        assert len(hex_code) == 7, "Each hex code must be 7 characters long."
        assert hex_code.startswith('#'), "Each hex code must start with '#' character."
        assert all(c in '0123456789ABCDEFabcdef' for c in hex_code[1:]), "Each hex code must contain valid hexadecimal characters."


    # Convert hex code to an RGB tuple
    RGB_tuples = [tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5)) for hex_code in hex_codes]

    return RGB_tuples