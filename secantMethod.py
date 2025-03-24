from sympy import *

x, f = symbols("x f")
g, d = symbols("g d")
recommencer0 = True

while recommencer0:
    try:
        f = sympify((input("f(x)=")))
        recommencer0 = False
    except:
        print("veuillez entrer une fonction valable")
# entrer des valeurs x1 et x2
while True:
    try:
        x1 = float(input("x1="))
        break
    except:
        print("entrer une valeur valabe")
while True:
    try:
        x2 = float(input("x2="))
        break
    except:
        print("veuillez entrer une valeur valable")
while True:
    try:
        iteration = int(input("entrer le nombre d'itération:"))
        break
    except:
        print("veuillez entrer une valeur valable")
while True:
    try:
        z = float(input("entrer le critère d'arrêt:"))
        break
    except:
        print("veuillez entrer une valeur valable")
# algo
j = 0
while j <= iteration:
    xn = 0
    if f.subs(x, x2) - f.subs(x, x1) == 0:
        print("division par zero, veuillez recommencer")
        exit()
    xn = x2 - ((x2 - x1) * f.subs(x, x2)) / (f.subs(x, x2) - f.subs(x, x1))

    if abs(xn - x2) < z:
        break
    else:
        x1 = x2
        x2 = xn
    j += 1
print("la racine est :", xn, "en %d itération" % j)

continuer = True

choix = input("voulez-vous visualiser la courbe? 'O' pour OUI et  autres touche pour 'NON':")

if choix.lower() == 'o':
    continuer = True
    plot(f, legend=True, line_color="red", show=True)
else:
    continuer = False



