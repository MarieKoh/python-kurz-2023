import pandas
import matplotlib.pyplot
platy = pandas.read_csv("platy_2021_02.txt")
matplotlib.pyplot.hist(platy['plat'], bins=20, edgecolor='black')
matplotlib.pyplot.title('Histogram platů zaměstnanců - únor 2021')
matplotlib.pyplot.xlabel('Plat')
matplotlib.pyplot.ylabel('Počet zaměstnanců')
matplotlib.pyplot.show()
