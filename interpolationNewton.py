import numpy as np
import matplotlib.pyplot as plt

# Saisie des points
xi = []
yi = []
pt = int(input("Entrer le nombre de points à utiliser : "))

# Vérifier qu'il y a au moins 2 points
if pt < 2:
    raise ValueError("Au moins 2 points sont nécessaires pour l'interpolation.")

print("Entrer des valeurs xi et yi :")
for i in range(pt):
    while True:
        try:
            a = float(input(f"x[{i}] = "))
            b = float(input(f"y[{i}] = "))
            if a in xi:
                print("Erreur : les valeurs de xi doivent être uniques. Veuillez réessayer.")
            else:
                xi.append(a)
                yi.append(b)
                break
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

# Calcul des différences divisées
def diff_div(x, y):
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    for i in range(1, n):
        for j in range(1, i + 1):
            F[i, j] = (F[i, j - 1] - F[i - 1, j - 1]) / (x[i] - x[i - j])
    return F

# Évaluation du polynôme de Newton
def P(x):
    s = 0
    for i in range(pt):
        p = 1
        for j in range(i):
            p *= (x - xi[j])
        s += c[i] * p
    return s

# Calcul des coefficients
F = diff_div(xi, yi)
c = np.diag(F)

# Génération des points pour la courbe
X = np.linspace(min(xi), max(xi), 500)
Y = [P(x_val) for x_val in X]

# Tracé de la courbe et des points d'entrée
plt.plot(X, Y, 'r', label="Polynôme d'interpolation")
plt.scatter(xi, yi, color='green', label="Points d'entrée")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolation polynomiale par différences divisées")
plt.grid()
plt.show()

# la valeur du polynôme en x = 3
print("Table des différences divisées :")
print(F)
print(f"Valeur du polynôme en x = 3 : {P(3)}")