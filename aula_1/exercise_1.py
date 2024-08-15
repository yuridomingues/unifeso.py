# 1- Write a program that reads a sequence of numbers and displays their sum.

def main() -> None:

    num1: int = int(input("Please, enter the first number: "))
    num2: int = int(input("Please, enter the second number: "))
    num3: int = int(input("Please, enter the third number: "))

    result: int = (num1 + num2 + num3)

    print(f"The sum of {num1}, {num2} and {num3} is = {result}")

if __name__ == "__main__":
    main()