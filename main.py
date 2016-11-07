#-*- coding:utf-8 -*-
#qpy:kivy
'''
Aplicación desarrollada por el equipo de HACKVISION, Bogotá D.C.; Colombia
	Licenciado en física ---------------------------------> Diego Alberto Parra Garzón     DESARROLLADOR DE CONTENIDO 
	Profesional en ciencia de la información -------------> Luis Ali Ortiz Martínez        DESARROLLADOR DE CONTENIDO  
	Profesional en ciencia de la información -------------> Juan David Bastidas Blanco     DESARROLLADOR DE CONTENIDO
	Ingeniero de sistemas ------------------------------->  Miguel Ángel Garzón            DESARROLLADOR DE CONTENIDO

'''
import kivy
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
from commands import getoutput
import ArduinoBluetooth
from ArduinoBluetooth import *
import HACKVISIONGPS
from kivy.clock import Clock
from HACKVISIONGPS import *
import Brujula
from Brujula import *            

kivy.require('1.9.0')
class servidorHACKVISION(App):
    def Label1(self):
        global lbl1
        lbl1 = Label()
        lbl1.text =  "Esperando instrucciones:"
        lbl1.pos = 200+self.xo,280+self.yo
        self.widget1.add_widget(lbl1)
        print "Esperando instrucciones:"

    def Label2(self):
        widget3 = Widget()
        img2 = Image()
        img2.source = "img/text.png"        
        x,y = 130, 370
        img2.pos = x+self.xo, y-160+self.yo
        img2.size= 300, 500
        lbl2 = Label()
        lbl2.pos = x+90+self.xo , y+40+self.yo
        lbl2.text = "            " + 'HACK-VISION DEMO\n CLIENTE BLUETOOTH  ENVIO\n'+ "          "+'            GPS'
        widget3.add_widget(img2)
        widget3.add_widget(lbl2)  
        self.widget1.add_widget(widget3)
        
 
        
    def IMAGENTUTORIAL(self):
        x,y = 430, 100
        widget3 = Widget()
        lbl2 = Label()
        lbl2.pos = x+250+self.xo , y+250+self.yo
        lbl2.text = "            " + 'MONTAJE MODULO BLUETOOTH - ULTRASONIDO \n EN PLACA ARDUINO UNO, CONEXION PINES'
        widget3.add_widget(lbl2)  
        self.IMAGEN = Image()
        self.IMAGEN.pos = x+self.xo, y-60+self.yo        
        self.IMAGEN.size= 500, 300
        widget3.add_widget(self.IMAGEN)
        self.widget1.add_widget(widget3)   

    def BotonImagen1(self):
        wid2 = Widget()
        Btn1 = Button()
        Btn1.background_normal = 'img/inico.png'
        Btn1.pos = 200+self.xo, 30+self.yo
        Btn1.bind(on_press = self.Verificaboton1 )
        self.widget1.add_widget(Btn1)

    def Verificaboton1(self, *args):
        if self.opcion1 == 0:
            self.EncenderBluetooth()
            self.opcion1 = 1

        if self.opcion1 == 1:
            pass
    
    def BotonImagen2(self):
        wid2 = Widget()
        Btn2 = Button()
        Btn2.background_normal =  'img/play.png'
        Btn2.pos = 140+self.xo, 100+self.yo
        Btn2.bind(on_press = self.Verificacionboton2 )
        self.widget1.add_widget(Btn2)
        

    def Verificacionboton2(self, *args):
        if self.opcion2 == 0:
            self.Mensaje1()
            self.opcion2 = 1
            self.opcion3 = 1

        if self.opcion2==1:
            pass
    

    def BotonImagen3(self):
        wid2 = Widget()
        Btn3 = Button()
        Btn3.background_normal = 'img/pause.png'
        Btn3.pos = 80+self.xo, 170+self.yo
        Btn3.bind(on_press = self.Verificacionboton3)
        self.widget1.add_widget(Btn3)

    def Verificacionboton3(self, *args):
        if self.opcion3 == 1:
            self.Mensaje2()
            self.opcion2 = 0
            self.opcion3 = 0

        if self.opcion3==0:
            pass


 

    def EncenderBluetooth(self, *args):
        print "Llamado a prender"
        try:
            Dispo = "HC-05"
            lbl1.text = "Espere conectando el Bluetooth"
            ArduinoB.obtenerCorrienteEnchufe('HC-05')
            Mensaje = "Dispositivo conectado"
            print Mensaje
            lbl1.text = Mensaje 
        except:
            Mensaje = "Dispositivo NO CONECTADO revise su conexion "
            print Mensaje
            ArduinoB.obtenerCorrienteEnchufe("HC-05")
            lbl1.text = Mensaje

    def ApagarBluetooth(self, *args):
        try:
            ArduinoB.Cerrar()
            Mensaje = "Conexion cerrada"
            print Mensaje 
            lbl1.text = Mensaje

        except:
            Mensaje = "Revise su conexion"
            print Mensaje
            lbl1.text = Mensaje


    def EscribirBluetooth(self, Mensaje, *args):
        try:
            ArduinoB.Escribir(Mensaje)
            Mensaje1 = "Se envio el mensaje ["+Mensaje+"] correctamente."
            print Mensaje1
            Mensa = Mensaje.split("\t")
            MensajeFinal = "\n\t\t\t\tLatitud: "+ Mensa[1]+ "\n\t\t\t\tLongitud: "+Mensa[2]+ "\n\t\t\t\tAltitud: "+ Mensa[3]+"\n\t\t\t\tRapidez: "+ Mensa[4]
            lbl1.text = MensajeFinal
        except:
            Mensaje1 =  "Fallo el envio del mensaje ["+Mensaje+"]  revise su conexion."
            print Mensaje1
            lbl1.text = Mensaje1
   


