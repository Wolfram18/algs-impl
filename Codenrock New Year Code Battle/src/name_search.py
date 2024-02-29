import sys
import re 

def name_search(text):
    return re.findall(r'[А-Я][А-Яа-я]+\s+[А-Я][А-Яа-я]+[^A-za-z]', text)

if __name__ == '__main__':
    for line in sys.stdin:
        print(*[x[:-1] for x in name_search(line)], sep=', ')
