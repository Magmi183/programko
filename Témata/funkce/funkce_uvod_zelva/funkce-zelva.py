"""
                        ███████╗██╗░░░██╗███╗░░██╗██╗░░██╗░█████╗░███████╗
                        ██╔════╝██║░░░██║████╗░██║██║░██╔╝██╔══██╗██╔════╝
                        █████╗░░██║░░░██║██╔██╗██║█████═╝░██║░░╚═╝█████╗░░
                        ██╔══╝░░██║░░░██║██║╚████║██╔═██╗░██║░░██╗██╔══╝░░
                        ██║░░░░░╚██████╔╝██║░╚███║██║░╚██╗╚█████╔╝███████╗
                        ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚══════╝
"""


"""
1) Připomeň si, jak se s želvou pohybuje, mění barvy atd.
   - jestli nevíš, koukni do souboru zelva-navod.py, kde je návod na základni práci s želvou
"""


"""
2) Zatím bez vlastních funkcí, udělej želví program, který udělá tyto kroky, jak jdou za sebou:
    - nakresli ČERVENÝ čtverec, jehož strany jsou dlouhé 100 ( ... forward(100) ... )
    - nakresli MODRÝ čtverec, jehož strany jsou dlouhé 100 ( ... forward(100) ... )
    - nakresli ZELENÝ čtverec, jehož strany jsou dlouhé 100 ( ... forward(100) ... )
    
Kde na obrazovce čtverce budou je jedno.
"""


"""
!! NOVÁ LÁTKA: FUNKCE (nech si vysvětlit nebo se podívej do návodu) 
3) Kód, který kreslí čtverec o hraně délky 100 dej do funkce. Zatím to bude funkce bez parametrů. Tedy vždy bude kreslit
čtverec s hranami délky 100 a na barvu zatím vůbec nešahá - používá tu, co je nastavená.

Potom svůj program uprav tak, aby na kreslení čtverce používal tu funkci. Stále ale zachovej barvy čtverců, to znamená,
že musíš příkaz color(barva) volat vždy před zavoláním funkce.
"""


# UKÁZKA FUNKCE:
def moje_funkce():
    print("nějaký")
    print("kód")
    print("co patří do funkce")

# použití funkce
moje_funkce()


"""
!! NOVÁ LÁTKA: FUNKCE S PARAMETREM (nech si vysvětlit nebo se podívej do návodu)
4) Pokud už máš funkci, která kreslí čtverec a program, který nakreslí červený, modrý a zelený čtverec, tak do funkce přidej
parametr barvy tak, ať nemusíš barvu psát před funkcí a můžeš ji rovnou říct, jakou barvu čtverce chceš.

Funkce tedy bude mít parametr "barva" a uvnitř funkce se mimo kreslení čtverce nastaví i barva pomocí příkazu color(barva).
"""


# UKÁZKA FUNKCE S PARAMETREM:
def oblibena_barva(barva):
    print("moje oblíbená barva je: " + barva)

# funkci můžeme volat s jinými parametry, pomocí čehož ovlivňujeme její chování
oblibena_barva("zelená")
oblibena_barva("růžová")


"""
!! NOVÁ LÁTKA: FUNKCE S VÍCE PARAMETRY (nech si vysvětlit nebo se podívej do návodu)
5) Do funkce která kreslí čtverec nějaké barvy přidej ještě další parametr: velikost hrany čtverce.

Program pak uprav tak, ať používá tuto funkci. První čtverec bude mít velikost 100, druhý 200 a třetí 123. Barvy zůstanou
jako v předešlých úkolech.
"""

# UKÁZKA FUNKCE S VÍCE PARAMETRY:
def cele_jmeno(jmeno, prijmeni):
    print("Jméno: " + jmeno + ", příjmení: " + prijmeni)
    print("Celé jméno: " + jmeno + " " + prijmeni)

cele_jmeno("Michal", "Janeček")
cele_jmeno("Tomáš", "Jedno")

