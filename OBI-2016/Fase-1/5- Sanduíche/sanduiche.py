def main(entrada=input, test=False):
    n, d = map(int, entrada().split())
    sanduiches = list(map(int, entrada().split()))
    
    c = "batata"

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()