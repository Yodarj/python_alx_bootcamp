import json
import urllib.request
import datetime as dt
import tkinter as tk

def zdobycie_info():
    with urllib.request.urlopen(f'''https://www.metaweather.com/api/location/search/?query={miasto_entry.get()}''') as f:
        dane_miasta = json.loads(f.read())
        id_miasta = dane_miasta[0]['woeid']

    with urllib.request.urlopen(f'''https://www.metaweather.com/api/location/{id_miasta}/''') as p:
        pogoda = json.loads(p.read())
        info.configure(text=pogoda)




root = tk.Tk()


miasto_label = tk.Label(master=root, text="Podaj miasto [angielska nazwa]:")
miasto_entry = tk.Entry(master=root)

miasto_label.pack()
miasto_entry.pack()

info_label = tk.Label(master=root, text="Pogodaaaaaaa")
info = tk.Label(master=root, text="-")

info_label.pack()
info.pack()

but = tk.Button(master=root, text="Kliknij, by sprawdzić pogodę", command=zdobycie_info)
but.pack()


root.mainloop()