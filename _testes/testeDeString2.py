import string

nome = "djalma"

def validaCaracteres(palavra: str) -> bool:
    for l in palavra:
        if l in [i for i in string.punctuation]:
            return False
    return True

# print(validaCaracteres(nome))

x = 11

if 10 > x > 5:
    print("10 e 5")

