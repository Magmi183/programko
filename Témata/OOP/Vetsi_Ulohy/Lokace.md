TODO 2023: meh, kontrola a doplnit nejak ten program (prochazeni lokacema)

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

## Vytvoření Instance

Nová instance se vytváří následovně:

```python
cesko = Lokace("Česká republika", "Zemský ráj to na pohled", nemecko, slovensko, rakousko, None)
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
