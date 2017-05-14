import re
import sys

texto = """fichero.doc
ficheroa.png wedwedwe.eded
dwedwedwed.poe
wedwedwed.kij
wedwedwed.jpg
wedwedwe.png
"""

pattern = r"^(?!.*.png).*$"  # filtrar lo que no tenga .png
pattern = r"^(?!.*png).*"  # TODO: por que necesita el ^ inicial para que funcione? El $ se puede quitar y sigue funcionando


for linea in texto.splitlines():
    match = re.search(pattern, linea)
    if match:
        print("Encontrado:", match.group(), "en linea: ", linea)  ## 'found word:cat')
    else:
        print("No encontrado: ", linea)

sys.exit()
patron = re.compile(r'\bfoo\b')  # busca la palabra foo. The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without change which is very handy for regular expressions (Java needs this feature badly!). I recommend that you always write pattern strings with the 'r' just as a habit.
cadena = "texto donde aaafooESTE_foo_NOwswd foo buscar eee aaa wokwiwfewew d. WEDW dwed 23·()·(/·"


match = re.search(patron, cadena)
print(match)

if match:
    print("Encontrado:", match.group()) ## 'found word:cat')
else:
    print("No encontrado")
