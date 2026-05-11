#imsira a senha
senha=input("Digite a senha: ")
#coloque os valores em falso para se tornar verdadeiros
tem_maiuscula= False
tem_minuscula= False
tem_caracter=False
tem_numero=False
caracteres_especiais= '"!@#$%¨&*()_-+=[]{}?/:;.,><\|
#letras maiúsculas
for caracter in senha:
    if caracter.isupper():
        tem_maiuscula = True

erros = []
if not tem_maiuscula:
    erros.append("Falta caracter maiúsculo")

if len (erros) ==0:
    print("Senha forte")
else:
    print("Senha inavalida")
    print("Requisitos ausentes")

    for erro in erros:
        print("- " + erro)
