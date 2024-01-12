def sumy(osudi):
    osudi.pop("", None)
    soucty = {jmeno: sum(hodnoty) for jmeno, hodnoty in osudi.items()}
    serazene_soucty = sorted(soucty.items(), key=lambda x: x[1], reverse=True)
    for jmeno, soucet in serazene_soucty:
        print(f"{jmeno}: {soucet}")