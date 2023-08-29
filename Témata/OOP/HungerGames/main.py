from Témata.OOP.HungerGames.entity.Lukostrelec import Lukostrelec
from entity.Ucastnik import Ucastnik
from arena.Arena import Arena

ucastnici = [Ucastnik("Maty", 10, 5, 7, 5), Ucastnik("Dan", 8, 4, 10, 5), Ucastnik("Dominik", 15, 4, 1, 5), Lukostrelec("Legolas", 10, 0, 8, 4)]

arena = Arena(ucastnici)
arena.start()


"""
TODO:
- dodelat komentare
- metodu start v Arene nejak vic rozdelit, aby sla lepe pouzit dedicnost
- vymyslet ulohy 
"""