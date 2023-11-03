# Co je to OOP a proč ho používat

Většina programů, aplikací či počítačových her je nějakým způsobem zasazena do reálného světa. Často se jedná o systémy, které mají za úkol nám pomáhat v každodenním životě.
Je jasné, že tyto programy musejí nějakým způsobem umět **zpracovávat a uchovávat data o reálných objektech/věcech/osobách**.

Například:

1. **Bakaláři**
  - online žákovská knížka
  - uchovává informace o **žácích**, **rozvrzích**, **učitelích** a tak dále (jaké další objekty vás napadají?)

2. **Alza**
  - jeden z největších eshopů v Evropě
  - statisíce **produktů** různých typů
  - několik **objednávek** za minutu

3. **Fortnite**
  - různé **postavičky**
  - spousta **typů zbraní**
  - miliony **hráčů** z celého světa


**Tučně** zvýrazněná slova jsou všechno entity, které musí aplikace nějakým způsobem zpracovávat. Již víme jak uchovávat jednoduché typy struktur jako je text, různé druhy čísel či seznamy.
Jak ale efektivně a přehledně ukládat komplexnější věci?

Představte si, že programujete e-shop, který prodává různé PC (již postavené) a vaše aplikace je musí umět uchovávat. Každé PC má jinou specifikaci (různá kapacita disku,
různě velká RAM, jiné CPU...). Ukážeme si nějaké způsoby jak to udělat.

## Jak reprezentovat objekt

### Pomocí seznamu
Jedna z možných cest jak počítače reprezentovat je jako seznam vlastností.

```python
# jméno, CPU, grafika, RAM (velikost), SSD (kapacita), HDD (kapacita)
pocitac_1 = ["Alza Individual R7", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 32, 2000, 6000]
pocitac_2 = ["Computron i9 Beast", "Intel Core i9-12900K 5.2 GHz", "NVIDIA RTX 4080", 64, 2000, 8000]
pocitac_3 = ["HyperTech Fusion R5", "AMD Ryzen 5 7600 4.5 GHz", "NVIDIA RTX 4060", 16, 1000, 4000]
pocitac_4 = ["Alza Individual i7 Ultra", "Intel Core i7-12800 4.9 GHz", "Intel Iris Graphics", 32, 1500, 5000]
pocitac_5 = ["OmegaForce Z2", "AMD Ryzen Threadripper 3995WX", "NVIDIA RTX 4090", 128, 4000, 10000]
pocitac_6 = ["ByteMaster Silver", "Intel Core i5-12600 4.5 GHz", "AMD Radeon RX 6800", 16, 500, 3000]
```

Toto řešení má ale mnoho nevýhod:
  - jak si zapamatujeme, že například `pocitac_1[0]` je jméno počítače?
  - co když mají počítače rozdílný počet vlastností?
  - je to přehledné?

# Pomocí TŘÍDY

Třída je něco jako šablona, kterou si vyrobíme, abychom mohli reprezentovat svoje vlastní entity (objekty).
Třída musí mít nějaké jméno a vlastnosti, například třída Pes by mohla mít vlastnosti rasa, stáří, barva_psa atd.

Použití tříd si ukážeme pomocí vlastní třídy `Pocitac`. Aby nedošlo ke zmatení, hodí se před dalším pokračováním **seznámit se s termíny jako jsou HDD, SSD a RAM**,
stačí jen na základní úrovni - jaké funkce plní a jaký je jejich hlavní parametr (velikost).

Třída pro počítač, která si umí zapamatovat vlastnosti použité výše by mohla vypadat takto:

```python
class Pocitac:
    def __init__(self, jmeno, cpu, grafika, ram, ssd, hdd):
        self.jmeno = jmeno
        self.cpu = cpu
        self.grafika = grafika
        self.ram = ram
        self.ssd = ssd
        self.hdd = hdd

```

