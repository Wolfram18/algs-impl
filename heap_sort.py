import sys
import re

def compare_nodes(array, id_parent, id_children):
    if array[id_parent] < array[id_children]:
        array[id_parent], array[id_children] = \
            array[id_children], array[id_parent]

def create_max_heap(numbers, size):
    for i in range(size // 2 - 1, -1, -1):
        compare_nodes(numbers, i, 2 * i + 1)
        if size > 2 * i + 2:
            compare_nodes(numbers, i, 2 * i + 2)

def heap_sort(numbers):
    size = len(numbers)
    create_max_heap(numbers, size)
    while size > 1:
        numbers[0], numbers[size - 1] = numbers[size - 1], numbers[0]
        size -= 1
        create_max_heap(numbers, size)

def main():
    for line in sys.stdin:  # get input strings one by one
        sequences = re.findall(r'-?\d+', line)  # returns sequences of numbers
        numbers = [int(item) for item in sequences]  # to integer
        heap_sort(numbers)
        print(','.join(map(str, numbers)))  # to string

if __name__ == "__main__":
    main()