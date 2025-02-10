# TP1: Méthodes d'optimisation en 1D

# 1. Méthode de la dichotomie

# 1.1 Implémentation de la méthode de la dichotomie
# On doit vérifier que f est unimodale sur [a, b]
# On souhaite trouver f(x) = 0
# f continue et f(a) * f(b) < 0

# importation des librairies et scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
from scipy.optimize import golden

# fonction à minimiser
def f(x):
    return x**2 - 2 * np.sin(x)


def dichotomie(f, a, b, epsilon):
    # initialisation
    n = 0
    
    # boucle
    while b - a > epsilon:
        n += 1
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, n

# contraintes de recherche
a = 0
b = 2
epsilon = 1e-5

# application de la méthode de la dichotomie
f_prime = lambda x: 2 * x - 2 * np.cos(x)
x_dichotomie, n_dichotomie = dichotomie(f_prime, a, b, epsilon)
print("-----------------------------")
print(f"Minimum de f: {x_dichotomie} en {n_dichotomie} itérations")
# --------------------------------------



# 1.2 Comparaison avec scipy
# 0 de f avec scipy bisect
root, result = bisect(f_prime, a, b, rtol=epsilon, full_output=True)
print(result)


# conclusion:
# les résultats sont cohérents et scipy est plus efficace

# --------------------------------------
# 2. Méthode de Newton

# 2.1. Conditions à vérifier sur f
# On doit vérifier que f est deux fois dérivable et que f'' est continue

# formulation de l'itéré
def newton(f, f_prime, f_second, x0, epsilon):
    # initialisation
    n = 0
    x = x0
    
    # boucle
    while abs(f_prime(x)) > epsilon:
        n += 1
        x = x - f_prime(x) / f_second(x)
    return x, n

# fonction à minimiser
def f(x):
    return x**2 - 2 * np.sin(x)

# contraintes de recherche
x0 = 1
epsilon = 1e-5

# application de la méthode de Newton
def f_prime(x):
    return 2 * x - 2 * np.cos(x)

def f_second(x):
    return 2 + 2 * np.sin(x)

x, n = newton(f, f_prime, f_second, x0, epsilon)
print("-----------------------------")
print(f"Minimum de f: {x} en {n} itérations")
# --------------------------------------


##########################################
# premier cas f est c1 + chg de signe, 2e cas f est c3 avec f'' != 0
#######################################

# --------------------------------------
# 3. Méthode de la section dorée

# 3.1 Implémentation de la méthode de la section dorée
# On doit vérifier que f est unimodale sur [a, b]
# On souhaite trouver f(x) = 0
# f continue et f(a) * f(b) < 0

# fonction à minimiser
def f(x):
    return x**2 - 2 * np.sin(x)

# section dorée avec fonction intervalle et précision
def section_doree(f, a, b, epsilon):
    # initialisation
    n = 0
    rho = (1 + np.sqrt(5)) / 2
    x1 = 1 / rho * a + (1 - 1 / rho) * b
    x2 = (1 - 1 / rho) * a + 1 / rho * b
    
    # boucle
    while b - a > epsilon:
        n += 1
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = 1 / rho * a + (1 - 1 / rho) * b
        else:
            a = x1
            x1 = x2
            x2 = (1 - 1 / rho) * a + 1 / rho * b
    return (a + b) / 2, n

# contraintes de recherche
a = 0
b = 2
epsilon = 1e-5

# application de la méthode de la section dorée
x, n = section_doree(f, a, b, epsilon)
print("-----------------------------")
print(f"Minimum de f: {x} en {n} itérations")

# 3.2 Comparaison avec scipy
# 0 de f avec scipy golden
results = golden(f, brack=(a, b), tol=epsilon, full_output=True)
print(f"Minimum de f: {results[0]} en {results[2]} itérations")


# --------------------------------------
# 4. Comparaison de toutes les méthodes sur une nouvelle fonction
# fonction à minimiser
def f(x):
    return - 1 / x + np.cos(x)

# contraintes de recherche
a = 2
b = 4
x0 = 2.5
epsilon = 1e-5

# application des méthodes
def f_prime(x):
    return 1 / x**2 + np.sin(x)

def f_second(x):
    return -2 / x**3 + np.cos(x)

x_dichotomie, n_dichotomie = dichotomie(f_prime, a, b, epsilon)

x_newton, n_newton = newton(f, f_prime, f_second, x0, epsilon)

x_section_doree, n_section_doree = section_doree(f, a, b, epsilon)

# output to the console
print("-----------------------------")
print(f"Minimum de f avec dichotomie: {x_dichotomie} en {n_dichotomie} itérations")
print(f"Minimum de f avec newton: {x_newton} en {n_newton} itérations")
print(f"Minimum de f avec section dorée: {x_section_doree} en {n_section_doree} itérations")

# conclusion:
# la méthode de Newton est la plus efficace
# la méthode de la section dorée est la moins efficace
# les résultats sont cohérents avec les attentes

# pour la representation graphique on utilisera la méthode suivante:
# on va tracer la fonction f sur l'intervalle [a, b]
# on va tracer les différents points obtenus par les méthodes en gradient de couleur par rapport au nombre d'itérations
# on redefinira les fonctions pour les adapter à la nouvelle fonction

# fonction à minimiser
def f(x):
    return - 1 / x + np.cos(x)

