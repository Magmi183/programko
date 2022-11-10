# Moc hezký úvod do for cyklů, ze kterého jsem také trochu čerpal, je zde (v češtině): https://www.itnetwork.cz/python/zaklady/cykly-v-pythonu
"""
            ███████╗░█████╗░██████╗░░░░░░█████╗░██╗░░░██╗██╗░░██╗██╗░░░░░██╗░░░██╗░██████╗
            ██╔════╝██╔══██╗██╔══██╗░░░░██╔══██╗╚██╗░██╔╝██║░██╔╝██║░░░░░██║░░░██║██╔════╝
            █████╗░░██║░░██║██████╔╝░░░░██║░░╚═╝░╚████╔╝░█████═╝░██║░░░░░██║░░░██║╚█████╗░
            ██╔══╝░░██║░░██║██╔══██╗░░░░██║░░██╗░░╚██╔╝░░██╔═██╗░██║░░░░░██║░░░██║░╚═══██╗
            ██║░░░░░╚█████╔╝██║░░██║░░░░╚█████╔╝░░░██║░░░██║░╚██╗███████╗╚██████╔╝██████╔╝
            ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚═════╝░╚═════╝░
"""

# Úvod do FOR cyklů

# SEKVENCE
# Co je to sekvence v Pythonu a proč to potřebujeme vědět?
# SEKVENCE jsou, zjednodušeně, takové proměnné, které obsahují více položek, v nějakém pořadí.

# 1) STRING - S jednou sekvencí jsme se již potkali - STRING - je sekvence znaků.
# Co je to vlastně string, text? Nějaké znaky, v nějakém pořadí.

# např. tento string je sekvence písmen v abecedním pořadí
abeceda = "abcdefghijklmnopqrstuvwxyz"

# ... EXISTUJÍ I DALŠÍ SEKVENCE, ale v tuto chvíli si vystačíme se stringem ...


################################################################################
###### FOR CYKLUS
################################################################################
"""
For cyklus podobně jako while cyklus slouží k tomu, když chceme VYKONAT NĚJAKÝ BLOK KÓDU VÍCEKRÁT.
Narozdíl od while cyklu, který se opakuje dokud je splněná podmínka, for cyklus se provede tolikrát, kolik
prvků má danná SEKVENCE. 

Ve for cyklu totiž narozdíl od while NENÍ ŽÁDNÁ PODMÍNKA. Místo toho očekává nějakou SEKVENCI.
Pojďme si to ukázat na příkladu.
"""

# TODO
# uděláme si string abeceda (což je sekvence znaků)
abeceda = "abcdefghijklmnopqrstuvwxyz"


# FOR cyklus:
for pismeno in abeceda: # můžeme číst jako: "pro každé písmeno v abecedě (pro každý znak ve stringu) udělej něco"
    print(pismeno)
