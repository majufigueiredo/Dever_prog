def main():
    print("Vamos jogar! Adivinhe qual é a comida favorita da Maria.")
    print("A dica é: Começa com M e termina com U.")
    
    resposta_correta = "macarrão"  # A comida favorita da Maria
    
    tentativa = input("Qual é a sua tentativa? ").lower()  # Converte a entrada para minúsculas
    
    if tentativa == resposta_correta:
        print("Parabéns, você acertou!!")
    else:
        print("Não foi dessa vez. Tente novamente!")

if __name__ == "__main__":
    main()
