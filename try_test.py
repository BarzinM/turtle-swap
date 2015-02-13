
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x')
parser.add_argument('y')
args = parser.parse_args()
x = float(args.x)
y = float(args.y)

result = "boobie"

try:
    result = x / y
    # raise Exception('lol')
except ZeroDivisionError:
    print 'something went super bad'
    # pass

print result
