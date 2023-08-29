# Hunger Games

Hunger Games je knižní (i filmová) série, která pojednává o reality show na život a na smrt.
Stručně řečeno, do uzavřené arény je umístěno několik účastníků, jejichž cílem je **zůstat na živu jako poslední.**

Na podobném principu se zakládá i myšlenka naší **textové hry**.

## Arena

Základním objektem hry je `Arena`. 
V konstruktoru přijámá seznam účastníků a definuje šance na různé akce.

```python
    def __init__(self, ucastnici):
        self.ucastnici = ucastnici
        self.kolo = 1
        self.sance_na_utok = 40
        self.sance_na_odpocinek = 40
        self.sance_na_predmet = 20
```

Šance na různé akce se nedají parametrizovat, pokud bychom chtěli přidat nové akce či změnit pravděpodobnosti stávajících aniž bychom přepisovalu
zdrojový kód `Areny`, museli bychom udělat novou třídu, která z `Areny` dědí.

### Spuštění hry

Pro spuštění hry stačí vytvořit seznam účastníků a ten pak poslat do konstruktoru při vytváření nové instance `Areny` a odstartovat hru
zavoláním metody `start`, čímž se spustí herní cyklus.
Účastníci musí být instance třídy `Ucastnik` nebo instance jejího potomka (třídy, která dědí z `Ucastnik`).

V našem případě se hra spouští ze souboru `main.py`, kde jsou kromě následujícího kódu ještě `importy` potřebných tříd.
```python
# vytvoření seznamu účastníků
ucastnici = [Ucastnik("Maty", 10, 5, 7, 5), Ucastnik("Dan", 8, 4, 10, 5), Ucastnik("Dominik", 15, 4, 1, 5), Lukostrelec("Legolas", 10, 0, 8, 4)]


# vytvoření instance Areny
arena = Arena(ucastnici)

# vše je připravené - můžeme odstartovat herní cyklus
arena.start()
```

## Herní cyklus

Herní cyklus je realizován následovně:

```python
        while len(self.ucastnici) > 1:
            input("Stiskni ENTER pro další kolo\n")
            print("------------------------------------------------------------")
            print(f"Kolo {self.kolo}")

            # zamícháme pořadí účastníků
            random.shuffle(self.ucastnici)

            for ucastnik in self.ucastnici:

                if ucastnik.hp <= 0:
                    # tento účastník je mrtvý, zřejmě zemřel dříve v tomto kole a proto je ještě v listu
                    continue

                # každý účastník udělá náhodnou akci
                akce = self.vygeneruj_akci()
                self.vyhodnot_akci(akce, ucastnik)

            self.odstran_mrtve()
            self.zobraz_stav_areny()
            self.kolo += 1
```

Tedy **dokud** zbývá více než jeden účastník, hraje se dále. Pro spuštění **kola** je vyžadován input od uživatele,
aby hra neskončila během jedné vteřiny. Uživatel si tak může v klidu číst jak hra probíhá a pokračovat do dalšího kola až
když má všechno přečtené.

Jedno **kolo** (cyklus) se stává z následujících akcí:
1. **zamíchání** seznamu účastníku (pomocí funkce `random.shuffle`)
2. **vygenerování náhodné akce** pro každého účastníka (funkce `vygeneruj akci`)
3. **vyhodnocení akce**, tzn.:
   - _Útok_: účastník zaútočí na náhodný cíl, zranění se odvíjí podle hodnoty co vrátí metoda `generuj_utok`,
      každý účastník ji může mít udělanou jinak, např. lučištník dává větší poškození, pokud má _luk_
   - _Odpočinek_: účastník odpočívá, odpočinek je realizován metodou `odpocivej` 
   - _Předmět_: účastník nalezl náhodný předmět (vygenerován metodou arény `vygeneruj_predmet`), to znamená, že se mu přidá do inventáře,
     jestli ale předmět bude účastníkovi jakkoliv užitečný už závisí na konkrétním účastníkovi, např. _luk_ je k ničemu, nemá li ho lučištník
4. **Vyfiltrování zemřelých** ze seznamu účastníků (metoda `odstran_mrtve`)
5. **Zobrazení zbývajících účastníků** (metoda `zobraz_stav_areny`)
6. Pokračování do **dalšího kola**, případně **vyhlášení vítěze**

## Účastník

Třída `Ucastnik` je šablonou základního účastníka, který nemá žádnou speciální vlastnost.
Je dán následujícími parametry:
1. **Jméno** - pro účely výpisu, nemá vliv na herní mechaniku
2. **HP** - počet životů účastníka
3. **Síla** - ovlivňuje útok účastníka
4. **Obratnost** - ovlivňuje (snižuje) přijaté poškození

Účastník má dále **inventář**, což je seznam předmětů. Tato základní verze účastníka předměty nijak nevyužívá.

Třída `Ucastnik` má následující metody (jež jsou volány z třídy `Arena`):
- `odpocivej()`: Pokud účastník není na plném HP, přičte si jeden život.
- `generuj_utok()`: Vrátí útok účastníka, v tomto případě je roven síle (která byla zadaná při vytváření instance).
- `prijmi_poskozeni(poskozeni)`: Tato metoda má zpracovat poškození ve výši danné parametrem. Tzn. na účastníka někdo zaútočil
   a tato metoda má vyhodnotit jak útok dopadl. Účastník může náhodně poškození uhnout (šance se zvyšuje s obratností).
   Pokud k úhybu nedojde, účastník přijme poškození v plné výši. Metoda **vrací přijaté poškození.** To je proto,
   abychom v areně věděli, kolik poškození bylo účastníkovi reálně způsobeno a mohli jsme tuto informaci vypsat uživateli.
- `prijmi_predmet(predmet)`: Přidá předmět do inventáře účastníka. 


## Lukostrelec

Třída `Lukostrelec` je potomek třídy `Ucastnik` (dědí ze třídy `Ucastnik`).
**Přepisuje** metodu `generuj_utok`, jinak nic. To znamená, že se chová uplně stejné jako `Ucastnik`, až na generování útoku.

V případě `Lukostrelce` je totiž vygenerovaný útok ovlivněn přítomností předmětu typu `Luk` v inventáři. Pokud se v něm nějaký
`Luk` nachází, `Lukostrelec` udělá poškození rovné síle nejsilnějšího `Luku` jež vlastní. Pokud žádný `Luk` nevlastní,
 udělá poškození ve výši své síly (stejně jako obyčejný `Ucastnik`).

Díky tomu, že je `Lukostrelec` potomek třídy `Ucastnik`, tak její instance můžeme posílat do `Areny`. Jinými slovy - `Lukostrelec`
je taky `Ucastnik`!

TODO2023: Revize tohoto textu.

# Úlohy

TODO2023: 
- novy ucastnik, nove predmety, nova arena