

with open("data/nakazeni-covid.csv", encoding="utf-8") as covid:
    maxi = 0
    dm = ""

    covid.readline()
    vicr = 0
    mr = 444444
    for radek in covid:
        datum, nakazeni, reinf,_,_,pon,_ = radek.split(";")
        nakazeni = int(nakazeni)
        reinf = int(reinf)

        pon = int(pon)

        if pon > 0:
            print(datum)
            break
    print(mr)



