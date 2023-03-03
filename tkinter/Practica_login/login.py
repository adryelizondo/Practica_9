from tkinter import Tk, Button, Frame, Label, Entry, messagebox 

idcorreo= "121040747@upq.edu.mx"
idcontraseña= "121040747"

#Validar datos
def validardatos(): 
    if idcorreo== correo1.get() and idcontraseña == Contraseña1.get():
        messagebox.showinfo("Se inicio sesión con exito")
    else: 
        messagebox.showerror("Los datos son incorrectos")

#Instanciamos la ventana
ventana= Tk()
ventana.title("Login")
ventana.geometry("500x400")

#Frames
seccion1=Frame(ventana, bg="blue") 
seccion1.pack(expand=True,fill="both")

#botones
correo = Label (seccion1, text="Correo", font="Arial", bg="white" )
correo.place(x=20, y=50)

Contraseña= Button (seccion1, text="Contraseña", font= "Arial 12", bg="white" )
Contraseña.place(x=20, y=100)

# Para crear caja de texto.
correo1 = Entry(seccion1)
correo1.place(x=90,y=50)

Contraseña1= Entry(seccion1)
Contraseña1.place(x=120,y=100)

#segundo frame 
seccion2=Frame(ventana,bg="white" )
seccion2.pack(expand=True,fill="both")

#boton login
Login=Button(seccion2, text="Login", font="Arial 12", bg="white", command= validardatos)
Login.pack()

#Llamamos el mainloop
ventana.mainloop()




