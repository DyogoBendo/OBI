if __name__ == '__main__':
    n, m = map(int, input().split())

    MAX_SIZE = (10 ** 6) + 1
    count = [0 for _ in range(MAX_SIZE)]
    forbiden = [0 for _ in range(MAX_SIZE)]
    
    for i in range(n + 1):
        if count[i] == 0:
            for j in range(1, m + 1):
                count[i + j] += 1
                forbiden[i + j] = j
        if count[i] == 1:
            count[i + forbiden[i]] += 1
            forbiden[i + forbiden[i]] = forbiden[i]
    
    if count[n] == 0:
        print("Carlos")
    else:
        print("Paula")