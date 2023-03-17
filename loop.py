kandidaten = ["stoppen", "Jan Visser", "Samir mohammed"]
lijst = []

for (i, kandidaat) in enumerate (kandidaten, start=0):
    print (i, kandidaat)

    keuze = 99
    while keuze !=0
        keuze = int(input("Maak een keuze (1-3)"))
        lijst.append (keuze)

        for k in lijst:
            f.write(str (k))
            f.close()

            f = open ("resultaten.txt", "rt")
            res = list(f.read())
            print(res)
            for (i, kandidaat) in enumerate (kandidaten, start=0):
                if i != 0:
                    print(f"{kandidaat} heeft {res.count}
