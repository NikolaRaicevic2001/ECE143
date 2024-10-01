import argparse
import ast  # To safely evaluate the input string as a list

import convert_hex_to_RGB as hex_RGB_function

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a list of color hex-codes (e.g., ['#FFAABB']) to list of RGB-tuples [(255,170,187)]")
    parser.add_argument("hex_codes", type=str, help="A list of color hex-codes to be converted")
    args = parser.parse_args()

    try:
        # Convert the input string to a list
        hex_codes_list = ast.literal_eval(args.hex_codes)
        result = hex_RGB_function.convert_hex_to_RGB(hex_codes_list)
        print(result)
    except (AssertionError, ValueError, SyntaxError) as e:
        print(f"Error: {e}")


