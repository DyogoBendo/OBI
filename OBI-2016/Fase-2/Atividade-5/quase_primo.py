from math import sqrt

def main(file_input=input, test=False):
    n, k = map(int, file_input().split())
    primos = list(map(int, file_input().split()))
    multiplos = {p * i for p in primos for i in range((n // p) + 1)}
    c = n - len(multiplos) + 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()