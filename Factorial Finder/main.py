def Factorial(num):
    result = 1
    for i in range(num):
        i += 1
        result *= i
    print(result)


def main():
    # Ex: 5
    num = int(input("Factorial of number: "))
    Factorial(num)


if __name__ == "__main__":
    main()