Uvnitř třídy je funkce `__init__`. Funkcím uvnitř tříd se říká **metody**. Jejich první parametr musí být vždy `self` (konkrétní objekt - vysvětlíme si).
Dalšémi parametry jsou informace, které potřebujeme znát, když vytváříme nový objekt. Uvnitř metody pak nastavíme vlastnosti počítače. Např. `self.jmeno = jmeno` znamená,
že jméno tohoto konkrétního počítače bude `jmeno` - hodnota, kterou jsme dostali v parametru. Každý počítač má své vlastní parametry.

## Instance

Konkrétní objekt (v našem případě počítač) vytvořený podle naší šablony se nazývá **instance**. Jak udělat novou instanci? 
Prostě napíšeme jméno třídy a do závorek konkrétní parametry - tím se automaticky zavolá metoda `__init__`. Té se taky někdy říká **konstruktor**,
protože slouží jen jednomu účelu - zkonstruování nového objektu. Výsledek si pak uložíme do proměnné.

```python
pocitac_1 = Pocitac("Alza Individual R7", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 32, 2000, 6000)
pocitac_2 = Pocitac("Computron i9 Beast", "Intel Core i9-12900K 5.2 GHz", "NVIDIA RTX 4080", 64, 2000, 8000)
pocitac_3 = Pocitac("HyperTech Fusion R5", "AMD Ryzen 5 7600 4.5 GHz", "NVIDIA RTX 4060", 16, 1000, 4000)
pocitac_4 = Pocitac("Alza Individual i7 Ultra", "Intel Core i7-12800 4.9 GHz", "Intel Iris Graphics", 32, 1500, 5000)
pocitac_5 = Pocitac("OmegaForce Z2", "AMD Ryzen Threadripper 3995WX", "NVIDIA RTX 4090", 128, 4000, 10000)
pocitac_6 = Pocitac("ByteMaster Silver", "Intel Core i5-12600 4.5 GHz", "AMD Radeon RX 6800", 16, 500, 3000)

```

### Konstruktor

Konstruktorem se nazývá metoda **`__init__`**. Pomocí ní si uživatel může parametrizovat vytvářenou instanci. Lze také 
**nastavit výchozí hodnoty** pro nějaké atributy (stejně jako u funkcí).

Například pokud máme třídu **Stul** a většina stolů,
které budeme vytvářet má 4 nohy, tak se hodí nastavit výchozí hodnotu na 4. To znamená, že když při vytváření nového stolu
nezadáme počet nohou, tak bude mít automaticky 4.

```python
class Stul:

    def __init__(self, nohy = 4):
        self.nohy = nohy

stul1 = Stul() # 4 nohy
stul2 = Stul() # 4 nohy
stul3 = Stul(6) # 6 nohou
```

### Přístup k atributům

Pro přístup ke konkrétním vlastnostem konkrétního počítače využijeme **tečkovou notaci**.

Na následujícím příkladu je vidět, jak tečková notace vypadá.
```python
print(f"Jméno prvního počítače je: {pocitac_1.jmeno}")
print(f"RAM druhého počítače je: {pocitac_2.ram}")
# ... k přístupu k hodnotě konkrétní vlastnosti nám stačí napsat jméno proměnné, tečku a jméno vlastnosti

# sečtení velikostí RAM všech počítačů (nevím z jakého důvodu, ale takto by se to dělalo :D)
celkova_velikost_ram = pocitac_1.ram + pocitac_2.ram + pocitac_3.ram + pocitac_4.ram + pocitac_5.ram + pocitac_6.ram
print(f"Počítače mají celkem: {celkova_velikost_ram} GB RAM paměti.")
```

## Přepsání atributů

Pokud chceme změnit nějakou vlastnost počítače, například **velikost ram**, opět použijeme tečkovou notaci, tentokrát ale s přiřazením.

```python
pocitac_1 = Pocitac("Alza Individual R7", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 32, 2000, 6000)
# změna RAM počítače z 32 na 64 GB
pocitac_1.ram = 64
```

## Metody

Jak již bylo řečeno výše, metody jsou funkce, které ale patří k nějaké konkrétní třídě. Dá se o nich přemýšlet jako o **schopnostech toho danného objektu.** 
Naše třída by například mohla mít metodu **popis**, kterou když zavoláme, tak **popíše ten konkrétní počítač, na kterém metodu použijeme**. Metoda není obyčejná funkce,
lze ji vždy použít jen na nějaké **konkrétní instanci** nějaké třídy. Do naší třídy přidáme metodu následovně:


