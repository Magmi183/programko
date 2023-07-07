"""
Bez proměnných se neobejdeme. Co to je?
Je to kousek paměti, který nějak pojmenujeme - a něco si do toho kousku uložíme.
Je to taková krabička, úschovna - kam si uložíme nějakou hodnotu, třeba číslo a později, podle jména si můžeme hodnotu vyzvednout.

Do proměnné můžeme dát String (text), Integer (celé číslo), Float (desetinné číslo) ale i mnoho dalších věcí...
V Pythonu při dělání nové proměnné nepíšeme, jakého typu je - Python si to odvodí sám. Typ můžeme bez problému měnit.
Např. do krabičky, kde byl text můžeme dát číslo.
Problém nastane ve chvíli, kdy se snažíme třeba sčitat číslo s textem - to pochopitelně nejde. Ukážeme si.
"""

# Takhle se vytvoří nové proměnné s nějakou hodnotu, jednoduše napíšu její název a pomocí = do ní dám hodnotu

jmeno = "Michal" # proměnná typu string
prijmeni = "Janecek" # proměnná typu string
tel_cislo = "608381565" # proměnná typu string - ikdyž je to "číslo", pokud je v uvozovkách tak je to pro Python string
vek = 10 # proměnná typu int
neco = input() # proměnný typu string - input vrátí vždy string!! Ikdyž je na vstupu číslo.

# Práci si můžeme usnadnit přiřazením do více proměnných najednou
a = b = c = 1
a, b, c = 1,2,3

# typ proměnných si můžeme zobrazit příkazem type

print(type(jmeno))
print(type(vek))

# S proměnnými můžeme dále pracovat - vytisknout je, sčítat..

# tady je to v pohodě, sčítám texty - to python umí, prostě je spojí za sebe, takže sečtením slov dostanu větu
print("Ahoj " + jmeno + " " + prijmeni)

# co když chci zobrazit i věk?

# print("Ahoj " + jmeno + " " + prijmeni + " je ti " + vek + " let.")

# ... tohle nebude fungovat! program spadne. Proč? Proměnná vek je Integer a já se jí pokouším sčítat s textem (String). To nejde.

# Naštěstí můžu typ proměnné změnit. Tomu se říká PŘETYPOVÁNÍ.

vek = str(vek) # přetypování na string

# teď už to bude fungovat
print("Ahoj " + jmeno + " " + prijmeni + " je ti " + vek + " let.")
print(type(vek)) # a typ se skutečně změnil

# Stejně tak z textu můžu udělat číslo

tel_cislo = int(tel_cislo)
print(type(tel_cislo))

# Nemůžu ale přetypovat vše! Z nějakého textu prostě číslo udělat nejde. Jak bych třeba udělat číslo ze jména? Program by spadl.

# jmeno = int(jmeno) # vyzkoušejte si, že to spadne...


# Do proměnné můžu přiřazovat input, tedy vstup od uživatele. Pozor - bude to vždy STRING - a to ikdyž uživatel zadá číslo.
# Když budu potřebovat, aby to nebyl String, musím si to přetypovat.

jmeno = input("Zadej jméno: \n")
prijmeni = input("Zadej příjmení: \n")
vek = input("Zadej věk: \n")

# Všimněte si, že tady nemusím přetypovávat věk - je to totiž string - všechno z input je string.
print("Ahoj " + jmeno + " " + prijmeni + " je ti " + vek + " let.")

# co když bych s tím ale chtěl počítat? Třeba zvýšit věk o rok?

# vek = vek + 1 # nebude fungovat, snažím se příčíst číslo k textu, to nejde, musím z věku udělat číslo

# 1. způsob:
vek = int(vek) + 1

# 2. způsob:

vek = int(vek)
vek = vek + 1