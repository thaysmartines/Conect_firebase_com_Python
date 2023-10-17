import pyrebase


config = {
    "apiKey": "AIzaSyDvxqlbNSDmWQxi0NvQ4dnAbDnjWr4P6Gg",
    "authDomain": "tarefas-fabrica-cb7ec.firebaseapp.com",
    "databaseURL": "https://tarefas-fabrica-cb7ec-default-rtdb.firebaseio.com",
    "projectId": "tarefas-fabrica-cb7ec",
    "storageBucket": "tarefas-fabrica-cb7ec.appspot.com",
    "messagingSenderId": "815717806231",
    "appId": "1:815717806231:web:4467768c5769b182be39d2",
    "measurementId": "G-T36N0ZQEF7"
}

firebase = pyrebase.initialize_app(config)

autenticacao = firebase.auth()
from getpass import getpass

email = input("\n Digite seu email:")
senha = getpass("\n Digite sua senha: ")

new_user = autenticacao.create_user_with_email_and_password(email,senha)
print("Usuário criado com sucesso!")

db = firebase.database()
# data2 = {
#     "cargo": "Desenvolvedor backend",
#     "Empresa": "Google"

# }
# data2 = {
#     "nome_tarefa":"banho e tosa",
#     "descricao": "levar o sushi para tosar",
#     "estado_tarefa": "Feito",
#     "data_tarefa":"30-10-2023"
# }

# db.child("Lista_tarefas").push(data2)


tarefas = db.child("Lista_tarefas").get()
# print(tarefas.val())

# for item in tarefas:
#     print("Task: ",item.val()['nome_tarefa'], "Status: ", item.val()['estado_tarefa'])



for item in tarefas:
    if item.val() ["estado_tarefa"]== "Feito":
        db.child("Lista_tarefas").child(item.key()).update({"estado_tarefa":"Fazendo"})







