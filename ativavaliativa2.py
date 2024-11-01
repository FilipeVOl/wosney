def calcular_idades(homem1, homem2, mulher1, mulher2):
    # Validando se todas as idades são números inteiros positivos
    if not all(isinstance(idade, int) and idade > 0 for idade in [homem1, homem2, mulher1, mulher2]):
        return "Erro: Todas as idades devem ser números inteiros positivos."

    # Identificando o homem mais velho e o mais novo
    if homem1 > homem2:
        homem_mais_velho = homem1
        homem_mais_novo = homem2
    else:
        homem_mais_velho = homem2
        homem_mais_novo = homem1

    # Identificando a mulher mais velha e a mais nova
    if mulher1 > mulher2:
        mulher_mais_velha = mulher1
        mulher_mais_nova = mulher2
    else:
        mulher_mais_velha = mulher2
        mulher_mais_nova = mulher1

    # Calculando a soma e o produto conforme as regras
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha

    return f"Soma (Homem mais velho + Mulher mais nova): {soma}\nProduto (Homem mais novo * Mulher mais velha): {produto}"

# Exemplo de uso
homem1 = 25  # Idade do primeiro homem
homem2 = 30  # Idade do segundo homem
mulher1 = 20  # Idade da primeira mulher
mulher2 = 18  # Idade da segunda mulher

resultado = calcular_idades(homem1, homem2, mulher1, mulher2)]
print (homem1, homem2, mulher1, mulher2);
print(resultado)
