def implica(p, q):
    return not p or q

# Gerar a tabela verdade para P, Q, M e R
def tabela_verdade():
    print("P | Q | M | P→Q | (P∨Q)→R | ¬P→(M→R) | R")
    print("-" * 42)

    # Todas as combinações possíveis para P, Q e M
    for P in [True, False]:
        for Q in [True, False]:
            for M in [True, False]:
                # Avaliar as condições lógicas
                cond1 = implica(P, Q)
                R = implica(P or Q, True) and implica(not P, implica(M, True))
                
                # Condições intermediárias para a tabela
                cond2 = implica(P or Q, R)
                cond3 = implica(not P, implica(M, R))
                
                # Exibir resultados formatados
                print(f"{P} | {Q} | {M} | {cond1} | {cond2} | {cond3} | {R}")

# Executar a tabela verdade
tabela_verdade()

# Passo 1: Liste todas as combinações possíveis para 𝑃, 𝑄 e 𝑀 No código, isso é feito usando for loops que percorrem todas as combinações de valores verdadeiros (True) e 
# falsos (False) para P, Q, e M.
# Passo 2: Avalie cada proposição lógica usando operadores de Python. Para isso, usamos a função implica para representar a implicação lógica 𝑃→Q,
# e operadores lógicos como or e and para as outras expressões.
# Passo 3: Exiba a tabela verdade formatada com os resultados para cada combinação. A tabela é exibida no terminal, com as colunas e os valores de cada combinação.
