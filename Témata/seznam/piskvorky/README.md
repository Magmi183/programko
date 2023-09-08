# Piškvorky

---

> Tento návod obsahuje některé užitečné tipy a postupy, kterých lze využít při programování piškvorek Pythonu.

## Jednoduchá verze (3x3)

V této části se budeme zabývat jednodušší verzí piškvorek, kde se hraje pouze na ploše **3x3**, hrací plánek bude mít tedy 3 řádky a 3 sloupce, celkem pouze 9 polí.

### Zadání


Naprogramuj jednoduché piškvorky na hrací ploše o velikosti 3x3, tedy celkem 9 polí.
Hráči se budou střídat. Pozici, na kterou chtějí umístit svůj symbol budou zadávat ve formátu souřadnic, tedy např.:
1 2 -> což znamená, že hráč si přeje umístit svůj symbol (křížek nebo kolečko) do druhého sloupce v prvním řádku.

Hraje se tak dlouho, dokud není znám vítěz, nebo dokud není remíza.


### Struktura programu

> Jak bude program vypadat? Jaké budou jeho jednotlivé části? Jaké kroky a v jakém pořadí je třeba udělat?

V této si stručně rozdělíme program na jednotlivé kroky/akce a nastíníme si, jak je budeme implementovat. Detailnější popis si necháme na později.

1. **Příprava hry**
   - Nejdřív budeme muset připravit věci nutné pro hru, tedy například **hrací plochu**, určit který hráč je jako první na tahu atd.
   - Zkrátka potřebujeme si promyslet, jaké proměnné budeme k běhu programu potřebovat.
2. **Herní cyklus**
   - Dalším krokem bude udělat **herní cyklus**. Tomuto se také někdy říká **herní smyčka**.
   - Tento cyklus se bude opakovat tak dlouho, dokud nebude znám vítěz.
   - Jeden průchod tímto cyklem bude představovat tah hráče. Jeden cyklus bude hrát hráč 1 a příští cyklus zase hráč 2. Takto se budou střídat tak dlouho, dokud někdo nevyhraje nebo nebude remíza.
   - **Co bude v tomto herním cyklu? Jaké akce musíme vykonat v jednom tahu?**
     1. Zobrazíme herní plochu, aby hráč viděl, jaký je nyní stav hry.
     2. Zeptáme se hráče, kam chce zahrát svůj tah a načteme vstup (řádek + sloupec).
     3. Zkontrolujeme, že zadal platné pole a umístíme jeho tah na naší herní plochu.
     4. Zkontrolujeme, jestli někdo nevyhrál, nebo jestli nenastala remíza.
     5. Na konci cyklu musíme změnit hráče, který je na tahu - jinak by příští cyklus hrál opět ten stejný hráč a jeho protivník by si jaksi nezahrál.

### Herní plocha

Jelikož předem známe velikost herní plochy, můžeme ji vytvořit poměrně jednoduše. Nabízí se udělat seznam, ve kterém budou další seznamy. Zní to možná složitě, ale je to pro člověka nejintuitivnější způsob, jak herní plochu reprezentovat.
Zkrátka budeme mít seznam řádků, kde každý řádek bude další seznam - seznam sloupců. 

Mohlo by to vypadat nějak takto:
```python
plocha = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]
```
Tímto způsobem jsme vytvořili seznam, který ma 3 položky (řádky tabulky), jež každá z nich je seznam, který má další 3 položky (sloupce v řádku).
Sloupečky jsou stringy (text), začínají jako mezera, což pro nás bude znamenat, že pole je zatím prázdné.

Když budeme chtít změnit například pole vlevo nahoře, znamená to **nultý** řádek a v něm **nultý** sloupec. (Připomínka: První položka v seznamu je na pozici 0.)
```python
plocha[0][0] = "x" # takto nastavíme pole vlevo nahoře na symbol x
```

### Hráč na tahu, symbol

Ještě než začneme dělat herní cyklus, potřebujeme ještě:
1. Proměnnou, ve které budeme mít informaci o tom, který hráč je zrovna na tahu
2. Symbol tohoto hráče (šlo by to udělat i jinak, toto je jen jeden způsob)

```python
hrac_na_tahu = 1 # Začíná hráč 1
symbol = "x" # hráč 1 bude mít symbol x (budeme jej měnit vždy na konci kola)
```

### Herní cyklus

Teď musíme udělat cyklus, který bude obsahovat většinu hry. Tedy **dokud** tento cyklus poběží, tak se bude hrát.
Nabízí se na to **while cyklus**. Jaká bude jeho podmínka? Co třeba: **dokud není znám vítěz, hraje se dál**.

