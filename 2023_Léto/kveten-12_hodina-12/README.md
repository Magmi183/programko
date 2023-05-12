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


