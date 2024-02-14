import sys
import math

def sum_of_arithmetic_progression(a1, d, n):
    return (2*a1 + d*(n - 1))*n/2

def warfare(line):
    opponents = float(line)
    n = math.ceil(opponents/2) # round up
    S = sum_of_arithmetic_progression(opponents, -2, n)
    print(int(S)) # print the answer to stdout

if __name__ == '__main__':
    for line in sys.stdin: # get input strings one by one
        warfare(line)
