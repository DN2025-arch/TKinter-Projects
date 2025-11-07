
numbers = [60, 30, 25, 16, 2, 6, 23, 78, 49, 40]

numbers[4] = "Shobhit"

print(numbers)

print(numbers[-1])  # -1, last value

print(len(numbers))  # length of values

numbers.append(27)
numbers.extend([5, 4, 69, 56, 32])  # Append but many values, list or tuple

numbers.remove(49)  # Remove value, not by position
numbers.remove(numbers[-1])

numbers.pop(2)  # Remove index position, default, last

print(numbers)

for number in numbers:
    print(number)

# List Slicing
print(numbers[0:9:2])  # Start:End:Step
