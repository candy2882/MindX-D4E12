# name = input('Your full name:')
# split = name.split()
# for index, value in enumerate(split):
#     split[index] = value.capitalize()
# print('Updated:', *split)

balance = int(input('Enter your balance:'))
print('Your updated balance', '{:,}'.format(balance))