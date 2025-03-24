import numpy as np

a = int(input("entrer le nombre d'inconnue:"))
M = np.zeros((a, a + 1))
x = np.zeros(a)
print("entrer les éléments de la matrice")
for i in range(a):
    for j in range(a + 1):
        M[i][j] = float(input("M[" + str(i) + "," + str(j) + ']' + "="))

# elimination de gauss
for i in range(a):
    if M[i, i] == 0.0:
        print("division par Zéro détecter")
        exit()
    for j in range(i + 1, a):
        div = M[j][i] / M[i][i]

        for k in range(a + 1):
            M[j][k] = M[j][k] - div * M[i][k]
# substitution
x[a - 1] = M[a - 1][a] / M[a - 1][a - 1]
for i in range(a - 2, -1, -1):
    x[i] = M[i][a]
    for j in range(i + 1, a):
        x[i] -= M[i][j] * x[j]
    x[i] = x[i] / M[i][i]
print("SOLUTION:")
for i in range(a):
    print('x%d=%0.2f' % (i, x[i]))