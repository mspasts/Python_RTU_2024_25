# Lūdzam lietotājam ievadīt teikumu
sentence = input("Ievadiet teikumu: ")

# Sadalām teikumu vārdos
words = sentence.split()

# Apgriežam katru vārdu
reversed_words = [word[::-1] for word in words]

# Apvienojam apgrieztos vārdus atpakaļ teikumā
reversed_sentence = " ".join(reversed_words)

# Izvadām rezultātu
print(f"Apgrieztie vārdi: {reversed_sentence}")
