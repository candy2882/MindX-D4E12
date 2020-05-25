fibonacci = [1]
months = int(input('How many months that you want to see? '))
for i in range(months+1):
    if i == 0:
        print('Month', i, ':', fibonacci[i], 'pair(s) of rabbit' )
    else:
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
        print('Month', i, ':', fibonacci[i], 'pair(s) of rabbit' )