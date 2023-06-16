texto = input()
textoTriste = texto.split(":-(")
total = len(textoTriste) - 1
textoFeliz = texto.split(":-)")
totalTriste = len(textoFeliz) - 1
if total > totalTriste:
    print('feliz')
elif totalTriste > total:
    print('triste')
else: 
    print("neutro")