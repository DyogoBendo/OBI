if __name__ == "__main__":
    c, n = map(int, input().split())
    local = {}
    internet = {}
    for i in range(c):
        id, version = input().split()
        local[id] = int(version)
    
    for i in range(n):
        id, version = input().split()
        try:
            if internet[id] < int(version):
                internet[id] = int(version)
        except:
            internet[id] = int(version)

    for id in internet.keys():
        try: 
            if local[id] < internet[id]:
                print(id, internet[id])
        except:
            print(id, internet[id])
    