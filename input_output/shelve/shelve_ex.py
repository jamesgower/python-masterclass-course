import shelve

# with shelve.open("ShelfTest") as fruit:
fruit = shelve.open("ShelfTest")
fruit["orange"] = "sweet, orange fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "sour, yellow citrus fruit"
fruit["grape"] = "small, sweet fruit grown in bunches"
fruit["lime"] = "sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + " : " + fruit[snack])

while True:
    shelf_key = input("Enter a fruit: ")
    if shelf_key.lower() == "quit":
        break
    if shelf_key in fruit:
        description = fruit.get(shelf_key)
        print(description)
    else:
        print("We don't have a " + shelf_key)

fruit.close()