# contraintes de recherche
a = 2
b = 4
x0 = 2.5
epsilon = 1e-5

# redefinition des methodes pour renvoyer toutes les valeurs
def dichotomie(f, a, b, epsilon):
    # initialisation
    n = 0
    x = []
    
    # boucle
    while b - a > epsilon:
        n += 1
        c = (a + b) / 2
        x.append(c)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return x, n

def newton(f, f_prime, f_second, x0, epsilon):
    # initialisation
    n = 0
    x = []
    
    # boucle
    while abs(f_prime(x0)) > epsilon:
        n += 1
        x0 = x0 - f_prime(x0) / f_second(x0)
        x.append(x0)
    return x, n

def section_doree(f, a, b, epsilon):
    # initialisation
    n = 0
    rho = (1 + np.sqrt(5)) / 2
    x1 = 1 / rho * a + (1 - 1 / rho) * b
    x2 = (1 - 1 / rho) * a + 1 / rho * b
    x = []
    
    # boucle
    while b - a > epsilon:
        n += 1
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = 1 / rho * a + (1 - 1 / rho) * b
        else:
            a = x1
            x1 = x2
            x2 = (1 - 1 / rho) * a + 1 / rho * b
        x.append((a + b) / 2)
    return x, n

# application des méthodes
def f_prime(x):
    return 1 / x**2 + np.sin(x)

def f_second(x):
    return -2 / x**3 + np.cos(x)

x_dichotomie, n_dichotomie = dichotomie(f_prime, a, b, epsilon)

x_newton, n_newton = newton(f, f_prime, f_second, x0, epsilon)

x_section_doree, n_section_doree = section_doree(f, a, b, epsilon)

# output to the console
print("-----------------------------")
print(f"Minimum de f avec dichotomie: {x_dichotomie[-1]} en {n_dichotomie} itérations")
print(f"Minimum de f avec newton: {x_newton[-1]} en {n_newton} itérations")
print(f"Minimum de f avec section dorée: {x_section_doree[-1]} en {n_section_doree} itérations")

# representation graphique sur 3 graphes
# initialisation des valeurs
x = np.linspace(a, b, 100)
y = f(x)

# initialisation des graphes
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# graphe 1
axs[0].plot(x, y, label="f(x)")

# graphe 2
axs[1].plot(x, y, label="f(x)")

# graphe 3
axs[2].plot(x, y, label="f(x)")

# graphe 1
axs[0].scatter(x_dichotomie, [f(x) for x in x_dichotomie], c=range(len(x_dichotomie)), cmap="plasma", label="dichotomie")
axs[0].set_title("Dichotomie")
axs[0].legend()

# graphe 2
axs[1].scatter(x_newton, [f(x) for x in x_newton], c=range(len(x_newton)), cmap="plasma", label="newton")
axs[1].set_title("Newton")
axs[1].legend()

# graphe 3
axs[2].scatter(x_section_doree, [f(x) for x in x_section_doree], c=range(len(x_section_doree)), cmap="plasma", label="section dorée")
axs[2].set_title("Section dorée")
axs[2].legend()

# save the plot with maximum quality
plt.savefig("plot.png", dpi=300)

# affichage
plt.show()

# --------------------------------------
# retour au debut pour refaire les graphes avec les nouvelles fonctions
# fonction à minimiser
def f(x):
    return x**2 - 2 * np.sin(x)

# contraintes de recherche
a = 0
b = 2
epsilon = 1e-5

# application des méthodes
def f_prime(x):
    return 2 * x - 2 * np.cos(x)

def f_second(x):
    return 2 + 2 * np.sin(x)

x_dichotomie, n_dichotomie = dichotomie(f_prime, a, b, epsilon)

x_newton, n_newton = newton(f, f_prime, f_second, x0, epsilon)

x_section_doree, n_section_doree = section_doree(f, a, b, epsilon)

# output to the console
print("-----------------------------")
print(f"Minimum de f avec dichotomie: {x_dichotomie[-1]} en {n_dichotomie} itérations")
print(f"Minimum de f avec newton: {x_newton[-1]} en {n_newton} itérations")
print(f"Minimum de f avec section dorée: {x_section_doree[-1]} en {n_section_doree} itérations")

# representation graphique sur 3 graphes
# initialisation des valeurs
x = np.linspace(a, b, 100)
y = f(x)

# initialisation des graphes
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# graphe 1
axs[0].plot(x, y, label="f(x)")

# graphe 2
axs[1].plot(x, y, label="f(x)")

# graphe 3
axs[2].plot(x, y, label="f(x)")

# graphe 1
axs[0].scatter(x_dichotomie, [f(x) for x in x_dichotomie], c=range(len(x_dichotomie)), cmap="plasma", label="dichotomie")
axs[0].set_title("Dichotomie")
axs[0].legend()

# graphe 2
axs[1].scatter(x_newton, [f(x) for x in x_newton], c=range(len(x_newton)), cmap="plasma", label="newton")
axs[1].set_title("Newton")
axs[1].legend()

# graphe 3
axs[2].scatter(x_section_doree, [f(x) for x in x_section_doree], c=range(len(x_section_doree)), cmap="plasma", label="section dorée")
axs[2].set_title("Section dorée")
axs[2].legend()

# save the plot with maximum quality
plt.savefig("plot_initial_func.png", dpi=300)

# affichage
plt.show()
# --------------------------------------