"""
                        ░██████╗██╗░░░░░░█████╗░██╗░░░██╗███╗░░██╗██╗██╗░░██╗
                        ██╔════╝██║░░░░░██╔══██╗██║░░░██║████╗░██║██║██║░██╔╝
                        ╚█████╗░██║░░░░░██║░░██║╚██╗░██╔╝██╔██╗██║██║█████═╝░
                        ░╚═══██╗██║░░░░░██║░░██║░╚████╔╝░██║╚████║██║██╔═██╗░
                        ██████╔╝███████╗╚█████╔╝░░╚██╔╝░░██║░╚███║██║██║░╚██╗
                        ╚═════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝
"""

# CO TO JE ?
# Slovník je jedna ze základních datových struktur v Pythonu. Podobně jako SEZNAM obsahuje nějaké hodnoty.
# Narozdíl od seznamu se ale k prvkům nepřistupuje přes index (tzn. pořadí v seznamu), ale pomocí KLÍČE.

# Každý záznam (položka) ve slovníku je složena z KLÍČE a HODNOTY.
# Zamyslete se jak vlastně funguje slovník v reálném životě. Když máme třeba česko-anglický slovník a chceme v něm něco najít,
# tak hledáme české slovo (KLÍČ) a když ho najdeme, vidíme jeho překlad (HODNOTA).

# SLOVNÍK UKÁZKA NA PŘÍKLADU:

slovnik_cesko_anglicky = {"Pes": "Dog",
                          "Kočka": "Cat",
                          "Had": "Snake",
                          "Počítač": "Computer",
                          "Jméno": "Name"}

# Nový slovník se vytvoří pomocí {} závorek, do kterých se pak zadají záznamy ve formátu:  klíč : hodnota .
# V tomto případě jsou klíče česká slova a hodnoty anglická slova. Nová slova se dají přidat později.

# HLEDÁNÍ VE SLOVNÍKU
# Přístup k hodnotám ve slovníku funguje podobně jako u seznamu, ale nezadává se index, nýbrž KLÍČ.

pes_anglicky = slovnik_cesko_anglicky['Pes']  # takto získáme hodnotu slova pes, v tomto případě "Dog"
print("Pes se anglicky řekne: " + pes_anglicky)

had_anglicky = slovnik_cesko_anglicky['Had']  # najdu ve slovníku klíč had a dostanu jeho hodnotu => Snake
print("Had se anglicky řekne: " + had_anglicky)

# Pozor! Naopak to nejde!
pes_cesky = slovnik_cesko_anglicky['Dog']  # TOTO NEBUDE FUNGOVAT, protože Dog není klíč, ale hodnota
# ... pokud bychom chtěli překládat i obráceně, potřebovali bychom další slovník.

# PŘIDÁNÍ ZÁZNAMU DO SLOVNÍKU
# Nové záznamy můžeme do slovníku přidávat i po jeho založení - většinou to tak i chceme.
# Na začátku často vytvoříme prázdný slovník a později do něj postupně přidáváme další a další položky, či měníme ty stávající.

slovnik = {}  # vytvoření prázdného slovníku
print(slovnik)  # jednoduché vypsání obsahu slovníku

# Pokud chceme přidat nový záznam, jednoduše napíšeme:
slovnik[1] = "jedna"  # KLÍČI 1 JSEM PŘIŘADIL HODNOTU "jedna"
# ... všimněte si, že KLÍČ nemusí být vždy string. To samé platí i pro hodnotu.

slovnik[2] = "dva"  # tento slovník slouží k převodu čísla na slovo
slovnik[3] = "pět"  # zde jsem udělal chybu, ukážeme si jak ji napravit

# PŘEPSÁNÍ ZÁZNAMU VE SLOVNÍKU
# Stejným způsobem jako se vkládá nový záznam se dá přepsat již existující. Slovník může obsahovat každý klíč jen jednou,
# proto když vložíme do slovníku klíč, který tam už je, tak se původní hodnota přepíše.

slovnik[3] = "tři"  # opětovným vložením klíče 3 přepíšeme jeho hodnotu

# SMAZÁNÍ ZÁZNAMU
# Záznam ze slovníku se dá smazat příkazem del, následovně:
del slovnik[3]  # smaže ze slovníku klíč 3 i s jeho hodnotou (celý záznam se smaže)

# DÉLKA SLOVNÍKU
# Stejně jako u stringu či u seznamu se dá délka slovníku zjistit příkazem len()
# délka slovníku = počet dvojic v něm
delka = len(slovnik)
print("Délka slovníku je: " + str(delka) + ".")

# OPERÁTOR IN (ZJIŠTĚNÍ PŘÍTOMNOSTI KLÍČE)
# Pomocí operátoru in mohu zjistit, jestli se nějaký klíč ve slovníku vyskytuje.

if 2 in slovnik:
    print("Slovník obsahuje klíč 2 a jeho hodnota je: " + slovnik[2])
else:
    print("Slovník neobsahuje klíč 2.")

# negací operátoru in se naopak můžu zeptat, jestli se klíč ve slovníku NEvyskytuje