#ENVIAR MENSAJES AL ARDUINO         
    def Mensaje1(self, *args):       
        Hilo2 = Clock.schedule_interval(self.DatosGPS, 1)
            
        
    def Mensaje2(self, *args):       
      #  self.EscribirBluetooth('22')
        try:
#            Clock.unschedule(self.Lectura)
            Clock.unschedule(self.DatosGPS)
            llbl1.text = "Procesos Finalizados correctamente "

        except:
            print "no se que paso con el schedule"

    def DatosGPS(self, *args):
        LecturaGPS = hackgps.ComienzaGPS()
        
        print LecturaGPS
        if (LecturaGPS==None):
            print "no hay lectura"
            pass
        if (LecturaGPS!=None):
            lec= str(LecturaGPS)
            print type(lec)
            print lec
            lbl1.text= lec
            self.EscribirBluetooth(lec)

#IDENTIFICADOR DE PROCESOS GPS
    def procesos_GPS(self):
        try:
            global hackgps
            print "Llamado a la libreria gps"
            hackgps = HACKVISIONGPS()
            Mensaje =  "Libreria gps activada"
            print Menaje
            lbl1.text = Mensaje
        except:
            Mensaje = "fallo al activar el gps"
            print Mensaje
            lbl1.text = Mensaje
        
            

# IDENTIFICADOR DE PROCESOS EN ARDUINO
    def Procesos_Arduino(self):
        try:
            global ArduinoB
            print "Llamado a la libreria"
            from ArduinoBluetooth import *
            
            print "paso el llamado"
            print "instanciando la clase ArduinoBluetooth"
            ArduinoB = ArduinoBluetooth()
            Mensaje = "Todos los procesos Arduino Activados "
            print Mensaje 
            lbl1.text = Mensaje
            
        except:
            Mensaje = "Fallo al activar los procesos Arduino"
            print Mensaje
            lbl1.text = Mensaje
        pass

# IDENTIFICADOR DE PROCESOS EN PYTHON
    def Procesos_Kivy(self):      
        Mensaje0 = "Cativado Label1"
        Mensaje1 = "Fallo al activar label 1"
        Mensaje2 = "Label2 Activado"
        Mensaje3 = "Fallo al Activar el label 2"
        Mensaje4 = "boton imagen1 activado"
        Mensaje5 = "Fallo Al activar la imagen boton1"
        Mensaje6 = "boton imagen2 activado"
        Mensaje7 = "Fallo Al activar la imagen boton2"
        Mensaje8 = "boton imagen3 activado"
        Mensaje9 = "Fallo Al activar la imagen boton3"
        Mensaje10 = "boton imagen4 activado"
        Mensaje11 = "Fallo Al activar la imagen boton4"
        try:
            self.Label1()
            print Mensaje0
        except:
            print Mensaje1

        try:
            self.Label2()
            print Mensaje2
        except:
            self.Label2()
            print Mensaje3

        try:
            self.BotonImagen1()
            print Mensaje4
        except:
            print Mensaje5
        
        try:
            self.BotonImagen2()
            Mensaje6
        except:
            print Mensaje7
        
        try:
            self.BotonImagen3()
            print Mensaje8
        except:
            print Mensaje9
        

        pass


    def PROCESOS(self):
        self.Procesos_Kivy()
        self.procesos_GPS()
        self.Procesos_Arduino()



        
    def build(self):
        self.opcion1 = 0
        self.opcion2 = 0
        self.opcion3 = 0
        self.xo = 0
        self.yo = -40
        self.RelativaDispo = RelativeLayout()
        self.widget1 = Widget()
        self.RelativaDispo.add_widget(self.widget1)
        self.PROCESOS()
        return self.RelativaDispo

if __name__=='__main__':
    servidorHACKVISION().run()
    