```python
class Pocitac:
    def __init__(self, jmeno, cpu, grafika, ram, ssd, hdd):
        # ... inicializace ...

    def popis(self):
        print(f"Počítač {self.jmeno} má následující specifikace:")
        print(f"• CPU: {self.cpu}")
        print(f"• Grafická karta: {self.grafika}")
        print(f"• RAM: {self.ram} GB")
        print(f"• SSD kapacita: {self.ssd} GB")
        print(f"• HDD kapacita: {self.hdd} GB")

```

Nyní můžeme metodu použít. Vybereme si konkrétní počítač, na kterém metodu zavoláme. Následujícím příkladem vlastně říkáme: "Počítači číslo 4, použij svoji schopnost popsat se."

```python
pocitac_4.popis()
```
... tento kód bude mít následující výstup:
```text
Počítač Alza Individual i7 Ultra má následující specifikace:
• CPU: Intel Core i7-12800 4.9 GHz
• Grafická karta: Intel Iris Graphics
• RAM: 32 GB
• SSD kapacita: 1500 GB
• HDD kapacita: 5000 GB
```

## Přístup k atributům instance uvnitř metody (self)

Pokud přistupujeme k atributům třídy přes instanci, napíšeme její jméno a název atributu (jak jsme si ukazovali nahoře).
```python
pes_alik = Pes("alík") # INSTANCE třídy pes (tzn. konkrétní pes - Alík), uložená v proměnné s názvem pes_alik
print(pes_alik.jmeno) # získání JMÉNA konkrétního psa (toho, co je uložený v proměnné pes_alik)
pes_alik.jmeno = "Rex" # podobným způsobem můžeme také změnit hodnotu atributu nějaké instance
```

**Jak ale přistupovat k atributům uvnitř metod?** Musíme použít slovíčko **self**, které v tomto případě jakoby nahradí název instance.
Pokud totiž zavoláme nějakou metodu na nějaké instanci, pošle se instance do metody jako parametr **self**. Pokud k ní tedy chceme přistoupit,
musíme přistupovat přes proměnnou **self**. Viz následující příklad (čtěte komentáře):

```python
class Pes:

    def __init__(self, jmeno):
        self.jmeno = jmeno
        
    def predstav_se(self):
        # pro přístup ke jménu používáme self - to se vždy nahradí instancí, na které metodu voláme (např. pes_alik)
        print("Ahoj, já jsem: " + self.jmeno)

pes_alik = Pes("alík") # vytvoření instance třídy Pes

# zavoláním metody predstav_se() na instanci "pes_alik" dojde k předání této instance do metody přes parametr SELF
# pokud v metodě následně chceme přistupovat k atributům této konkrétní instance, uděláme tak přes self
pes_alik.predstav_se()

```

Pojďme si to shrnout krok za krokem:
1. Zavoláme `pes_alik.predstav_se()`
2. Tím se spustí `predstav_se(self)` kde `self` bude `pes_alik`
3. Uvnitř metody je řádek `print("Ahoj, já jsem: " + self.jmeno)`
   - ten vypíše jméno psa `pes_alik`, protože se díváme na `self.jmeno` a `self` je v tomto případě `pes_alik` 

### Co by se stalo, kdybychom nepoužili self?

V takovém případě by se jednalo o normální proměnnou (ne atribut patřící k instanci).


Např. Tato metoda by vůbec nefungovala (nastal by ERROR), jelikož se snažíme přečíst proměnnou `jmeno`, která neexistuje.
```python
class Pes:
    
    def predstav_se(self):
            print("Ahoj, já jsem: " + jmeno)

```

## Složitější příklad (použití metod)

Pojďme si nyní ukázat složitější a praktičtější možné využití metod. Naše třída nyní umí pro každý počítač zaznamenat kapacitu jednoho SSD a jednoho HDD.
Mnoho počítačů ale nemá jen jedno HDD (pevný disk) či SSD. Přesněji řečeno, počítač může ale nemusí mít obojí a SSD i HDD může mít několik.
Celková kapacita úložiště je pak zjednodušeně řečeno součtem kapacit všech disků.

