# Flask

## Pojmy

#### Server
Server je počítač, na kterém běží vaše aplikace a který umožňuje ostatním počítačům se k němu připojit.
Může to být klidně váš počítač, pokud si ho správně nakonfigurujete.
Když spustíme Flask aplikaci na Replitu, Replit spustí aplikaci na nějakém svém počítači a my se k ní můžeme připojit pomocí nějakého odkazu.
To znamená, že na něj pošleme nějaký požadavek a ten počítač (server) nám něco odpoví, například nám pošle HTML soubor.

#### URL
Je to zápis adresy nebo lokace, kde se nachází nějaká věc. Prakticky je potřeba vědět hlavně to, že výchozí bod, tedy místo, kde začínáme, se obvykle označuje jako /.
Takto vypadá lokace konkrétního videa na platformě tiktok: 

```http request
https://www.tiktok.com/@toilet.fuq/video/7251398836789333290
```

Takto vypadá adresa složky Témata na mém počítači:
```http request
/Users/michaljanecek/Programs/programko/Témata
```

# Základy HTML

HTML (HyperText Markup Language) je jazyk, který se používá k vytváření webových stránek.
Pomocí různých "tagů" říkáme webovým stránkám jakou mají mít **strukturu**.
Design a vzhled té struktuře můžeme dodat pomocí stylů, pokud styly nepoužijeme, bude stránka úplně basic.


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

## Užitečné stránky

### CodePen

Skvělá stránka, na které je spousta designů a stránek.

https://codepen.io/

### ChatGPT nebo jiná AI

Na generování HTML/CSS je to naprosto ideální.
Většinou se nejedná o složité komplexní programování, ale spíše o nudnou práci a kreativitu, což AI klidně může udělat za nás!
