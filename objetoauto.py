class Auto():
    marca = ""
    modelo = ""
    ano = 0
    color = ""
    tipo = ""
    cilindros = ""

    #constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    #declaracion del metodo arrancar
    def arrancar(self):        
        print(f'El auto {self.marca} {self.modelo} arranco')

    #declaracion del metodo detener
    def detener(self):        
        print(f'El auto {self.marca} {self.modelo} se detuvo')

    #declaracion del metodo estacionar
    def estacionar(self):        
        print(f'El auto {self.marca} {self.modelo} se estaciono')


#se instancia el objeto auto
veyron = Auto('bugatti','veyron')

veyron.arrancar()

veyron.detener()

