from laptop import Laptop
from laptop import laptop_business
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random

class App:
    def __init__(self, root):
        self.root= root
        self.laptops= []
        self.imagenes = [
            "C:\\Users\\Usuario\\Desktop\\programacion\\MODULO6\\poo\\img\\img1.jpeg",
            "C:\\Users\\Usuario\\Desktop\\programacion\\MODULO6\\poo\\img\\img2.jpeg",
            "C:\\Users\\Usuario\\Desktop\\programacion\\MODULO6\\poo\\img\\img3.jpeg",
            "C:\\Users\\Usuario\\Desktop\\programacion\\MODULO6\\poo\\img\\img4.jpeg",
            
            ]

        root.title("INGRESAR LOS DATOS")
        self.setup_ui()
    
    def setup_ui(self):
        ttk.Label(self.root, text="marca").grid(row=0,column=0)
        self.marca= tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)

        ttk.Label(self.root, text="procesador").grid(row=1,column=0)
        self.procesador= tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)

        ttk.Label(self.root, text="memoria").grid(row=2,column=0)
        self.memoria= tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.root, text="costo").grid(row=3,column=0)
        self.costo= tk.StringVar()
        ttk.Entry(self.root,textvariable=self.costo).grid(row=3,column=1)

        ttk.Label(self.root, text="impuesto").grid(row=4,column=0)
        self.impuesto= tk.StringVar()
        ttk.Entry(self.root,textvariable=self.impuesto).grid(row=4,column=1)

        ttk.Button(self.root, text="agregar laptop", command=self.agregar_laptop).grid(row=5,column=0)
        
        self.mostrar_laptops= tk.Text(self.root, height=10, width=50)

        self.mostrar_laptops.grid(row=6, column=1, columnspan=2)

        
        self.canva= tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=6)


    
    def agregar_laptop(self):
        nueva_laptop= laptop_business(self.marca.get(),self.procesador.get(),self.memoria.get(),self.costo.get(),self.impuesto.get())
        self.laptops.append(nueva_laptop)
        # print(self.laptops[0])
        self.mostrar_laptops.insert(  tk.END, f"{nueva_laptop}")

        self.mostrar_imagen()

    def mostrar_imagen(self):
        imagen_path= random.choice(self.imagenes)
        imagen= Image.open(imagen_path)
        imagen= imagen.resize((200,200), Image.Resampling.LANCZOS)
        photo= ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW, image= photo)
        self.canva.image= photo


    
root= tk.Tk()

app= App(root)
root.mainloop()




        