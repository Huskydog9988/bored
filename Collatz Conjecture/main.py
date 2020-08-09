def Collatz(num):
    steps = 0
    while num != 1:
        if num%2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        steps += 1
    # Prints num of steps taken
    print(steps)


def main():
    # Ex: 5
    num = int(input("Input: "))
    Collatz(num)


if __name__ == "__main__":
    main()