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