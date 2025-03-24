# Numerical Methods in Python  
> **Méthodes Numériques en Python**  

## 📚 Content / Contenu

### 1️⃣ **Linear Systems Solvers / Résolution de systèmes linéaires**  

- **LU Decomposition**  
  Factorization of a square matrix `A` into `L * U` for solving linear equations.  
  > Factorisation d’une matrice carrée `A` sous la forme `L * U`.  

- **Gauss-Jordan Elimination**  
  A method for solving systems of equations by transforming the augmented matrix into the reduced row echelon form.  
  > Méthode permettant d’obtenir la matrrice identité et les solutions d’un système.  

- **Gauss-Seidel Iterative Method**  
  Iterative solver for linear systems using successive approximations.  
  > Méthode itérative pour résoudre des systèmes linéaires par approximations successives.  

- **Jacobi Method**  
  Another iterative method for solving systems of linear equations.  
  > Une autre méthode itérative pour résoudre des systèmes d'équations linéaires.  

- **Cholesky Decomposition**  
  Decompose a positive-definite matrix into `L * L^T`.  
  > Factorisation d'une matrice définie positive sous la forme `L * L^T`.  

---

### 2️⃣ **Root-Finding Methods / Recherche de racines d’équations**  

- **Bisection Method**  
  A simple root-finding algorithm that repeatedly divides an interval in half and selects the subinterval in which the root lies.  
  > Méthode de la bisection qui divise successivement un intervalle en deux et choisit le sous-intervalle où la racine se trouve.  

- **Fixed Point Iteration**  
  Numerical method to find solutions of `f(x) = 0` by transforming the equation into `x = g(x)`.  
  > Méthode numérique pour trouver les racines d’une équation à partir de `x = g(x)`.  

- **Secant Method**  
  A root-finding algorithm using two starting points without computing derivatives.  
  > Méthode de la sécante pour trouver des racines sans dérivée.  

- **Newton's Method (for roots)**  
  A method for finding successively better approximations of the roots of a real-valued function.  
  > Méthode de Newton pour trouver des approximations successives des racines d'une fonction réelle.  

- **Newton's Interpolation**  
  A polynomial interpolation method based on the divided differences of a function.  
  > Méthode d'interpolation polynomiale de Newton basée sur les différences divisées d'une fonction.  

- **Lagrange Interpolation**  
  Polynomial interpolation using the Lagrange basis polynomials.  
  > Interpolation polynomiale utilisant les polynômes de base de Lagrange.  

---

## 📁 File Structure / Structure des fichiers

| File / Fichier             | Description                                                   |
|----------------------------|---------------------------------------------------------------|
| `LU.py`                    | LU decomposition and solving linear systems                   |
| `gauss_jordan.py`          | Gauss-Jordan elimination                                      |
| `gauss_seidel.py`          | Gauss-Seidel iterative solver                                 |
| `jacobi.py`                | Jacobi method for solving linear systems                      |
| `cholesky.py`              | Cholesky decomposition for positive-definite matrices         |
| `point_fixe.py`            | Fixed point iteration with optional curve visualization       |
| `secante.py`               | Secant method with optional plot                              |
| `newton.py`                | Newton's method for finding roots                             |
| `bisection.py`             | Bisection method for root-finding                             |
| `interpolation_newton.py`  | Newton's interpolation for polynomial fitting                 |
| `interpolation_lagrange.py`| Lagrange interpolation for polynomial fitting                 |

---

## ✅ Requirements  

- Python 3.9 or higher / Python 3.9 ou supérieur  
- `numpy`  
- `sympy`  
- `matplotlib` (for visualization)  

### Installation  

```bash
pip install numpy sympy matplotlib
