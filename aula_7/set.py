set_A = {1,2,3,4,5}
set_B = {2,3,5,7,9}
set_A_intersection_B = set_A.intersection(set_B)


print(f"A \u222A B = {set_A.union(set_B)}")
print(f"A \u2229 B = {set_A_intersection_B}")

set_diff_A_B = set_A - set_B
set_A = set_diff_A_B.union(set_A_intersection_B)

print(f"A - B = {set_diff_A_B}")
print(f"A = {set_A}")
