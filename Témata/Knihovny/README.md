# Knihovny

Tato lekce slouží k seznámení se s pojmem **knihovna** v kontextu programování a k **vyzkoušení si pár vybraných Python knihoven.** 

**Řekneme si:**
  - co je to knihovna
  - jak fungují knihovny v Pythonu
  - jak používat příkaz **pip** k instalaci nových balíčků
  - ukázka některých nejpoužívanějších knihoven (co nejsou automaticky nainstalovány) + procvičení na příkladech
    - knihovna **PIL** pro práci s obrázky
    - knihovna **matplotlib** pro tvorbu grafů a vizualizaci dat

TODO 2023: Doplnit do tohoto souboru obrázky - generické (knihovna?), ukázky z PIL, ukázky z matplotlib, cokoliv co mě napadne

## Co je to knihovna

Knihovna je soubor nástrojů, funkcí a tříd, které byly vytvořeny tak, aby usnadnily a zrychlily programování.
Místo toho, abyste vytvářeli funkce od nuly, můžete využít již hotové knihovny.

Prostě někdo jiný naprogramoval nějaký užitečný kód, který dal ostatním lidem k používání. Nemá cenu vše programovat od začátku,
nějaké věci se prostě nemění, např. různé matematické funkce.


## Jak fungují knihovny v Pythonu

Python má obrovskou komunitu lidí, kteří vytváří knihovny pro různé účely. Vytvořit knihovnu může kdokoliv.
Dá se také podílet na zlepšování už existujících knihoven - například aby byly rychlejší, kód byl přehlednější atd.

### Import

Pokud chceme v našem kódu používat jakoukoliv knihovnu, musíme ji takzvaně **importovat**. **Import** je příkaz, který
se píše zpravidla na začátek souboru. Struktura příkazu je následující: `import nazev_knihovny`, kde `nazev_knihovny` je knihovna, kterou chceme používat.
Například pokud chceme generovat náhodná čísla, můžeme využít knihovnu `random`, a nemusíme tak vymýšlet způsob, jak generovat náhodná čísla.
Prostě použijeme funkce, které už naprogramoval někdo jiný a které jsou navíc ověřené rokama praxe.

```python
import random

# Generuje náhodné číslo mezi 1 a 10 (včetně obou koncových hodnot)
cislo = random.randint(1, 10)
print(cislo)

# Vrátí náhodný prvek z listu
ovoce = random.choice(['jablko', 'banán', 'kiwi'])
```

Často se také setkáte s použitím `from ... import ...`, což je příkaz, který slouží k tomu, chceme-li z nějaké knihovny vyzobnout jen něco. Například pokud víme, že z knihovny `random`
budeme používat jen některé funkce, mohli bychom výše ukázaný program napsat takto:

```python
from random import randint, choice

# Generuje náhodné číslo mezi 1 a 10 (včetně obou koncových hodnot)
cislo = randint(1, 10)
print(cislo)

# Vrátí náhodný prvek z listu
ovoce = choice(['jablko', 'banán', 'kiwi'])
```

To kód může učinit přehlednějším. Tím, že jsme importovali přímo konkrétní funkce z knihovny, nemusíme před každé volání psát `random.` .

## Instalace knihovny

Pokud chceme používat nějakou knihovnu, musíme si ji nejdříve nainstalovat. To však neplatí pro malou skupinu tzv. **standardních knihoven.**

### Standardní knihovny

V Pythonu existuje několik knihoven, které se nainstalují spolu s instalaci samotného Pythonu. To znamená, že pokud máte nainstalovaný Python, máte i tyto knihovny.

I přes to je však **musíme importovat, pokud je chceme používat.** Můžete se ptát, proč nejsou importovány automaticky. Je to z toho důvodu, že zbytečné
importování by vedlo k větší spotřebě paměti, zpoždění při spuštění programu, potenciální kolizi jmen atd.
Takže - pokud tyto knihovny chceme používat, musíme je importovat, ale nemusíme je instalovat.

**Příkladem těchto knihoven jsou**:
1. `random` - pro generování náhodných čísel a jiných náhodných operací
2. `datetime` - pro práci s daty a časem
3. `os` - pro interakci s operačním systémem
4. `math` - matematické funkce

## Jak nainstalovat knihovnu

