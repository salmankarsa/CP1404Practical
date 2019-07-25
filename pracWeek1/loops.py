for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0,110,10):
    print (i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number = int(input("Input number: "))
for i in range(0, number):
    print('*', end=' ')

stars = int(input("Input number: "))
for i in range(stars+1):
    print(i*'*')
