def main(entrada=input, test=False):
    l, n = map(int, entrada().split())
    c = (n - 1) + (l - n + 1) ** 2    

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()