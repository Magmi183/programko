import matplotlib.pyplot as plt

# Testovací data (počet bodů z kvízu)
prezdivky = ['xxx_chleba_xxx', 'marty', 'skibi', 'karel']
skore = [8, 6, 9, 7]

# Nastavení velikosti grafu
plt.figure(figsize=(10, 6))

# Vytvoření sloupcového grafu s různými barvami
barlist = plt.bar(prezdivky, skore, color=['blue', 'green', 'red', 'purple'])

# Přidání titulku a popisů os
plt.title('Skóre v kvízu', fontsize=16)
plt.xlabel('Přezdívky', fontsize=14)
plt.ylabel('Skóre', fontsize=14)

# Přidání mřížky
plt.grid(axis='y')

# Zobrazení grafu
plt.show()