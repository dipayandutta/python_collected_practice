import sys

print ("This is the name of the python script %s "%(sys.argv[0]))
print ("Total number of arguments are %s"%(len(sys.argv)))
print ("Arguments are %s"%(str(sys.argv)))

argument_1 = sys.argv[1]
if argument_1 == "hello":
    print ("Yes")
else:
    print ("NO")


print ("Python program for basic understanding clearance")
