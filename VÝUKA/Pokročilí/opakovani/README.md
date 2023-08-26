# Opakování

## Co byste měli znát

### Proměnné

- co je to proměnná
- typy proměnných (int, str, float, bool) a operace s nimi
  - jestli se dá sčítat string s číslem
  - jestli se dá násobit text
  - a tak dále - je důležíté mít povědomí o tom jak a proč se to chová zrovna takto
- funkce na **přetypování**
  - `str()`, `int()`
- mít povědomí o funkcích (vlastnostech) stringu jako jsou `startswith()`, `count()` a dalších metodách [stringu](https://www.w3schools.com/python/python_ref_string.asp).
- že `input()` vždy vrácí proměnnou typu `string` !

### Podmínky

- klíčová slova `if`, `else` a `elif`
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
