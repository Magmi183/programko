# Klient

Běžně používáme webové prohlížeče jako je `Google Chrome`, `Safari` či `Microsoft Edge`.
Webové prohlížeče odesílají požadavky na servery (to, kde jsou spuštěné aplikace jako je Flask atd.),
a zobrazují odpovědi (např. HTML) co od serveru dostanou.

Klient však nemusí být nutně jen webový prohlížeč, ale třeba i Python program.
Můžeme mít například webovou službu, která poskytuje informace o počasí (nebo třeba o pokémonech), kterou budeme chtít 
použít z našeho Python programu.

## API

V úlohách a následujícím textu se používá pojem **API**.
Představte si pod tím stránky, které jsou určeny primárně pro jiné programy. Slouží k tomu, aby dvě aplikace mohli komunikovat mezi sebou.

V našem kontextu webu to může vypadat následovně:
- Stránka může např. vracet HTML (to jsou ty klasické, co znáte) - **není API**.
- Stránka může vracet třeba i SLOVNÍK, který je pro běžného uživatele k ničemu, ale třeba Python program s tím zase může pracovat lépe, než s HTML.
**Takovým stránkám se říká API.**

Je to hodně zjednodušená definice API, ale pro naše účely stačí.


## requests

Velmi populární Python knihovna (`import requests`) pro webovou komunikaci.
Umožňuje nám z Pythonu jednodušše posílat požadavky na server, tak jako to dělá webový prohlížeč.

`requests` umožňuje odesílat různé typy požadavků, jako jsou GET, POST, PUT, DELETE atd., s minimální konfigurací.
Podporuje také pokročilé funkce, jako je zasílání hlaviček, cookies, a správa timeoutů.
Většinou věcí se zabývat vůbec nebudeme, pro teď nám vystačí základní metoda `GET`.

### Různé metody
Metody `GET` a `POST` jsou dva základní způsoby, jakými aplikace komunikují s webovými servery.
I když slouží k podobnému účelu - k výměně dat mezi klientem a serverem - mají mezi sebou klíčové rozdíly, které ovlivňují jejich použití v různých situacích.

#### GET

Pro teď nás bude zajímat hlavně metoda `GET`.
Metoda `GET` se obvykle používá pro získání dat ze serveru. Např. načtení webové stránky je většinou výsledek metody `GET`,
kterou posílá webový prohlížeč na server.

Je jednoduchá a rychlá, vhodná pro situace, kdy potřebujeme jen načíst informace bez toho, abychom na server něco odesílali.

```python
# Odeslání GET požadavku na PokeAPI pro získání informací o Pokémonovi Pikachu
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
```

#### POST

Metoda POST se používá, když chceme na server odeslat nějaká data, například formuláře.
Touto metodou se budeme více zabývat později.

## Převod Odpovědi serveru na Slovník v Pythonu

Při práci s webovými aplikacemi v Pythonu často získáváme odpovědi ve formě, kterou je třeba dále zpracovat, aby byly informace snadno použitelné v našem kódu.
Knihovna `requests` nabízí jednoduchý způsob, jak tyto odpovědi převést na strukturovanou formu, která je v Pythonu velmi dobře zpracovatelná – konkrétně na **slovník**.

### Krok 1: Odeslání Požadavku
Prvním krokem je odeslání požadavku na server pomocí knihovny requests.
Toto obvykle vypadá nějak takto:

```python
import requests

# Odeslání GET požadavku na PokeAPI pro získání informací o Pokémonovi Pikachu
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
```

### Krok 2: Převod Odpovědi na Slovník
Jakmile máme odpověď, můžeme ji převést na slovník pomocí metody `.json()`:

```python
data = response.json()
```

Tento krok automaticky zpracuje odpověď a převede ji na slovník, který je pak snadno přístupný a manipulovatelný v Pythonu.

### Přístup k Datům
Po převedení na slovník můžeme k jednotlivým prvkům přistupovat pomocí klíčů, stejně jako u jakéhokoli jiného slovníku v Pythonu:

```python
# Získání ID Pokémona Pikachu
pokemon_id = data['id']

# Zobrazení ID Pokémona
print(f'ID Pokémona Pikachu je: {pokemon_id}')
```

Tímto způsobem můžete snadno pracovat s daty získanými z webových serverů ve vašich Python aplikacích.
Tato metoda je základním kamenem pro vývoj aplikací, které interagují s různými webovými službami.




TODO: Ukázat a vysvětlit debugger, a že se hodí např. ke zorientování v datovém formátu.