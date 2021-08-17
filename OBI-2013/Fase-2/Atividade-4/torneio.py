def main(file_input=input, test=False):
    n, k = map(int, file_input().split())   
    habilidades = [] 
    for i in range(n):
        habilidades.append(int(file_input()))
    

    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()