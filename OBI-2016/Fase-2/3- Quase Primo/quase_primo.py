from math import sqrt

def main(entrada=input, test=False):
    n, k = map(int, entrada().split())
    primos = list(map(int, entrada().split()))
    multiplos = {p * i for p in primos for i in range((n // p) + 1)}
    c = n - len(multiplos) + 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()