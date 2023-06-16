caixa1 = int(input())
caixa2 = int(input())
caixa3 = int(input())
lista = [caixa1,caixa2,caixa3]
lista.sort()
viagens = 3
maior = lista[2]
medio = lista[1]
menor = lista[0]
if menor + medio < maior:
    viagens = 1
elif medio < maior or menor < medio:
    viagens = 2
print(viagens)