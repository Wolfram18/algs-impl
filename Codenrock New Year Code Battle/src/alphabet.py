import sys
import string

alphabet = string.ascii_lowercase  # latin alphabet

def encode(line):
    line = line.replace(" ", "").rstrip('\n')
    ind_list = [alphabet.find(x) + 1 for x in line.lower()]
    print(','.join(map(str, ind_list)))

if __name__ == '__main__':
    for line in sys.stdin:  # get input strings one by one
        encode(line)
