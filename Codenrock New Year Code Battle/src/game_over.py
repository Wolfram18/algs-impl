import sys
import re 

def parsing_R(line):
    name = re.search(r'[А-Яа-я]+', line)
    days = [int(x) for x in re.findall(r' \d+ ', line)]
    hours = [int(x[:-1]) for x in re.findall(r' \d+:', line)]
    minutes = [int(x[1:]) for x in re.findall(r':\d+', line)]
    return name[0], days, hours, minutes

def parsing_T(line):
    day = int(re.search(r'^\d+ ', line)[0])
    hour = int(re.search(r' \d+:', line)[0][:-1])
    minute = int(re.search(r':\d+', line)[0][1:])
    return day, hour, minute

def search(robots, periods): 
    for i in range(len(periods)):
        print(f"{periods[i][0]} {periods[i][1]}:{periods[i][2]}")
        for j in range(len(robots)):
            game = True
            for k in range(0, len(robots[j][1]), 2):
                if periods[i][0] > robots[j][1][k] and periods[i][0] < robots[j][1][k+1]:
                    game = False
                elif periods[i][0] == robots[j][1][k]:
                    if periods[i][1] > robots[j][2][k]:
                        game = False
                    elif periods[i][1] == robots[j][2][k]:
                        if periods[i][2] >= robots[j][3][k]:
                            game = False
                elif periods[i][0] == robots[j][1][k+1]:
                    if periods[i][1] < robots[j][2][k+1]:
                        game = False
                    elif periods[i][1] == robots[j][2][k+1]:
                        if periods[i][2] <= robots[j][3][k+1]:
                            game = False
            if game:
                print(f"{robots[j][0]} GAME CONTINUES")
            else:
                print(f"{robots[j][0]} GAME OVER")

if __name__ == '__main__':
    robots = []
    periods = []
    for line in sys.stdin: 
        if (line[0] == 'R'):
            robots.append(parsing_R(line[2:]))
        elif (line[0] == 'T'):
            periods.append(parsing_T(line[2:]))
        elif (line[0] == '0'): 
            search(robots, periods)