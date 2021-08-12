def main(file_input=input, test=False):
    n = int(file_input())
    c = set()
    for _ in range(n):
        c.add(int(file_input()))
    

    if not test:
        print(len(c))
    else:
        return [len(c)]

if __name__ == '__main__':
    main()