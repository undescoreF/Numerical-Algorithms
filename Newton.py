from sympy import symbols, diff, sympify, plot

x = symbols("x")
recommencer0 = True

while recommencer0:
    try:
        f = sympify(input("f(x) = "))
        recommencer0 = False
    except:
        print("Veuillez entrer une fonction valable.")

print("******************** Méthode de Newton ********************")

# Saisie des paramètres
while True:
    try:
        a = float(input("Valeur initiale approchée d'une racine : "))
        break
    except:
        print("Veuillez entrer un nombre valide.")

while True:
    try:
        z = float(input("Critère d'arrêt : "))
        assert z > 0
        break
    except:
        print("Le critère d'arrêt doit être un nombre positif.")

while True:
    try:
        n = int(input("Nombre max d'itérations : "))
        assert n > 0
        break
    except:
        print("Veuillez entrer un entier positif.")

# Méthode de Newton
xx = a
i = 0
while i < n:
    f_val = f.subs(x, xx)
    df_val = diff(f).subs(x, xx)
    if df_val == 0:
        print("La dérivée est nulle, arrêt du calcul.")
        break
    next_x = xx - (f_val / df_val)
    if abs(next_x - xx) < z:
        xx = next_x
        break
    xx = next_x
    i += 1

if i < n:
    print(f"Nombre d'itérations effectuées : {i}")
    print(f"La racine approximative est : {xx.evalf()}")
else:
    print(f"Aucune solution trouvée après {n} itérations.")

# Visualisation de la courbe
choix = input("Voulez-vous visualiser la courbe ? Tapez 'O' pour OUI, autre touche pour NON : ")
if choix.lower() == 'o':
    plot(f, (x, xx - 5, xx + 5), legend=True, line_color="red")
