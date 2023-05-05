# mostrar na tela
print("mostrando algo na tela")

#pegar uma informação
input()

#salvar uma informação na variavel
variavel = input()

#transformar a informação em numero
numero = int(input())

#criar uma lista
lista = []

#adicionar uma variavel na lista
variavelNova = "batata"
lista.append(variavelNova)

#checar o item da lista
item = lista[0]

#organizar uma lista 
lista = [44,13,72]
lista.sort()
# lista = [13,44,72]

# escolher quantos itens tem na lista
quantidade = int(input())
listaFinal = []
for rep in range(quantidade):
  listaFinal.append(int(input()))
