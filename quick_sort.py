import sys
import re
import random

def is_less(left, right):
    if (left.isdigit() and right.isdigit()):
        return int(left) < int(right)
    else:
        return left < right
        
def is_more(left, right):
    if (left.isdigit() and right.isdigit()):
        return int(left) > int(right)
    else:
        return left > right

def quick_sort(numbers, first, last):
    if first >= last: return
    pivot = numbers[random.randint(first, last)]
    i, j = first, last
    while i <= j:
        while is_less(numbers[i], pivot): i += 1
        while is_more(numbers[j], pivot): j -= 1 
        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i, j = i + 1, j - 1
    quick_sort(numbers, first, j)
    quick_sort(numbers, i, last)

def quick_sort_functional(numbers):
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
        quick_sort(str_list, 0, len(str_list)-1)
        print(','.join(map(str, str_list))) # to string
 
if __name__ == "__main__":
    main()
