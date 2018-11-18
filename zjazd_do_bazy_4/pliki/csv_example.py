import csv

with open("dane/train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    wiek_m = 0
    surv_m = 0
    ilosc_m = 0
    ilosc_cal_m = 0
    wiek_k = 0
    ilosc_k = 0
    surv_k = 0
    ilosc_cal_k = 0
    for row in data:
        if row['Sex'] == 'male':
            ilosc_cal_m += 1
        elif row['Sex'] == 'female':
            ilosc_cal_k += 1

        if row['Survived'] == '1' and row['Sex'] == 'male':
            surv_m+=1
        elif row['Survived'] == '1' and row['Sex'] == 'female':
            surv_k+=1

        if row['Age'] == '' or row['Sex']=='':
            continue
        elif row['Sex'] == 'male':
            ilosc_m+= 1
            wiek_m += float(row['Age'])
        elif row['Sex'] == 'female':
            ilosc_k+= 1
            wiek_k += float(row['Age'])






    print("Średni wiek mężczyzn:", round(wiek_m/ilosc_m,2))
    print("Średni wiek kobiet:", round(wiek_k/ilosc_k,2))
    print("Ile % mężczyzn przeżyło:", round(surv_m/(ilosc_cal_m),4)*100)
    print("Ile % kobiet przeżyło:", round(surv_k/(ilosc_cal_k),4)*100)

