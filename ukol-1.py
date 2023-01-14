jmeno = input("Napiste sve jmeno: ")
print(jmeno + "@czechitas.cz")

jmeno_a_prijmeni = input("Napiste sve jmeno a prijmeni: ")
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
jmeno, prijmeni = jmeno_a_prijmeni.split()
print(jmeno.capitalize(), prijmeni.capitalize())
print(jmeno.capitalize()[0] + ".", prijmeni.capitalize()[0] + ". ")
if len(jmeno)>5:
    print(jmeno[0].capitalize() + ". " + prijmeni.capitalize())
else: 
    print(jmeno.capitalize(), prijmeni.capitalize())