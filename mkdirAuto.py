import os

amount = int(input('How much folders need to create: '))
fname = input('How folders will be named: ')
cdir = os.getcwd()

for sex in range(amount):
    try:
        os.mkdir((fname + str(sex +1)))
    except FileExistsError:
        print(f'This folder/s are already created \nCreated new folder/s up to {amount}')
