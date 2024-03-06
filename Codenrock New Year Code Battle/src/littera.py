import sys

def mirror_replace(c, init):
    left_key = ord(c) - init + 1
    area = left_key // 17
    in_area = left_key - 16*area
    right_code = abs(in_area - 16) + 16*area
    return chr(init + right_code)

def encode(line):
    code = ""
    for c in line.replace('ё','е').replace('Ё','Е'):
        if c.isupper():
            code += mirror_replace(c, ord('А'))
        elif c.islower():
            code += mirror_replace(c, ord('а'))
        else: #elif c == ' ':
            code += c
    return code
            
if __name__ == '__main__':
    for line in sys.stdin:
        print(encode(line))
