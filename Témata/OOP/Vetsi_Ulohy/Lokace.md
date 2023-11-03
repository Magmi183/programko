# Velká Úloha: LOKACE

Cílem této úlohy je vytvořit třídu `Lokace`, která slouží k modelování geografických lokací a jejich vzájemných vztahů.

## Atributy

| Atribut          | Datový typ | Popis                                                                                         |
|------------------|------------|-----------------------------------------------------------------------------------------------|
| `jmeno`          | `str`      | Jméno lokace. Například: "Česká republika".                                                    |
| `popis`          | `str`      | Stručný popis lokace. Například: "Zemský ráj to na pohled".                                    |
| `lokace_sever`   | `Lokace`   | Odkaz na lokaci, která se nachází severně od aktuální lokace.                                 |
| `lokace_jih`     | `Lokace`   | Odkaz na lokaci, která se nachází jižně od aktuální lokace.                                   |
| `lokace_zapad`   | `Lokace`   | Odkaz na lokaci, která se nachází západně od aktuální lokace.                                 |
| `lokace_vychod`  | `Lokace`   | Odkaz na lokaci, která se nachází východně od aktuální lokace.                                |

**Výchozí hodnoty atributů lokace jsou None**, uživatel je tedy nemusí zadávat.

## Vytvoření Instancí (příklad)

Nové instance se vytváří následovně:

```python
nemecko = Lokace("Německo", "Země aut a piva") # lokace nenastaveny, budou None
slovensko = Lokace("Slovensko", "Tatry a Dunaj")
rakousko = Lokace("Rakousko", "Alpy a vídeňský štrúdl")
# u Česka nastavíme všechny lokace kromě východu (bude None)
cesko = Lokace("Česká republika", "Zemský ráj to na pohled", lokace_sever=nemecko, lokace_jih=slovensko, lokace_zapad=rakousko)
```

## Metody

### `nastav_lokaci_sever(lokace: Lokace)`

Nastaví lokaci na severní světové straně podle hodnoty parametru.

### `nastav_lokaci_jih(lokace: Lokace)`

Nastaví lokaci na jižní světové straně podle hodnoty parametru.

### `nastav_lokaci_zapad(lokace: Lokace)`

Nastaví lokaci na západní světové straně podle hodnoty parametru.

### `nastav_lokaci_vychod(lokace: Lokace)`

Nastaví lokaci na východní světové straně podle hodnoty parametru.

## Příklad použití

V následujícím příkladu doplňujeme východní lokaci pro Českou republiku:

```python
cesko.nastav_lokaci_vychod(polsko)
```

## Rozšíření

Pokud už máte třídu `Lokace` hotovou, otestujte ji spuštěním souboru `lokace.py`. Pokud funguje, zamyslete se, jak ji rozšířit.

### Nápady pro inspiraci:

Vyberte si některou z následujích možností a realizujte ji nebo se jimi inspirujte a udělejte cokoliv jiného.

1. Vymyslete jednoduché RPG, jehož základní mechanika je chození po `Lokacích`
   - nejdřív vymyslete, co byste chtěli udělat, pak prodiskutujeme jak (všechno jde)
   - cílem může být navštívit všechny lokace a neumřít (charakter může mít životy)
2. Udělejte podtřídy `Lokace`, kde každá bude mít nějaké své unikátní metody, např.:
    - `Stat` - lokace představující stát, může mít atributy jako `pocet_obyvatel` či metodu `zjisti_pocasi()`
    - `Mesto` - lokace představující stát, může mít atribut `stat` - stát kde se nachází
3. Přidávání `Lokací`
    - dejte uživateli možnost přidat novou `Lokaci` ke stávající 
    - umožněte odstranit `Lokaci`