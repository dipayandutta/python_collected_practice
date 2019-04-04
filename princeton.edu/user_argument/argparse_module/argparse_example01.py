import argparse

parser = argparse.ArgumentParser(description='Process some integers')
parser.add_argument('integers',metavar='N',type=int,nargs='+',help='integer for accumulator')
parser.add_argument('--sum',dest='accumulate',action='store_const',const=sum,default=max)

args = parser.parse_args()
print (args.accumulate(args.integers))