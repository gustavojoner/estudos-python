matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = linha2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Valor [{l, c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print(f'A soma dos números pares foi: {pares}')
for l in range(0, 3):
    coluna3 += matriz[l][2]
print(f'A soma da terceira coluna foi: {coluna3}')
for c in range(0, 3):
    if c == 0:
        linha2 = matriz[1][c]
    elif matriz[1][c] > linha2:
        linha2 = matriz[1][c]
print(f'O maior número da 2 linha foi {linha2}')
