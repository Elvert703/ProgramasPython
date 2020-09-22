class persona (object):

    def __init__ (self,nombre,estadocivil,edad,escolaridad):
        self.nombre = nombre
        self.estadocivil = estadocivil
        self.edad = edad
        self.escolaridad = escolaridad


    def __str__ (self):
        valor = " nombre " + self.nombre
        valor = valor + " estadocivil " + self.estadocivil
        valor = valor + " edad " + str(self.edad)
        valor = valor + " escolaridad " + self.escolaridad
        return valor

nom = raw_input("Ingrese su nombre")
estado = raw_input("Ingrese su estado civil")
e = int(raw_input("Ingrese su edad"))
esco= raw_input("Ingrese su grado academico")

person = persona(nom,estado,e,esco)
print person
