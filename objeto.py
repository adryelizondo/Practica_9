
from Personaje import *

#1. Solicitar datos
print("-----------Datos Heroe----------------")
especieH= input("Escribe la especie del Heroe: ")
nombreH= input("Escribe el nombre del Heroe: ")
alturaH= float("Escribe la altura del Heroe: ")
recargaH= int("Cuantas Balas recargas al Heroe: ")

print("------------Datos del villano------------")
especieV= input("Escribe la especie del Villano: ")
nombreV= input("Escribe el nombre del Villano: ")
alturaV= float("Escribe la altura del Villano: ")
recargaV= int("Cuantas Balas recargas al Villano: ")

#2.Crear onjetos de clase personaje 

heroe= Personaje(especieH,nombreH,alturaH)
villano= Personaje(especieV,nombreV,alturaV)

#3. Usar atributos y metodos
#Ejemplo del set para ir al atributo 

heroe.setNombre(" Pepe Pecas ")

print("-----------Datos del heroe------------")
print ("El personaje se llama: " + heroe.getNombre())
print ("Pertenece a la especie: " + heroe.getEspecie())
print ("y Tiene una altura de: " + str(heroe.GetAltura()))
heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)

#Ejemplo de un metodo privado
#heroe.__pensar()

print("-------------Datos Villano-------------")
print ("El personaje se llama: " + villano.getNombre())
print ("Pertenece a la especie: " + villano.getEspecie())
print ("y Tiene una altura de: " + str(villano.getAltura()))
villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV)

