# Source data
lst_A = [number for number in range(11)]
lst_B = [chr(letter) for letter in range(ord('a'), ord('i'))]

# Point a
lst_C = []
for i in lst_A[1:len(lst_A) - 1]:
    lst_C.append(i)
for i in lst_B[1:len(lst_B) - 1]:
    lst_C.append(i)
# for i in lst_C:
#     print(i, end=" ")

# Point b
index_d = lst_C.index("d")
# print(index_d)

# Point c
lst_B.remove("d")