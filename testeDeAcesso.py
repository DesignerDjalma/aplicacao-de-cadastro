x = {
    'Processos': {
    '1':                    {'data': 'HOJE', 'denominacao': 'Sitio', 'id': 4, 'municipio': 'Belém', 'nome': 'Djalma', 'situacao': 'Doação', 'zee': 'ZEE'},
    '2':                    {'data': 'HOJE', 'denominacao': 'Sitio', 'id': 4, 'municipio': 'Belém', 'nome': 'Djalma', 'situacao': 'Doação', 'zee': 'ZEE'},
    '-NJC9fmiwX-zqtacPlzv': {'data': 'HOJE', 'denominacao': 'Sitio', 'id': 4, 'municipio': 'Belém', 'nome': 'Djalma', 'situacao': 'Doação', 'zee': 'ZEE'},
    '-NJCA7m64Z3DYQ9l4qNY': {'data': 'HOJE', 'denominacao': 'Sitio', 'id': 4, 'municipio': 'Belém', 'nome': 'Djalma', 'situacao': 'Doação', 'zee': 'ZEE'},
    }
}


json_usuarios = {
    "Usuarios":{
        '-NJC9fmiwX-zqtacPlzv':{ "username":"dj_crazy", "password":"12345678", 'email':'3djhey@gmail.com' },
        '-NJCA7m64Z3DYQ9l4qNY':{ "username":"mary_lee", "password":"87654321", 'email':'maryly@gmail.com' },
    }
}



print(json_usuarios['Usuarios'])
# lista rapida
lista_usernames = { json_usuarios['Usuarios'][users]['username']:users for users in json_usuarios['Usuarios']}

# for index, users in enumerate(json_usuarios['Usuarios']):
#     print("-"*40)
#     print(f"Usuario[{index+1}]: {users}")
#     print(json_usuarios['Usuarios'][users]['username'])
#     print("-"*40)


print(lista_usernames)

userInput = "mary_lee"

if userInput in lista_usernames:
    verificar_senha = True
    _id = lista_usernames[userInput]
    print(f"{verificar_senha}: {_id}")
    
    # agora ver se a senha bate

else:
    verificar_senha = False
    print(verificar_senha)
    # Usuario não encontrado



    