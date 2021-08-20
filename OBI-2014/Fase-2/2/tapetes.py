def main(file_input=input, test=False):
    l, n = map(int, file_input().split())
    c = (n - 1) + (l - n + 1) ** 2    

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()