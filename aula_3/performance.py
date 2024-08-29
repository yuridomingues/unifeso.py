# FOR WAY 
# from time import perf_counter
# from intertools import chain

# list1 = list(range(0, 50_000_000))
# list2 = list(range(50_000_001, 100_000_001))

# start = perf_counter()

# for number in list2:
#     list1.append(number)

# end = perf_counter()

# print(f"The list has {len(lista):,} elements.")
# print(f"Execution time {end - start} seconds.")

# WORST WAY

# from time import perf_counter
# from intertools import chain

# list1 = list(range(0, 50_000_000))
# list2 = list(range(50_000_001, 100_000_001))

# list = list1 + list2

# FAST WAY
print(f"The list has {len(lista):,} elements.")
print(f"Execution time {end - start} seconds.")

from time import perf_counter
from intertools import chain

list1 = list(range(0, 50_000_000))
list2 = list(range(50_000_001, 100_000_001))

list = list(chain(list1, list2))

print(f"The list has {len(lista):,} elements.")
print(f"Execution time {end - start} seconds.")

