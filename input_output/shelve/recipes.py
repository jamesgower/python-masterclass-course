import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["soup"] = soup

    # without writeback=True, make a temp_list and reassign value:
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list

    # temp_list = recipes["beans on toast"]
    # temp_list.append("cheese")
    # recipes["beans on toast"] = temp_list

    # with writeback=True you can overwrite/append values with temp variables
    # recipes["blt"].append("cheese")
    recipes["beans on toast"] = beans_on_toast
    recipes.sync()
    beans_on_toast.append("cheese") # wont append because sync is in wrong spot

    for snack in recipes:
        print(snack, recipes[snack])