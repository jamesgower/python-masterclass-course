parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
parrot_list.append("A Norwegian Blue")
for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1,3,5,7,9]
nums = even + odd
numbers_in_order = sorted(nums)
print(nums)

list_1 = []
list_2 = list()

if list_1 == list_2:
    print("The lists are equal")

another_even = list(even)

print(another_even is even)

another_even.sort(reverse=True)
print(even)