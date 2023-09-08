# Opakování

## Co byste měli znát

### Proměnné

- co je to proměnná
- typy proměnných (int, str, float, bool) a operace s nimi
  - jestli se dá sčítat string s číslem
  - jestli se dá násobit text
  - a tak dále - je důležité mít povědomí o tom jak a proč se to chová zrovna takto
- funkce na **přetypování**
  - `str()`, `int()`
- mít povědomí o funkcích (vlastnostech) stringu jako jsou `startswith()`, `count()` a dalších metodách [stringu](https://www.w3schools.com/python/python_ref_string.asp).
- že `input()` vždy vrácí proměnnou typu `string` !

### Podmínky

- klíčová slova `if`, `else` a `elif`¨
- že se podmínky vyhodnocují postupně a pokud je jedna splněna, tak se další `elify` už vůbec nekontrolují
- jak fungují operátory `or` a `and`, a jak fungují závorky
  - Kontrolní otázky:
    - jak dopadne výraz `(True and False) or 8 == 8` ?
    - jak dopadne výraz `4 == 4 and (5 == "pět" or True)`
- že se dají podmínky libovolně vnořovat
- operátory **==**, **!=**, **<=** a **>=**
- co je to **blok kódu**

### While cyklus

- stejné jako `if`, **ale** blok kódu se neudělá jen jednou, ale tak dlouho, **DOKUD** je podmínka splněná
- že se často používá, když chceme, aby program běžel donekonečná
  - například **herní cyklus**
- je potřebné dát si pozor, aby se program **nezacyklil**


### FOR cyklus

- co je to **sekvence**
  - string, seznam, range
- jak se používá funkce `range()`
- co dělá funkce `len()`
- jak funguje **for** cyklus a jak se liší oproti `while` cyklu


### Seznam

- jak se vytváří seznam (_hranaté_ závorky)
- procházení seznamu pomocí **while** cyklu vs. **for**  cyklu
  - kdy se hodí jaký způsob?
- že je to **sekvence**
- jak se dá zjistit délku seznamu (příkaz `len`)
- **přidání/odebrání** položky a [další metody](https://www.w3schools.com/python/python_ref_list.asp)
  - stačí mít povědomí o tom, jaké metody existují
  - `sort`, `reverse`, `clear` ...


### Slovník

- jak se vytváří slovník (_chlupaté_ závorky)
- co je to **klíč** a co **hodnota**
- jaký je rozdíl oproti **seznamu**
- jak vložit/přepsat hodnotu ve slovníku + jak smazat hodnotu
- jak se dá procházet slovník (v cyklu)
  - pouze klíče, pouze hodnoty, obojí
- uvést příklady, kdy se více hodí slovník než seznam

### Funkce

- jak se definuje nová funkce
- co je to **návratová hodnota** (`return`)
- co jsou to **parametry**
- k čemu se funkce používají a proč jsou užitečné