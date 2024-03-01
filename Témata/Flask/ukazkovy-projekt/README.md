# Ukázkový projekt

Tento projekt obsahuje ukázky a vysvětlení základních principů kombinace Flasku, HTML a CSS.

## main.py

Tento soubor nastartuje celou aplikaci. Je to normální Python soubor, kde ale používáme Flask - 
`from Flask import Flask`. V tomto souboru definujeme jaké stránky bude náš server mít.

### Přidání nové stránky

Novou stránku přidáme následovně:
1. Vytvoříme funkci v souboru `main.py`.
   - tato funkce bude vracet (`return`) obsah stránky
   - může to být buď jednoduchý string, číslo nebo třeba **html soubor**
2. Přidáme nad funkci kód `@app.route('/')`
   - říká se tomu _dekorátor_, je to něco, co přidává nějaké funkci další vlastnosti, v tomto případě
     dekorátor označí jaká funkce se má volat, když uživatel navštíví určitou stránku (cestu)
   - místo `/` můžeme doplnit jakoukoliv cestu, např. `/kontakty`

#### Přidání stránky co vrací text

```python
@app.route("/nahodny-cislo")
def nahodny_cislo():
  nahodny = random.randrange(10)

  return "Tvoje dnešní číslo je: " + str(nahodny)
```

#### Přidání stránky co vrací HTML

Všechny **html** soubory dáváme do složky `templates`.
Pokud pak chceme nějaký zobrazit, uděláme to následovně: 
```python
@app.route("/ukazka")
def ukazkove_html():

  return render_template("ukazka.html")
```

Tento kód zajistí to, že když uživatel půjde na stránku `/ukazka`, tak se mu zobrazí soubor `ukazka.html` ze složky `templates`.

#### Přidání stránky s parametry

Při použití <> v cestě Flask aplikace můžete definovat proměnné části URL. Tyto proměnné se poté předají do funkce, která je spojena s danou cestou. V našem případě jsme definovali cestu /soucet/<cislo1>/<cislo2>, kde <cislo1> a <cislo2> jsou proměnné části, které budou sloužit jako vstupní parametry pro naši funkci.

Uživatel zavolá tuto službu tím, že ve svém prohlížeči zadá URL adresu, která odpovídá definované cestě, a nahradí `<cislo1>` a `<cislo2>` skutečnými hodnotami, které chce sečíst. Například, pokud uživatel zadá URL `http://[adresa-serveru]/soucet/5/3`, cesta bude odpovídat naší definované cestě a proměnné `cislo1` a `cislo2` budou mít hodnoty `5` a `3`.

Všimněte si, že názvy parametrů ve funkci musí odpovídat názvům v cestě. Proměnné `cislo1` a `cislo2` budou předány jako řetězce (stringy), takže je potřeba je převést na číselný typ (např. int), aby bylo možné provést sčítání. Výsledek poté vrátíme jako string.

```python
@app.route('/soucet/<cislo1>/<cislo2>')
def soucet(cislo1, cislo2):
    vysledek = int(cislo1) + int(cislo2)  # Převod na int a sčítání
    return f'Výsledek součtu {cislo1} a {cislo2} je {vysledek}.'
```


### Přidání stylu

HTML stránka se dá zkrášlit přidáním stylů. Ty se definují v souborech s příponou `.css`, a musí být ve složce
`static`. Pokud máme např. soubor `styl.css`, můžeme ho do `HTML` přidat přidáním tohoto řádku:
```html
    <link rel="stylesheet" type="text/css" href="static/styl.css">
```
Řádek se musí přidat do `head` části souboru, výsledek tedy bude vypadat zhruba následovně:
```html
<head>
    <link rel="stylesheet" type="text/css" href="static/styl.css">
    <title>Ukázková stránka</title>
</head>
```