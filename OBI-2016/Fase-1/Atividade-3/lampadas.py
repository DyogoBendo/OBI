def main(file_input=input, test=False):
    ia, ib, fa, fb = map(int, file_input().split())    
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