import tkinter
import progressbar
import time

def sumuj():
    a = float(a_entry.get())
    b = float(b_entry.get())
    wynik.configure(text=a + b)


root = tkinter.Tk()

root.title("Sumator")

a_label = tkinter.Label(master=root, text="parametr A")
a_entry = tkinter.Entry(master=root)

a_label.pack()
a_entry.pack()

b_label = tkinter.Label(master=root, text="parametr B")
b_entry = tkinter.Entry(master=root)

b_label.pack()
b_entry.pack()

wynik_label = tkinter.Label(master=root, text="Wynik")
wynik = tkinter.Label(master=root, text="-")

wynik_label.pack()
wynik.pack()

but = tkinter.Button(master=root, text="Kliknij", command=sumuj)
but.pack()


root.mainloop()
