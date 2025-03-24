from sympy import *
x = symbols("x")
recommencer0 = True

while recommencer0:
    try:
        f = sympify(input("f(x) = "))
        recommencer0 = False
    except:
        print("Veuillez entrer une fonction valable")

print("******************** Méthode des points fixes ********************")

while True:
    try:
        x0 = float(input("Entrer la valeur x0 : "))
        break
    except:
        print("Recommencer")

while True:
    try:
        z = float(input("Critère d'arrêt (epsilon) : "))
        assert z > 0
        break
    except (ValueError, AssertionError):
        print("Valeur incorrecte. Recommencer.")

while True:
    try:
        n = int(input("Nombre maximal d'itérations : "))
        assert n > 0
        break
    except (ValueError, AssertionError):
        print("Recommencer.")

while True:
    try:
        g = sympify(input("Entrer g(x) : "))
        break
    except:
        print("Recommencer.")

x1 = g.subs(x, x0)
i = 0
while abs(x1 - x0) > z and i < n:
    x0 = x1
    x1 = g.subs(x, x0)
    i += 1

pprint(g)
print("La racine approchée est :", x1.evalf(), "\nNombre d'itérations :", i)

choix = input("Voulez-vous visualiser la courbe ? (O pour Oui) : ")
if choix.lower() == 'o':
    plot(f, legend=True, line_color="red", show=True)
