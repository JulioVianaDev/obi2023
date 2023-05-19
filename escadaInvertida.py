degraus = int(input("Numero de degraus: "))
for i in range(degraus,0,-1):
    for j in range(0, i):
      print(f"* {degraus} ",end=" ")
    print("\n")