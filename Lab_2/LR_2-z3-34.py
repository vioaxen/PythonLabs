s = "Революция!"

slice_1 = s[2:-1]

middle_index = len(s) // 2
slice_2 = s[middle_index:middle_index + 2]

new_string = slice_1 + slice_2

print(new_string)