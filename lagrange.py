from sympy import symbols, expand, simplify
import numpy as np
import matplotlib.pyplot as plt

# Saisie des points
xi = []
yi = []
pt = int(input("Entrer le nombre de points à utiliser : "))
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


x = symbols("x")

# Construire le polynôme de Lagrange
Pn = 0
for i in range(pt):
    Li = 1
    for j in range(pt):
        if i != j:
            Li *= (x - xi[j]) / (xi[i] - xi[j])
    Pn += yi[i] * Li

# simplification
Pn = simplify(Pn)
print("Le polynôme de Lagrange est :", Pn)


# Convertir le polynôme symbolique en une fonction numérique
Pn_numeric = lambda x_val: Pn.subs(x, x_val)

# Générer des points pour la courbe
X = np.linspace(min(xi), max(xi), 500)
Y = [Pn_numeric(x_val) for x_val in X]

# courbe
plt.plot(X, Y, label="Polynôme de Lagrange")
plt.scatter(xi, yi, color='red', label="Points d'entrée")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolation de Lagrange")
plt.grid()
plt.show()