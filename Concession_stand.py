#dictionary simple program
menu = {"nachos": 3.5,
        "sprite": 1.5,
        "milo": 2,
        "popcorn": 4,
        "candy": 3.5}

cart = []
total = 0

print("=========== MENU ===========")
for snack, price in menu.items():
    print(f"{snack:10}: ${price:.2f}")
print("============================")

while True:
    food = str(input("Enter your orders (q to quit) : ")).lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not found")

print()

print("=========Receipt=========")

for food in cart:
    price = menu[food]
    total += price
    print(f"{food:13} : ${price:.2f}")
print()
print(f"Total         : ${total:.2f}")
print("=========================")
