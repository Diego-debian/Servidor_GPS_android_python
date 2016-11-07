'''
clase Bluetooth Arduino referencia de la api de pyjnius 
Hack-vision demo
Colombia Bogota
Diego Parra 
Luis Ali
'''
#qpy:kivy

from jnius import autoclass

class ArduinoBluetooth:
   
    def obtenerCorrienteEnchufe(self, Nombre):
        conectar_dispositivo = self.AdaptadorBluetooth.getDefaultAdapter().getBondedDevices().toArray()
        self.enchufe = None
        for dispositivo in conectar_dispositivo:
            if dispositivo.getName() == Nombre:
                self.enchufe = dispositivo.createRfcommSocketToServiceRecord(
                    self.UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
             #   self.recibir = self.enchufe.getInputStream()
                self.recibir = self.Lecturabufer(self.EntradaDeDatos(self.enchufe.getInputStream()))
                self.enviar = self.enchufe.getOutputStream()
                self.enchufe.connect()
                self.conexion = True
                print "paso la conexion en la clase"
        return self.conexion
                
            
    def Escribir(self, Mensaje, *args):
        if self.conexion == True:
            self.enviar.write(Mensaje)
            print "Mensaj enviado"
        else:
            print "Dispositivo no esta conectado"

    def LeerNUMERO(self, *args):
        CadenaDatos = ""
        if self.conexion == True:
            print "revisando conexion"
            print self.conexion
            lectura =1
            if (lectura>0):
                CadenaDatos =  float(self.recibir.readLine())                
                print "Lectura correcta ", CadenaDatos 
        return CadenaDatos
        

    def LeerCADENA(self, *args):
        CadenaDatos = ""
        if self.conexion == True:
            print "revisando conexion"
            print self.conexion
            lectura =1
            if (lectura>0):
                CadenaDatos =  str(self.recibir.readLine())
                print "Lectura correcta ", CadenaDatos 
        return CadenaDatos        

    def Cerrar(self):
        if self.conexion:
            self.enchufe.close()
            print "Dispositivo cerrado"

    def __init__(self):
        self.AdaptadorBluetooth = autoclass('android.bluetooth.BluetoothAdapter')
        self.DispositivoBluetooth = autoclass('android.bluetooth.BluetoothDevice')
        self.enchufe_Bluetooth = autoclass('android.bluetooth.BluetoothSocket')
        self.UUID = autoclass('java.util.UUID')
        self.Lecturabufer = autoclass('java.io.BufferedReader')
        self.EntradaDeDatos = autoclass('java.io.InputStreamReader')
        self.conexion = False
        
        
    def __del__(self):
        print "destructor de la clase ArduinoBluetooth"
        
#Arduino = ArduinoBluetooth()
#Arduino.obtenerCorrienteEnchufe("HC-05")
#Arduino.Escribir('1')
#print Arduino.Leer()
