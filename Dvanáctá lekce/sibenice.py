tajenka = "Zaciname s programovanim"
uhodnuto = "******** * *************"

zivotu = 10

spatne = []
dobre = []

while uhodnuto != tajenka and zivotu >= 0:

    print(f"Zbývá ti {zivotu} životů. Dobře jsi uhodl písmena {dobre}, špatně písmena {spatne}. \n"
          f"Aktuální stav tajenky je: {uhodnuto}. ")
    tip = input("Hádej písmeno! \n")
    ok_vstup = False
    while not ok_vstup:
        if tip in dobre or tip in spatne:
            tip = input("Tohle písmeno už jsi hádal, zkus to znovu: \n")
        elif len(tip) != 1 or not tip.isalpha():
            tip = input("Neplatný vstup: \n")
        else:
            ok_vstup = True

    tip = tip.lower()

    if tip in tajenka.lower():
        print("Hezky! Tohle písmeno jsi zandal správně.")
        for index in range(len(tajenka)):
            if tajenka[index].lower() == tip:
                uhodnuto = list(uhodnuto)
                uhodnuto[index] = tajenka[index]
                uhodnuto = "".join(uhodnuto)
        dobre.append(tip)
    else:
        print("Bohužel... Máš o jeden život méně.")
        spatne.append(tip)
        zivotu -= 1

if zivotu <= 0:
    print("Prohrál jsi...")
    print("Tajenka byla: " + tajenka)
else:
    print("Vyhrál si! Gratuluji.")