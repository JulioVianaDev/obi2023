degraus = int(input("Numero de degraus: "))
for i in range(degraus):
    for j in range(i + 1):
        print(j+1,end=" ")
    print("\n")