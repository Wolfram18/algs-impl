import sys

def transformation(input):
    cycle_list = sorted([input[i+1:]+input[:i+1] for i in range(len(input))])
    output = ""
    for s in cycle_list:
        output += s[len(s)-1]
    return output

if __name__ == '__main__':
    for line in sys.stdin:
        print(transformation(line[:-1]))
