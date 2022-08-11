class Auto():
    marca = ""
    modelo = ""
    ano = 0
    color = ""
    tipo = ""
    cilindros = 0

    #constructor
    def __init__(self, marca, modelo, ano, color, tipo, cilindros):
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
veyron = Auto('bugatti','veyron', 2012, 'verde', 'deportivo',8)
lamborgini = Auto('lamborgini','gallardo', 2014, 'negro', 'deportivo',10)

veyron.arrancar()

lamborgini.arrancar()