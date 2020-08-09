def Fibonacci(Start):
    sequence = Start
    while True:
        n1 = sequence[-1]
        n2 = sequence[-2]
        finale = n1+n2
        sequence.append(finale)
        print(finale)

def main():
    # Ex: 0
    one = int(input("Starting number 1: "))
    # Ex: 1
    two = int(input("Starting number 2: "))
    Fibonacci([one,two])


if __name__ == "__main__":
    main()