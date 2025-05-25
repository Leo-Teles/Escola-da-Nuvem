idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Categoria: Criança")
elif 13 <= idade <= 17:
    print("Categoria: Adolescente")
elif 18 <= idade <= 59:
    print("Categoria: Adulto")
elif idade >= 60:
    print("Categoria: Idoso")
else:
    print("Idade inválida")