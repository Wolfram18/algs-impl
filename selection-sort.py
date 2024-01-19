import sys
import re

def selection_sort(numbers):
   for step in range(len(numbers)-1):
       for i in range(step, len(numbers)-1):
           if numbers[step] > numbers[i+1]:              
               numbers[step], numbers[i+1] = numbers[i+1], numbers[step]
   return numbers

def main():
    for line in sys.stdin: # get input strings one by one
        sequences = re.findall(r'\b\d+\b', line) # returns sequences of numbers
        numbers = [int(item) for item in sequences] # to integer
        numbers = selection_sort(numbers)
        print(','.join(map(str, numbers))) # to string
 
if __name__ == "__main__":
    main()
