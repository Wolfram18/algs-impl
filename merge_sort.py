import sys
import re

def merge_sort(numbers):
    if (len(numbers) == 1):
        return numbers
    merge_sort(numbers[0:int(len(numbers)/2)]) # left
    merge_sort(numbers[int(len(numbers)/2):])  # right
    numbers = selection_sort(numbers) # recursion
    return numbers
    
def selection_sort(numbers):
    for step in range(len(numbers)-1):
        for i in range(step, len(numbers)-1):
            if numbers[step] > numbers[i+1]:              
                numbers[step], numbers[i+1] = numbers[i+1], numbers[step]
    return numbers

def main():
    for line in sys.stdin: # get input strings one by one
        sequences = re.findall(r'-?\d+', line) # returns sequences of numbers
        numbers = [int(item) for item in sequences] # to integer
        numbers = merge_sort(numbers)
        print(','.join(map(str, numbers))) # to string
 
if __name__ == "__main__":
    main()