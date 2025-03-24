#récupérer la matrice et le second membre
def get_matrices():
    taille = int(input("----->Quelle est la taille de la matrice : "))
    matrice = []
    for i in range(taille):
        print(f"-----Entrer les éléments de la ligne {i + 1}-----")
        ligne = [float(input(f"a{i + 1}{j + 1} = ")) for j in range(taille)]
        matrice.append(ligne)

    print("======MATRICE======")
    for row in matrice:
        print(row)

    print("Entrer les éléments du second membre:")
    second_member = [float(input(f"b{i + 1} = ")) for i in range(taille)]

    print("======SECOND MEMBRE======")
    print(second_member)

    return matrice, second_member


# créer la matrice augmentée (matrice | second membre)
def matrice_aug(matrice, second_member):
    for i in range(len(matrice)):
        matrice[i].append(second_member[i])
    return matrice


def inverse_matrice(matrice, N):
    # Création de la matrice augmentée (matrice | identité)
    for i in range(N):
        matrice[i].extend(matrice_ident(N)[i])

    # Méthode de Gauss-Jordan
    for i in range(N):
        max_row = max(range(i, N), key=lambda r: abs(matrice[r][i]))
        matrice[i], matrice[max_row] = matrice[max_row], matrice[i]

        # Normalisation de la ligne i
        factor = matrice[i][i]
        matrice[i] = [x / factor for x in matrice[i]]

        # Elimination des autres lignes
        for j in range(N):
            if j != i:
                factor = matrice[j][i]
                matrice[j] = [matrice[j][k] - factor * matrice[i][k] for k in range(2 * N)]

    # Extraire la partie droite (matrice inversée)
    return [row[N:] for row in matrice]


#matrice identité de taille N
def matrice_ident(N):
    return [[1 if i == j else 0 for j in range(N)] for i in range(N)]


if __name__ == "__main__":
    matrice, second_member = get_matrices()
    matrice_augmente = matrice_aug(matrice, second_member)
    print("Matrice augmentée :")
    for row in matrice_augmente:
        print(row)

    # calcul
    inverse = inverse_matrice(matrice_augmente, len(matrice))
    print("Matrice inverse obtenue :")
    for row in inverse:
        print(row)
