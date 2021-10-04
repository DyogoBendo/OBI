import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))

for i in range(1, 6):
    path = current_dir + f"/tests/{i}"
    for file in os.listdir(path):
        try:
            a = int(file[:2])
        except:
            try:
                a = int(file[0])
            except:
                continue
        if file[-1] == "n":            
            os.rename(path +"/"+file, path+f"/in{a}")
        else:
            os.rename(path +"/"+file, path+f"/out{a}")