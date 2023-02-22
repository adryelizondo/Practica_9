class Personaje:
 
      #definimos el constructor de personaje 
	 def __init__(self, esp,nom,alt):
		self.especie=esp
		self.nombre=nom
		self.altura=alt 


	#atributos Personaje
	especie="Humano"
	nombre= "Master Chief"
	altura= "2.70"

	#Metodos Personaje

 	def correr(self,status):
	if(status):
	print("El personaje "+ self.nombre + "esta corriendo")
	else: 
	print("El personaje "+ self.nombre + "se detuvo")

 	def lanzarGranadas(self):
	print("El personaje "+ self.nombre + "Lanzo una granada")

 	def recargarArma(self, municiones):
	cargador=10
	cargador= cargador + municiones
	print("El arma tiene "+ str(cargador) + "balas") 