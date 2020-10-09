word1 = input("Ingrese una palabra: ")
word2 = input("Ingrese otra palabra: ")
num_word1 = len(word1)
num_word2 = len(word2)
res = abs(num_word1 - num_word2)
if num_word1 > num_word2:
    print(f"La palabra {word1} tiene {res} letras mas que la palabra {word2} ")
elif num_word1 < num_word2:
    print(f"La palabra {word2} tiene {res} letras mas que la palabra {word1}")
elif num_word1 == num_word2:
    print("Las palabras tiene el mismo numero de letras")
