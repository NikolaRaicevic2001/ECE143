import argparse

import compute_sum_to_n as sum_function

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Function that computes the sum of all non-negative integers including specified value n.")
    parser.add_argument("n", type=int, help="A non-negative integer.")
    args = parser.parse_args()

    try:
        result = sum_function.compute_sum_to_n(args.n)
        print(result)
    except (AssertionError, ValueError, SyntaxError) as e:
        print(f"Error: {e}")


