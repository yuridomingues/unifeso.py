# list = list(range(-10, 51))
# Fastest method
# print(list[::2])

# Simple method
#  for number in list:
#      if number % 2 == 0:
#          print(f"Number {number} is even.")
#     else: 
#         print(f"Number {number} is odd.")

# Read negative method
# for number in list:
#     if number < 0:
#         print(f"Number {number} is negative.")
#     elif number % 2 == 0:
#         print(f"Number {number} is even.")
#     else:
#         print(f"Number {number} is odd.")

# Get the smallest and biggest even number in the sequence.
list = list(range(-5, 6))
smallest_even = max(list) + 1
biggest_even = min(list) - 1

for number in list:
    if number < 0:
        print(f"Number {number} is negative.")
    elif number % 2 == 0:
        print(f"Number {number} is even.")
        # Get the smallest even number in the sequence.
        if number < smallest_even:
            smallest_even = number
        # Get the largest even number in the sequence.
        if number > biggest_even:
            biggest_even = number
    else:
        print(f"Number {number} is odd.")
        
print(f"The smallest even number is {smallest_even}")
print(f"The biggest even number is {biggest_even}")