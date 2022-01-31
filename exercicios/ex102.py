def fatorial(n, show = False):
    """
    Calcula o fatorial de um número
    :param n: valor do número
    :param show: OPCIONAL mostrar ou não a conta
    :return: retorna o valor do resultado
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
help(fatorial)
print(fatorial(5, show = True))
