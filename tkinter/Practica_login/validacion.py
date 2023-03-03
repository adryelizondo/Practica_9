from tkinter import messagebox

class validacion:
     
   def __init__(self,idcorreo,idcontraseña,correo1,contraseña1):
        self.correo1 = idcorreo
        self.contraseña1 = idcontraseña
        self.correo1 = correo1
        self.contraseña1 = contraseña1

        def validar_datos (self):
         if self.idcorreo.get()== self.correo1 and self.idcontraseña.get()==self.correo2:
            messagebox.showinfo("Se inicio sesion con exito")
         else:
            messagebox.showerror("Los datos ingresados son incorrectos")
