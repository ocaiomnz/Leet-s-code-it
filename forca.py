import random

def jogar_forca():
    palavras = ['python', 'programacao', 'desafio', 'computador', 'algoritmo']
    palavra_secreta = random.choice(palavras)
    letras_descobertas = []
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")
    
    while tentativas > 0:
        letra = input("Digite uma letra: ")
        
        if letra in letras_descobertas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if letra in palavra_secreta:
            letras_descobertas.append(letra)
        else:
            tentativas -= 1
            print("Letra incorreta! Você tem", tentativas, "tentativas restantes.")
        
        palavra_atual = ""
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_descobertas:
                palavra_atual += letra_secreta
            else:
                palavra_atual += "_"
        
        print(palavra_atual)
        
        if palavra_atual == palavra_secreta:
            print("Parabéns! Você acertou a palavra secreta:", palavra_secreta)
            break
    
    if tentativas == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)

jogar_forca()
