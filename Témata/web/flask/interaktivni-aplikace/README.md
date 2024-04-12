# Interaktivní webová aplikace

Interaktivní webovou aplikací v tomto kroužku myslíme takové webové stránky,
které umí posbírat data od uživatele do formuláře a po odeslání formuláře je zpracovat.

## GET vs POST

Existují 2 základní typy požadavků. Jsou to defakto 2 módy, jak se dá přistupovat ke konkrétní stránce.
Každá stránka si pak musí nastavit (např. pomocí IF a ELSE) co bude dělat, když ji přijde požadavek typu GET a co bude dělat,
když ji přijde požadavek typu POST.

1. **GET**
   - základní typ, se kterým jsme pracovali doteď
   - požadavkem prostě říkáme: _stránko, DEJ mi to, co mám zobrazit_
     - např. pošli mi HTML, které mám zobrazit

2. **POST**
   - na rozdíl od GET je uzpůsobený k tomu, abychom pomocí něj posílali nějaká data
   - požadavkem říkáme: _stránko, tady máš data, a na základě nich mi pošli to, co mám zobrazit_ 

### Jak udělat stránku, co umí odpovídat na GET i POST

Do `@app.route` přidáme i parametr `methods`, jehož hodnota bude seznam metod, které stránka má umět, např.:
`@app.route('/priklad', methods=['GET', 'POST'])`.

Uvnitř funkce se pak podíváme na hodnotu `request.method`, čímž zjistíme, jestli nám přišel GET nebo POST.
Pokud přišel POST, víme, že jsou to data z formuláře, takže si je můžeme vytáhnout pomocí `request.form.get('name')`,
kde `name` je jméno formulářové položky.


```python
@app.route('/priklad', methods=['GET', 'POST'])
def priklad():
    # Pokud je požadavek typu POST, znamená to, že uživatel poslal své odpovědi
    if request.method == 'POST':
        # Získáme data z formuláře
        jmeno = request.form.get('name')

        # Ukážeme data (nebo cokoliv jiného, můžeme to dále zpracovat atd.)
        return f"<h1>Ahoj {jmeno}e!</h1>"
    else:
        # Když metoda není POST (uživatel neodesílá žádná data), tak se jedná o GET,
        # pošleme mu tedy formulář, aby jej mohl vyplnit.
        return '''<form method="POST">
                    <label for="name">Jméno:</label>
                    <input type="text" id="name" name="name">
                    <button type="submit">Odeslat</button>
               </form>'''
```


## Jak to funguje

1. Uživatel si stránku otevře ve webovém prohlížeči.
    - webový prohlížeč pošle **GET** požadavek (to se děje automaticky)
2. Server obdrží GET požadavek a rozhodne se, co uživateli pošle nazpátek. 
    - jelikož dostal **GET** požadavek, tak uživateli pošle normální stránku 
    - v našem případě to bude stránka s formulářem, kam uživatel může vyplnit nějaké informace.
    - formulář taky obsahuje tlačítko typu **submit**
3. Uživatel vyplní formulář na stránce.
4. Uživatel zmáčkne tlačítko typu **submit**
   - tím dojde k poslání dat z formuláře na **server** pomocí **POST** požadavku
5. Server obdrží POST požadavek s daty z formuláře a rozhodne se, co uživateli pošle nazpátek.
   - v tomto případě dostal **POST** požadavek
   - proto se podívá na data (z formuláře), pak s nima něco může udělat, například nějaký výpočet,
     a vrátí uživateli typicky stránku s nějakým výsledkem


## Formulář (\<form\>)

Tento HTML element definuje samotný formulář a může obsahovat různé vstupní prvky (položky formuláře).

Atribut **action** určuje, kam se data po odeslání pošlou. Pokud je atribut vynechaný,
pak se data pošlou na stejnou stránku, na které je formulář.


Tento formulář odešle data jako součást **POST** požadavku na adresu `/registrace`.
```html
<form action="/registrace" method="post">
  <!-- Vstupní prvky formuláře zde -->
</form>
```

### Textové pole (\<input type="text"\>)
Slouží pro jednořádkový textový vstup.

```html
<label for="name">Jméno:</label>
<input type="text" id="name" name="user_name">
```

### Heslo (\<input type="password">)
Textové pole pro heslo, znaky jsou skryté.

```html
<label for="password">Heslo:</label>
<input type="password" id="password" name="password">
```

### Odesílací tlačítko (\<input type="submit"> nebo \<button type="submit">)
Tlačítko pro odeslání formuláře. Po kliknutí se vezmou data co jsou aktuálně ve formuláři a pošlou se na stránku specifikovanou ve formuláři (pokud není specifikovaná žádná, tak se pošlou na aktuální).

