class persona():
    #definicion de los atributos de la clase.
    def __init__(self,nombre,edad,direccion,escolaridad,jobi):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.escolaridad = escolaridad
        self.jobi= jobi

  

    def mayoredad(self):
        if self.edad > 18:
            print "mayor de edad"
        else:
            print "no es mayor"

    def __str__(self):
        var = "nombre: " + self.nombre + " edad: " + str(self.edad)
        var = var + " direccion: " + self.direccion + " Escolaridad: " + self.escolaridad + " jobi: " + self.jobi
        return var



nom = raw_input("Ingrese su nombre: ")
eda = int(raw_input("Ingres su edad: "))
direc = raw_input("Ingrese su direccion: ")
esco = raw_input("Ingrese su grado academico: ")
jobi = raw_input("Ingrese su pasatiempo favorito")
person = persona(nom,eda,direc,esco,jobi)
person.mayoredad()
print person
        
    
