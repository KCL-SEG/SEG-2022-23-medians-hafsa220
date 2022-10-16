"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()
LengthOfList = len(numbers)

if LengthOfList%2 == 1:
    i = math.floor(LengthOfList/2)
    print ("The median of this list is", numbers[i])
else:
    i = math.ceil(LengthOfList/2)
    add = numbers[i] + numbers[i-1]
    median = add/2
    print ("The median of this list is", median)
