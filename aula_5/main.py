def main():
    sum: int = 0

    for number in range(0, 101):
        sum = sum + number

    print(f"Sum = {sum}.")

if __name__ == "__main__":
    main()