if 2 not in slovnik:
    print("Klíč 2 ve slovníku není.")

# PROCHÁZENÍ SLOVNÍKU
# Pro průchod slovníkem obvykle využijeme FOR cyklus.
# Průchod = "prolistování", cyklus nad slovníkem, projití celého slovníku
# Záleží ovšem, jestli nás zajímají pouze klíče, hodnoty, nebo obojí

#   1 - PROCHÁZENÍ klíčů
for klic in slovnik:  # pokud slovník procházím takto, jako by to byl seznam, procházím pouze klíče
    print(klic)

#   2 - PROCHÁZENÍ hodnot
for hodnota in slovnik.values():  # pro procházení hodnot zavolám na slovníku metodu values() (anglicky hodnoty)
    print(hodnota)

#   3 - PROCHÁZENÍ obojího (klíč, hodnota)
#   Obvykle nás zajímá obojí, tedy klíč i hodnota.
for klic, hodnota in slovnik.items():  # zavolám metodu items() (anglicky položky)
    print("Klíč: " + str(klic) + ", jeho hodnota: " + hodnota)

# METODY SLOVNÍKU
# Stejně jako u seznamu, i slovník má v Pythonu spoustu metod.
# Pojďme si některé ukázat.

#  - - 1) SMAZÁNÍ OBSAHU SLOVNÍKU (clear)
test_slovnik = {1: "a", 2: "b", 3: "c", 4: "d"} # slovník obsahující 4 položky (klíč-hodnota páry)
print(f"Slovník před clearem: {test_slovnik}")
test_slovnik.clear() # metoda clear vymaže veškerý obsah slovníku
print(f"Slovník po clearu: {test_slovnik}")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#  - - 2)  ZÍSKÁNÍ POLOŽKY (get)
test_slovnik = {1: "a", 2: "b", 3: "c", 4: "d"}
# pokud chceme získat nějakou hodnotu ze slovníku, např. třetí písmeno abecedy, uděláme:
print(f"Třetí písmeno abecedy je: {test_slovnik[3]}") # tohle už známe

# ale co když položka neexistuje?
print(f"Páté písmeno abecedy je: {test_slovnik[5]}") # zde program SPADNE, jelikož náš slovník klíč 5 nezná

# Jak toto obejít? Jednu možnost už jsme si ukazovali - můžeme nejdříve manuálně zkontrolovat, jestli se danný klíč ve slovníku nachází.
if 5 in test_slovnik:
    print(f"Páté písmeno abecedy je: {test_slovnik[5]}")
else:
    print("Bohužel, tento klíč se ve slovníku nenachází.")

# DRUHÁ MOŽNOST, abychom se vyvarovali této podmínce, je použít metodu get.
# Ta nikdy nespadne  - místo toho, když nezná klíč, tak vrátí hodnotu None.
vysledek = test_slovnik.get(5)
print(f"Páté písmeno abecedy je: {vysledek}") # program zde sice vypíše None, ale je to většinou lepší, než kdyby spadl

# pokud ale chceme, můžeme simulovat podobnou podmínku jako výše

if vysledek == None:
    # metoda get vrátila None, to znamená, že klíč ve slovníku nebyl
    print("Bohužel, tento klíč se ve slovníku nenachází.")
else:
    # metoda NEvrátilo None, takže tam klíč byl a můžeme vypsat hodnotu k němu přiřazenou
    print(f"Páté písmeno abecedy je: {test_slovnik[5]}")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#  - - 3)  POPNUTÍ PÁRU (popitem)
# slovem POP se v programování většinou myslí ZÍSKÁNÍ a zároveň ODEBRÁNÍ posledního vloženého prvku
test_slovnik = {1: "a", 2: "b", 3: "c", 4: "d"}

test_slovnik[5] = "e" # přidáme nový prvek do slovníku

posledni = test_slovnik.popitem() # metoda 'popitem' vrátí a zároveň odebere poslední přidanou dvojici
print(f"Odebral jsem dvojici: {posledni}")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#  - - 4)  Metody na získání klíču, hodnot a párů
# Tyto metody jsme si ukázali už při procházení slovníku. Pojďme si je jen připomenout.

# KLÍČE - metoda keys vrátí SEZNAM KLÍČŮ ve slovníku
klice = test_slovnik.keys()

# HODNOTY - metoda values vrátí SEZNAM HODNOT ve slovníku
# Hodnoty se ve slovníku mohou vyskytovat opakovaně. Všechny případné duplicitní hodnoty se budou vícekrát vyskytovat
# i ve výsledném seznamu.

hodnoty = test_slovnik.values()

# PÁRY - metoda items vrátí seznam všech položek (položka = klíč + hodnota) ve slovníku
# každá položka je DVOJICE, kde první prvek je klíč a druhý je hodnota
polozky = test_slovnik.items()

# seznam dvojic se dá procházet tímto způsobem
for klic, hodnota in polozky:
    # postupně se procházejí dvojice
    print(f"První prvek ve dvojici (klíč): {klic}, druhý prvek ve dvojici (hodnota): {hodnota}.")
