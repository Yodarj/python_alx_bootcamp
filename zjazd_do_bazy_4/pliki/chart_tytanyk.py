import csv
import matplotlib.pyplot as plt

with open("dane/train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    dane = list(data)

for i in dane:
    print(i['Survived'])


# colors = ['r', 'g']
#
# plt.bar(data['Survived'], data, color=colors)
# plt.show()