"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""

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
Úloha 1: Slovník smajlíků (emoji)

Vašim úkolem je udělat program, kde uživatel může zadávat různé názvy smajlíků a jako odpověď dostane smajlíka, který danné slovo reprezentuje.
Např. uživatel zadá "radost" a program odpoví: 😄.

Pokud uživatel zadá nějaký název, který program nezná, tak dá uživateli možnost, aby zadal smajlíka, který ke slovu patří (a program se ho tak "naučil").
Program by měl běžet v nekonečném for cyklu a neustále vyřizovat požadavky uživatele.

Fungovat by měl program tak, že si bude udržovat slovník smajlíků, kde klíč bude slovo reprezentující smajlíka (např. "klaun") a hodnota bude emoji (🤡).

NÁPOVĚDA: Inspirujte se ukázkovou úlohou (ČJ => AJ slovník).

JAK NAPSAT EMOJI ==> Zmáčkněte WINDOWS KEY (logo) + TEČKU a můžete si vybrat emoji.
"""

# pro začátek můžete použít tento slovník
emoce_emoji_slovnik = {"radost": "😄",
                       "klaun": "🤡",
                       "selfmade businessman": "🤑",
                       "láska": "🥰",
                       "nevěřící": "🤨"}

""" 
Úloha 2: Slovník kvadrátů

Udělej slovník, kde klíče budou čísla 1, 2, 3, 4 ... 10 a jejich hodnoty budou
jejich kvadráty - druhé mocniny. Tedy čísla 1, 4, 9, 16 ... 100. Pro vytvoření slovníku
použij for cyklus. Program by měl umět jednodušše udělat i větší slovník (např. pro
všechna čísla od 1 do 1000), proto je potřeba navrhnout řešení tak, aby bylo škálovatelné.

Hotový slovník následně libovolným způsobem vypište.
"""

""" 
Úloha 3: Spojení slovníků

Máte 2 slovníky, vaším úkolem je tyto slovníky sloučit. Vytvořte tedy nový slovník,
kde budu všechny klíče-hodnoty z původních dvou slovníků. Máte zaručeno, že slovníky
neobsahují stejné klíče.
"""

# TYTO DVA SLOVNÍKY SLUČTE DO JEDNOHO!
slovnik_cj_aj = {"pes": "dog", "kočka": "cat", "had": "snake", "počítač": "computer", "jméno": "name"}
slovnik_aj_cj = {"dog": "pes", "cat": "kočka", "snake": "had", "computer": "počítač", "name": "jméno"}


"""
Úloha 4: Tombola

Máte zadaný slovník "osudi", kde klíč je jméno hráče, a hodnota je seznam bodů, které hráč nasbíral.

Úkoly: 1) Projděte slovník a u každého hráče vypište, kolik měl celkem lístů.
       2) Zjistěte, kdo jich měl nejvíc.
       BONUS) Udělejte program, který náhodně vylosuje nějakého hráče. Pravděpodobnost se musí úměrně zvětšovat s počtem bodů.
              Např. ten kdo má celkem 18 bodů má 2x větší šanci na vylosování, než ten, který má 9 bodů 
       
"""


osudi = {
    "Influencer": [5, 1, 4, 4, 2, 2, 5, 4, 4, 4, 2],
    "Boss": [4, 2, 2, 2, 1, 4, 2, 3, 5, 4, 2, 1],
    "Hugo": [3, 3, 1, 4, 3, 4, 3, 4, 1, 2, 1, 1],
    "Svarta": [2, 2, 1, 3, 5, 1, 3, 2, 2],
    "Skibidi": [1, 3, 5, 5, 1, 3, 3, 5, 4, 2, 5, 3, 5, 5, 3],
    "Robert": [5, 1, 1, 3, 3, 3],
    "Smolík": [4, 4],
    "Bulhar": [3, 1, 5, 1, 1]
}


""" 
Úloha 4: Známky

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
