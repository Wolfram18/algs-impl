import sys
import re

def merge_sort(numbers):
    if (len(numbers) == 1):
        return numbers
    left = numbers[0:int(len(numbers)/2)]
    right = numbers[int(len(numbers)/2):]
    merge_sort(left)
    merge_sort(right)
    return merger(numbers, left, right)

def merger(numbers, left, right):
    i = j = k = 0
    while i != len(left) and j != len(right):
        if left[i] < right[j]:
            numbers[k] = left[i]
            i+=1
        else:
            numbers[k] = right[j]
            j+=1
        k+=1
    while i != len(left):
        numbers[k] = left[i]
        i+=1
        k+=1
    while j != len(right):
        numbers[k] = right[j]
        j+=1
        k+=1
    return numbers

def main():
    for line in sys.stdin: # get input strings one by one
        sequences = re.findall(r'-?\d+', line) # returns sequences of numbers
        numbers = [int(item) for item in sequences] # to integer
        numbers = merge_sort(numbers)
        print(','.join(map(str, numbers))) # to string
 
if __name__ == "__main__":
    main()
