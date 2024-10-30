# Hipótese e Tese do Teorema da Bissetriz Interna

def bissetriz_interna_ratio(ab, ac, bc):
    # Calcular a razão das partes divididas pela bissetriz interna
    bd_dc_ratio = ab / ac
    bd = (bc * bd_dc_ratio) / (1 + bd_dc_ratio)
    dc = bc - bd
    return bd, dc, bd_dc_ratio

# Usos
ab = 5
ac = 3
bc = 8
bd, dc, ratio = bissetriz_interna_ratio(ab, ac, bc)
print(f"Segmentos BD: {bd}, DC: {dc}, Razão BD/DC: {ratio}")

# Hipótese e Tese do Teorema da Bissetriz Externa

def bissetriz_externa_ratio(ab, ac, bc):
    # Calcular a razão das partes divididas pela bissetriz externa
    bd_dc_ratio = ab / ac
    bd = (bc * bd_dc_ratio) / (bd_dc_ratio - 1)  # Ajuste para bissetriz externa
    dc = bd - bc
    return bd, dc, bd_dc_ratio

# Usos
ab = 5
ac = 3
bc = 8
bd, dc, ratio = bissetriz_externa_ratio(ab, ac, bc)
print(f"Segmentos BD: {bd}, DC: {dc}, Razão BD/DC: {ratio}")

