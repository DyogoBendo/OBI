if __name__ == "__main__":
    l = []
    n = int(input())
    
    for i in range(n):
        k = int(input())
        if k == 0:
            try:                
                l.pop(-1)
            except:
                pass
        else:
            l.append(k)    
    print(sum(l))
        