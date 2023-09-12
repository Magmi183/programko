from Lukostrelec import Lukostrelec
from Ucastnik import Ucastnik
from Arena import Arena

# vytvoření seznamu účastníků
ucastnici = [Ucastnik("Maty", 10, 5, 7), Ucastnik("Dan", 8, 4, 10), Ucastnik("Dominik", 15, 4, 1), Lukostrelec("Legolas", 10, 0, 8)]


# vytvoření instance Areny
arena = Arena(ucastnici)

# vše je připravené - můžeme odstartovat herní cyklus
arena.start()