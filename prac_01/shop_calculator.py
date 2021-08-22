total_price = 0

number_of_items = int(input("Number of Items: "))
while number_of_items < 0:
    number_of_items = int(input("Invalid number of items!\nNumber of Items: "))
for i in range(1, number_of_items + 1):
    price = float(input(f"Price of Item {i}: "))
    total_price += price

if total_price > 100:
    total_price *= 0.1

print(f"Total price for {number_of_items} item/s is ${total_price:.2f}")
