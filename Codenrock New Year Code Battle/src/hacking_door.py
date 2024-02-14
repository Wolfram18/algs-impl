import sys

def hacking_door(line):
    res = list(filter(lambda x : x.isdigit(), line.split(",")))
    sticks = [int(x) for x in res[:-1]]
    length = int(res[len(res) - 1])
    key = []
    for i in range(length):
        if (i+1 in sticks or i+1 == length):
            key.append('X')
        else:
            key.append('0')
    for i in range(3):
        print(*[x for x in key], sep='')
    print(*['X' for x in range(length)], sep='')

if __name__ == '__main__':
    for line in sys.stdin:
        hacking_door(line)
