def main():
    st.write("Vamos jogar! Adivinhe qual é a comida favorita da Maria.")
    st.write("A dica é: Começa com M e termina com U.")
    
    resposta_correta = "macarrão"  # A comida favorita da Maria
    
    tentativa = st.text_input("Qual é a sua tentativa? ").lower()  # Converte a entrada para minúsculas
    
    if tentativa == resposta_correta:
        st.write("Parabéns, você acertou!!")
    else:
        st.write("Não foi dessa vez. Tente novamente!")

if __name__ == "__main__":
    main()
