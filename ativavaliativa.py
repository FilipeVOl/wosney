def calcular_salario(salario_fixo, comissao_por_carro, numero_carros_vendidos, total_vendas):
    # Calcula a comissão por carro vendido
    comissao_total = comissao_por_carro * numero_carros_vendidos
    
    # Se o número de carros vendidos for zero, o salário final é apenas o salário fixo
    if numero_carros_vendidos == 0:
        return salario_fixo
    
    # Calcula o percentual sobre o total das vendas
    percentual_sobre_vendas = 0.05 * total_vendas

    # Se o número de carros vendidos for maior que 10, aplica o bônus adicional
    if numero_carros_vendidos > 10:
        bonus_adicional = 0.10 * total_vendas
    else:
        bonus_adicional = 0

    # Salário final é a soma de todos os componentes
    salario_final = salario_fixo + comissao_total + percentual_sobre_vendas + bonus_adicional
    return salario_final

# Usos
salario_fixo = 2000  # Exemplo de salário fixo
comissao_por_carro = 300  # Exemplo de comissão por carro
numero_carros_vendidos = 12  # Exemplo de carros vendidos
total_vendas = 150000  # Exemplo de total de vendas

salario = calcular_salario(salario_fixo, comissao_por_carro, numero_carros_vendidos, total_vendas)
print (salario_fixo, comissao_por_carro, numero_carros_vendidos, total_vendas);
print(f"O salário final do vendedor é: R$ {salario:.2f}")
