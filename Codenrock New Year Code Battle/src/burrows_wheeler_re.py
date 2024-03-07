import sys

def re_transformation(input):
    if len(input) == 0:
        return None
    re_cycle_list = ["" for s in input]
    while len(re_cycle_list[0]) < len(input):
        re_cycle_list = sorted([input[i]+re_cycle_list[i] for i in range(len(input))])
    for s in re_cycle_list:
        if s[len(s)-1] == '|':
            return s

if __name__ == '__main__':
    for line in sys.stdin:
        print(re_transformation(line[:-1]))