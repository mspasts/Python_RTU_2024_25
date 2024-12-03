def is_palindrome(text:str, 
                  is_alpha_numeric_only=True, 
                  is_case_sensitive=False) -> bool:
    # Noņem atstarpes un padara visu tekstu mazajiem burtiem
    # cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # for this exercise it was sufficient to just lower and replace whitespace
    if is_case_sensitive:
        cleaned_text = text.replace(" ", "")
    else: # means we do not care about case sensitivity
        cleaned_text = text.lower().replace(" ", "")

    if is_alpha_numeric_only:
        # keep only alphanumeric characters
        cleaned_text = ''.join(char for char in cleaned_text if char.isalnum())

    # Salīdzina apstrādāto tekstu ar tā apgriezto versiju
    # ievērosim, ka nav vajadzīgs if cleaned_text == cleaned_text[::-1]!!
    return cleaned_text == cleaned_text[::-1]
 
# # Lietotāja ievade
# user_input = input("Ievadiet tekstu, lai pārbaudītu, vai tas ir palindroms: ")
 
# # Funkcijas izsaukums ar lietotāja ievadu
# if is_palindrome(user_input):
#     print("Teksts ir palindroms!")
# else:
#     print("Teksts nav palindroms.")

# tests
print(f"Test 1: 'Alus ari ira sula' {is_palindrome('Alus ari ira sula') }")
print(f"Test 2: 'Alus ari      ira    sula' {is_palindrome('Alus ari      ira    sula') }")

# negative tests
print(f"Test 3: 'Alus ira sul' {is_palindrome('Alus ira sul') }")
