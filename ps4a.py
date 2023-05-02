def get_permutations(cadena):
    if len(cadena) == 1:
        return [cadena]

    permuA = get_permutations(cadena[1:])
    letra1 = cadena[0]
    permutaciones = set()

    for k in permuA:
        for i in range(len(permuA) + 1):
            permutaciones.add(k[:i] + letra1 + k[i:])

    return list(permutaciones)



