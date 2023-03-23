import pandas 
teploty = pandas.read_html('temperature.htm')
teploty = teploty[0]

print(teploty.head())
praha = teploty[teploty.City == "Prague"]
print(praha)

vyssi_teplota = teploty[teploty.AvgTemperature > 80]
print(vyssi_teplota)
evropa = teploty[teploty.Region == "Europe"]
vyssi_teplota_evropa = evropa[evropa.AvgTemperature > 60]

print(vyssi_teplota_evropa)
extremni_hodnoty = teploty[(teploty.AvgTemperature > 80) | (teploty.AvgTemperature < -20)]
print(extremni_hodnoty)
