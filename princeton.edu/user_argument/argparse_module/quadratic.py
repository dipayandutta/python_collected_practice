import argparse
import math

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--firstnumber',action='store',dest='firstnumber',help='Please provide the first number')
	parser.add_argument('--secondnumber',action='store',dest='secondnumber',help='Please provide the second number')

	numbers = parser.parse_args()
	discriminant = float(numbers.firstnumber)*float(numbers.firstnumber) - 4.0*float(numbers.secondnumber)
	d = math.sqrt(discriminant)

	print((-float(numbers.firstnumber)+float(discriminant))/2.0)
	print((-float(numbers.firstnumber)-float(discriminant))/2.0)
if __name__ == '__main__':
	main()
