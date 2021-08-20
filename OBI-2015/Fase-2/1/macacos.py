def main(file_input=input, test=False):
    n = int(file_input())
    arvores = []
    for i in range(n):
        x, h = map(int, file_input().split())
        arvores.append((x, h))

    c=0
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()