import tkinter as tk

def seleccion():
    window.config(text="{}".format(opcion.get()))

def reiniciar():
    opcion.set(None)
    window.config(text="")

root = tk.Tk()
opcion = tk.StringVar()
opcion.set(None)
tk.Radiobutton(root, text="Capitan America", variable=opcion, 
            value='Capitan America', command=seleccion).pack(anchor=tk.W)

tk.Radiobutton(root, text="Iro man", variable=opcion, 
            value='Iro man', command=seleccion).pack(anchor=tk.W)
tk.Radiobutton(root, text="Hulk", variable=opcion,   
            value='Hulk', command=seleccion).pack(anchor=tk.W)
tk.Radiobutton(root, text="Thanos", variable=opcion,   
            value='Thanos', command=seleccion).pack(anchor=tk.W)

window = tk.Label(root)
window.pack()
tk.Button(root, text="Reiniciar", command=reiniciar).pack()

root.mainloop()