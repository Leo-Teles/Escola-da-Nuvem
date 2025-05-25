nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: R$ "))
total_vendas = float(input("Digite o total de vendas no mês: R$ "))

comissao = total_vendas * 0.15

total_receber = salario_fixo + comissao

print(f"O valor total a receber é = R$ {total_receber:.2f}")
