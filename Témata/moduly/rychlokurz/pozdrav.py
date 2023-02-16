"""
Funkce, která jako parametr přijímá jméno, které má pozdravit.
Druhý parametr je jazyk, ve kterém má funkce pozdravit.
Funkce nic nevrací, pouze vypisuje do konzole.
"""
def pozdrav(jmeno, jazyk):
    pozdravy = {"cj" : "Dobry den, pane ",
                "aj" : "Hello sir ",
                "pl" : "Dzień dobry Panu, "}

    pozdrav = ""
    if jazyk not in pozdravy:
        print("Zadal jsi neznámý jazyk.")
        return
    else:
        pozdrav = pozdravy[jazyk]

    print(pozdrav + jmeno)

# tato podmínka bude TRUE pouze v případě, že spouštíme přímo tento soubor
# pokud tento skript (soubor) někam importujeme abychom mohli používat jeho funkcionalitu, bude tato podmínka FALSE
if __name__ == "__main__":
    jmeno = input("Jak se jmenuješ?  ")
    jazyk = input("Zadej jazyk z nabídky cj-aj-pl: ")
    pozdrav(jmeno, jazyk)