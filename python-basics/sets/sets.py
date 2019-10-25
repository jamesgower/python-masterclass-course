farm_animals = {"sheep", "cow", "hen"};
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals, wild_animals)

empty_set = set()
empty_set_fail = {}
# will fail as it becomes a dictionary, not set - which doesnt have add method
# empty_set_fail.add()

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# union method merges two sets into one
print(even.union(squares))
print(len(even.union(squares)))

# intersection method returns the values of two sets where contain the same value
# it can be called with the "intersection" method or by calling "&"
print("-" * 40)
print(even.intersection((squares)))
print(even & squares)
print(squares.intersection((even)))
print(squares & even)

print("_" * 40)

# difference method takes two arguments (a and b). The set difference of a and b is a set of elements
# that exists only in set a but not set b. It can be invoked by the difference method or by using - between
# two sets.
print(sorted(even))
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

# the difference_update method changes the first set to be the difference between itself and the second list,
# i.e it removes all elements from set b from set a, and stores the value in set a.
print("=" * 40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

print("=" * 40)

even = set(range(0, 40, 2))
print(sorted(even))
print(sorted(squares))

# symmetric difference returns a set which contains values which are either in set a or set b, but not both:
# the method can be called by using the method or by using a caret (^) between two sets.
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
print(sorted(even ^ squares))

# removal of values from a set can be done using the remove or discard method. Remove will throw an error if the
# value is not in the set, whereas discard will not.

squares.remove(4)
squares.remove(16)
print(squares)

squares = {4, 6, 16}

print("=" * 40)

print(even)
print(squares)
if squares.issubset(even):
    print("squares is subset of even")

if even.issuperset(squares):
    print("even is superset of squares")


