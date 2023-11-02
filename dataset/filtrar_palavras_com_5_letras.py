palavras_5_letras = []

with open("palavras.txt", "r", encoding="utf8") as arquivo:
    lista_de_palavras = arquivo.readlines()

    for palavra in lista_de_palavras:
        if len(palavra) == 7:
            palavras_5_letras.append((palavra[0:5]))

    arquivo.close()

with open("palavras_5_letras.txt", "a+", encoding="utf8") as arquivo:
    for palavra in palavras_5_letras:
        arquivo.write(palavra)
        arquivo.write("\n")