linhas = int(input())
textoTotal = ''
for i in range(linhas):
    textLinha = str(input())
    textoTotal += textLinha
abriu = 0
fechou = 0
for caracter in textoTotal:
    if caracter == "{":
        abriu += 1
    if caracter == "}":
        if abriu > -1:
            abriu -=1
        else:
            quebrouTotal = "S"
        fechou += 1
if abriu == 0 and quebrouTotal != "S":
    print("S")
else: 
    print("N")