TODO 2023: Příkaz pip, atd. Ukázat nejlépe na nějaké knihovně co budeme používat.


# Pillow

Pillow je knihovna, která nám umožňuje pracovat s obrázky. Díky ní můžeme obrázky otevírat, měnit je, a pak je zase uložit. Můžeme například:
- zjistit informace o obrázku (šířka, výška...)
- měnit rozměry
- libovolně obrázek otáčet
- aplikovat filtry
- převádět mezi barevnými formáty
- a další

## Ukázka funkcí Pillow

V souboru [pillow-ukazka-funkci.py](pillow/pillow-ukazka-funkci.py) naleznete ukázku práci s `Pillow`. 
Soubor obsahuje načtení obrázku, následnou aplikaci nejrůznějších operací na něj a následné uložení.

Demonstraci práce s textem najdete pro přehlednost odděleně v souboru [pillow-prace-s-textem.py](pillow/pillow-prace-s-textem.py).

Jelikož je `Pillow` velmi známá a rozšířená knihovna, můžete spoustu materiálu najít i na internetu. 
Skvělým pomocníkem pro tento typ práve vám může být i ChatGPT!

## Úlohy


### Meme Generátor

Cílem je vytvořit jednoduchý **Meme Generátor**, kde si uživatel může vybrat z předem připravených memes a následně do nich přidat vlastní text.

Ve složce `pillow/memes/` naleznete nějaké memes bez textu. Pokud chcete dát uživateli více možností, stáhněte sí více obrázků.

<div style="display: flex; justify-content: space-between;">
    <div style="flex: 1; margin-right: 1%;">
        <img src="pillow/memes/choice.webp" alt="Choice" style="width: 100%; object-fit: cover;">
    </div>
    <div style="flex: 1; margin-right: 1%;">
        <img src="pillow/memes/drake.webp" alt="Drake" style="width: 100%; object-fit: cover;">
    </div>
    <div style="flex: 1; margin-right: 1%;">
        <img src="pillow/memes/looking.webp" alt="Guy" style="width: 100%; object-fit: cover;">
    </div>
    <div style="flex: 1; margin-right: 1%;">
        <img src="pillow/memes/turn.webp" alt="Turn" style="width: 100%; object-fit: cover;">
    </div>
</div>


#### Jak na to

Je na vás, jak se rozhodnete úlohu pojmout, nebojte se experimentovat. 

Můžete začít programem, který bude umět pracovat jen s jedním konkrétním memem. Zeptáte se uživatele na text a umístíte ho na **správné místo do obrázku**.
Pro začátek bude stačit, když text umístíte na absolutní pozici. Souřadnice pozice, kam text budete umisťovat, zjistěte odhadem, pokus/omyl nebo si obrázek otevřte např. v Malování, kde si na pozici najeďte a souřadnice si opište.

Pokračovat můžete programem, který memů bude umět víc. Uživatel si na začátku zvolí meme a program se následně zeptá na text. Všimněte si, že každý meme bude potřebovat vlastní zacházení - text se v nich nachází na různých místech
a navíc jich může být rozdílný počet.

Zvažte následující funkcionality:
1. **Kontrola vstupu**
   - program by měl kontrolovat, že text není moc dlouhý
2. **Náhled**
    - program může umožňovat _náhled_ memu (pomocí příkazu `show`), aby uživatel nemusel meme opakovaně ukládat jen kvůli drobným úpravám


### Grafický editor

Udělejte jednoduchý **textový grafický editor**. Program by měl fungovat zhruba následovně:
1. **Uživatel zadá cestu k obrázku, který chce upravovat.**
2. **Program si obrázek načte.**
   - pokud danný obrázek neexistuje, proces se zopakuje
2. **Program opakovaně dává uživateli možnosti, co s obrázkem dělat.**
   - umístění textu (jaký a kam, případně barva/velikost)
   - rotace obrázku
   - změna velikosti
   - a další
3. **Až bude uživatel hotov, tak se program zeptá, kam má obrázek uložit a uloží výsledný obrázek.**

Pomocí příkazu `show` můžete uživateli průběžně zobrazovat náhled obrázku, aby viděl, jak aktuálně vypadá.

### Hledání cesty (soutěžní úloha)

TODO: Bude přidáno později.

# Matplotlib

TODO 2023: Celé toto zpracovat