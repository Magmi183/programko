import matplotlib.pyplot as plt

# Data vyjadřující kolik snědl člověk jablek za den a kolikrát byl u doktora poslední rok
pocet_snezenych_jablek = [5, 0, 1, 1, 2, 0, 0, 8, 3, 4, 5, 6, 7, 0]
pocet_navstev_doktora = [0, 10, 2, 5, 6, 1, 4, 1, 3, 2, 1, 0, 3, 8]

# Vytvoření scatter plotu (bodového grafu)
plt.scatter(pocet_snezenych_jablek, pocet_navstev_doktora)

# Přidání názvů os a titulku
plt.xlabel('Počet snězených jablek')
plt.ylabel('Návštěv doktora')
plt.title('Platí známé tvrzení "An apple a day keeps the doctor away."?')

# Zobrazení grafu
plt.show()
