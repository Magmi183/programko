# Úvod do funkcí 🚀

## Funkce bez parametrů

Když chceme používat stejný kus kódu na více místech, můžeme ho "zabalit" a udělat z něj **funkci**.
Tu pak můžeme opakovaně používat, aniž bychom museli kód psát znovu a tím jej duplikovat. 
To nám ušetří spoustu práce a udrží náš kód čistý a přehledný.

### Příklad

Představme si, že chceme vypsat malou násobilku čísla 8. Může to být pro účely třeba nějakého matematického vzdělávacího programu.

```python
# Program, který vypíše malou násobilku čísla 8
# pro přehlednost pak ještě oddělí čárou
cislo = 8
for i in range(11):
    print(f"{i} * {cislo} = {cislo * i}")
print("------------------------------------------------------------------")


# ... a teď nějaký další, random kód ...
print("Tak to byla ta násobilka.")
print("Chceš ji vidět znovu?")
print("OK...")
# ... teď, když ji chceme vytisknout znovu, musíme opsat ten kód


cislo = 8
for i in range(11):
    print(f"{i} * {cislo} = {cislo * i}")
print("------------------------------------------------------------------")
```

Je vidět, že pokud chceme násobilku vypsat znovu, máme problém - musíme totiž kód zduplikovat.
Navíc je tu další problém - co když si to rozmyslíme, a budeme chtít násobilku jiného čísla? Nebo co když budeme chtít změnit jak se násobilka vypisuje?
Nezbyde nám nic jiného, než kód změnit na obou místech. To zvětšuje pravděpodobnost, že uděláme chybu. To je ošklivé.

**Řešením je kód zabalit do funkce.**
K tomu použijeme slovíčko `def`, vymyslíme si název funkce, a kód který do funkce patří označíme odsazením, podobně jako třeba u podmínky.
```python
def ukaz_nasobilku_8():
    cislo = 8
    for i in range(11):
        print(f"{i} * {cislo} = {cislo * i}")
    print("------------------------------------------------------------------")
```

Toto pouze vytvoří funkci, pokud ji chceme použít, **musíme ji zavolat.** To se dělá následovně:
```python
ukaz_nasobilku_8() # zavolám poprvé
ukaz_nasobilku_8() # klidně můžu znovu ...
```

## Funkce s parametrem

Většinou nechceme, aby funkce vždy dělala úplně to stejné, ale aby se kód třeba jen trochu lišil. Například chceme funkci,
která umí kreslit čtverec, ale chceme si umět vybrat barvu. Je nesmysl pro každou barvu dělat novou funkci, to bychom si moc nepomohli a kód by byl ještě ošklivější.

V příkladu s násobilkou jsme na tom podobně, chceme mít funkci, která umí vypsat násobilku, ale nechceme se limitovat na konkrétní číslo.
Proto do funkce přidáme **parametr**, kterým funkci můžeme ovlivnit.

```python
def ukaz_nasobilku(cislo):
    for i in range(11):
        print(f"{i} * {cislo} = {cislo * i}")
    print("------------------------------------------------------------------")
```

Takže, jak jsme si ukázali, přidáním parametru `cislo` do definice funkce `ukaz_nasobilku`, jsme funkci výrazně rozšířili její použitelnost.
Teď můžeme tuto funkci použít k vypsání násobilky libovolného čísla, které jako argument (hodnotu parametru) předáme:

```python
ukaz_nasobilku(10)  # Zavolá funkci a vypíše násobilku čísla 10
ukaz_nasobilku(5)   # Zavolá funkci a vypíše násobilku čísla 5
```

### Jak to funguje?

Když voláme funkci `ukaz_nasobilku` s konkrétním číslem, toto číslo se předá do funkce jako hodnota parametru `cislo`. Ve funkci pak tento parametr použijeme k dynamickému generování výstupu - v našem případě násobilky zadaného čísla.

### Proč je to užitečné?

Díky parametrům můžeme psát kód, který je mnohem flexibilnější a lépe znovupoužitelný. Nemusíme psát novou funkci pro každou drobnou variaci úlohy; místo toho můžeme jednu funkci přizpůsobit různým situacím prostřednictvím parametrů.

### Další příklad: Funkce na pozdrav

Ukážeme si to na dalším jednoduchém příkladu. Můžeme mít funkci `pozdrav`, která jako parametr přijímá jméno osoby a podle toho ji pozdraví:

```python
def pozdrav(jmeno):
    print("Ahoj " + jmeno + ", jak se máš?")
```

A pak můžeme funkci volat s různými jmény:

```python
pozdrav("Pavel")  # Vypíše: Ahoj Pavel, jak se máš?
pozdrav("Lucie")  # Vypíše: Ahoj Lucie, jak se máš?
```

## Funkce s více parametry

Někdy potřebujeme, aby naše funkce mohla zpracovat více různých vstupů, aby byla ještě flexibilnější. Toho dosáhneme přidáním **více parametrů** do definice funkce.

### Příklad

```python
def pozdrav(jmeno, formalita):
    if formalita:
        print("Dobrý den, " + jmeno + ". Jak se máte?")
    else:
        print("Ahoj " + jmeno + "! Jak to jde?")
```

Když funkci voláme, můžeme jí předat jak jméno, tak i boolean (True/False) hodnotu, která určí, jestli chceme být formální, nebo neformální:

```python
pozdrav("Jakub", True)  # Formalni pozdrav
pozdrav("Tereza", False)  # Neformalni pozdrav
```

### Význam pořadí parametrů
Je důležité si uvědomit, že při volání funkce s více parametry je třeba dodržet pořadí, ve kterém jsou parametry definovány.
Například v naší funkci pozdrav, jméno musí přijít jako první argument a formalita jako druhý.

### Pojmenované argumenty

Pro zvýšení čitelnosti a flexibilitě můžeme při volání funkce použít pojmenované argumenty:

```python
pozdrav(jmeno="Emma", formalita=True)
pozdrav(formalita=False, jmeno="Oliver")
```

### Výchozí hodnoty parametrů

Můžeme definovat funkce s výchozími hodnotami pro některé parametry, což nám umožní volat funkci i bez explicitního zadání všech argumentů:

```python
# pokud uživatel nezadá úroveň formality, automaticky se nastaví na "False"
def pozdrav(jmeno, formalita=False):
    if formalita:
        print("Dobrý den, " + jmeno + ". Jak se máte?")
    else:
        print("Ahoj " + jmeno + "! Jak to jde?")

pozdrav("Lucas")  # Implicitně neformální, protože formalita má výchozí hodnotu False
pozdrav("Eva", True)  # Explicitně formální
```

## Návratová hodnota

Materiály najdeš v souboru: [funkce_navratova_hodnota.py](funkce_navratova_hodnota.py)

