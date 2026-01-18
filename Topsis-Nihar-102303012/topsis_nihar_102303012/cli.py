import sys
from .topsis_core import topsis


def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2].replace(" ", "")
    impacts = sys.argv[3].replace(" ", "")
    output_file = sys.argv[4]

    try:
        topsis(input_file, weights, impacts, output_file)
        print("Output saved to:", output_file)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
