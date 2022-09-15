"""
Býci a krávy
---------
Býci a krávy je známá logická hra. Normálně je pro 2 hráče, ale vaším úkolem je naprogramovat verzi pro jednoho hráče,
který bude hrát s počítačem.

Pravidla:
    Počítač si myslí náhodné čtyřmístné číslo a hráč se jej snaží uhodnout. Číslo nesmí obsahovat více stejných číslic!!
    Hraje se na kola - v každém kole hráč udělá jeden tip a počítač mu řekne,
    kolik tipl správně číslic a zároveň jsou na správném místě (býci) a kolik tipl správně číslic,
    ale nejsou na správném místě (krávy). Např. Pokud si počítač myslí číslo 4271 a hráč tipne 1234,
    počítač řekne: 1 býk a 2 krávy. Hráč se totiž trefil číslicí 2, která je i na správném místě, dále pak číslicemi 1 a 4,
    které už ale nejsou na správném místě. Proto tedy 1 býk a 2 krávy. Hráč má 8 kol na to, aby číslo uhodl.
    S počtem kol a délkou čísla můžete experimentovat, ale nejdříve udělejte základní verzi.

https://en.wikipedia.org/wiki/Bulls_and_Cows
https://cs.wikipedia.org/wiki/Logik_(hra)
"""