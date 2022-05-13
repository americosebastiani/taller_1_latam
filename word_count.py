#import re
from collections import Counter
with open ('lorem_ipsum.txt','r') as file:
    texto=file.read()
#texto=re.sub(r'[^\w\s]', '', texto.lower())
print(texto)
#analisis de letras:
text_letter=texto.replace("", " ")
text_letter=text_letter.split()

letras=Counter(text_letter).keys()
unique_letters=Counter(text_letter).values()
print(f"el numero de caracteres distintos es :{len(unique_letters)}")

# #analisis de palabras 

texto_palabra = texto.split()
words=Counter(texto_palabra).keys()
words_number=Counter(texto_palabra).values() 
print(f"el numero de palabras distintas es :{len(words_number)}")


"""nota:
    los valores alcanzados no son los mismos a los esperados por el
"""