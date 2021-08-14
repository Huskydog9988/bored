import math


def main():
    x = input("Pick a large number, the bigger the better: ")
    x = float(x)

    pi = x * math.sin(math.radians(180 / x))

    print(pi)


if __name__ == "__main__":
    main()
