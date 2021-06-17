from math import inf

if __name__ == '__main__':
    vogais = ["a", "e", "i", "o", "u"]
    valor_vogais = [ord("a"), ord("e"), ord("i"), ord("o"), ord("u")]    

    p = input()
    pn = ''
    for c in p:
        if c in vogais:
            pn += c
        else:
            pn += c

            menor = inf
            vv = ''
            for v in valor_vogais:
                k = abs(v - ord(c))
                if menor > k:
                    menor = k
                    vv = chr(v)
            pn += vv

            if c == "z":
                pn += "z"
            else:         
                i = 0       
                while True:
                    i += 1
                    l = chr(ord(c) + i)
                    if l not in vogais:
                        break
                if l == "w":
                    l = "x"
                if l == "y":
                    l = "z"
                pn += l
    print(pn)


    