from PIL import Image, ImageFilter, ImageEnhance

obrazek = Image.open("obrazky/skibidi.webp")

# zvětšíme jas
enhancer = ImageEnhance.Brightness(obrazek)
bright_obrazek = enhancer.enhance(2.5)

# aplikujeme CONTOUR filter
contour_obrazek = bright_obrazek.filter(ImageFilter.CONTOUR)

# otočíme obrázek o 45 stupňů
rotated_obrazek = contour_obrazek.rotate(45)

# uložíme výsledek
rotated_obrazek.save("obrazky/skibidi_enhance.webp")
