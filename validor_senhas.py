print("-" * 118)
print("Insira uma senha que tenha: Letra maiúscula; Letra minúscula; Um caracter especial; Um número é no mínimo 8 caracteres")

print("-" * 118)
# Inserir a senha

senha = input("Digite a senha: ")

#Variáveis de controle
tem_maiuscula = False
tem_minuscula = False
tem_caracter_especial = False
tem_numero = False
caracteres_especiais = "!@#$%^&*()_-+=[]{}?/:;.,><|"

#Percorrer a string caractere por caractere
for caracter in senha:
    if caracter.isupper():
        tem_maiuscula = True
    elif caracter.islower():
        tem_minuscula = True
    elif caracter.isdigit():
        tem_numero = True
    elif caracter in caracteres_especiais:
        tem_caracter_especial = True

#Lista para armazenar o que falta
erros = []

#Verificação de Comprimento
if len(senha) < 8:
    erros.append("Mínimo de 8 caracteres")

#Verificação das flags
if not tem_maiuscula:
    erros.append("Falta caractere maiúsculo")
if not tem_minuscula:
    erros.append("Falta caractere minúsculo")
if not tem_numero:
    erros.append("Falta um número")
if not tem_caracter_especial:
    erros.append("Falta caractere especial")

#Resultado Final
print("-" * 20)
if len(erros) == 0:
    print("Senha forte")
else:
    print("Senha inválida")
    print("Requisitos ausentes:")
    for erro in erros:
        print("- " + erro)