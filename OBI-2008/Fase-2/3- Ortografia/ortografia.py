# resolução utiliza programação dinâmica
# https://github.com/lurodrigo/solved-problems/blob/master/obi/2008-nivel2-fase2/ortografia/ortografia@lurodrigo.cpp

def editDistance(s, ls, t, lt):
    ed = [[0 for _ in range(lt + 1)] for _ in range(ls + 1)]    

        
    for i in range(ls + 1):        
        ed[i][0] = i
    for j in range(lt + 1):
        ed[0][j] = j
    

    for i in range(1, ls + 1):
        for j in range(1, lt + 1):            
            ed[i][j] = min(
                1 + ed[i-1][j], # remoção
                1 + ed[i][j-1], # inserção
                ed[i-1][j-1] + (0 if s[i - 1] == t[j - 1] else 1)
            )        
    return ed[ls][lt] < 3


def main(entrada=input, test=False):
    n, m = map(int, entrada().split())
    dic, word = ([] for _ in range(2))

    for i in range(n):
        dic.append(entrada().strip())
    for i in range(m):
        word.append(entrada().strip())
    c = []
    for i in range(m):
        r = ""
        for j in range(n):
            if editDistance(word[i], len(word[i]), dic[j], len(dic[j])):                
                if test:
                    r += dic[j] + " "
                else:
                    print(dic[j], end=" ")
        if not test:            
            print()
        else:            
            c.append(r)    
    c = list(map(lambda letra:letra.strip(), c))    
    if test:
        return c

if __name__ == '__main__':
    main()
