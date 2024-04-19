"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░

Úlohy na Jinja2.
"""

"""
Úloha 1: BMI, Převodník jednotek, Kurz krypta

Vyberte si nějakou úlohu, co jste dělali minule a upravte ji tam, aby se výsledek (po odeslání formuláře)
zobrazoval na stejné stránce jako formulář.

Příklad: 1) Kalkulátor BMI zobrazí hodnotu pod formulářem.
         2) Převodník jednotek zobrazí výsledek převodu pod/vedle formuláře.
         3) Kurz krypta - to samé.
         
         Je na vás, jak konkrétně to zrealizujete.
"""

"""
Úloha 2: Vesmírný Věk

Jeden rok = doba, za kterou Země obehně jednou kolem Slunce.
Pro každou planetu je ale tato doba jiná. Podívejte se na následující tabulku:
    Merkur	0.24
    Venuše	0.62
    Země	1.00
    Mars	1.88
    Jupiter	11.86
    Saturn	29.46
    Uran	84.01
    Neptun	164.79
    Pluto	248.59

Udělejte aplikaci, kde:
  1) uživatel zadá svůj věk
  2) vybere si jednu z planet
  3) odešle formulář
  4) na stránce se mu zobrazí, kolik by mu bylo let, kdyby žil na jiné planetě (a počítal roky podle ní).
     Vypočítáte to tak, že vydělíte roky uživatele koeficientem planety.
     např. Pokud je uživateli na Zemi 10 let, pak na Marsu je mu 10/0.24 let = 41.6 let
     
Níže máte nápovědy:

"""

# slovník koeficientů
planeta_roky = {
    'Merkur': 0.24,
    'Venuše': 0.62,
    'Země': 1.00,
    'Mars': 1.88,
    'Jupiter': 11.86,
    'Saturn': 29.46,
    'Uran': 84.01,
    'Neptun': 164.79,
    'Pluto': 248.59
}

"""
HTML FORMULÁŘ:


<form method="post">
        Zadejte svůj věk na Zemi (v letech):
        <input type="number" name="earth_age" required><br>
        Vyberte planetu:
        <select name="planet" required>
            <option value="Merkur">Merkur</option>
            <option value="Venuše">Venuše</option>
            <option value="Země">Země</option>
            <option value="Mars">Mars</option>
            <option value="Jupiter">Jupiter</option>
            <option value="Saturn">Saturn</option>
            <option value="Uran">Uran</option>
            <option value="Neptun">Neptun</option>
            <option value="Pluto">Pluto</option>
        </select><br>
        <input type="submit" value="Vypočítej">
    </form>

"""



"""
Úloha 3: Volby

Udělejte volební aplikaci, kde budou uživatelé hlasovat pro jednoho ze 4 kandidátů.

PO ODESLÁNÍ hlasu uživateli zobrazte průběžné výsledky.
Inspirujte se stránkou "/anketa" v ukázce.


BONUS: Udělejte ještě separátní stránku "/registrace", kde se uživatel může zaregistrovat do voleb jako kandidát
       a ostatní pro něj pak budou moci hlasovat.
"""

"""
Úloha 4: Nápadník a Hlasování

Vytvořte webovou aplikaci rozdělenou na dvě stránky (bude potřeba vytvořit 2 endpointy): 
  - jedna pro přidávání nápadů a 
  - druhá pro zobrazení a hlasování o nápadech

Uživatelé mohou přidávat své nápady a hlasovat pro nápady ostatních.

Funkcionalita:
    1) Přidávání nápadů:

        Stránka s formulářem pro zadání nápadu.
        Tlačítko pro odeslání nápadu.
        Odkaz na stránku pro hlasování.
    
    2) Zobrazení a hlasování o nápadech:

        Stránka zobrazuje seznam všech nápadů s počtem hlasů.
        Možnost hlasování pomocí radio buttonů a submit buttonu.
        Odkaz zpět na stránku pro přidávání nápadů.
"""


# TODO: Po dokonceni tohoto tematu pridat do "klient" i sekci na POST, a nasledne vytvori nejake klienty co posilaji data.
# TODO: Vymyslet jak udelat 1 vote per IP v uloze na volby.