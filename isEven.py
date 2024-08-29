list = list(range(-10, 51))
# Fastest method
# print(list[::2])

# Step by step method
#  for number in list:
#      if number % 2 == 0:
#          print(f"Number {number} is even.")
#     else: 
#         print(f"Number {number} is odd.")

# Read negative method

for number in list:
    if number < 0:
        print(f"Number {number} is negative.")
    elif number % 2 == 0:
        print(f"Number {number} is even.")
    else:
        print(f"Number {number} is odd.")