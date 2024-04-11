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

