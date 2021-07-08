if __name__ == '__main__':
    numero = input()
    s = ""
    numbers = [str(i) for i in range(11)]
    letters = [list("abc"), list("def"), list("ghi"), list("jkl"), list("mno"), list("pqrs"), list("tuv"), list("wxyz")]

    for c in numero:
        if c in numbers or c == "-":
            s += c        
        else:            
            for k in range(len(letters)):                
                if c.lower() in letters[k]:
                    s += str(k + 2)
    print(s)