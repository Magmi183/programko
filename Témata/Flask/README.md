# Flask

## Pojmy

vysvetlit tyto pojmy, stručně, obecně ale i v kontextu naší práce

1. Server
2. Webový prohlížeč
3. URL 


# Základy HTML

HTML (HyperText Markup Language) je jazyk, který se používá k vytváření webových stránek.
Pomocí různých "tagů" říkáme webovým stránkám jakou mají mít **strukturu**.
Design a vzhled té struktuře můžeme dodat pomocí stylů.

## Webový prohlížeč

Zjednodušeně řečeno, **webový prohlížeč** je aplikace, která umí zpracovávat a zobrazovat **.html** soubory.
Zkuste si jít na jakoukoliv stránku, kliknout někde pravým tlačítkem a vybrat možnost `Inspect Element`.
Uvidíte, z jakého kódu se stránka vygenerovala, a navíc se můžete kódem inspirovat (nebo si ho přivlastnit) při výrobě vlastních stránek.


## Tagy 

## `<html>`
Tento tag říká prohlížeči, že to, co vidí, je HTML dokument. Všechno, co patří na webovou stránku, by mělo být uvnitř tohoto tagu.

```html
<html>
  <!-- Sem přijde veškerý obsah stránky -->
</html>
```

## `<head>`

V hlavičce stránky (`<head>`) dáváme informace, které nejsou přímo vidět na stránce, ale jsou důležité, jako název stránky nebo odkazy na CSS styly.

```html
<head>
  <title>Název mé stránky</title>
</head>
```

## `<body>`
Vše, co chcete, aby bylo vidět na stránce, patří do těla stránky (`<body>`). Text, obrázky, tlačítka - to vše sem přijde.

```html
<body>
  <h1>Vítejte na mé portfolio stránce</h1>
  <p>Toto je ukázka paragrafu.</p>
</body>
```


## `<h1>, <h2>, <h3> ... <h6>`
Tyto tagy se používají pro nadpisy. `<h1>` je největší nadpis a `<h6>` je nejmenší.


```html
<h1>Tohle je velký nadpis</h1>
<h2>Tohle je trochu menší nadpis</h2>
```


## `<p>`
Tento tag se používá pro odstavce textu. Je to základní stavební prvek pro text na webových stránkách.

```html
<p>Tohle je odstavec textu, kde můžete psát vše, co chcete sdělit.</p>
```

## `<a>`
Tento tag se používá pro odkazy. Můžete pomocí něj odkázat na jinou stránku nebo na jiné místo na stejné stránce.

```html
<a href="http://www.example.com">Navštivte moji stránku</a>
```

## `<img>`
Pomocí tohoto tagu můžete vložit obrázek na svou stránku. Musíte specifikovat cestu k souboru obrázku.

```html
<img src="obrazek.jpg" alt="Popis obrázku">
```

## `<ul> a <ol>`
Tyto tagy se používají pro seznamy. `<ul>` je neuspořádaný seznam (s odrážkami), zatímco `<ol>` je uspořádaný seznam (s čísly).
```html
<ul>
  <li>První položka seznamu</li>
  <li>Druhá položka seznamu</li>
</ul>

<ol>
  <li>První položka uspořádaného seznamu</li>
  <li>Druhá položka uspořádaného seznamu</li>
</ol>
```

## Cesta

`/` = výchozí bod