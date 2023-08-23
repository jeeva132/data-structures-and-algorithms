def MoveHyphen(strn):
    newstr = ''
    for i in range(len(strn)):
        if strn[i] == '-':
            newstr = strn[i] + newstr
        else:
            newstr +=strn[i]
    return newstr

print(MoveHyphen('Move-Hyphens-to-Front'))