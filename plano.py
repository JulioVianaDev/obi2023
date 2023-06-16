mega = int(input())
meses = int(input())
gasto = 0
for i in range(meses):
    mes = int(input())
    gasto +=mes
total = mega * (meses +1)
print(total - gasto )
