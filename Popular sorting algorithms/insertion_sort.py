import sys
import re

def insertion_sort(numbers):
    for step in range(1, len(numbers)):
        current = step
        for i in range(step-1, -1, -1):
            if numbers[current] < numbers[i]:
                numbers[current], numbers[i] = numbers[i], numbers[current]
                current = i
    return numbers

def main():
    for line in sys.stdin: # get input strings one by one
        sequences = re.findall(r'-?\d+', line) # returns sequences of numbers
        numbers = [int(item) for item in sequences] # to integer
        numbers = insertion_sort(numbers)
        print(','.join(map(str, numbers))) # to string
 
if __name__ == "__main__":
    main()