```html
<input type="submit" value="Odeslat">
<!-- nebo -->
<button type="submit">Odeslat</button>
```

### Radio tlačítka (\<input type="radio">)
Pro výběr **jedné** možnosti z více možností.

```html
<label><input type="radio" name="gender" value="male"> Muž</label>
<label><input type="radio" name="gender" value="female"> Žena</label>
```

### Zaškrtávací pole (\<input type="checkbox">)
Pro výběr **jedné nebo více** možností.

```html
<label><input type="checkbox" name="interest" value="coding"> Programování</label>
<label><input type="checkbox" name="interest" value="music"> Hudba</label>
```


### Rozbalovací seznam (\<select>)
Rozbalovací menu s možnostmi.

```html
<label for="country">Země:</label>
<select id="country" name="country">
  <option value="cz">Česká republika</option>
  <option value="sk">Slovensko</option>
</select>
```


### Textová oblast (\<textarea>)
Pro víceřádkový textový vstup.

```html
<label for="message">Zpráva:</label>
<textarea id="message" name="message" rows="4" cols="50"></textarea>
```

### Datum (\<input type="date">)
Pro výběr data.

```html
<label for="birthday">Datum narození:</label>
<input type="date" id="birthday" name="birthday">
```


### Email (\<input type="email">)
Textové pole s validací emailové adresy.

```html
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

### Číslo (\<input type="number">)
Textové pole pro číselné hodnoty.

```html
<label for="quantity">Množství:</label>
<input type="number" id="quantity" name="quantity" min="1" max="5">
```


## Přidání PARAMETRŮ do stránky


### Co už umíme: Vracet stránku, která má pořád stejný vzhled
Zatím umíme vrátit HTML soubor jako odpověď na požadavek. Pokud HTML soubor obsahuje formulář,
uživatel ho může vyplnit a odeslat, čímž se pošle POST požadavek. V takové situaci si umíme z požadavku vytáhnout data, která
uživatel vyplnil do formuláře a nějak je zpracovat. Následně umíme uživateli odeslat výsledek nebo novou HTML stránku.

### Co chceme: Upravovat vzhled stránky na základě parametrů

Ale co když chceme pouze upravit stávající stránku? Například **zobrazit výsledek vedle formuláře**.
Pokud máme třeba kalkulátor BMI, bylo by ideální, kdyby se po stisknutí tlačítka ODESLAT uživateli zobrazilo BMI na té stejné stránce,
třeba v nějakém předtím neviditelném políčku pod formulářem. Přesměrování uživatele na jinou stránku není ideální.

### Jak to udělat: Předáme stránce parametry

**Toho docílíme pomocí přidání parametrů do stránky.** Je to podobné jako u funkcí. Zkrátka můžeme vzhled stránky ovlivnit tím,
co jí pošleme za parametry. Může to být třeba jen jedno číslo, které stránka zobrazí, ale i celý seznam prvků.
Stránka následně **ovlivní svůj vzhled na základě parametrů, které dostala.**

K předání parametrů využijeme funkci `render_template`, kterou už známe, akorát
ji používáme jen s jedním parametem - název HTML souboru, který chceme zobrazit.

Pro předání parametrů stránce stačí ony parametry přidat i do `render_template`.

# Příklad

Uděláme stránku, kde uživatel může zadat **dvě čísla - OD a DO**.
Po vyplnění čísel a stisknutí tlačítka odeslat se uživateli zobrazí **náhodné číslo z danného rozsahu.**
Číslo se uživateli **zobrazí na stejné** stránce. 

## Část 1: Endpoint

Následující kód zobrazuje způsob, jakým stránku informujeme o stavu (čísle).
Všimněte si, že **vždy** nastavíme `number = None`. Ale, pokud je požadavek typu POST,
což znamená, že uživatel vyplnil formulář, tak se podíváme jaká čísla vyplnil a vygenerujeme náhodné číslo
a uložíme si ho do `number`.

V proměnné `number` tedy bude buď `None` (pokud byl požadavek typu GET), nebo
nějaké číslo (pokud byl požadavek typu POST).

Nakonec tuto hodnotu předáme stránce `cislo.html` následujícím způsobem, a výslednou stránku zobrazíme:
` return render_template('cislo.html', number=number)`

```python
@app.route('/nahodne-cislo', methods=['GET', 'POST'])
def random_number():
    number = None  # Není nastaveno, dokud uživatel neodešle formulář
    if request.method == 'POST':
        # Získáme data z formuláře
        od = int(request.form.get('od'))
        do = int(request.form.get('do'))  

        # Generujeme náhodné číslo v zadaném rozsahu
        number = random.randint(od, do)

    # zde je number buď None, nebo nějaké číslo
    return render_template('cislo.html', number=number)
