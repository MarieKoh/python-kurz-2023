import pandas 

zam_praha = pandas.read_csv("zam_praha.txt")
zam_plzeň = pandas.read_csv("zam_plzeň.txt")
zam_liberec = pandas.read_csv("zam_liberec.txt")

zam_praha["mesto"] = "Praha"
zam_plzeň["mesto"] = "Plzeň"
zam_liberec["mesto"] = "Liberec"

zamestnanci = pandas.concat([zam_praha, zam_plzeň, zam_liberec])

platy = pandas.read_csv("platy_2021_02.txt")

zamestnanci_platy = zamestnanci.join(platy.set_index('cislo_zamestnance'), on='cislo_zamestnance', how='left', rsuffix='_plat')

print("Rozměry tabulky zamestnanci: ", zamestnanci.shape)
print("Rozměry tabulky platy: ", platy.shape)
print("Rozměry tabulky zamestnanci_platy: ", zamestnanci_platy.shape)

prumerne_platy = zamestnanci_platy.groupby("mesto")["plat"].mean()
print("Průměrné platy v jednotlivých kancelářích:\n", prumerne_platy)