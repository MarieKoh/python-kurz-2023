sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadejte prosim kod soucastky: ")

if kod_soucastky not in sklad:
    print(f"Bohuzel soucastka neni na sklade.")
elif kod_soucastky in sklad:
    mnozstvi = int(input("Kolik si chcete koupit soucastek? "))
    if sklad[kod_soucastky] < mnozstvi:
        print(f"Lze prodat pouze omezene mnozstvi kusu.")
        sklad[kod_soucastky] = 0
    else:
        print(f"Poptavku lze uspokojit v plne vysi.")
        sklad[kod_soucastky] -= mnozstvi