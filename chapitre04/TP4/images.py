from PIL import Image, ImageDraw

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)


def afficher_test():
    image = Image.new('RGB', (500, 500), BLANC)
    draw = ImageDraw.Draw(image)
    draw.text((250, 250), "OK !", fill=NOIR)
    image.show()


def afficher_image(pixels, taille_pixel=50):
    image = Image.new('RGB', _taille_image(pixels, taille_pixel), BLANC)

    for y in range(len(pixels)):
        for x in range(len(pixels[y])):
            if pixels[y][x] == 1:
                _dessiner_pixel(image, x, y, taille_pixel)

    image.show()


def _taille_image(pixels, taille_pixel):
    hauteur = len(pixels) * taille_pixel
    largeur = len(pixels[0]) * taille_pixel
    return largeur, hauteur


def _dessiner_pixel(image, x, y, taille_pixel, couleur=NOIR):
    coord_debut = x * taille_pixel, y * taille_pixel
    coord_fin = coord_debut[0] + taille_pixel, coord_debut[1] + taille_pixel
    draw = ImageDraw.Draw(image)
    draw.rectangle([coord_debut, coord_fin], fill=couleur)
