from sympy import symbols, sympify, solve, plot

# Définir la variable symbolique
x = symbols("x")

# Saisie et validation de la fonction
while True:
    try:
        f = sympify(input("f(x) = "))
        break
    except:
        print("Erreur : Veuillez entrer une fonction valide !")

print("\n************* Méthode de la Dichotomie *************")

# Saisie des bornes
while True:
    try:
        g = float(input("Entrer la borne gauche : "))
        d = float(input("Entrer la borne droite : "))
        if g >= d:
            print("Erreur : La borne gauche doit être inférieure à la borne droite !")
            continue
        if f.subs(x, g) * f.subs(x, d) >= 0:
            print("Erreur : Pas de changement de signe dans l'intervalle !")
            print("Solutions exactes connues (approximation) :")
            for sol in solve(f, x):
                print(f"-> {float(sol)}")
            continue
        break
    except:
        print("Entrée invalide, veuillez recommencer !")

# Paramètres d'arrêt
while True:
    try:
        n_max = int(input("Nombre maximal d'itérations : "))
        if n_max <= 0:
            print("Erreur : Ce nombre doit être supérieur à zéro !")
            continue
        break
    except:
        print("Erreur : Entrez un nombre entier valide !")

while True:
    try:
        epsilon = float(input("Critère d'arrêt (précision) : "))
        if epsilon <= 0:
            print("Erreur : Ce nombre doit être positif !")
            continue
        break
    except:
        print("Erreur : Entrez un nombre valide !")

# Méthode de dichotomie
i = 0
while abs(d - g) > epsilon and i < n_max:
    i += 1
    m = (g + d) / 2
    if f.subs(x, m) == 0:
        print(f"\nRacine exacte trouvée : {m}")
        break
    elif f.subs(x, g) * f.subs(x, m) < 0:
        d = m
    else:
        g = m

if i < n_max:
    approx_root = (g + d) / 2
    print(f"\nRacine approchée après {i} itérations : {approx_root}")
else:
    print(f"Pas de solution trouvée en {n_max} itérations !")

# courbe
choice = input("\nVoulez-vous afficher la courbe ? (O pour oui) : ")
if choice.lower() == 'o':
    plot(f, (x, g - 1, d + 1), line_color="red", legend=True, show=True)
