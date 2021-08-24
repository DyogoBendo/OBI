def main(entrada=input, test=False):
    ia, ib, fa, fb = map(int, entrada().split())    
    c = 0
    if ib != fb:
        c += 1
        if ia == fa:
            c += 1
    else:
        if ia != fa:
            c += 1

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()