import re
# 8 caracteres, pelo menos uma letra (m ou M) e 1 numero
# "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
# Adicionando pelo menos 1 special
#"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
# M ou m e 1 numero
# "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
# M ou m , 1, @,  de 8 a 10 chars
#"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,10}$"

# ui = "32c@@W2f2d"
# x = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$",
#         ui
#         )
# if x:
#     print(x.string)
# else:
#     print("N deu match")



# _letras_numeros_especiais = "[A-Za-z\d@$!%*?&]{8,32}"
# _minusculas = "[a-z]"
# _maiusculas = "[A-Z]"
# _digitos = "\d" or "[0-9]"
# _especiais = "[@$!%*?&]"
# _pelo_menos_um_elemento_de = "?=.*"
#_regex_expression = "^[a-z0-9]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$"


email = "djalma.filho@gmail.com"

regex = re.compile(R'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


if re.fullmatch(regex, email):
    print("Valid email")
else:
    print("Invalid email")



