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

slovnik_cesko_anglicky = {"Pes": "Dog", "Kočka": "Cat", "Had": "Snake", "Počítač": "Computer", "Jméno": "Name"}

# Nový slovník se vytvoří pomocí {} závorek, do kterých se pak zadají záznamy ve formátu:  klíč : hodnota .
# V tomto případě jsou klíče česká slova a hodnoty anglická slova. Nová slova se dají přidat později.

# HLEDÁNÍ VE SLOVNÍKU
# Přístup k hodnotám ve slovníku funguje podobně jako u seznamu, ale nezadává se index, nýbrž KLÍČ.

pes_anglicky = slovnik_cesko_anglicky['Pes'] # takto získáme hodnotu slova pes, v tomto případě "Dog"
print("Pes se anglicky řekne: " + pes_anglicky)

had_anglicky = slovnik_cesko_anglicky['Had'] # najdu ve slovníku klíč had a dostanu jeho hodnotu => Snake
print("Had se anglicky řekne: " + had_anglicky)


# Pozor! Naopak to nejde!
pes_cesky = slovnik_cesko_anglicky['Dog'] # TOTO NEBUDE FUNGOVAT, protože Dog není klíč, ale hodnota
# ... pokud bychom chtěli překládat i obráceně, potřebovali bychom další slovník.

# PŘIDÁNÍ ZÁZNAMU DO SLOVNÍKU
# Nové záznamy můžeme do slovníku přidávat i po jeho založení - většinou to tak i chceme.
# Na začátku často vytvoříme prázdný slovník a později do něj postupně přidáváme další a další položky, či měníme ty stávající.

slovnik = {} # vytvoření prázdného slovníku
print(slovnik) # jednoduché vypsání obsahu slovníku

# Pokud chceme přidat nový záznam, jednoduše napíšeme:
slovnik[1] = "jedna" # KLÍČI 1 JSEM PŘIŘADIL HODNOTU "jedna"
# ... všimněte si, že KLÍČ nemusí být vždy string. To samé platí i pro hodnotu.

slovnik[2] = "dva" # tento slovník slouží k převodu čísla na slovo
slovnik[3] = "pět" # zde jsem udělal chybu, ukážeme si jak ji napravit

# PŘEPSÁNÍ ZÁZNAMU VE SLOVNÍKU
# Stejným způsobem jako se vkládá nový záznam se dá přepsat již existující. Slovník může obsahovat každý klíč jen jednou,
# proto když vložíme do slovníku klíč, který tam už je, tak se původní hodnota přepíše.

slovnik[3] = "tři" # opětovným vložením klíče 3 přepíšeme jeho hodnotu

# SMAZÁNÍ ZÁZNAMU
# Záznam ze slovníku se dá smazat příkazem del, následovně:
del slovnik[3] # smaže ze slovníku klíč 3 i s jeho hodnotou (celý záznam se smaže)

# DÉLKA SLOVNÍKU
# Stejně jako u stringu či u seznamu se dá délka slovníku zjistit příkazem len()
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
for klic in slovnik: # pokud slovník procházím takto, jako by to byl seznam, procházím pouze klíče
    print(klic)

#   2 - PROCHÁZENÍ hodnot
for hodnota in slovnik.values(): # pro procházení hodnot zavolám na slovníku metodu values() (anglicky hodnoty)
    print(hodnota)

#   3 - PROCHÁZENÍ obojího (klíč, hodnota)
#   Obvykle nás zajímá obojí, tedy klíč i hodnota.
for klic, hodnota in slovnik.items(): # zavolám metodu items() (anglicky položky)
    print("Klíč: " + str(klic) + ", jeho hodnota: " + hodnota)


# TO-DO: Přidat další info: různé způsoby vytvořeni slovníku, funkce pop, popitem, get, clear
# Hezký český materiál na slovník: https://naucse.python.cz/lessons/beginners/dict/



""" 
UKÁZKOVÁ ÚLOHA - ČJ => AJ slovník

Máme česko-anglický slovník, který slouží k překladu z češtiny do angličtiny.
Úkolem je napsat program, který se zeptá uživatele na nějaké české slovo a řekne mu jeho překlad.
Pokud se slovo ve slovníku nenachází, dá program uživateli možnost slovo vložit.
Tato funkcionalita by měla být v donekonečna se opakujícím while cyklu.
"""

slovnik_cj_aj = {"pes": "dog", "kočka": "cat", "had": "snake", "počítač": "computer", "jméno": "name"}

while True:
    slovo = input("Zadej slovo, které chceš přeložit: ")

    if slovo in slovnik_cj_aj: # pokud je slovo ve slovníku, tak ho přeložíme
        print(slovo + " se anglicky řekne: " + slovnik_cj_aj[slovo])
    else: # JINAK dáme uživateli možnost do slovníku slovo přidat
        print("Bohužel, slovo " + slovo + " ve slovníku není. Přejete si jej přidat? ano/ne: ")
        pridat = input()
        if pridat.lower() == "ano": # pokud uživatel zadal ano, přidáme slovo
            slovnik_cj_aj[slovo] = input("Zadej překlad slova " + slovo + ": ")


""" 
Úloha 1: Slovník kvadrátů

Udělej slovník, kde klíče budou čísla 1, 2, 3, 4 ... 10 a jejich hodnoty budou
jejich kvadráty - druhé mocniny. Tedy čísla 1, 4, 9, 16 ... 100. Pro vytvoření slovníku
použij for cyklus. Program by měl umět jednodušše udělat i větší slovník (např. pro
všechna čísla od 1 do 1000), proto je potřeba navrhnout řešení tak, aby bylo škálovatelné.

Hotový slovník následně libovolným způsobem vypište.
"""



""" 
Úloha 2: Spojení slovníků

Máte 2 slovníky, vaším úkolem je tyto slovníky sloučit. Vytvořte tedy nový slovník,
kde budu všechny klíče-hodnoty z původních dvou slovníků. Máte zaručeno, že slovníky
neobsahují stejné klíče.
"""

# TYTO DVA SLOVNÍKY SLUČTE DO JEDNOHO!
slovnik_cj_aj = {"pes": "dog", "kočka": "cat", "had": "snake", "počítač": "computer", "jméno": "name"}
slovnik_aj_cj = {"dog": "pes", "cat": "kočka", "snake": "had", "computer": "počítač", "name": "jméno"}


""" 
Úloha 3: Známky

Máte 2 seznamy:
    - seznam jmen
    - seznam známek
Tyto seznamy obsahují informaci o tom, kdo dostal jakou známku. Jména i známky jsou 
seřazeny tak, že první jméno patří k první známce, druhá známka k druhému jménu apod.

Vaším úkolem je udělat slovník, kde klíč bude jméno a hodnota bude známka, kterou ten člověk dostal.
Úlohy vyřešte pomocí for cyklu! Program musí fungovat beze změny i v případě, že
se do seznamů přidají/odeberou další jména a známky!

NELZE to tedy udělat způsobem:
slovnik["Franta Vomacka"] = 4
slovnik["Robert Vomacka"] = 4
slovnik["Abdul"] = 5
...
"""

# SEZNAM JMEN
jmena = ["Franta Vomacka", "Robert Vomacka", "Abdul", "Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas", "Michal", "Tomas"]
# SEZNAM ZNÁMEK
znamky = [4, 4, 5, 1, 2, "3-"]

# ... tedy Franta Vomacka dostal 4, Robert Vomacka taky 4, Abdul dostal 5 ... a tak dále ...
# Vytvořte seznam, kde klíč je jméno a hodnota je známka, kterou ten člověk dostal.