from tkinter import Tk, Button, Frame, Label, Entry, messagebox 
from validacion import *

correo = "121040747@upq.edu.mx"
contraseña = "121040747"

def validar():
    Validacion=validar_datos(correo1.get(), contraseña1()) 


#Instanciar Ventana
ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("720x480")

#Frames
section1 = Frame(ventana,bg="black")
section1.pack(expand=True,fill='both')
section2 = Frame(ventana,bg="gray")
section2.pack(expand=True,fill='both')
section3 = Frame(ventana,bg="white")
section3.pack(expand=True,fill='both')

#Crear Etiquetas / Botones
iniciolabel = Label(section1,text=" INICIO DE SESION")
iniciolabel.pack()
correolabel = Label(section1,text="Ingrese correo: ")
correolabel.place(x=50,y=100,width=105,height=25)
contraseñalabel = Label(section2,text="Ingrese Contraseña: ")
contraseñalabel.place(x=50,y=100,width=120,height=25)
                        

#Cajas de texto
correo1 = Entry(section1)
correo1.place(x=250,y=100,width=200,height=25)

contraseña1 = Entry(section2)
contraseña1.place(x=250,y=100,width=200,height=25)

#Botones
Login = Button(section3, text="Iniciar", bg="blue")
Login.pack()

# Main para la ventana 
ventana.mainloop()



