import os

amount = int(input('How much folders need to create: '))
fname = input('How folders will be named: ')
cdir = os.getcwd()

for sex in range(amount):
    os.mkdir((fname + str(sex +1)))
