import numpy as np
from fractions import Fraction

# Entrée de la taille de la matrice
l = int(input("Entrer le nombre de lignes (et de colonnes pour une matrice carrée): "))
c = int(input("Entrer le nombre de colonnes: "))

# Vérifier que la matrice est carrée
if l != c:
    print("La matrice doit être carrée pour la décomposition LU.")
    exit()

# Entrer les valeurs dans la matrice
A = np.zeros((l, c))
for i in range(l):
    for j in range(c):
        A[i][j] = float(input(f"M[{i},{j}] = "))

# Copie de A et initialisation de L
U = np.copy(A)
L = np.identity(l)

# Décomposition LU
for i in range(l):
    if U[i, i] == 0:
        print("Division par zéro détectée.")
        exit()
    for j in range(i+1, l):
        L[j, i] = U[j, i] / U[i, i]
        U[j] = U[j] - L[j, i] * U[i]

print("******************************************************* Décomposition L et U **************************************************************")
AffichL = L.astype(str)
AffichU = U.astype(str)

# Convertir les matrices L et U en fractions
for i in range(l):
    for j in range(l):
        AffichL[i, j] = str(Fraction(AffichL[i, j]).limit_denominator())
        AffichU[i, j] = str(Fraction(AffichU[i, j]).limit_denominator())

# Afficher les matrices L et U
print("Matrice L:")
print(AffichL)
print("Matrice U:")
print(AffichU)

# Résolution de l'équation AX = B
B = np.zeros((l, 1))
print("Veuillez entrer les valeurs du vecteur B:")
for i in range(l):
    B[i] = float(input(f"B[{i}] = "))

# Détermination de Y (substitution avant)
y = np.zeros((l, 1))
for i in range(l):
    y[i] = B[i]
    for j in range(i):
        y[i] = y[i] - L[i, j] * y[j]

print("Solution Y:")
for i in range(l):
    print(f"y[{i}] = {Fraction(y[i][0]).limit_denominator()}")

# Détermination de X (substitution arrière)
x = np.zeros((l, 1))
for i in range(l-1, -1, -1):
    x[i] = y[i]
    for j in range(i+1, l):
        x[i] = x[i] - U[i, j] * x[j]
    x[i] = x[i] / U[i, i]

print("\nSolution X:")
for i in range(l):
    print(f"x[{i}] = {Fraction(x[i][0]).limit_denominator()}")


#or
#methode_LU
def LU(M, ligne, B):
    colonne = ligne
    U = np.copy(M)
    L= np.identity(ligne)
#decomposition de la matrice
    for i in range(ligne):
        if U[i,i]==0:
            print("division par zero détectée")
            exit()
        for j in range(i+1,ligne):
            L[j,i] = U[j,i]/U[i,i]
            U[j]=U[j]-L[j,i]*U[i]

#determinatioN de Y
    y=np.zeros((ligne,1))
    for i in range(ligne):
        y[i]=B[i]
        for j in range(i):
            y[i]=y[i]-L[i,j]*y[j]
    AffichY=np.copy(y)
    j=0
    for i in AffichY.tolist():
        print("y[{}]=".format(j),Fraction(*i).limit_denominator(),end='  ' )
        j+=1
#détermination de X
    x=np.zeros((ligne,1))
    for i in range(ligne-1,-1,-1):
        x[i]=y[i]
        for j in range(i+1,ligne):
            x[i]=x[i]-U[i,j]*x[j]
        x[i]=x[i]/U[i,i]
    AffichX=np.copy(x)
    j=0
    print("\n")
    for i in AffichX.tolist():
        print("x[{}]=".format(j),Fraction(*i).limit_denominator(),end='  ' )
        j+=1
