class ninja:    
    #contructor de objetos de la clase
    def __init__(self,nombre,apellido,mascotas = '', premio= '', comida_mascota = ''):
      self.nombre = nombre
      self.apellido = apellido
      self.mascotas = mascotas
      self.premio = premio
      self.comida_mascota = comida_mascota

    def caminar(self):
        print("el ninja " + self.nombre + self.apellido + " esta caminando y paseando a " + self.mascotas.nombre)

    def alimentar(self):
        print("el ninja " + self.nombre + self.apellido + " esta alimentando a " + self.mascotas.nombre)

    def banar(self):
        print("el ninja " + self.nombre + self.apellido + " esta banando a "  + self.mascotas.nombre)

    def reganar(self):
        print("el ninja " + self.nombre + self.apellido + " esta reganando a" +  self.mascotas.nombre)


