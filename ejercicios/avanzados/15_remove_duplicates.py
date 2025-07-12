numbers = [1, 2, 3, 3, 4, 5, 5, 6]
numbers_no_duplicates = []

for number in numbers:
    if number not in numbers_no_duplicates:
        numbers_no_duplicates.append(number)

print("Lista original:", numbers)
print("Lista sin duplicados:", numbers_no_duplicates)