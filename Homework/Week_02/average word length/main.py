import argparse
import average_word_length

# Function to convert string input to boolean
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Compute the average length of the words in the input string. Exclude duplicated words if 'unique' is set to True.")
    parser.add_argument("instring", type=str, help="An input text of type string.")
    parser.add_argument("unique", type=str2bool, help="A boolean: if True, exclude duplicated words.")

    # Parse the arguments
    args = parser.parse_args()

    try:
        # Call the compute_average_word_length function
        result = average_word_length.compute_average_word_length(args.instring, args.unique)
        print(f"Average word length: {result}")
    except (AssertionError, ValueError, SyntaxError) as e:
        print(f"Error: {e}")