Opět je mnoho způsobů, jak tento while cyklus sestrojit. Ukážeme si jeden z nich. Založíme si proměnnou `vitez` (ještě před while cyklem).
Na začátku ji nastavíme na hodnotu 0. To pro nás bude znamenat, že zatím nikdo nevyhrál. Pokud později zjistíme, že vyhrál hráč 1 nebo 2, nastavíme hodnotu proměnně `vitez` na 1 nebo 2.
Pokud nastala remíza, nastavíme hodnotu `vitez` na -1.

|           | 0                     | 1              | 2              | -1      |
|-----------|-----------------------|----------------|----------------|---------|
| **vitez** | Zatím nikdo nevyhrál. | Hráč 1 vyhrál. | Hráč 2 vyhrál. | Remíza. |

Jak tedy bude vypadat náš herní cyklus, pokud chceme aby se opakoval tak dlouho, dokud nikdo nevyhrál?

```python
while vitez == 0:
    # - zobraz aktuální stav hry (herní plochu)
    # - vyzvi hráče, který je právě na tahu, aby zadal kam chce umístit svůj symbol
    # - zkontroluj, že uživatel zadal správné hodnoty, pokud ne, ať je zadá znovu
    # - umísti symbol na hráčem zvolené místo
    # - zkontroluj vítěze/remízu
    # - pokud nikdo nevyhrál, změň hráče, který je na tahu a cyklus může jet znova
```

> Podmínku herní smyčky již máme, teď se podíváme na její obsah. Tedy jednotlivé kroky, které se budou opakovat pro tah každého hráče.


#### 1) Zobrazení stavu hry

Před začátkem každého kola je potřeba hráčům ukázat aktuální stav hry (herní plochu).

Mohli bychom zkusit jednodušše udělat `print(plocha)`, což sice herní plochu zobrazí, ale v poměrně ošklivém formátu:
`[['x', 'o', 'o'], ['x', 'x', 'o'], ['x', 'o', ' ']]`. Sice jdou vidět všechna pole, ale ve hře se téměř nedá orientovat.
Je potřeba plochu zobrazit ve čtvercovém formátu a jednotlivé řádky + sloupce očíslovat.

Paradoxně se jedná asi o nejtěžší část implementace, proto níže najdete celý kód potřebný pro hezký výpis herní plochy.
**Myšlenka je následující:**
1. Nejdříve vytiskneme čísla sloupců.
2. Potom budeme for cyklem **postupně procházet řádky** a v nich
   **dalším for cyklem** tisknout jednotlivé sloupečky. Nevytiskneme je hned,
   ale nejdřív mezi ně umístíme zarážku `|`, aby byl výstup hezký.


Takto vypadá kód (můžete si jej zkopírovat do vašeho programu):
```python
# Vypsání herní plochy (aktuální stav hry)
print("   1 2 3") # čísla sloupců
for cislo_radku in range(3): # projdu každý řádek
    radek = str(cislo_radku + 1) + " |" # přidám číslo řádku a stěnu
    for cislo_sloupce in range(3): # projdu každý sloupec
        radek += plocha[cislo_radku][cislo_sloupce] + "|" # přidám do řádku aktuální políčko (kombinace řádku a sloupce)
    print(radek) # řádek který jsem si sestavil vypíšu, vnější cyklus bude pokračovat dalším řádkem
```

a takto jeho výstup:
```text
   1 2 3
1 |x|o|o|
2 |x|x|o|
3 |x|o| |
```

#### 2) Načtení vstupu

Po zobrazení plochy je potřeba **vyzvat aktuálního hráče**, aby zadal **řádek** a **sloupec** kam chce umístit svůj symbol.
- **Načtěte vstup do dvou proměnných**, které následně přetypujte na `int`. (`input()` vždy vrací string, my ale potřebujeme čísla).

**Ale POZOR**, předpokládáme, že uživatel zadává čísla od jedné, ale v programování se čísluje od 0.
Proto je potřeba od řádku i sloupce odečíst 1.

```python
radek -= 1
sloupec -= 1
```

Např. první pole v prvním řádku dostaneme takto: `plocha[0][0]`.
Pokud bychom napsali `plocha[1][1]`, znamená to druhý řádek a druhý sloupec.


#### 3) Kontrola vstupu

Uživatel zadal **řádek** a **sloupec**, ale než jeho symbol umístíme na hrací plochu, je **potřeba zkontrolovat**, že:
1. **řádek a sloupec existuje** (např. že uživatel nechce dát symbol na padesátý řádek)
   2. řádek musí být 0, 1 nebo 2 
   3. sloupec musí být 0, 1 nebo 2 
