import sys
import re

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[int(len(numbers)/2)]
    left = [n for n in numbers if n < pivot]
    equal = [pivot] * numbers.count(pivot)
    right = [n for n in numbers if n > pivot]
    return quick_sort(left) + equal + quick_sort(right)

def main():
    for line in sys.stdin: # get input strings one by one
        str_list = line[:-1].split(sep=',') # split by ','
        str_list = quick_sort(str_list)
        print(','.join(map(str, str_list))) # to string
 
if __name__ == "__main__":
    main()
