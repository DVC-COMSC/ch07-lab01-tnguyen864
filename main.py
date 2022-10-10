# List for 5 int values
numbers = []

# Get 5 int values from user
i = 0
print("Enter 5 integer values: ")
while i < 5:
    num = int(input(""))
    numbers.append(num)
    i += 1

# Get sum - (max + min) of values in list
sum = sum(numbers) - (min(numbers) + max(numbers))

# Print sum - (max + min)
print("List:", numbers)
print("Min value:", min(numbers))
print("Max value:", max(numbers))
print("Sum - max/min:", sum)