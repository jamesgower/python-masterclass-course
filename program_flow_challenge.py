ip = input("Please enter an IP address: ")
segment = 1
seg_length = 0
# char = ''
if ip[-1] != '.':
    ip += '.'

for char in ip:
    if char == ".":
        print("segment {} contains {} characters".format(segment, seg_length))
        segment += 1
        seg_length = 0
    else:
        seg_length += 1

# if char != '.':
#     print("segment {} contains {} characters".format(segment, seg_length))
