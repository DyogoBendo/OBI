def main(entrada=input, test=False):    
    f, c, e, b = map(int, entrada().split())

    fs = ((b - 1) // c) + e
    cs = ((b - 1) % c)

    r = "PROXIMO VOO" if fs > f else f'{fs} {chr(ord("A") + cs)}'    
    if not test:
        print(r)                
    else:
        return [r]

if __name__ == '__main__':
    main()
