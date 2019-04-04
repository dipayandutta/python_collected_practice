import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square",help="display the square of int number",type=int)
argument = parser.parse_args()
print (int(argument.square**2))
