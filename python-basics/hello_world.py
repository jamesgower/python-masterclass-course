print("Hello World!")

splitString = "This is a\nsplit\nstring"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

age = 24

print("My age is {0} years".format(24))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(
    31, "January", "March", "May", "July", "August", "October", "December"))

print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

#?   Text formatting   :#
#! Python 2 Syntax !#
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))

#: Python 3 Syntax :#
# < left justifies the text
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))

# .50 adds 50 decimal places, f is for fraction
print("Pi is approximately {0:12.50f}".format(22/7))

# You dont NEED to specify indexes:
for i in range(1, 12):
    print("No. {:2} squared is {:<4} and cubed is {:<4}".format(i, i**2, i**3))