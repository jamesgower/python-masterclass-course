import shelve

books = shelve.open("book")

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans on toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}

books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["maintenance"]["loose"])
books.close()
