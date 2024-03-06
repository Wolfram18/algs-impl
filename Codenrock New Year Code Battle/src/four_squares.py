import sys
import string
import re

def get_key_alph(alphabet, key_word):
    for c in alphabet:
        if c not in key_word:
            key_word += c
    return key_word

def encode(mes_input, alphabet, key_alph):
    mes_output = ""
    pos = 0
    while pos < len(mes_input):
        if pos+1 < len(mes_input):
            idx11 = alphabet.find(mes_input[pos])
            idx22 = alphabet.find(mes_input[pos+1])
            idx12 = idx11//5*5 + idx22%5
            idx21 = idx22//5*5 + idx11%5
            mes_output += key_alph[0][idx12]
            mes_output += key_alph[1][idx21]
        else:
            mes_output += mes_input[pos]
        pos += 2
    return mes_output

if __name__ == '__main__':
    alphabet = string.ascii_uppercase.replace('J','')
    key_alph1 = get_key_alph(alphabet, "CRIPTOGAF")
    key_alph2 = get_key_alph(alphabet, "SEGURT")
    for line in sys.stdin:
        mes_input = re.sub(r"[\sJ]", "", line)
        print(encode(mes_input, alphabet, (key_alph1, key_alph2)))
