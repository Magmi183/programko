# Jedna z možných cest je reprezentovat každý počítač jako SEZNAM.

# jméno, CPU, grafika, RAM (velikost), SSD (kapacita), HDD (kapacita)
pocitac_1 = ["Alza Individual R7", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 32, 2000, 6000]
pocitac_2 = ["Computron i9 Beast", "Intel Core i9-12900K 5.2 GHz", "NVIDIA RTX 4080", 64, 2000, 8000]
pocitac_3 = ["HyperTech Fusion R5", "AMD Ryzen 5 7600 4.5 GHz", "NVIDIA RTX 4060", 16, 1000, 4000]
pocitac_4 = ["Alza Individual i7 Ultra", "Intel Core i7-12800 4.9 GHz", "Intel Iris Graphics", 32, 1500, 5000]
pocitac_5 = ["OmegaForce Z2", "AMD Ryzen Threadripper 3995WX", "NVIDIA RTX 4090", 128, 4000, 10000]
pocitac_6 = ["ByteMaster Silver", "Intel Core i5-12600 4.5 GHz", "AMD Radeon RX 6800", 16, 500, 3000]



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Pocitac:
    def __init__(self, jmeno, cpu, grafika, ram, ssd, hdd):
        self.jmeno = jmeno
        self.cpu = cpu
        self.grafika = grafika
        self.ram = ram
        self.ssd = ssd
        self.hdd = hdd

    def popis(self):
        print(f"Počítač {self.jmeno} má následující specifikace:")
        print(f"• CPU: {self.cpu}")
        print(f"• Grafická karta: {self.grafika}")
        print(f"• RAM: {self.ram} GB")
        print(f"• SSD kapacita: {self.ssd} GB")
        print(f"• HDD kapacita: {self.hdd} GB")

    def zobraz_kapacitu(self):
        celkova_kapacita = sum(self.ssd) + sum(self.hdd)
        print(f"Celková kapacita úložiště počítače {self.jmeno} je {celkova_kapacita} GB:")
        print(f"• SSD kapacita: {sum(self.ssd)} GB")
        print(f"• HDD kapacita: {sum(self.hdd)} GB")

    def pridej_hdd(self, velikost):
        self.hdd.append(velikost)

    def pridej_ssd(self, velikost):
        self.ssd.append(velikost)

    def odeber_hdd(self, velikost):
        if velikost in self.hdd:
            self.hdd.remove(velikost)
        else:
            print(f"HDD o velikosti {velikost} GB nebyl nalezen.")

    def odeber_ssd(self, velikost):
        if velikost in self.ssd:
            self.ssd.remove(velikost)
        else:
            print(f"SSD o velikosti {velikost} GB nebyl nalezen.")


"""
# Verze, kde SSD a HDD je jedno číslo
pocitac_1 = Pocitac("Alza Individual R7", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 32, 2000, 6000)
pocitac_2 = Pocitac("Computron i9 Beast", "Intel Core i9-12900K 5.2 GHz", "NVIDIA RTX 4080", 64, 2000, 8000)
pocitac_3 = Pocitac("HyperTech Fusion R5", "AMD Ryzen 5 7600 4.5 GHz", "NVIDIA RTX 4060", 16, 1000, 4000)
pocitac_4 = Pocitac("Alza Individual i7 Ultra", "Intel Core i7-12800 4.9 GHz", "Intel Iris Graphics", 32, 1500, 5000)
pocitac_5 = Pocitac("OmegaForce Z2", "AMD Ryzen Threadripper 3995WX", "NVIDIA RTX 4090", 128, 4000, 10000)
pocitac_6 = Pocitac("ByteMaster Silver", "Intel Core i5-12600 4.5 GHz", "AMD Radeon RX 6800", 16, 500, 3000)
"""

pocitac_1 = Pocitac("Alza Individual R7", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 32, [1000, 1000], [2000, 2000, 2000])
pocitac_2 = Pocitac("Computron i9 Beast", "Intel Core i9-12900K 5.2 GHz", "NVIDIA RTX 4080", 64, [500, 1500], [4000, 4000])
pocitac_3 = Pocitac("HyperTech Fusion R5", "AMD Ryzen 5 7600 4.5 GHz", "NVIDIA RTX 4060", 16, [250, 250, 500], [1000, 1000, 2000])
pocitac_4 = Pocitac("Alza Individual i7 Ultra", "Intel Core i7-12800 4.9 GHz", "Intel Iris Graphics", 32, [500, 1000], [2500, 2500])
pocitac_5 = Pocitac("OmegaForce Z2", "AMD Ryzen Threadripper 3995WX", "NVIDIA RTX 4090", 128, [2000, 2000], [4000, 2000, 4000])
pocitac_6 = Pocitac("ByteMaster Silver", "Intel Core i5-12600 4.5 GHz", "AMD Radeon RX 6800", 16, [250, 250], [1500, 1500])


# Přístup k atributům (vlastnostem)

print(f"Jméno prvního počítače je: {pocitac_1.jmeno}")
print(f"RAM druhého počítače je: {pocitac_2.ram}")
# ... k přístupu k hodnotě konkrétní vlastnosti nám stačí napsat jméno proměnné, tečku a jméno vlastnosti

# sečtení velikostí RAM všech počítačů (nevím z jakého důvodu, ale takto by se to dělalo :D)
celkova_velikost_ram = pocitac_1.ram + pocitac_2.ram + pocitac_3.ram + pocitac_4.ram + pocitac_5.ram + pocitac_6.ram
print(f"Počítače mají celkem: {celkova_velikost_ram} GB RAM paměti.")


# Použití METODY

pocitac_4.popis()

print("+- - - - - - - - - - -+")
pocitac_1.zobraz_kapacitu()

# Používání metod na SSD, HDD a zobrazení kapacity - začínáme s počítačem bez uložiště
pocitac = Pocitac("King Comp", "AMD Ryzen 7 7800X3D 5 GHz", "AMD Radeon Graphics", 4, [], [])

pocitac.pridej_hdd(1000)
pocitac.pridej_hdd(1000)
pocitac.pridej_hdd(1000)

pocitac.pridej_ssd(500)
pocitac.pridej_ssd(2000)

pocitac.odeber_hdd(1000)

pocitac.zobraz_kapacitu()

print(str(pocitac))