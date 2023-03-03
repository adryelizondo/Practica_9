from typing import Self


class Personaje:
 
#definimos el constructor de personaje 
 def __init__(self,esp ,nom,alt):
      
#encapsulamos nuestros atributos
  self.__especie= esp
  self.__nombre= nom
  self.__altura= alt 

#Metodos Personaje
#Nombramos de nueva forma nuestros atributos 
def correr(self,status):
	if(status):
          print("El personaje "+ self.__nombre + "esta corriendo")
        else: 
         print("El personaje "+self.__nombre + "se detuvo")

def lanzarGranadas(self):
 print("El personaje "+ self.__nombre + "Lanzo una granada")

def recargarArma(self, municiones):
	cargador=10
	cargador= cargador + municiones
	print("El arma tiene "+ str(cargador) + "balas") 
def __pensar(self):
    print("Estoy pensando :((( ")
    
#declarar getters and setters de atributos
def getNombre(self):
     return self.__nombre
def setNombre(self, nom):
     self.__nombre = nom
def getEspecie (self,esp):
     self.__especie = esp
def getAltura(self):
     return self.__altura
def setAltura(self, alt):
     self.__altura= alt 