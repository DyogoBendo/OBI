if __name__ == '__main__':
    codes = {
        "D": 0,
        "A": 1,
        "P": 2,
        "C": 2
    }
    t = 0

    c = int(input())
    d = input()
    
    for k in d:
        t += codes[k]
    print(t)