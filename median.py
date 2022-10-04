"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
median_value = 0

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        numbers.sort()

        if len(numbers) % 2 == 1:
            median_index = len(numbers) // 2
            median_value = int(numbers[median_index])
        else:
            median_index = (len(numbers) - 1) // 2
            median_value  = float((numbers[median_index] + numbers[median_index + 1]) / 2)

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(median_value)
