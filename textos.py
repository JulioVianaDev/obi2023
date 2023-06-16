texto = str(input())
contador = 0
for i in texto:
    if i == "A":
        contador += 1
print(contador)

print(texto.count("!"))