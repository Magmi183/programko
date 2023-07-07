# Piškvorky

---

> Tento návod obsahuje některé užitečné tipy a postupy, kterých lze využít při programování piškvorek Pythonu.

## Jednoduchá verze (3x3)

V této části se budeme zabývat jednodušší verzí piškvorek, kde se hraje pouze na ploše **3x3**, hrací plánek bude mít tedy 3 řádky a 3 sloupce, celkem pouze 9 polí.

### Zadání

```text
HRA - PIŠKVORKY - Jednoduchá verze (3x3)

Naprogramuj jednoduché piškvorky na hrací ploše o velikosti 3x3, tedy celkem 9 polí.
Hráči se budou střídat. Pozici, na kterou chtějí umístit svůj symbol budou zadávat ve formátu souřadnic, tedy např.:
1 2 -> což znamená, že hráč si přeje umístit svůj symbol (křížek nebo kolečko) do druhého sloupce v prvním řádku.

Hraje se tak dlouho, dokud není znám vítěz, nebo dokud není remíza.
```


### Struktura programu

> Jak bude program vypadat? Jaké budou jeho jednotlivé části? Jaké kroky a v jakém pořadí je třeba udělat?

V této si stručně rozdělíme program na jednotlivé kroky/akce a nastíníme, jak je budeme implementovat. Detailnější popis si necháme na později.

1. **Příprava hry**
   - Nejdřív budeme muset připravit věci nutné pro hru, tedy například **hrací plochu**, určit který hráč je jako první na tahu atd.
   - Zkrátka potřebujeme si promyslet, jaké proměnné budeme k běhu programu potřebovat.
2. **Herní cyklus**
   - Dalším krokem bude udělat herní cyklus. Tomuto se také někdy říká herní smyčka.
   - Tento cyklus se bude opakovat tak dlouho, dokud nebude znám vítěz.
   - Jeden průchod tímto cyklem bude představovat tah hráče. Jeden cyklus bude hrát hráč 1 a příští cyklus zase hráč 2. Takto se budou střídat tak dlouho, dokud někdo nevyhraje nebo nebude remíza.
   - **Co bude v tomto herním cyklu? Jaké akce musíme vykonat v jednom tahu?**
     1. Zobrazíme herní plochu, aby hráč viděl, jaký je nyní stav hry.
     2. Zeptáme se hráče, kam chce zahrát svůj tah a načteme vstup.
     3. Zkontrolujeme, že zadal platné pole a umístíme jeho tah na naší herní plochu.
     4. Zkontrolujeme, jestli někdo nevyhrál, nebo jestli nenastala remíza.
     5. Na konci cyklu musíme změnit hráče, který je na tahu - jinak by příští cyklus hrál opět ten stejný hráč a jeho protivník by si jaksi nezahrál.

### Herní plocha

Jelikož předem známe velikost herní plochy, můžeme si ji vytvořit poměrně jednoduše. Nabízí se udělat seznam, ve kterém budou další seznamy. Zní to možná složitě, ale je to pro člověka nejintuitivnější způsob, jak herní plochu reprezentovat.
Zkrátka budeme mít seznam řádků, kde každý řádek bude další seznam - seznam sloupců. 

Mohlo by to vypadat nějak takto.
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
Nabízí se na to **while cyklus**, jaká bude jeho podmínka? Co třeba: **dokud není znám vítěz, hraje se dál**.

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




# TODO