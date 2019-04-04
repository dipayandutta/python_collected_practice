import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s',action='store',dest='value')
parser.add_argument('-a',action='append',dest='collection',default=[])
parser.add_argument('--version',action='version',version='%(prog)s 1.0')

results = parser.parse_args()
print ('value %s'%(results.value))
print('collections %s'%(results.collection))
print("-----------------------------------------")

for items in results.collection:
	print (items)
