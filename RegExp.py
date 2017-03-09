import re
import sys


patron = re.compile(r'\bfoo\b')  # busca la palabra foo. The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without change which is very handy for regular expressions (Java needs this feature badly!). I recommend that you always write pattern strings with the 'r' just as a habit.
cadena = "texto donde aaafooESTE_foo_NOwswd foo buscar eee aaa wokwiwfewew d. WEDW dwed 23·()·(/·"


match = re.search(patron, cadena)
print(match)

if match:
    print("Encontrado:", match.group()) ## 'found word:cat')
else:
    print("No encontrado")
