def main(entrada=input, test=False):
    n, q = map(int, entrada().split())      

    c = "batataa"
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()