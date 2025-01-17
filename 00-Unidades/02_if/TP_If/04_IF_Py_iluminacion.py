import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        #Valores
        precio_lampara = 800
        cantidad_lamparas_texto = self.combobox_cantidad.get()
        cantidad_lamparas_numero = int(cantidad_lamparas_texto)
        marca_lampara = self.combobox_marca.get()
        precio_lampara = precio_lampara * cantidad_lamparas_numero
        #Calculos
        if(cantidad_lamparas_numero >= 6):
            precio_lampara = precio_lampara / 2
        if(cantidad_lamparas_numero == 5 and marca_lampara == "ArgentinaLuz"):
            descuento_40 = 40 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_40
        elif(cantidad_lamparas_numero == 5):
            descuento_30 = 30 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_30
        if(cantidad_lamparas_numero == 4 and marca_lampara == "ArgentinaLuz"):
            descuento_25 = 25 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_25
        elif(cantidad_lamparas_numero == 4 and marca_lampara == "FelipeLamparas"):
            descuento_25 = 25 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_25
        elif(cantidad_lamparas_numero == 4):
            descuento_20 = 20 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_20
        if(cantidad_lamparas_numero == 3 and marca_lampara == "ArgentinaLuz"):
            descuento_15 = 15 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_15
        elif(cantidad_lamparas_numero == 3 and marca_lampara == "FelipeLamparas"):
            descuento_10 = 10 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_10
        elif(cantidad_lamparas_numero == 3):
            descuento_5 = 5 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_5
        if(precio_lampara > 4000):
            descuento_5 = 5 * precio_lampara / 100
            precio_lampara = precio_lampara - descuento_5
        alert("LamparasOferton", "El precio de la/s lampara/s es: " + str(precio_lampara))
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()