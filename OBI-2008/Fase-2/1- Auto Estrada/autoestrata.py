def main(entrada=input, test=False):    
    codes = {
        "D": 0,
        "A": 1,
        "P": 2,
        "C": 2
    }
    t = 0

    c = int(entrada())
    d = entrada().strip("\n")
    
    for k in d:
        t += codes[k]    

    if not test:
        print(t)
    else:
        return [t]

if __name__ == '__main__':
    main()