Upravíme tedy naší třídu tak, že budeme předpokládat, že vlastnosti (atributy) `ssd` i `hdd` jsou **seznamy čísel**, ne jen jedno číslo. To znamená,
že např. `pocitac.hdd = [1000, 1000, 2000, 100]` by znamenalo, že počítač obsahuje 2 pevné disky (HDD) o velikosti 1000 GB, jeden disk o velikosti 2000 GB a poslední disk o velikosti 100 GB.
A `pocitac.ssd = []` zase znamená, že tento počítač nemá žádné SSD (a tedy asi všechno ukládá na pevné disky, neboli HDD).

#### Upravená třída a příklad použití

Do naší třídy tedy přidáme následující metody:
  - `zobraz_kapacitu(self)`, která přehledně zobrazí celkovou kapacitu počítače (HDD + SSD), i částečné kapacity dle druhu úložiště
  - `pridej_hdd(self, velikost)`, která do počítače (do seznamu pevných disků) přidá nový o velikosti `velikost`
  - `pridej_ssd(self, velikost)`, která do počítače (do seznamu SSD) přidá nový o velikosti `velikost`
  - `odeber_hdd(self, velikost)` a `odeber_ssd(self, velikost)`, které odeberou hdd, resp. ssd o danné velikosti ze seznamu 

```python
class Pocitac:
    
    # ... funkce __init__ (viz výše) ...

    # ... funkce na popis (viz výše) ...
    
    def zobraz_kapacitu(self):
        celkova_kapacita = sum(self.ssd) + sum(self.hdd)
        print(f"Celková kapacita úložiště počítače {self.jmeno} je {celkova_kapacita} GB:")
        print(f"• SSD kapacita: {sum(self.ssd)} GB")
        print(f"• HDD kapacita: {sum(self.hdd)} GB")
    
    def pridej_hdd(self, velikost):
        self.hdd.append(velikost)

    def pridej_ssd(self, velikost):
        self.ssd.append(velikost)

    def odeber_hdd(self, velikost):
        if velikost in self.hdd:
            self.hdd.remove(velikost)
        else:
            print(f"HDD o velikosti {velikost} GB nebyl nalezen.")

    def odeber_ssd(self, velikost):
        if velikost in self.ssd:
            self.ssd.remove(velikost)
        else:
            print(f"SSD o velikosti {velikost} GB nebyl nalezen.")
```

Pojďme nyní naše nové metody vyzkoušet. Uděláme novou instanci třídy `Pocitac`, která na začátku nebude mít žádné SSD ani HDD. Postupně budeme pomocí našich metod
přidávat a ubírat nové disky a nakonec použijeme metodu `zobraz_kapacitu(self)`, která nám přehledně vypíše aktuální stav úložiště.

```python
pocitac = Pocitac("King Comp", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 4, [], [])

pocitac.pridej_hdd(1000)
pocitac.pridej_hdd(1000)
pocitac.pridej_hdd(1000)

pocitac.pridej_ssd(500)
pocitac.pridej_ssd(2000)

pocitac.odeber_hdd(1000)

pocitac.zobraz_kapacitu()
```

Tento program vypíše následující:

```text
Celková kapacita úložiště počítače King Comp je 4500 GB:
• SSD kapacita: 2500 GB
• HDD kapacita: 2000 GB
```

Což odpovídá - program sečte kapacitu všech HDD = 1000 + 1000 a SSD = 2500, následně je vypíše a zobrazí i jejich součet.

### Úprava metody popis a implementace __str__

Naše stará metoda `popis` stále předpokládá, že vlastnosti `hdd` i `ssd` jsou jednočíselné. Musíme ji tedy upravit tak, aby hezky fungovala se seznamem čísel.

Pojďme se ale nejdřív zamyslet, k čemu vlastně metoda `popis` slouží - je to vlastně textová (string) reprezentace našeho objektu. 
Když jsme dříve chtěli na text převést třeba číslo, dělali jsme to pomocí příkazu `str(cislo)`. Co se stane, když zkusíme něco podobného s naší novou třídou?

