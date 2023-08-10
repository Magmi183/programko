# Knihovny

Tato lekce slouží k seznámení se s pojmem **knihovna** v kontextu programování a k **vyzkoušení si pár vybraných Python knihoven.** 

**Řekneme si:**
  - co je to knihovna
  - jak fungují knihovny v Pythonu
  - jak používat příkaz **pip** k instalaci nových balíčků
  - ukázka některých nejpoužívanějších knihoven (co nejsou automaticky nainstalovány) + procvičení na příkladech
    - knihovna **PIL** pro práci s obrázky
    - knihovna **matplotlib** pro tvorbu grafů a vizualizaci dat

TODO: Doplnit do tohoto souboru obrázky - generické (knihovna?), ukázky z PIL, ukázky z matplotlib, cokoliv co mě napadne

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

TODO: Příkaz pip, atd. Ukázat nejlépe na nějaké knihovně co budeme používat.