4. **místo je volné**
   5. je potřeba zkontrolovat, jestli je na danném místě v tabulce mezera, protože jinak by došlo
      k přepsání symbolu
   6. to znamená zkontrolovat, že platí následující podmínka: `plocha[radek][sloupec] == ' '`

Pokud uživatel zadal neplatný řádek/sloupec, je potřeba ho nechat opravit se. Může se stát, že uživatel zadává
neplatná pole opakovaně, proto je potřeba **kontrolovat správnost ve while cyklu**.
Tedy: **DOKUD** je to špatně, zadávej znova.

Můžete to udělat tak, že si nejdříve načtete vstup (bez while cyklu) a následně
uděláte while cyklus, kde budete kontrolovat správnost. Pokud to uživatel zadal na první pokus správně,
tak se while cyklus ani jednou nespustí, což je v pořádku.

#### 4) Umístění symbolu

Umístění symbolu na hrací plochu je přímočaré.

```python
plocha[radek][sloupec] = symbol
```
Jenom pro ujasnění:
- `plocha` je seznam seznamů
- `plocha[radek]` je konkrétní seznam ze seznamu seznamů (řádek)
- `plocha[radek][sloupec]` je konkrétní sloupec z konkétního řádku
- `plocha[radek][sloupec] = symbol` je přepsání konkrétního sloupce v konkrétním řádku na `symbol`


#### 5) Kontrola vítěze/remízi

Na konci kola je potřeba **zkontrolovat stav hry** - je možné, že právě zahraným tahem hra skončila
a další kolo by již nemělo být zahájeno.

Možností jak vyhrát je v této verzi 8 (3 řádky + 3 sloupce + 2 diagonály).
Jeden ze způsobů jak zkontrolovat, jestli některý hráč vyhrál je udělat **8 podmínek**, 
kde postupně zkontrolujeme všechny varianty. 
Pro vítězný řádek/sloupec/diagonálu musí platit, že **symboly v něm jsou stejné a nejsou to mezery**. 

```python
# příklad kontroly vítězství v prvním řádku
if plocha[0][0] != ' ' and plocha[0][0] == plocha[0][1] and plocha[0][0] == plocha[0][2]:
    vitez = hrac_na_tahu
    # všechny symboly v prvním řádku jsou stejné a nejsou to mezery, takže vyhrál hráč, který právě zahrál tah
```

Pokud nikdo nevyhrál, je ještě potřeba zjistit, zdali **nenastala remíza**.
Opět je několik způsobů, např.:
- počítat si počet tahů a nahlásit remízu po devíti tazích
- vždy zkontrolovat, jestli na ploše zbývá alespoň jedna mezera

V případě detekce vítěze/remízi je potřeba patřičně nastavit hodnotu proměnné `vitez`,
aby se ukončil herní cyklus.

#### 6) Změna hráče

Každý cyklus představuje kolo jednoho hráče. Na konci cyklu je tedy potřeba hráče změnit,
aby se hráčí střídali (tzn. aby příští iteraci (kolo) cyklu hrál ten, co teď nehrál). 

Stačí **jednoduchá podmínka** - pokud je `symbol` roven hodnotě `"x"`, tak ho změníte na `"o"`, jinak na `"x"`.
Pokud používáte i další proměnné pro sledování hráče na tahu, musíte je změnit také. 
Princip je stejný - pokud byl na tahu _hráč 1_, změníte ho na _hráče 2_, a obráceně.

### Vyhodnocení hry

Po skončení **while** cyklu (herního cyklu) víme, že hra skončila - buď někdo vyhrál, nebo nastala remíza.
Pomocí **podmínky** a proměnné `vitez` už jen stačí zkontrolovat jaká z těchto situací nastala a vypsat to hráčům pomocí 
příkazu `print`.


## Těžká verze (NxN)

Těžká verze se od jednoduché liší tím, že si uživatel **může zvolit velikost herní plochy**.
V předchozí verzi měla herní plocha vždy 3 řádky a 3 sloupce, teď bude mít **N řádků** a **N sloupců**  - herní plocha tedy bude **vždy čtvercová**.
Uživatel si velikost plochy zvolí na začátku programu tím, že **zadá jedno číslo (N)**.

Princip hry zůstává stejný, ale v programu bude potřeba udělat mnoho změn. Zejména se musí předělat:
- příprava herní plochy 
- systém detekce vítěze/remízi


### Vytvoření herní plochy

TODO

```python
velikost_plochy = int(input("Zadej velikost hrací plochy: "))

plocha = []
for cislo_radku in range(velikost_plochy):
    radek = []
    for cislo_sloupce in range(velikost_plochy):
        radek.append(" ")
    plocha.append(radek)
```

### Vyhodnocení vítěze

TODO