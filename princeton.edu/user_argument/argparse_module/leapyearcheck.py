import argparse

def checkleapyear():
	parser = argparse.ArgumentParser()

	parser.add_argument('--year',action='store',dest='year',help='please provide a number')

	result = parser.parse_args()
	print (" provided Year === {}".format(result.year))
	year = int(result.year)

	isLeapYear = (year %4 == 0)
	isLeapYear = isLeapYear and (year % 100 != 0)
	isLeapYear = isLeapYear or (year % 400 == 0 )

	print(isLeapYear)

def main():
	checkleapyear()

if __name__ == '__main__':
	main()
