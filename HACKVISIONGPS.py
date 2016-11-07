#-*-coding:utf-8-*-
#qpy:2
#qpy:kivy
'''
Aplicación desarrollada por el equipo de HACKVISION, Bogotá D.C.; Colombia
	Licenciado en física ---------------------------------> Diego Alberto Parra Garzón     DESARROLLADOR DE CONTENIDO 
	Profesional en ciencia de la información -------------> Luis Ali Ortiz Martínez        DESARROLLADOR DE CONTENIDO  
	Profesional en ciencia de la información -------------> Juan David Bastidas Blanco     DESARROLLADOR DE CONTENIDO
	Ingeniero de sistemas ------------------------------->  Miguel Ángel Garzón            DESARROLLADOR DE CONTENIDO

'''

from plyer import gps
import time

class HACKVISIONGPS:
    def DatosGPS(self, **kwargs):
        datosGps = '{lat},{lon},{altitude},{speed}'.format(**kwargs)
        cadena= str(datosGps)
        cadena1 = cadena.split(',')
        lat = cadena1[0] #Dato de latitud
        lon= cadena1[1]  #Dato de longitud
        alt= cadena1[2] #dato de altitud desde el nivel del mar
        rap = cadena1[3] #Datos de la rapidez relativa con respecto al sistema

        print "latitud: " ,lat ,"\n longitud: ", lon, "\n altitude: ", alt, "\n rapidezRelativa: ",rap,"\r\n"
        self.datosRelativos = "\t"+lat+"\t"+lon+"\t"+alt+"\t"+rap+"\t\r\n"
        self.bufergps()
        
    
    def bufergps(self):
        datos  = self.datosRelativos
        return datos
        
    def ComienzaGPS(self, *args):
        global datosRelativos
      #  datosRelativos=0
        try: 
            
            gps.configure(on_location=self.DatosGPS)
            if True:     
                gps.start()
                datosRelativos=self.bufergps()
                return datosRelativos
        except:
            datosRelativos=0
            print datosRelativos
            pass
        return datosRelativos
    def __init__(self):
        try:
            print "comenzando el gps"
            self.ComienzaGPS()
            print "GPS LISTO"
        except: 
            print "Fallo al activar el gps, revise su conexion, o su plataforma no es la correcta"
