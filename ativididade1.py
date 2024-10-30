def lal_semelhanca(lado1_a, lado1_b, angulo_a, lado2_a, lado2_b, angulo_b):
    if (lado1_a / lado2_a == lado1_b / lado2_b) and (angulo_a == angulo_b):
        return True
    return False

def aa_semelhanca(angulo1_a, angulo1_b, angulo2_a, angulo2_b):
    if angulo1_a == angulo2_a and angulo1_b == angulo2_b:
        return True
    return False

def lll_semelhanca(lado1_a, lado1_b, lado1_c, lado2_a, lado2_b, lado2_c):
    if (lado1_a / lado2_a == lado1_b / lado2_b == lado1_c / lado2_c):
        return True
    return False


# Verificar semelhança
def verificar_semelhanca(tipo, *args):
    if tipo == 'LAL':
        return lal_semelhanca(*args)
    elif tipo == 'AA':
        return aa_semelhanca(*args)
    elif tipo == 'LLL':
        return lll_semelhanca(*args)
    else:
        return "Critério inválido"


# Teste dos códigos
print(verificar_semelhanca('LAL', 3, 4, 90, 6, 8, 90))  # True
print(verificar_semelhanca('AA', 45, 90, 45, 90))  # True
print(verificar_semelhanca('LLL', 3, 4, 5, 6, 8, 10))  # True
print(verificar_semelhanca('LAL', 3, 4, 90, 5, 7, 90))  # False
