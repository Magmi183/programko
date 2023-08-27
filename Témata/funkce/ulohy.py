# Úlohy na funkce, předpokládají znalost parametrů i návratové hodnoty
# >> úlohy nemusí být seřazeny dle obtížnosti
#  - - - - - - - - - - - - - - - - - - - - - - - > > > > > > > > > > > >
"""
"""

"""
Úloha 1: Je to palindrom?

Udělej funkci, která uživateli řekne, zda-li je danný string palindrom. Palindrom je text, který se dá číst i pozpátku a má stejný význam.

PARAMETRY FUNKCE:
    - text (u kterého chceme ověřit, zda-li se jedná o palindrom)

NÁVRATOVÉ HODNOTA:
    - boolean (True nebo False), podle toho, jestli se jedná o palindrom (True), nebo ne (False)
"""

# PŘEVODNÍK JEDNOTEK - ÚLOHA 2.
# >>>> Následující 3 úlohy na sebe postupně navazují

"""
>   Úloha 2a: Převodník jednotek (teplota)

    Udělej funkci, která převede stupně Celsia na stupně Fahrenheita a naopak.

    PARAMETRY FUNKCE:
        - číslo (stupně k převodu)
        - mód (který bude udávat, jestli se převádí z C do F, nebo naopak)

    NÁVRATOVÁ HODNOTA:
        - převedené stupně

"""

"""
>   Úloha 2b: Převodník jednotek (délka)

    Udělej funkci, která bude převádět mezi palci a centimetry.

    PARAMETRY FUNKCE:
        - číslo (délka k převodu)
        - mód (který bude udávat, jestli se z palců do cm, nebo naopak)

    NÁVRATOVÁ HODNOTA:
        - převedená délka

"""

"""
>   Úloha 2c: Převodník jednotek (univerzální)

    Udělej funkci, která bude umět převádět jak délku tak stupně, podle toho co si uživatel přeje.

    PARAMETRY FUNKCE:
        - číslo (hodnota k převodu)
        - další parametry, dle kterých lze specifikovat, jestli chceme převádět délku či stupně, a také odkud kam

    NÁVRATOVÁ HODNOTA:
        - převedená hodnota (např. stupně z F do C), podle toho co si uživatel přál

"""

"""
    Úloha 3: BMI Kalkulátor

    Na základě tělesné váhy a výšky lze pro každého člověka spočítat hodnota BMI.
    BMI, neboli Body Mass Index je číslo, které nějakým způsobem vyjadřuje, jestli má člověk zdravou váhu.

    Nejdříve udělejte pouze základní verzi pro dospělé, tedy pouze na základě výšky a váhy.

    DOBROVOLNÝ ÚKOL: Přidejte i evaluaci, tedy řekněte uživateli, do jaké kategorie spadá (podváha, normální váha, nadváha...).

"""

"""
    Úloha 4: Caesarova šifra

    Udělej funkci, která umí zašifrovat/dešifrovat text pomocí Caesarovy šifry.
    Caesarova šifra funguje tak, že vezme slovo a každé písmeno v něm posune o nějaký počet písmen (každé o stejný počet).
    Pokud tedy chceme zašifrovat např. slovo "ahoj" s posunem 2, vznikne nám "cjql", jelikož písmeno "a" se posune na "c",
    písmeno "h" na "j" atd.

    Úlohu je vhodné rozdělit si na následující podúlohy:
        1) Udělej funkci, která zašifruje jedno písmeno. V parametru přijme písmeno a posun, vrátí výsledek.
           Např. posun("a", 2) vrátí "c".
           Pokud tě nenapadá, jak posunout písmeno, zeptej se. Můžeš zkusit ChatGPT.
        2) Uprav funkci tak, aby uměla i dešifrovat. Případně na to vytvoř separátní funkci.
        3) Udělej funkci, která už umí zašifrovat celá slova. Využij v ní funkce vytvořené v předchozích krocích.


"""