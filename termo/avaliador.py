def return_dict_contagem(palavra: str):
    letras = set(palavra)

    contagem = {}

    for letra in letras:
        contagem[letra] = palavra.count(letra)

    return contagem

def avaliar(palavra_correta: str, chute: str):
    contagem = return_dict_contagem(palavra_correta)

    result = ""

    letras_encontradas = ""

    for pos in range(5):
        if palavra_correta[pos] == chute[pos]:
            result += "V"
            letras_encontradas += chute[pos]
        elif chute[pos] in palavra_correta and palavra_correta[pos] != chute[pos]:
            letras_encontradas += chute[pos]
            if contagem[chute[pos]] >= letras_encontradas.count(chute[pos]) :
                result += "A"
            else:
                result += "C"
        else:
            result += "C"

    return result
