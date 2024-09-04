LIMIT = 100 # Convention: Constants are written in uppercase

def soma_for() -> int:
    sum: int = 0

    for number in range(0, LIMIT + 1):
        sum = sum + number
        print(number)
    
    return sum

def soma_while() -> int:
    i: int = 0 # Counter variable
    sum: int = 0

    while i <= LIMIT: 
        sum = sum + i
        i = i + 1

def main():
    # Can change the result to sum_for() to test the for loop
    result = sum_while()
    print(result)

if __name__ == "__main__":
    main()