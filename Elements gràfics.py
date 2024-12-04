import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def fitxer_nou_pressionat(event=None):
    messagebox.showinfo("Fitxer nou", "Has pressionat per a crear un nou fitxer!")
    
finestra = tk.Tk()
finestra.title("Finestra amb diferents elements gràfics")
finestra.config(width=600, height=800)

etiqueta = ttk.Label(text="Exemple d'etiqueta")
etiqueta.place(x=20, y=20)

caixa_de_text = ttk.Entry()
caixa_de_text.insert(0, "Exemple de caixa de text")
caixa_de_text.place(x=140, y=20, width=140)

botó = ttk.Button(text="Exemple de botó")
botó.place(x=20, y=60)

combobox = ttk.Combobox(state="readonly", values=["Python", "C", "C++", "Java"])
combobox.place(x=20, y=100)

check = ttk.Checkbutton(text="Exemple de botó de check")
check.place(x=20, y=140)

listbox = tk.Listbox()
listbox.insert(tk.END, "Python", "C", "C++", "Java")
listbox.place(x=20, y=180)

notebook = ttk.Notebook()
web_label = ttk.Label(notebook, text="www.recursospython.com")
forum_label = ttk.Label(notebook, text="foro.recursospython.com")
notebook.add(web_label, text="Web", padding=20)
notebook.add(forum_label, text="Foro", padding=20)
notebook.place(x=20, y=360)

progressbar = ttk.Progressbar()
progressbar.place(x=20, y=460, width=200)
progressbar.step(50)

listbox = tk.Listbox()
listbox.insert(tk.END, *(f"Elemento {i}" for i in range(100)))
listbox.place(x=20, y=500)
scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.place(x=140, y=500, height=170)

spin = ttk.Spinbox(from_=10, to=30, increment=0.5, format="%.1fºC", wrap=True)
spin.insert(0, "10ºC")
spin["state"] = "readonly"
spin.place(x=20, y=680, width=70)

treeview = ttk.Treeview()
item = treeview.insert("", tk.END, text="Element 1")
subitem = treeview.insert(item, tk.END, text="Subelement 1")
treeview.insert(subitem, tk.END, text="Subelement 1.1")
item2 = treeview.insert("", tk.END, text="Element 2")
treeview.insert(item2, tk.END, text="Subelement 2")
treeview.place(x=300, y=20)

barra_menus = tk.Menu()
menu_fitxer = tk.Menu(barra_menus, tearoff=False)
menu_fitxer.add_command(
    label="Nou",
    accelerator="Ctrl+N",
    command=fitxer_nou_pressionat
)
finestra.bind_all("<Control-n>", fitxer_nou_pressionat)
barra_menus.add_cascade(menu=menu_fitxer, label="Fitxer")

finestra.config(menu=barra_menus)
finestra.mainloop()