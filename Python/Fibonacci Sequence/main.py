
# computes result of n1 & n2
def Finale(n1, n2):

    # compute number
    finale = n1+n2

    return finale


# computes a full Fibonacci Sequence
def Fibonacci(start1, start2):
    sequence = [start1, start2]

    while True:

        n1 = sequence[-1]
        n2 = sequence[-2]

        sequence.append(Finale(n1, n2))

        # get final
        finale = sequence[-1]
        print(finale)

        # input("Press Enter to continue...")


def main():
    # Ex: 0
    one = int(input("Starting number 1: "))
    # Ex: 1
    two = int(input("Starting number 2: "))

    Fibonacci(one, two)


if __name__ == "__main__":
    main()
