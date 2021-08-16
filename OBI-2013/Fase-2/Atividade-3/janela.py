def main(file_input=input, test=False):
    f = list(map(int, file_input().split()))
    f.sort()
    f1, f2, f3 = f    

    a1 = (0 + f1) * 100
    a2 = (f2 - f1 - 200) * 100 if f2 - f1 - 200 > 0 else 0
    a3 = (f3 - f2 - 200) * 100 if f3 - f2 - 200 > 0 else 0
    a4 = (600 - f3 - 200) * 100

    c = a1 + a2 + a3 + a4


    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()