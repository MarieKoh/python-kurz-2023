import re

regularni_vyraz = re.compile(r"^(?:(?:0?[1-9]|[12][0-9]|3[01])[./] ?(?:0?[1-9]|1[0-2])[./] ?(?:\d{4}|\d{2})|(?:\d{1,2}[./] ?){2}(?:\d{4}|\d{2}))$")
vstup = input("Zadej datum: ")

vstup_ok = regularni_vyraz.fullmatch(vstup)

print(vstup_ok)
