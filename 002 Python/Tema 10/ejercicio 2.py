import tkinter as tk


window = tk.Tk()
elemento = tk.StringVar()
cajaDeAutos = tk.Listbox(window)

for auto in ["Toyota","Mercedez","BMW","Audi","Rolls Royce", "Chevrolet"]:
    cajaDeAutos.insert(tk.END, auto)

cajaDeAutos.pack()
label = tk.Label(text="Marca de autos")
label.pack()

window.mainloop()