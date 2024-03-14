import sys
import re
import string

alph_lower = string.ascii_lowercase  # lowercase latin alphabet
alph_upper = string.ascii_uppercase  # uppercase latin alphabet

def direction(course, count, step, size):
    if course and count + 1 == size:
        return False, count, 0
    elif course and count + 1 < size:
        return True, count + 1, step
    elif not course and count - 1 == -1:
        return True, count, 0
    elif not course and count - 1 > -1:
        return False, count - 1, step

def transposition(word): # nshoimteg
    after_change = [None]*len(word)
    course = True
    count = -1
    for i in range(len(word)):
        step = 0
        while (step != 2):
            course, count, step = direction(course, count, step, len(word))
            if after_change[count] == None:
                step += 1
                if step == 2:
                    after_change[count] = word[i]
                if i + 1 == len(word):
                    after_change[count] = word[i]
                    step = 2
    return ''.join(after_change)

def caesar(word): # bgvcwahsu
    step = alph_lower.index(word[0].lower())
    mod_func = lambda z,s: (alph_lower.find(z) + s)%25
    div_func = lambda z,s: (alph_lower.find(z) + s)//25
    char_list = [alph_lower[mod_func(x,step) - div_func(x,step) + 1] for x in word.lower()]
    char_list = [x.upper() if y.isupper() else x for x, y in zip(char_list, word)]
    return ''.join(char_list)

def encryption(data):
    words = re.findall(r'[0-9]+|[A-z]+|.|,|\?|!|"|\'', data)
    words = [caesar(transposition(word)) if re.match(r'[0-9]+|[A-z]+', word) else word for word in words]
    return "".join(words)

if __name__ == '__main__':
    data = "" 
    for line in sys.stdin: 
        data += line # something
    print(encryption(data))