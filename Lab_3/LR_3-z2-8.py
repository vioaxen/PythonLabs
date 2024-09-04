# Source data
string_S = "1 2 3 4 5"
A = set(map(int, string_S.split()))
B = {5, 7, 12}

# Point a
count_unique_el = len(A)

# Point b
common_el = A.intersection(B)

# Point c
C = A.union(B)

# Point d
B.clear()

print(f"Count unique elements: {count_unique_el}")
print(f"A and B have common elements. Count: {len(common_el)}" if len(common_el) > 0 else "No common elements")
print(f"Set C: {C}")
print(f"Set B: {B}")