import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str,help="input string")
args = parser.parse_args()

inp = args.input
output=inp[::-1]
print(output)