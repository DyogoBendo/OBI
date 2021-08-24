from math import inf

def main(entrada=input, test=False):
    n, k = map(int, entrada().split())
    valores = list(map(int, entrada().split()))
    valores.sort()

    l = n - k - 1
    c = inf

    for i in range(n - l):        
        a = valores[i]
        b = valores[i + l]        
        c = b - a if b - a < c else c

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()