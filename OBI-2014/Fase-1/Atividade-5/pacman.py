def main(file_input=input, test=False):
    n = int(file_input())
    c = 0
    atual = 0    
    for i in range(n):
        l = file_input()
        if i % 2 == 0:
            for j in range(n):                        
                if l[j] == "o":
                    atual += 1
                if l[j] == "A":
                    atual = 0
                if atual > c:
                    c = atual
        else:
            for j in range(n - 1, -1, -1):                
                if l[j] == "o":
                    atual += 1
                if l[j] == "A":
                    atual = 0
                if atual > c:
                    c = atual        
    if not test:
        print(c)
    else:
        return [c]

if __name__ == '__main__':
    main()