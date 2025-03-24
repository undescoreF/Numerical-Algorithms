import numpy as np
from fractions import Fraction

# entrer de la taille  la matrice

l = int(input("entrer le nombre de ligne:"))
c = int(input("entrer le nombre de colone:"))

# entrer des valeurs dans la matrice

A = np.zeros((l, c))
for i in range(l):
    for j in range(c):
        A[i][j] = float(input("A[" + str(i) + "," + str(j) + ']' + '='))
# verification de la symétrie
if np.array_equal(A, A.T) and np.all(np.linalg.eigvals(A) > 0):
    print("la matrice est symetrique et positive\n", )
    print("******decomposistion en A=L*Lt***********")
    L = np.zeros((l, c))
    for j in range(l):
        for i in range(j, l):
            if i == j:
                som = 0
                for k in range(j):
                    som += L[i, k] ** 2
                L[i, j] = (A[i, j] - som) ** 0.5
            else:
                som = 0
                for k in range(j):
                    som += L[i, k] * L[j, k]
                L[i, j] = (A[i, j] - som) / L[j, j]
    print("L=", L)
    print("\n")
    print("Lt=", L.T)

else:
    print("Matrice non positive ou non symetrique", A)
    exit()
print(
    "********Resoltion de l'équation AX=B***************")
B = np.zeros((l, 1))
U = L.T
print("veuillez entrer les valeurs du vecteur B")
for i in range(l):
    B[i] = float(input("B[{}]=".format(i)))
# determinatioN de Y
y = np.zeros((l, 1))
for i in range(l):
    som = 0
    for j in range(i):
        som += L[i, j] * y[j]
    y[i] = (B[i] - som) / L[i, i]

AffichY = np.copy(y)
j = 0
for i in AffichY.tolist():
    print("y[{}]=".format(j), Fraction(*i).limit_denominator(), end='  ')
    j += 1
# détermination de X
x = np.zeros((l, 1))
for i in range(l - 1, -1, -1):
    som = 0
    for j in range(i + 1, l):
        som += U[i, j] * x[j]
    x[i] = (y[i] - som) / U[i, i]
AffichX = np.copy(x)
j = 0
print("\n")
for i in AffichX.tolist():
    print("x[{}]=".format(j), Fraction(*i).limit_denominator(), end='  ')
    j += 1