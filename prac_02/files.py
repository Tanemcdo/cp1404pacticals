# out_file = open("name.txt", "w")
# out_file.write(input("What is you name?: "))
#
# in_file = open("name.txt", "r")
# print("Your name is {}".format(in_file.read()))
# in_file.close()

in_file = open("numbers.txt", "r")
number_one = int(in_file.readline())
number_two = int(in_file.readline())
print(number_one+number_two)

total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)

