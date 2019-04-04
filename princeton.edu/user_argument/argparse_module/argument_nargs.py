from argparse import ArgumentParser

description = 'Testing for passing multiple arguments and to get list of args'
parser = ArgumentParser(description=description)
parser.add_argument('-i','--item',action='store',dest='alist',type=str,nargs='*',default=['hello','world'])
parser.add_argument('-s','--store',action='store',dest='value',type=int)
result = parser.parse_args()
print ("Value of the variable {}".format(result.value))
print ("List of items in the list {}".format(result.alist))
