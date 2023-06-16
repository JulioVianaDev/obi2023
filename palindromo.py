numero = int(input())
lista = list(map(int,input().split()))
operacoes = 0
i = 0
j = numero - 1
for pos in range(numero//2):
    if lista[i] != lista[j]:
      operacoes+=1
    else:
      i+=1
      j-=1
print(operacoes)
