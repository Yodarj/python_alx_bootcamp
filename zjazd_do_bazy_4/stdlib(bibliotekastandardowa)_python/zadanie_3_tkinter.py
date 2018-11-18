import tkinter
import progressbar
import time

def koszt_przejazdu():
    dystans = float(dystans_entry.get())
    spalanie_na_100 = float(spalanie_na_100_entry.get())
    cena_paliwa = float(cena_paliwa_entry.get())
    wynik.configure(text=round((dystans/100)*spalanie_na_100*cena_paliwa,2))


root = tkinter.Tk()

root.title("Sumator")

dystans_label = tkinter.Label(master=root, text="Wpisz dystans")
dystans_entry = tkinter.Entry(master=root)

dystans_label.pack()
dystans_entry.pack()

spalanie_na_100_label = tkinter.Label(master=root, text="Wpisz spalanie na 100km")
spalanie_na_100_entry = tkinter.Entry(master=root)

spalanie_na_100_label.pack()
spalanie_na_100_entry.pack()

cena_paliwa_label = tkinter.Label(master=root, text="Wpisz cenę paliwa")
cena_paliwa_entry = tkinter.Entry(master=root)

cena_paliwa_label.pack()
cena_paliwa_entry.pack()

wynik_label = tkinter.Label(master=root, text="Koszt paliwa")
wynik = tkinter.Label(master=root, text="-")

wynik_label.pack()
wynik.pack()

but = tkinter.Button(master=root, text="Kliknij", command=koszt_przejazdu)
but.pack()


root.mainloop()