graveto1 = int(input())
graveto2 = int(input())
graveto3 = int(input())
lista = [graveto1,graveto2,graveto3]
lista.sort()
maior = lista[2]
medio = lista[1]
menor = lista[0]
if menor + medio >= maior:
    print("S")
else:
    print("N")