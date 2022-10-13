with open("arq.txt", "r") as entrada:
    caracteres = entrada.read()

dentro=0
virgulas=0
for caracter in caracteres:
    if caracter == "\"" and not dentro:
        dentro = 1
    elif caracter == "\"" and dentro:
        dentro = 0

    if caracter==",":
        virgulas+=1
    
    if caracter =="," and not dentro:
        

with open("out.txt", "w") as saida:
    saida.write(caracteres)