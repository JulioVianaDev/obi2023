degraus = int(input("quantos degraus tem a escada? "))
for i in range(degraus):
    for j in range(i +1):
        print("* ",end="")
    print("\n")