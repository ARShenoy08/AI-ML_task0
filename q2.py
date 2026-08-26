def process_list(number):
    result = numbers.copy()
    for number in result.copy():
        if number < 0:
            result.remove(number)
    result.append(0)
    result.sort()
    return result

n = int(input("How many elements in the list : "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))
result = process_list(numbers)
print("Original:", numbers)
print("Result:", result)

