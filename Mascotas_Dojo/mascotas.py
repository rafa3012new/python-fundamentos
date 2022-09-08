import ninjas

class mascota:    
    #contructor de objetos de la clase
    def __init__(self,nombre,tipo,golosinas='',salud='',energia=''):
      self.nombre = nombre
      self.tipo = tipo
      self.golosinas = golosinas
      self.salud = salud
      self.energia = energia

    def dormir(self):
        print("la mascota " + self.nombre + " esta durmiendo")

    def comer(self):
        print("la mascota " + self.nombre + " esta comiendo")

    def jugar(self):
        print("la mascota " + self.nombre + " esta jugando")

    def sonido(self,sonido):
        print("la mascota " + self.nombre + " esta " + sonido)

class cria(mascota):
    #contructor de objetos de la clase
    def __init__(self,breeding,mezcla,superpoder=''):
      self.breeding = breeding
      self.mezcla = mezcla




print("\n\n")

#se instancian las clases ninja
subzero = ninjas.ninja('Sub','Zero')
scorpion = ninjas.ninja('Scor','Pion')
reptile = ninjas.ninja('Rep','Tile')

print("\n\n")

#se instancian las clases macotas
hielito = mascota('Hielito','hielo')
fueguito = mascota('Fuegito','fuego')
lagartija = mascota('Lagartija','reptil')


#se ejecutan los metodos de las clases ninja
hielito.comer()
fueguito.dormir()
lagartija.jugar()

print("\n\n")


#asignacion de una instancia a otra
subzero.mascotas = hielito
scorpion.mascotas = fueguito
reptile.mascotas = lagartija

#imprimir relacion
print("la mascota de " + subzero.nombre + subzero.apellido  + " es " + subzero.mascotas.nombre)
print("la mascota de " + scorpion.nombre + scorpion.apellido  + " es " + scorpion.mascotas.nombre)
print("la mascota de " + reptile.nombre + reptile.apellido  + " es " + reptile.mascotas.nombre)

print("\n\n")


#se ejecutan los metodos de las clases ninja
subzero.caminar()
scorpion.alimentar()
reptile.banar()

print("\n\n")

#se aplica la herencia
aguita = cria(1,'hielo-fuego')
aguita.nombre = 'Aguita'
humito = cria(1,'fuego-hielo')
humito.nombre = 'Humito'
camaleon = cria(1,'reptil')
camaleon.nombre = 'Camaleon'

#acciones de las crias
aguita.sonido('chorreando')
humito.sonido('soplando')
camaleon.sonido('silvando al cambiar de color')

print("\n\n")
