cadena="ABCDEFGHI"
num=len(cadena)
columna=3
for c in range(0,num-1, 3):
    print(" ".join(cadena[c:c+columna]))
