from utils import generer_tableau
from utils import generer_matrice_carree
from random import randint


def rechercher(tab, valeur):
    """
    Retourne True si valeur est dans le tableau tab
    """
    for i in range(len(tab)):
        if tab[i] == valeur:
            return True

    return False


def rechercher_matrice(mat, valeur):
    """
    Retourne True si valeur est dans la matrice carrée mat
    """
    taille = len(mat)

    for ligne in range(taille):
        for colonne in range(taille):
            if mat[ligne][colonne] == valeur:
                return True

    return False


def comparer_premier_dernier(tab):
    """
    Retourne True si la dernière valeur du tableau est plus grande ou égale à la première
    """
    assert len(tab) > 0, "Tableau vide"
    comparaison = tab[len(tab) - 1] >= tab[0]
    return comparaison
