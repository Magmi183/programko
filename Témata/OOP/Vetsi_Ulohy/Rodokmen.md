# Rodokmen

Cílem této úlohy je vytvořit třídu `Clovek`, která slouží k modelování rodokmenu.
Každý člověk v rodokmenu má jméno, pohlaví a odkaz na rodiče. Pokud není rodič znám, hodnota je `None`.

## Atributy

| Atribut          | Datový typ  | Popis                                                                                  |
|------------------|-------------|----------------------------------------------------------------------------------------|
| `jmeno`          | `str`       | Jméno člověka.                                                                         |
| `pohlavi`        | `str`       | Pohlaví člověka ("muž" nebo "žena").                                                   |
| `otec`           | `Clovek`    | Odkaz na objekt, který reprezentuje otce.                                              |
| `matka`          | `Clovek`    | Odkaz na objekt, který reprezentuje matku.                                             |

## Vytvoření Instance

Nová instance se vytváří následovně:

```python
jan = Clovek("Jan", "muž", None, None)
```

## Metody

### `nastav_otce(otec: Clovek)`

Nastaví otce daného člověka.

### `nastav_matku(matka: Clovek)`

Nastaví matku daného člověka.

### `vypis_potomky()`

**Rekurzivní metoda,** která vypíše všechny známé potomky danného člověka.


### `vypis_predky()`

**Rekurzivní metoda,** která vypíše všechny známé předky danného člověka.

## Příklad použití

```python
ondrej = Clovek("Jan", "muž", None, None)
marie = Clovek("Marie", "žena", None, None)
jan = Clovek("Jan", "muž", None, marie)

jan.nastav_otce(ondrej)
jan.vypis_predky()
```

## Testování

Poté co třídu naprogramujete, můžete program vyzkoušet s následujícími daty, abyste nemuseli zdlouhavě psát svůj vlastní nebo smyšlený rodokmen.

**Britská královská rodina (ChatGPT):**

```python
# Definice třídy Clovek
class Clovek:
    def __init__(self, jmeno, pohlavi, otec, matka):
        self.jmeno = jmeno
        # váš kód
        # váš kód
        # váš kód
        
# Zjednodušený rodokmen britské královské rodiny
kralovna_viktorie = Clovek("Královna Viktorie", "žena", None, None)
princ_albert = Clovek("Princ Albert", "muž", None, None)

edward_vii = Clovek("Edward VII", "muž", kralovna_viktorie, princ_albert)
alexandra = Clovek("Alexandra", "žena", None, None)

george_v = Clovek("George V", "muž", edward_vii, alexandra)
mary = Clovek("Mary", "žena", None, None)

george_vi = Clovek("George VI", "muž", george_v, mary)
elizabeth_bowes_lyon = Clovek("Elizabeth Bowes-Lyon", "žena", None, None)

elizabeth_ii = Clovek("Elizabeth II", "žena", george_vi, elizabeth_bowes_lyon)
prince_philip = Clovek("Prince Philip", "muž", None, None)

charles = Clovek("Charles", "muž", elizabeth_ii, prince_philip)
diana = Clovek("Diana", "žena", None, None)

william = Clovek("William", "muž", charles, diana)
catherine = Clovek("Catherine", "žena", None, None)

harry = Clovek("Harry", "muž", charles, diana)
meghan = Clovek("Meghan", "žena", None, None)

# Děti Williama a Catherine
george = Clovek("George", "muž", william, catherine)
charlotte = Clovek("Charlotte", "žena", william, catherine)
louis = Clovek("Louis", "muž", william, catherine)

# Děti Harryho a Meghan
archie = Clovek("Archie", "muž", harry, meghan)
lilibet = Clovek("Lilibet", "žena", harry, meghan)

```