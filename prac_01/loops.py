
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c

stars = int(input("How many stars? \n>> "))
for i in range(1, stars + 1):
    print("*", end="")
print()

# d

stars = int(input("How many stars? \n>> "))
for i in range(1, stars + 1):
    print(i * "*", end='\n')
print()
