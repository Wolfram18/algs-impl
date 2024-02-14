import sys

def encode_message(message):
    encoded_string = ""
    i = 0
    while (i < len(message)):
        count = 1
        ch = message[i]
        while (i < len(message)-1): 
            if (message[i] == message[i + 1]): 
                count += 1
                i += 1
            else: 
                break
        encoded_string += str(count) + ch + ','
        i += 1
    return encoded_string[:-1]

if __name__ == '__main__':
    for line in sys.stdin:
        print(encode_message(line[:-1]))