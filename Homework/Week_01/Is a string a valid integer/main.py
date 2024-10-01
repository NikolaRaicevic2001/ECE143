import argparse

import is_string_integer as str_int_function

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a character is a valid integer in base 10.")
    parser.add_argument("char", type=str, help="A single character to be checked")
    args = parser.parse_args()

    try:
        result = str_int_function.is_string_integer(args.char)
        print(result)
    except AssertionError as e:
        print(f"Error: {e}")
