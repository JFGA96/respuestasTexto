"""
import tkinter

def accion_de_mi_boton():
    print("Mi boton ha sido presionado!")

mi_ventana = tkinter.Tk()
mi_ventana.geometry("640x480")

mi_boton = tkinter.Button(text="Mi botón!", command=accion_de_mi_boton)
mi_boton.pack()

mi_boton_2 = tkinter.Button(text="Mi botón 2!", command=accion_de_mi_boton)
mi_boton_2.pack()

mi_ventana.mainloop()
"""
"""
import tkinter as tk
from tkinter import Entry, Label, StringVar, ttk
from tkinter import *
from textwrap import wrap
from tkinter import font

contexto="Decir Coca-Cola es sinónimo de fiesta, celebración o quedada con amigos. Esta bebida universal, creada en Atlanta un 8 de mayo de 1886, se sirve de la misma manera en cumpleaños infantiles o barras de discotecas. Su historia arranca hace 132 años en el pequeño laboratorio del farmacéutico John S. Pemberton quien quería crear un jarabe contra los problemas de digestión que además aportase energía, incluso se llegó a decir que en la fórmula inicial había un porcentaje de cocaína algo que la compañía siempre ha negado. La farmacia Jacobs fue la primera en comercializar el preparado a un precio de 5 centavos el vaso, vendiendo unos nueve cada día. Era solo el inicio de una historia que ha convertido a la Coca-Cola en la bebida más famosa del mundo."


class Application(ttk.Frame):
    def leervariable():
         mesaje= lbpregunta.get

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.geometry("400x500")
        self.text = tk.StringVar(value=(contexto))
        entrada=StringVar()
        txtusuario=Entry(main_window,textvariable=entrada,bd=1).place(x=80,y=280)
        lbpregunta=Label(text="Pregunta",font=("Agency FB",11)).place(x=10,y=280)
        lbRespuesta=Label(text="Respuesta",font=("Agency FB",14)).place(x=10,y=320)
        botontomar=Button(main_window,text="Realizar pregunta",fg='black',font=("Agency FB",12), command=leervariable )
        botontomar.grid(row=4,column=0,padx=5,pady=10)
        print(entrada)
        self.label = tk.Label(self, text="text:")
        self.label.grid(column=0, row=0, pady=10, padx=10, sticky="e")
        self.label2 = tk.Label(self, textvariable=self.text)
        self.grid_columnconfigure(1, weight=1)
        self.label2.grid(column=1, row=0, pady=20, padx=10,  sticky="nswe")
        self.label2.bind( "<Configure>", self.on_label_resize)


    def on_label_resize(self,  event):
        event.widget["wraplength"] = event.width

   
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.pack(expand=True, fill='both')
    root.mainloop()"""



from tkinter import *

contexto="Decir Coca-Cola es sinónimo de fiesta, celebración o quedada con amigos. Esta bebida universal, creada en Atlanta un 8 de mayo de 1886, se sirve de la misma manera en cumpleaños infantiles o barras de discotecas. Su historia arranca hace 132 años en el pequeño laboratorio del farmacéutico John S. Pemberton quien quería crear un jarabe contra los problemas de digestión que además aportase energía, incluso se llegó a decir que en la fórmula inicial había un porcentaje de cocaína algo que la compañía siempre ha negado. La farmacia Jacobs fue la primera en comercializar el preparado a un precio de 5 centavos el vaso, vendiendo unos nueve cada día. Era solo el inicio de una historia que ha convertido a la Coca-Cola en la bebida más famosa del mundo."


def guardardatos():
    global newmensaje
    mensaje=mesajeTxt.get(1.0, "end-1c")
    
    if botonguardar:
        print(mensaje)
        return(mensaje)

    etiquetacombo=Label(text=mensaje,fg="red",font=("Popinns",12))
    etiquetacombo.grid(row=6, column=0,padx=20,pady=1)
    
def enviardatos():
    newmensaje=StringVar()
    newmensaje=guardardatos()
    print(newmensaje)
    
   



ventana= Tk()
ventana.title("mensaje")
ventana.geometry("400x500")

miframe=Frame(ventana)
miframe.grid()

Label(miframe,text="Pregunta",fg="gray",font=("Poppins",12)).grid(row=0,column=0,padx=6,pady=1,sticky="w")


mesajeTxt= Text(miframe,width=45,height=5)
mesajeTxt.grid(row=1, column=0,padx=10,pady=1)

mesajeTxt2= Text(miframe,width=45,height=5)
mesajeTxt2.grid(row=7, column=0,padx=10,pady=1)


mensajeNombre = StringVar()


botonguardar= Button(miframe,text="guardar",fg="black",font=("Poppins",12), command=guardardatos)
botonguardar.grid(row=4, column=0,padx=5,pady=10)

botonEnviar= Button(miframe,text="enviar",fg="black",font=("Poppins",12), command=enviardatos)
botonEnviar.grid(row=5, column=0,padx=5,pady=10)

ventana.mainloop()