```python
pocitac = Pocitac("King Comp", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 4, [], [])
print(str(pocitac))
```

Tento kód vypsal následující řádek: `<__main__.Pocitac object at 0x106c6b5b0>`. Pokud totiž naše třída neobsahuje implementaci metody `__str__`,
tak když ji chceme převést na string, její výchozí chování je takové, že oznámí o jaký objekt se jedná (_Pocitac_), v jakém souboru byla definována (___main___)
a na jakém místě v paměti (RAM) našeho počítače je uložena (_0x106c6b5b0_). Místo v paměti bude pochopitelně pokaždé někde jinde.

Pokud chceme, aby se naše třída uměla převést na string nějak lépe, stačí do ní doplnit metodu `__str__`, která bude vracet textovou reprezentaci našeho objektu.
V našem případě by mohla vypadat následovně:

```python
    def __str__(self):
        ssd_kapacity = ', '.join([str(velikost) for velikost in self.ssd])
        hdd_kapacity = ', '.join([str(velikost) for velikost in self.hdd])
        
        return (f"Počítač {self.jmeno}:\n"
                f"• CPU: {self.cpu}\n"
                f"• Grafická karta: {self.grafika}\n"
                f"• RAM: {self.ram} GB\n"
                f"• SSD kapacity: {ssd_kapacity} GB\n"
                f"• HDD kapacity: {hdd_kapacity} GB")
```

Když zavoláme `print(str(pocitac))`, tak se do konzole vypíše následující text:
```text
Počítač King Comp:
• CPU: AMD Ryzen 7 7800X3D 5 GHz
• Grafická karta: AMD Radeon Graphics
• RAM: 4 GB
• SSD kapacity: 500, 2000 GB
• HDD kapacity: 1000, 1000 GB
```
Což už je celkem hezká textová reprezentace našeho počítače. Všimněte si, že metoda `__str__` sama nic nevypisuje, pouze vrací pomocí `return` výsledný text,
se kterým si pak můžeme dělat co chceme. Kdybychom chtěli metodu, která text rovnou vypíše, mohli bychom ji udělat následovně:

```python
def popis(self):
    print(str(self))
```

Pokud tuto metodu použijeme způsobem `pocitac.popis()`, výsledek bude stejný jako u `print(str(pocitac))`.
Pojďme si rozebrat, co se stane na řádku `pocitac.popis()`:
  1. **Zavolá se metoda popis na konkrétním počítači** (`pocitac`), což znamená, že `self` parametr metody `popis(self)` bude mít hodnotu `pocitac`.
  2. Uvnitř metody se pak zavolá `str(self)`, kde `self` (jak jsme řekli v kroku 1) je náš konkrétní `pocitac`. Proto tento příkaz dopadne stejně jako bychom
     zavolali rovnou `str(pocitac)` mimo tělo metody.
  3. Jelikož naše třída implementuje metodu `__str__`, tak `str(self)` vrátí textový řetězec (string) podle toho jak jsme naprogramovali metodu `__str__` - 
     tedy řetězec obsahující všechny známé informaci o danném PC a to v hezkém odrážkovém formátu.
  4. Výsledek (řetězec vrácený metodou `__str__`, která byla zavolána příkazem `str(self)`) se vypíše pomocí příkazu `print`. 


## Dědičnost

Na vysvětlení dědičnosti použijeme tyto skvělé materiály: https://naucse.python.cz/course/pyladies/beginners/inheritance/

1. Udělejte si dle předlohy třídy `Kotatko` a `Stenatko`.
2. Udělejte třídu `Zviratko`
3. Předělejte dle předlohy třídy `Kotatko` a `Stenatko` tak, aby dědily ze třídy `Zviratko`
4. **Samostatná práce:**
   - přidejte alespoň jednu novou metodu do `Zviratko`
     - musí to být něco, co umí všechny zvířata
   - přidejte alespoň jeden nový druh zvířete
   - přepište vaši novou metodu v každé podtřídě `Zviratko` (inspirujte se metodou `sněz`)