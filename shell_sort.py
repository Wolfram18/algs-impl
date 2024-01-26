import sys
import re


def shell_sort(numbers):
    step = len(numbers) // 2
    while step > 0:
        series = len(numbers) - step
        for i in range(series):
            if numbers[i] > numbers[i + step]:
                numbers[i], numbers[i + step] = numbers[i + step], numbers[i]
        step -= 1
    return numbers


def main():
    for line in sys.stdin:  # get input strings one by one
        sequences = re.findall(r'-?\d+', line)  # returns sequences of numbers
        numbers = [int(item) for item in sequences]  # to integer
        numbers = shell_sort(numbers)
        print(','.join(map(str, numbers)))  # to string


if __name__ == "__main__":
    main()