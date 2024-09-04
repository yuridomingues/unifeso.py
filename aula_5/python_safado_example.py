from dataclasses import dataclass # this is baguncinha

@dataclass(frozen=True)
class Parameters:
    MAX = 100 

MAX = 100 # Convention: Constants are written in uppercase

def soma_for() -> int:
    sum: int = 0

    for number in range(0, Parameters.MAX + 1):
        sum = sum + number
        print(number)
    
    return sum

def soma_while() -> int:
    i: int = 0 # Counter variable
    sum: int = 0

    while i <= Parameters.MAX: 
        sum = sum + i
        i = i + 1

def main():

    parameters = Parameters()
    parameters.MAX = parameters.MAX + 1
    print(f"MAX = {parameters.MAX}")

if __name__ == "__main__":
    main()