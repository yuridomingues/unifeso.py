# PURPOSES:
# 1. Read the amount of numbers 'n'.
# 2. Read 'n' numbers.
# 3. Calculate the sum of the 'n' numbers.
# 4. Display the sum of the 'n' numbers.

def main() -> None:

    n: int = int(input("Enter the amount of numbers: "))
    
    if n >= 0:
        list_numbers: list[int] = []
        i: int = 1

        while (i <= n):
            num: int = int(input(f"Enter the {i}º number: "))
            list_numbers.append(num)  # append() is a method that adds an element to the list.
            i = i + 1
            
        sum_list = 0

        for num in list_numbers:
            sum_list1 = sum_list + num

        sum_list = 0
        for num in len(list_numbers):
            sum_list2 = sum_list + num (i - 1)
            
        
        print(sum_list1 + sum_list2)
    else:
        print("Invalid amount of numbers.")
    
if __name__ == "__main__":
    main()