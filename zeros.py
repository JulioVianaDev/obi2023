quantidade = int(input())
lista = []
for i in range(quantidade):
    numero = int(input())
    lista.append(numero)
    if numero == 0:
        if i ==0:continue
        del(lista[-1])
        del(lista[-1])
print(sum(lista))