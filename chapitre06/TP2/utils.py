from random import randint


def generer_tableau(taille):
    return [randint(1, taille) for _ in range(taille)]


def generer_matrice_carree(taille):
    return [[randint(1, taille ** 2) for j in range(taille)] for i in range(taille)]
