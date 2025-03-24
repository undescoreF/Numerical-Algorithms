import math


# Vérifier si une matrice est à diagonale dominante
def is_diagonally_dominant(matrix):
    n = len(matrix)
    for i in range(n):
        diagonal = abs(matrix[i][i])
        row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if diagonal <= row_sum:
            return False
    return True


# la norme d'un vecteur
def vector_norm(vector):
    return math.sqrt(sum(x ** 2 for x in vector))


# soustraire deux vecteurs
def subtract_vectors(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]


# Méthode de Jacobi
def jacobi(A, b, X0, max_iter, tol):
    n = len(A)
    X = X0.copy()
    X_new = [0] * n
    convergence = False

    for k in range(max_iter):
        for i in range(n):
            sigma = sum(A[i][j] * X[j] for j in range(n) if j != i)
            X_new[i] = (b[i] - sigma) / A[i][i]

        # Calcul de la norme relative
        diff = subtract_vectors(X_new, X)
        norm_diff = vector_norm(diff)
        norm_X_new = vector_norm(X_new)

        if norm_X_new == 0:
            norm_X_new = 1e-10

        relative_error = norm_diff / norm_X_new

        # Vérifier la convergence
        if relative_error < tol:
            print(f"************ CONVERGENCE ATTEINTE APRÈS {k + 1} ITÉRATIONS ***********")
            print(f"Solution trouvée : {X_new}")
            convergence = True
            break

        # Mettre à jour X pour la prochaine itération
        X = X_new.copy()

    if not convergence:
        print(f"xxxxxxxxxxxxxxxxxxx CONVERGENCE NON ATTEINTE APRÈS {max_iter} ITÉRATIONS xxxxxxxxxxxxxxxxxxx")
        print(f"Dernière approximation : {X_new}")

    return X_new


# Exemple d'utilisation
if __name__ == "__main__":
    # Matrice A et vecteur b
    A = [[3, 1, 1],
        [1, 5, 2],
        [2, -1, -6]]
    b = [2, 17, 18]

    if not is_diagonally_dominant(A):
        print("Attention : La matrice n'est pas à diagonale dominante. La convergence n'est pas garantie.")

    X0 = [0, 0, 0]
    max_iter = 100
    tol = 1e-6  # Tolérance pour la convergence

    # Appliquer la méthode de Jacobi
    solution = jacobi(A, b, X0, max_iter, tol)
