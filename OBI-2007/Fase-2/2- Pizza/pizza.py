def sum_max_sublist(pizza, n):    
    init = 0
    end = 0
    max_sum = 0
    while init < n:
        s = 0
        while end < n:                                    
            s += pizza[end]
            end += 1
            if s < 0:                
                break
            if s > max_sum:
                max_sum = s            
        init = end
    return max_sum

def main(entrada=input, test=False):    
    n = int(entrada())
    fatias = list(map(int, entrada().split()))    
    n = len(fatias)

    fatias_inversa = fatias 
    fatias_inversa.reverse()           

    m1 = sum_max_sublist(fatias, n)
    m2 = sum_max_sublist(fatias_inversa, n)

    m = m1 if m1 > m2 else m2    

    if not test:
        print(m)
    else:
        return [m]

if __name__ == '__main__':
    main()
