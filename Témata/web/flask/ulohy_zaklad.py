"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""
# DÍLČÍ FLASK ÚLOHY - MŮŽETE JE KLIDNĚ VŠECHNY DĚLAT V RÁMCI JEDNOHO PROJEKTU
# Nejedná se o velké těžké úlohy, ale spíše jednodušší malé nezávislé zadání.


##### ! !
# ÚLOHA 1: VYBERTE si buď úlohu 1a, 1b, nebo udělejte nějakou jinou jednoduchou stránku, ale musí na ní být nějaký obrázek a text.
# ! ! ! !

"""
ÚLOHA 1a: Stránka

Udělejte stránku /meme, která bude vracet html soubor, ve kterém bude:
- nadpis
- obrázek nějakého meme
- vysvětlení proč je to meme vtipné

Nápověda:
 - Založte soubor meme.html ve složce templates.
 - Upravte main.py tak, že přidáte /meme endpoint.
 
"""


"""
ÚLOHA 1b: Stránka

Vytvořte stránku "/blog", kde budou zapsány 2-3 krátké příspěvky.

Každý příspěvek by měl mít nadpis, datum publikování a krátký text. Alespoň jeden by měl mít obrázek.

Nápověda:
 - Založte soubor blog.html ve složce templates.
 - Upravte main.py tak, že přidáte /blog endpoint.
"""

"""
ÚLOHA 2: Náhodný VTIP

Udělejte stránku /nahodny-vtip, která uživateli zobrazí náhodný vtip.

Nápověda:
 - Připravte si pár vtipů, následně vždy náhodně vyberte jeden z nich. Můžete použít seznam vtipů níže.
"""

vtipy = [
    "Pes vchází do úřadu práce. Úředník říká: 'Vau, mluvící pes! S tvým talentem tě určitě zaměstnáme v cirkuse.' Pes odpovídá: 'Cirkus? Co by cirkus chtěl s instalatérem?'",
    "Moje přítelkyně se se mnou rozešla, protože si myslí, že jsem posedlý fotbalem. Teď jsem na dně - chodili jsme spolu tři sezóny.",
    "Jaké plemeno psa mají kouzelníci? Labra-kadabra-dory!",
    "Šel jsem do restaurace, kde měli napsáno, že podávají snídani kdykoliv. Tak jsem si objednal míchaná vejce během renesance.",
    "Nejlepší na životě ve Švýcarsku? Nejsem si jistý, ale vlajka je velké plus."
]


"""
ÚLOHA 3: Codepen

Najděte si nějaký jednoduchý design/prvek na stránce https://codepen.io/ a přidejte ho do svého projektu.
Na Codepenu uvidíte HTML i CSS část, pokud prvek obsahuje i Javascript část, najděte něco jiného. 

"""


"""
ÚLOHA 4: Síť

Úkolem je vytvořit alespoň 3 stránky (html soubory), které na sebe navzájem odkazují.
Můžete si vymyslet něco vlastního nebo se inspirovat příkladem níže:

Struktura projektu (příklad):
1. Hlavní stránka (index.html):

    Nadpis: "Vítejte na naší mini-webové síti!"
    Krátký úvodní text.
    Odkazy na všechny následující stránky.

2. O nás (about.html):

    Nadpis: "O nás"
    Několik vět o "tvůrcích" webu (mohou být fiktivní).
    Odkaz zpět na hlavní stránku.

3. Kontakty (contact.html):

    Nadpis: "Kontaktujte nás"
    Fiktivní kontaktní informace (email, telefon).
    Odkaz zpět na hlavní stránku.
    
4. Galerie (gallery.html):

    Nadpis: "Naše galerie"
    Několik obrázků (mohou být libovolné obrázky z internetu).
    Odkaz zpět na hlavní stránku.
"""