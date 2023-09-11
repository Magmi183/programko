import matplotlib.pyplot as plt

# Data o počtech hráčů her (smyšlená)
hry = ['Minecraft', 'Fortnite', 'Among Us', 'Roblox']
pocty_hracu = [15, 7, 5, 8]

# Kód
plt.figure(figsize=(10, 6))
# vytvoření grafu, předání dat, nastavení formátu procent (automaticky, jedno desetinné místo)
plt.pie(pocty_hracu, labels=hry, autopct='%1.1f%%', startangle=90)
plt.title('Oblíbené hry')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
