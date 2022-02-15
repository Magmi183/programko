"""
Pojďme si ukázata některé funkce Stringů - jak se o nich vně programu můžeme dozvědět více informací.
V následujících ukázkách uživatele vždy vyzveme, aby něco napsal a na oplátku mu vytiskneme nějakou informaci o tom, co zadal.
Funkce na stringu se volají tak, že se za string (textový řetězec) napíše tečka, název funkce a její parametry.
Parametr je něco, čím upřesňujeme činnost funkce, ale její základná funkcionalita zůstává stejná. Například tím
specifikujeme, jaké písmeno chceme ve věte spočítat.
např. "text".nazev(parametry funkce)
"""

# Zjištění délky vstupu od uživatele
print(input("Něco napiš:\n").__len__())

# Rozdělení textového řetězce na více částí
print(input("Něco napiš:\n").split(' ')) # rozdělení podle mezer - Věta se rozpadne na slova.
print(input("Něco napiš:\n").split('a')) # rozdělení podle písmena a - Věta se rozpadne na tolik částí + 1, kolikrát obsahuje písmeno a.

# Spočítat počet specifického znaku ve stringu (zde je hezky vidět, na co je parametr - specifikujeme,
# jaký znak chceme spočítat, ale funkcionalita zůstává stejná)
print(input("Něco napiš:\n").count('a'))

# Najdeme první pozici písmene/řetězce ve stringu.
# První pozice je 0!! V programování všechno zpravidla číslujem od 0.
# Pokud funkce nic nenajde, vrátí -1. Zkuste si to.
print(input("Něco napiš:\n").find('a'))
print(input("Něco napiš:\n").find("kocka"))

# Následující funkce řeknou buď True/False (pravda/lež) na základě toho, jestli danný string začíná, respektive končí
# nějakým konkrétním písmenem
print(input("Něco napiš:\n").startswith('M'))
print(input("Něco napiš:\n").endswith('.')) # končí věta tečkou ?

# Následující funkce opět vrací True/False, všechny se ptají na jinou otázku:
print(input("Něco napiš:\n").isdecimal()) # je string pouze z čísel ?
print(input("Něco napiš:\n").isnumeric()) # je string číslo ?
print(input("Něco napiš:\n").isalpha()) # je string pouze z písmen ?
print(input("Něco napiš:\n").isupper()) # je string psán velkým písmem ?
print(input("Něco napiš:\n").islower()) # je string psán malým písmem ?


jmeno = "MICHAL"
jmeno = jmeno.lower() # převedení stringu na malá písmena
print(jmeno)
jmeno = jmeno.upper() # převedení na velká písmena
print(jmeno)

"""
Úloha 1 - odpoved na kviz:
Vemte si váš kvíz (z úlohy na příkaz print).
Nechte uživatele napsat odpověď a pomocí některé z funkcí, které můžete volat na stringu, např. startswith vymyslete
program, který napíše True/False na základě toho, zdali uživatel odpověděl na otázku správně.
"""

# Způsobů, jak to naprogramovat je nekonečně. Tady je jeden z nich.

print("Jaká je nejvyšší hora světa?")
print("")
print("a) Smrk")
print("b) Sněžka")
print("c) Mariánský příkop")
print("d) Mt. Everest")

odpoved = input()

print(odpoved.lower().startswith('d'))