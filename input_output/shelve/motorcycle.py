import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 Dream"
    bike["colour"] = "Red"
    bike["engine_size"] = 250
    # bike["engin_size"] = 250

    del bike["engin_size"]

    for key in bike:
        print(key)

    print("*" * 40 )

    # print(bike["engin_size"]) # unwanted
    print(bike["engine_size"])
    print(bike["colour"])