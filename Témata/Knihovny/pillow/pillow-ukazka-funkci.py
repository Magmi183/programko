from PIL import Image, ImageFilter, ImageEnhance

obrazek = Image.open("obrazky/ddmm.jpeg")

# příkazem show() můžeme obrázek zobrazit
# obrazek.show()


# INFORMACE O OBRÁZKU
# ------------------------------------------------------------------

sirka, vyska = obrazek.size
print(f"Šířka obrázku je: {sirka}, výška je: {vyska}")


# ZMĚNA VELIKOSTI OBRÁZKU
# ------------------------------------------------------------------

# v Pillow se rozměr udává jako DVOJICE INTŮ, tedy (int, int)
polovicni_rozmer = (int(sirka * 0.5), int(vyska * 0.5))
dvojnasobny_rozmer = (int(sirka * 2), int(vyska * 2))
fixni_rozmer = (100, 100)

# Vytvoření nových obrázků s novými velikostmi
zmenseny_obrazek = obrazek.resize(polovicni_rozmer)
zvetseny_obrazek = obrazek.resize(dvojnasobny_rozmer)
obrazek100x100 = obrazek.resize(fixni_rozmer)


# ROTACE OBRÁZKU
# ------------------------------------------------------------------

# Obrázek orotujeme o 90 stupňů
orotovany_obrazek = obrazek.rotate(90)


# PŘEVOD DO ČERNOBÍLÉ
# ------------------------------------------------------------------

# Příkazem convert se dá obrázek převést do jiného režimu, např. L = Černobílý
# Je možný i převod na RGB, RGBA, CMYK a další.
cernobily = obrazek.convert("L")


# APLIKACE FILTRU NA OBRÁZEK
# ------------------------------------------------------------------

# Pillow nabízí několik předpřipravených filtrů. Ukážeme si pár z nich.

# Rozmazání
rozmazany_obrazek = obrazek.filter(ImageFilter.BLUR)

# Zvýšení ostrosti (opak rozmazání)
ostry_obrazek = obrazek.filter(ImageFilter.SHARPEN)

# Comic Book Effect (CONTOUR + SHARPEN filtry)
comic_effect = obrazek.filter(ImageFilter.CONTOUR).filter(ImageFilter.SHARPEN)
# comic_effect.show()


# ÚPRAVA KONTRASTU A JASU
# ------------------------------------------------------------------
# JAS => ovlivňuje celkovou světlost nebo tmavost obrázku
# KONTRAST => ovlivňuje rozdíl mezi světlými a tmavými oblastmi obrázku

# Zvětšení jasu znamená zesvětlení všech pixelů obrázku,
# zatímco zvětšení kontrastu znamená zvýraznění rozdílů mezi světlými a tmavými oblastmi.

# Zvýšení jasu
enhancer = ImageEnhance.Brightness(obrazek)
svetlejsi_obrazek = enhancer.enhance(1.5)  # zvýšení jasu o 50%
# svetlejsi_obrazek.show()

# Snížení jasu
tmavsi_obrazek = enhancer.enhance(0.5)  # snížení jasu o 50%
# tmavsi_obrazek.show()

# Zvýšení kontrastu
contrast = ImageEnhance.Contrast(obrazek)
zvetseny_kontrast_obrazek = contrast.enhance(2.0)  # dvojnásobný kontrast
# zvetseny_kontrast_obrazek.show()

# Snížení kontrastu
snizeny_kontrast_obrazek = contrast.enhance(0.5)  # snížení kontrastu o 50%
# snizeny_kontrast_obrazek.show()

# ------------------------------------------------------------------
# UKÁZKA POUŽITÍ VÍCE FUNKCÍ NAJEDNOU
# ------------------------------------------------------------------
# Načtení obrázku, aplikace transformací a následné uložení.

obrazek = Image.open("obrazky/ddmm.jpeg")

# ZMĚNA VELIKOSTI OBRÁZKU
sirka, vyska = obrazek.size
dvojnasobny_rozmer = (int(sirka * 2), int(vyska * 2))
zvetseny_obrazek = obrazek.resize(dvojnasobny_rozmer)

# PŘEVOD NA ČERNOBÍLÝ
cernobily_obrazek = zvetseny_obrazek.convert("L")

# ZVÝŠENÍ JASU A KONTRASTU
enhancer_jas = ImageEnhance.Brightness(cernobily_obrazek)
jasnejsi_obrazek = enhancer_jas.enhance(1.5)  # zvýšení jasu o 50%

contrast = ImageEnhance.Contrast(jasnejsi_obrazek)
vysoky_kontrast = contrast.enhance(2.0)  # dvojnásobný kontrast

# APLIKACE COMIC BOOK EFEKTU
comic_effect = vysoky_kontrast.filter(ImageFilter.CONTOUR).filter(ImageFilter.SHARPEN)

# ULOŽENÍ OBRÁZKU
comic_effect.save("obrazky/finalni_vysledek.jpeg")