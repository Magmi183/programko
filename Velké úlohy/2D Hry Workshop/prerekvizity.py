"""
HRACÍ PLOCHA

Při vytváření 2D textové hry je základ udělat nějaké herní pole (mřížku). Například pokud chceme udělat piškvorky, musíme
v počítači nějak nasimulovat mřížkovaný papír, na kterém se bude hrát.
"""

# Pojďme si nejdříve rozmyslet, jak bychom udělali mřížku, která má jenom jeden řádek a jednotlivá pole jsou prázdná,
# tedy například stringy obsahující pouze mezeru či pomlčku.
# No, jednodušše uděláme list.

radka = [' '] * 10