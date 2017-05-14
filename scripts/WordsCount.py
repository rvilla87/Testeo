import sys
import string
import operator

f = open("files/text.txt", "r")

minimCaracteres = 3
occurPalabras = {}
caracteresFiltrados = str.maketrans("", "", "()[].,!@#$<>«»")

for linea in f:
    # quitamos los caracteres filtrados definidos anteriormente y separamos por espacio para listar las palabras
    for palabra in linea.translate(caracteresFiltrados).split():
        if len(palabra) >= minimCaracteres:
            if not palabra in occurPalabras:
                occurPalabras[palabra] = 1
            else:
                occurPalabras[palabra] += 1
f.close()

# ordenamos por valor (que no llave, para llave sería operator.itemgetter(0))
sorted_occurPalabras = sorted(occurPalabras.items(), key=operator.itemgetter(1), reverse=True)
#In python3 I used a lambda: sorted(d.items(), key=lambda x: x[1])

for palabra, ocurrencias in sorted_occurPalabras:
    # mostramos solo las que aparecen más de 1 vez
    if ocurrencias > 1:
        print("La palabra %s aparece %d veces" % (palabra, ocurrencias))


