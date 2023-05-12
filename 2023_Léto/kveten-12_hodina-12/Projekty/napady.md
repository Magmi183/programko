# Hodina 12.
_12. května 2023_

## Plán

Slovník, rekurze, opakování formou projektu.
- Výběr/vymyšlení vlastního projektu a práce na něm.


### Nápady pro inspiraci:

#### TODO List

Úkolem je udělat program, který bude sloužit jako TODO list, tedy seznam věcí, které je potřeba udělat.
Aplikace musí obsahovat minimálně tyto funkce:
- přidat novou položku do TODO listu
- odebrat položku z TODO listu
- možnost vypsat celý TODO list
- uložit TODO list do souboru (aby uživatel nepřišel o data po skončení aplikace)
- načíst TODO list ze souboru


#### Textová hra

Vymysli si textové RPG a naprogramuj ho. Téma hry může být například uniknutí z Escape Roomu. Uživatel začíná v jedné z místností a jeho cílem je uniknout.
V každé místnosti má k dispozici nějaké akce, předměty a volbu, kam může jít dál. Hráč může mít inventář, životy, či jiné suroviny.
V místnostech se mohou nacházet různé úkoly/pasti, které hráč musí překonat.


#### Šibenice

Úkolem je naprogramovat hru šibenice (Hangman).

      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
     |___

Počítač si myslí nějaké slovo a uživatel vidí jen kolik to slovo má písmen. Uživatel postupně hádá písmena. Pokud se písmeno ve slově nachází,
tak se příslušná písmena ve slově odkryjí. Pokud ne, tak ztrácí život. Uživatel má také možnost kdykoliv tipnout si celou tajenku, ale pokud tipne špatně, rovněž ztratí život.

Bonusové funkce:
- možnost uložit/načíst hru
- zobrazování šibenice (např. jeden řádek šibenice za každý ztracený život)


#### Hledání cesty v bludišti

Úkolem programu je načíst ze souboru bludiště a následně rozhodnout o tom, zda li je možné dostat se z bodu A do bodu B.
Např.:
```text
####################
E  ###   ######### #
## # # #   ##     #
#  # # ##### #### #
# ####     # #  # #
### ####### #  # ##
#   #     # #  #  #
### # ### # #  #  #
# #   # # #    #  #
# ##### # ######  #
#     # #   #     #
##### # # # # #####
#   # # # # #     #
# ### ### # #######
# #   #     #     #
# ### # ##### ### #
# #   # #     #   #
# # ### # ### ### #
# #     # #   #  S
####################
```
Existuje cesta z bodu E do bodu S?

Postup:
1. Načíst si bludiště ze souboru, uložit si ho do proměnné (seznam seznamů). Jednotlivé znaky v seznamech budou buď " " (volné pole) nebo "#" (zeď). Také je potřeba si poznamenat, kde je START (S) a kde CÍL (E).
2. Pomocí algoritmu Prohledávání do šířky (BFS) rozhodni, jestli existuje cesta.

#### Prohledávání do šířky

Prohledávání do šířky je jedním z nejznámějších algoritmů pro hledání cest. Funguje tak, že začne na políčku start a koukne se, na jaká všechna pole se může jedním krokem ze startu dostat. Potom se podívá, na jaká všechna pole se může dostat z těchto nových polí, s tím, že už se nevrací na již prozkoumaná pole. Takto se opakuje dál a dál, dokud jsou ještě nějaká neprozkoumaná pole.
Pokud už žádná pole k prozkoumání nejsou, cesta ze startu do cíle neexistuje. Pokud při hledání narazíme na cíl, máme vyhráno.

![Maze Solution](maze.gif)


Při aplikaci na bludiště ho můžeme použít k nalezení cesty z bodu A do bodu B. Tady je podrobný popis kroků, které BFS podniká:

### 1. Inicializace
- Vytvoříme frontu (queue) a do ní vložíme počáteční bod (start), bod je dvojice souřadnic. Tento bod označíme jako navštívený.
  - Potřebné proměnné:
    - `queue`: seznam nebo jiná datová struktura, která reprezentuje frontu. Tato fronta bude uchovávat body, které ještě musíme prozkoumat.
    - `visited`: množina nebo jiná datová struktura, která uchovává body, které jsme již navštívili. Může to být taky slovník, kde si pro každý bod uchováváme buď TRUE (byl navštíven) nebo FALSE (nebyl zatím navštíven).

### 2. Prohledávání
- Základ BFS je cyklus, který běží tak dlouho, dokud zbývají nějaké body k prozkoumání.
- Dokud je fronta neprázdná, odebíráme z ní bod. Pokud je tento bod cílový, máme vyhráno. V opačném případě přidáme do fronty všechny sousední body, které jsme ještě nenavštívili, a označíme je jako navštívené.
- Sousední body aktuálního bodu vyčteme z našeho pole (bludiště). Do fronty samozřejmě přidáme jen prázdná pole, ne zdi.

### 3. Opakování
- Opakujeme krok 2, dokud nenajdeme cílový bod nebo dokud fronta nebude prázdná. Pokud je fronta prázdná a stále jsme nenašli cílový bod, znamená to, že cesta mezi počátečním a cílovým bodem neexistuje.


**Bonus:**
Pokud chceme nejen zjistit, zda cesta existuje, ale také ji rekonstruovat, budeme potřebovat ještě jednu proměnnou:
- `came_from`: slovník nebo jiná datová struktura, která pro každý navštívený bod uchovává bod, ze kterého jsme do něj přišli. Tuto informaci pak můžeme použít k rekonstrukci cesty zpět od cílového bodu k počátečnímu bodu.
