from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont

# Načteme obrázek jak jsme zvyklí
obrazek = Image.open("obrazky/ddmm.jpeg")

# Vytvoříme Draw objekt pro kreslení na obrázku
draw = ImageDraw.Draw(obrazek)

# Definujeme font a velikost písma
# stáhnout si můžete libovolný font, pak jen musíte zadat, kam jste ho dali
font = ImageFont.truetype("./fonty/impact.ttf", size=45)

# Samotný text a barva
text = "ANO\nNA TOMTO MÍSTĚ\nJSEM NAPSAL\nSVŮJ PRVNÍ PROGRAM"
text_color = (0, 0, 0) # ve formátu RGB

# Pozice textu na obrázku
# text_position = (100, 10) # můžeme napsat ABSOLUTNÍ pozici (konkrétní čísla)

# nebo umístit text např. do středu obrázku (postup na následujích 10 řádcích)
# pozice se bude odvíjet od velikosti obrázku i textu, takže bude nutné ji nejdříve spočítat

sirka, vyska = obrazek.size # zjistíme rozměry obrázku

# Získání rozměrů textového pole (text_bbox je seznam se souřadnicemi levého horního + pravého dolního rohu)
text_bbox = draw.textbbox((0,0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# vypočítáme, kde by měl začínat text na ose X a Y
text_x = (sirka - text_width) // 2
text_y = (vyska - text_height) // 2
text_position = (text_x, text_y)

# Kreslení textu na obrázek
draw.text(text_position, text, fill=text_color, font=font)

# Zobrazíme obrázek
obrazek.show()

# Uložíme obrázek
obrazek.save("obrazky/ddmm_text.jpeg")



