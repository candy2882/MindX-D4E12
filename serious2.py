numbers = [1, 6, 8, 1, 2, 1, 5, 6]
your_number = int(input('Enter your number:'))
i = 0
for index, value in enumerate(numbers):
    if numbers[index] == your_number:
        i = i +1
print(your_number, 'appears', i, 'times in my list') 