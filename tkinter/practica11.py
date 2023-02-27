from tkinter import Tk, Button, Frame, messagebox
def mostrarMensajes():
    messagebox.showinfo("Aviso", "Presionaste el boton azul")


#1. Instaciamos el objeto ventana
ventana= Tk()
ventana.title("Ejemplo de 3 frames ")
ventana.geometry("600x400")

#2. agregamos los frames
seccion1=Frame(ventana, bg="red") 
seccion1.pack(expand=True,fill="both")

seccion2=Frame(ventana, bg="gray") 
seccion2.pack(expand=True,fill="both")

seccion3=Frame(ventana, bg="pink") 
seccion3.pack(expand=True,fill="both")

#3. Agregamos botones 
botonAzul= Button(seccion1,text="Boton Azul", fg="blue", command=mostrarMensajes)
botonAzul.place(x=60, y=60)

botonNegro= Button (seccion2,text="Boton negro", fg="white", bg="black" )
botonNegro.grid(row=0, column=0)

botonAmarillo= Button (seccion2,text="Boton Amarillo",fg="white", bg="yellow")
botonAmarillo.grid(row=1, column=1)

botonVerde= Button (seccion3,text="Boton verde",fg="white", bg="green")
botonVerde.configure(height=2, width=10)
botonVerde.pack()

#llamamos al main (el main loop se pone hasta el final del código)
ventana.mainloop()