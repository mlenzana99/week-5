#shoppingcart for product information and price
#have an exit clause
#at the end show items and prices

foods = []
prices= []
total= 0

while True:
    food = input("enter food item or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"enter price item {food}: R"))
        foods.append(food)
        prices.append(price)

print("-----Your Cart-----")

for food in foods:
    print(food, end= " " )
    
for price in prices:
    total += price

print("\n")
print(f"Total is: R{total}")