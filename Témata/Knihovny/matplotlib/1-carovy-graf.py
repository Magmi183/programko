import matplotlib.pyplot as plt

# SPOJNICOVÝ GRAF

#  - REÁLNÁ DATA O DOCHÁZCE NA KROUŽEK V ROCE 22/23 (1. termín)

# Data
daty = [
    '16.09', '23.09', '30.09', '07.10', '14.10', '21.10', '28.10', '04.11',
    '11.11', '18.11', '25.11', '02.12', '09.12', '16.12', '23.12', '30.12',
    '06.01', '13.01', '20.01', '27.01', '03.02', '10.02', '17.02', '24.02',
    '03.03', '10.03', '17.03', '24.03', '31.03', '07.04', '14.04', '21.04',
    '28.04', '05.05', '12.05', '19.05', '26.05', '02.06', '09.06', '16.06'
]
pritomni = [9, 7, 4, 6, 5, 3, 0, 5, 5, 4, 4, 5, 6, 4, 0, 0, 5, 6, 5, 5, 0, 3, 5, 4, 5, 2, 0, 5, 4, 0, 4, 5, 4, 4, 3, 3, 3, 5, 3, 5]

# Vytváření grafu
plt.figure(figsize=(15, 5)) # nastavení velikosti grafu
plt.plot(daty, pritomni, marker='o', label='Přítomní') # přidání dat do grafu
plt.xlabel('Datum schůzky') # popis osy x
plt.ylabel('Počet účastníků') # popis osy y
plt.title('Docházka na prográmku') # titulek grafu
plt.xticks(rotation=45) # rotace popisků na ose x (aby se datumy nepřekrývaly)
plt.legend()
plt.grid(True) # zobrazení mřížky (nastaveno na True - tzn. ano, chceme)

# Zobrazit graf
plt.show()