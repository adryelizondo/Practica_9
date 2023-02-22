
from Personaje import *

#1. Solicitar datos
    print("")
    print("####### Datos Heroe #")
    especieH= input("Escribe la especie del Heroe: ")
    nombreH= input("Escribe el nombre del Heroe: ")
    alturaH= float("Escribe la altura del Heroe: ")
    recargaH= int("ECuantas Balas recargas al Heroe: ")

    print("")
    print("####### Datos villano #")
    especieV= input("Escribe la especie del Villano: ")
    nombreV= input("Escribe el nombre del Villano: ")
    alturaV= float("Escribe la altura del Villano: ")
    recargaV= int("ECuantas Balas recargas al Villano: ")

    #2.Crear onjetos de clase personaje 

    heroe= Personaje(especieH,nombreH,alturaH)
    villano= Personaje(especieV,nombreV,alturaV)


    #3. Usar atributos 

    print("")
    print("##### Objetos heroe ####")
    print ("El personaje se llama: " + heroe.nombre)
    print ("Pertenece a la especie: " + heroe.especie)
    print ("y Tiene una altura de: " + str(heroe.altura))
    heroe.correr(True)
    heroe.lanzarGranadas()
    heroe.recargarArma(recargaH)

    print("")
    print("##### Objetos Villano ####")
     print ("El personaje se llama: " + villano.nombre)
    print ("Pertenece a la especie: " + villano.especie)
    print ("y Tiene una altura de: " + str(villano.altura))
    villano.correr(False)
    villano.lanzarGranadas()
    villano.recargarArma(recargaV)

#3. Usar metodos

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(87)