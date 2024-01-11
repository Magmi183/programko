"""
                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""


"""
Úloha 1: Básnička

Vyzvěte uživatele, ať zadá básničku. (fungovat to ale bude s jakýmkoliv textem)
Tu potom uložte do souboru "uzivatelova_basnicka.txt".
"""



"""
Úloha 2: Terminátor (počítač slov)

V souboru "duchodci_terminator.txt" se nachází příběh, který pojednává o skupině důchodců, která naprogramovala terminátora, kterého posléze vystřelili na měsíc.

Vaším úkolem je zeptat se uživatele na nějaké slovo a spočítat, kolikrát se v textu vyskytuje.
Například, pokud uživatel zadá slovo "terminátor", program spočítá, kolikrát se v textu vyskytuje řetězec "terminátor",
tedy počítají se i odvozená slova jako např. "terminátora" apod.

Nápověda: Načti si celý text metodou read() a následně využij metodu stringu count().
"""



"""
Úloha 3: Nejmenší teplota

V souboru teploty.csv, který obsahuje záznamy o teplotních měřeních najděte, kde a kdy byla naměřena nejmenší teplota.
Je zaručeno, že nejmenší teplota byla naměřena POUZE NA JEDNOM MÍSTĚ a POUZE JEDNOU. Jinými slovy, existuje jen jeden "minimální" záznam.
"""



"""
Úloha 4: Nejčastější teplota

Najdi teplotu, která byla naměřena nejvícekrát (a zjisti kolikrát).

Prerekvizita: slovník. (pokud jsi nedělal slovník, jdi na jiný úkol)
"""



"""
Úloha 5: Kolik si vydělal

Soubor kluci.csv obsahuje záznamy o výdělcích jednotlivých kluků. Vždy, když šel kluk na brigádu, zaznamenalo se na 
samostatný řádek kolik si ten den vydělal korun. Řádky v tabulce vypadají nějak takto:

Vojtík,19027
Honza,94604
Adam,1819
Lukáš,36022
... a tak dále.

Vaším úkolem je zeptat se uživatele, který z kluků ho zajímá a následně mu říct, kolik si ten kluk vydělal peněz CELKEM.

Jména kluků byla vybírána z tohoto seznamu:
ceska_jmena_kluci = ["Tomík", "Bertík", "Míša", "Honza", "Vojtík", "Pája", "Adam", "Lukáš"]
"""



"""
Úloha 6: COVID-19 přírustky nakažených (reálná data)

>> SOUBOR:
V souboru data/nakazeni-covid.csv se nacházejí data o denních přírůstcích nově nakažených osob nemocí Covid-19. 
Data jsem stáhl z oficiálního portálu ministerstva zdravotnictví: https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19 .
Z datasetu jsem akorát odstranil některé sloupce a nahradil prázdné buňky nulou.

>> POPIS DAT:
Dataset obsahuje 7 sloupců, jejichž názvy hovoří samy za sebe:
    - datum (den)
    - nove_pripady (celkem)
    - nove_reinfekce 
    - pripady_neockovani_neprodelali 
    - pripady_neockovani_prodelali 
    - pripady_ockovani_neprodelali 
    - pripady_ockovani_prodelali

>> ÚKOLY:
    1) Zjistěte, který den se nakazilo nejvíce lidí (za celou dobu pandemie).
    2) Zjistěte, který den se poprvé nakazilo více než 50 tisíc lidí.
    3) Jaký rok (2020, 2021, 2022) se nakazilo nejvíce lidí? Jaký naopak nejméně?
    4) Kdy (den) se poprvé nakazil očkovaný člověk?

    ... TODO

    ∞) Vymyslete si nějaký vlastní úkol nad tímto datasetem, nejlépe něco co vás samotné zajímá.

"""