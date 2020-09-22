class Automovil ():
    def __init__(self, gasolina, km, propietario, placa):
        self.propietario = propietario
        self.placa = placa
        self.gasolina = gasolina
        self.venta = False
        self.odometro = km
        self.prendido = False
        

    def getGasolina(self):
        galones= int(raw-input("Ingrese la cantidad de galones"))
        self.gasolina = self.gasolina + galones
        print "Tu vehiculo ahora tiene", galones, " de gasolina"
        self.menu()
   

    def getOdometro(self):
        return self.odometro

    def addGasolina(self, galones ):
        self.gasolina = self.gasolina + galones 

              

    def arrancar(self):
        if self.gasolina > 0:
            self.prendido = True
            print "El carro esta encendido"
        else:
            print "No puedo arrancar, no tengo gasolina"
        self.menu()

    def moverse(self,km):
        if not self.prendido:
            print "No esta arrancado su carro"
            return

        if self.gasolina >= km:
            print "Avanzo ", km, "Kilometros"
            self.odometro = self.odometro + km
            self.gasolina = self.gasolina - km
        else:
            print "No hay suficiente gasolina"

    def __str__(self):
        valor = 'gasolina' +  str(self.gasolina)
        valor = valor + ' odometro' + str(self.odometro)
        valor = valor + ' prendido:' + str(self.prendido)
        valor = valor + ' propietario:' + self.propietario
        valor = valor + ' placa:' + self.placa
        return valor

    def cambiopropietario(self):
        Vender = raw_input("Desea efectuar la vente de este vehiculo:  si/no")
        if Vender.lower() == "si":
            nombre = raw_input("Ingrese el nombre del nuevo propietario")
            self.propietario = propietario
        else:
            print "No deseo vender el vehiculo"
            self.menu()

    def cambioplacas(self,placa):
        cambio = raw_input("Desea hacerle cambio de placas a su vehiculo:  si/no")
        if cambio.lower() == "si":
            placa= int(raw_input("Ingrese el nuevo numero de placas para su vehiculo"))
            self.placa = placa
        else:
            print "Deseo continuar con la misma placa: Gracias"
            self.menu()

    def menu(self):
        opcion = raw_input("""Favor Ingrese la opcion que desea ver"
"A",  Instancia del Carro
"B",  Print del contenido
"C",  Venta del Carro
"D",  Cambio de Placa
"E",  Ponga gasolina
"F",  Arranque el Carro
"G",  "Conduzca el Carro
"H",  Salir
""")

        if opcion == "A":
           propietario = raw_input("Ingrese nombre del propietario")
           placa = (raw_input("Ingrese numero de Placas"))
           print "El vehiculo con numero de placas", placa,"pertenece a ", propietario
        elif opcion == "B":
             miCarro = Automovil(2, 500, propietario ,placa)
        elif opcion == "C":
              self.cambiopropietario (nombre)
        elif opcion == "D":
              self.placa()
        elif opcion == "E":
            self.getgasolina ()
        elif opcion == "F":
             self.getgasolina ()
        elif opcion == "G":
            self.getgasolina ()
        elif opcion == "H":
            print "Gracias por utilizar este sistema"

miCarro = Automovil( 21321,123,3, "placa" )
miCarro.menu()


        








        
    
    

                          
        
        
