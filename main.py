string = [input().split(" ")]
set_1 = set(string[0][0])
set_2 = set(string[0][1])
set_3 = set(string[0][2])

if sorted(set_1) == sorted(set_2) == sorted(set_3):
    print("YES")
else:
    print("NO")
# set_1 = set(string_1)
# set_2 = set(string_2)
# if sorted(set_1) == sorted(set_2):
#     print("YES")
# else:
#     print("NO")

