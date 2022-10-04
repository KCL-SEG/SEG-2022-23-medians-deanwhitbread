"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        numbers.sort()
        median_index = 0

        if len(numbers) % 2 == 1:
            median_index = len(numbers) // 2
            return int(numbers[median_index])
        else:
            median_index = (len(numbers) - 1) // 2
            arith_mean = (numbers[median_index] + numbers[median_index + 1]) / 2
            return float(arith_mean)

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
