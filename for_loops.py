number = "9,232,232,232,232,232"
num = ''
# for i in range(1,20):
#     print("i is now {}".format(i))

# for i in range(0, len(number)):
#     print(number[i])

# num = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         num += number[i]

# newNumber = int(num)
# print("the number is {}".format(newNumber))


for char in number:
    # in checks if the characters on the right are in the string to the left
    if char in '0123456789':
        num += char

newNumber = int(num)
print("Number is {}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of lift"]:
    print("This parrot is " + state)

for i in range(0,100,5):
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("==================")