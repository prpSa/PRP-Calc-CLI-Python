# importing required modules
import argparse


# create a parser object
parser = argparse.ArgumentParser(description = "Calculator for addition, subtraction, multiplication and division")
  
# add argument
parser.add_argument("-add", nargs = '*', metavar = "n", type = int, 
                     help = "(Addition)Numbers separated by spaces will be added.")

parser.add_argument("-sub", nargs = 2, metavar = ('n1','n2'), type = int, 
                     help = "(Subtraction)Only 2 numbers separated by spaces will be added.")

parser.add_argument("-mul", nargs = 2,  metavar = ('n1','n2'), type = int, 
                     help = "(Multiplication)Only 2 numbers separated by spaces will be added.")

parser.add_argument("-div", nargs = 2,  metavar = ('n1','n2'), type = int, 
                     help = "(Division)Only 2 numbers separated by spaces will be added.")

parser.add_argument("-mod", nargs = 2, metavar = ('n1','n2'), type = int, 
                     help = "(Modulus)Only 2 numbers separated by spaces will be added.")  

parser.add_argument("-exp", nargs = 2, metavar = ('n1','n2'), type = int, 
                     help = "(Exponentiation)Only 2 numbers separated by spaces will be added.")   

parser.add_argument("-flrd", nargs = 2, metavar = ('n1','n2'), type = int, 
                     help = "(Floor division)Only 2 numbers separated by spaces will be added.") 




  
# parse the arguments from standard input
args = parser.parse_args()
  
# check if add argument has any input data.
# If it has, then print sum of the given numbers

if args.add != None:
    print(sum(args.add))
elif args.sub != None:
    print(args.sub[0]-args.sub[1])
elif args.mul != None:
    print(args.mul[0]*args.mul[1])
elif args.div != None:
    print(args.div[0]/args.div[1])
elif args.mod != None:
    print(args.mod[0]%args.mod[1])   
elif args.exp != None:
    print(args.exp[0]**args.exp[1])
elif args.flrd != None:
    print(args.flrd[0]//args.flrd[1])