```

## Část 2: HTML

Už víme, jak stránce předat parametr. Zbývá ještě upravit HTML tak, aby na parametr
umělo nějakým způsobem reagovat.

Na to se ve Flasku používá speciální jazyk - _Jinja2_ - který je však velmi podobný Pythonu.
Umožňuje nám například používat proměnné, podmínky a cykly přímo uvnitř HTML.

### Získání hodnoty parametru

Nejjednodušší způsob jak použít Jinja2 je pomocí `{{}}` závorek.
Díky nim se můžeme podívat na hodnotu parametru a ovlivnit tak např. text stránky.

Pokud například stránce předáme parametr `jmeno` (pomocí `render_template`), 
pak můžeme jeho hodnotu využít následovně:

```python
# kód, který předá parametr
return render_template('jmeno.html', jmeno="Marek")
```
A HTML využívající Jinja2:
```html
<!DOCTYPE html>
<html>
<p>Ahoj {{ jmeno }}!</p>
</body>
</html>
```

### Podmínky

Dalším způsobem jak použít _Jinja2_ jsou podmínky. Ty se píšou `{% ZDE %}`.
Příkladem využití je např. když máme stránku, která funguje ve dvou módech:
   1. Když jde uživatel poprvé na stránku (posílá GET požadavek).
   2. Když už uživatel na stránce něco vyplnil a odeslal formulář (přes POST požadavek).

Pomocí podmínky můžeme poznat v jakém "módu" jsme.

#### Příklad

V následujícím příkladě lze vidět,
že parametry se do `render_template` vkládají vždy, ale rozdíl je v tom, že pokud je
požadavek typu GET, tak jsou prázdné (mají hodnoty None nebo prázdné stringy). Oproti tomu,
pokud je požadavek typu POST, tak se do proměnných nahrajou data z formuláře.

```python
@app.route('/bmi', methods=['GET', 'POST'])
def bmi_calculator():
    height = ''
    weight = ''
    result = None
    if request.method == 'POST':
        height = request.form.get('height', '')
        weight = request.form.get('weight', '')
        if height and weight:
            bmi = float(weight) / (float(height) ** 2)
            result = round(bmi, 2)

    return render_template('bmi_form.html',
                           height=height,
                           weight=weight,
                           result=result)
```

Následující stránka pak používá podmínku, aby se rozhodla, jestli zobrazí i část s výsledkem.
To udělá jen tehdy, když nějaký výsledek vůbec má (to nastane v případě, že byl požadavek typu POST).
Všimněte si taky použití proměnných `height` a `weight`. Bez nich data z formuláře po odeslání zmizeli,
což by nebylo ideální.

```html
<body>
    <h1>BMI Kalkulátor</h1>
    <form method="post">
        Výška (m): <input type="text" name="height" value="{{ height }}"><br>
        Váha (kg): <input type="text" name="weight" value="{{ weight }}"><br>
        <input type="submit" value="Vypočítej BMI">
    </form>
    {% if result is not none %}
        <h3>Vaše BMI: {{ result }}</h3>
    {% endif %}
</body>
```

Alternativně lze rovnou přes podmínku zjistit, jestli odpovídáme na GET nebo POST požadavek, a to následovně: `    {% if request.method == 'POST' %}
`

**POZOR** - podmínku je potřeba "zavřít" kódem `{% endif %}`.
V klasickém Pythonu se používá odsazení, aby se poznalo, co do podmínky patří.
To zde nejde, proto se používá takovéto "manuální" uzavření. Cokoliv co je mezi
začátkem podmínky a `{% endif %}` tak patří do bloku co se dělá, jeli podmínka splněna.


### Cykly

Mechanismus je stejný jako u podmínek.
Rozdíl je v tom, že jako parametr předáme SEZNAM a pak v cyklu přidáváme prvky do HTML.

```python
votes = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
@app.route('/anketa', methods=['GET', 'POST'])
def anketa():
    if request.method == 'POST':
        option = request.form['option']
        if option in votes:
            votes[option] += 1

    return render_template('anketa.html', votes=votes)
```

```html
<!-- Sekce pro zobrazení výsledků -->
 {% if request.method == 'POST' %}
 <div id="results">
     <h2>Výsledky</h2>
     <ul>
     {% for option, count in votes.items() %}
         <li>Možnost {{ option }}: {{ count }} hlas(ů)</li>
     {% endfor %}
     </ul>
 </div>
 {% endif %}
```


