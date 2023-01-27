**Kolize ve hře**
-
Máme ve hře nějaké objekty (zdi) a naším cílem je, aby se panáček, či cokoliv jiného, nemohl při pohybu do zdí "zabořit".
Prostě když se někam hýbe, nemůže to být směrem do zdi nebo do nějaké jiné překážky.

Co je potřeba udělat (v následujícím pořadí):
1. **Udělat funkci, která bude hýbat s postavičkou.** Když budeme chtít změnit pozici, nenapíšeme tedy jen např. `pozice_x += 3`, ale zavoláme funkci, která bude začínat nějak takto:
```python
def pohni(x, y, pozice_postavicka_x, pozice_postavicka_y):
    # tady bude nějaký kód (pohyb)
    
    
    return pozice_postavicka_x, pozice_postavicka_y
```
Tato funkce přijímá 4 parametry:
- `x` což je o kolik chci posunout postavičkou ve směru X (doprava/doleva)
- `y` to samé, ale směr y (nahoru/dolu)
- `pozice_postavicka_x` aktuální X pozice naší postavy 
- `pozice_postavicka_y` aktuální Y pozice naší postavy

Následně aktualizuje pozice (tento kód v ukázce není) a vrátí je pomocí `return pozice_postavicka_x, pozice_postavicka_y`.
Pokud bych chtěl postavou popojít o 10 doprava, použil bych funkci nějak takto:
```python
# zavolám funkci na aktualizaci pohybu, ta mi vrátí aktualizované souřadnice, které si hned uložím
pozice_postavicka_x, pozice_postavicka_y = pohni(10, 0, pozice_postavicka_x, pozice_postavicka_y)
```
2. Všude v kódu, kde hýbu postavičkou, tak použít tuto novou funkci.
3. Zatím jsme sice trochu vylepšili náš kód, ale vůbec neřešili kolize. Je potřeba udělat funkci, která zkontroluje každou překážku a zjistí, jestli není s naší postavičkou v kolizi.
Musíme tedy udělat funkci, která přijímá následující parametry:
- `rect` nějaký pygame rect - tohle je ten výřez, který zabírá naše postavička na obrazovce, dá se získat např. takto: `postava_rect = postava.get_rect(topleft=(pozice_x_postava, pozice_postava))`
- `seznam_pozic` což bude seznam souřadnic, na kterých se nachází překážky (jejich levý horní roh)
- `velikost_objektu` což je velikost překážky - nestačí přece vědět, kde je levý horní roh, musíme vědět i její velikost. V tomto případě předpokládáme, že překážka má čtvercový tvar.

Funkce pak pomocí for cyklu zkontroluje, jestli jakákoliv překážka koliduje s naším objektem. Pokud ano, vrátí `True`, jinak vrátí `False`.
```python
def kolize_s_pozici_ze_seznamu(rect1, seznam_pozic, velikost_objektu):
    for pozice in seznam_pozic:
        rect_objektu = pygame.Rect(pozice[0], pozice[1], velikost_objektu, velikost_objektu)
        if rect1.colliderect(rect_objektu):
            return True
    return False
```
4. Teď tuto funkci musíme použít. Jak a kde? 