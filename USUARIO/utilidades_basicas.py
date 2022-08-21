import os

def limpiar():
  os.system('cls')


def printgrid(fields=[], data=[], caracter = "*", separacion = 12):
  #Ciclo General que imprime la Grid
  maxlargo = len(fields)*(separacion-2)
  # print(maxlargo)
  cadena = ''

  #se imprime una linea
  for i in range(0,maxlargo+separacion-6):
    print(caracter,end='')

  print(caracter)

  #se imprimen los titulos
  for i in range(0,len(fields)):
    cadena = caracter + fields[i].center(separacion-1) 
    print(cadena, end= '')

  print(caracter.center(int(separacion/2)-5))

  # #se imprime una linea
  for i in range(0,maxlargo+separacion-5):
    print(caracter,end='')


  print("\r")

  for i in range(0, len(data)):
      for j in range(0, len(data[i])): 
         cadena = caracter + data[i][j].center(separacion-1) 
         print(cadena,end='')
      print(caracter.center(int(separacion/2)-5))
  
  # print("\r")

  # #se imprime una linea
  for i in range(0,maxlargo+separacion-5):
    print(caracter,end='')


def digitos(numeros = "0"):

  matriz = []
  matriz = [[" " for i in range(5)] for j in range(10)]
  print_matriz = []
  print_matriz = [[" " for i in range(1)] for j in range(5)]
  caracter = " "
  digito = 0
  
 
  # Digito 0
  matriz[0][0] = "###"
  matriz[0][1] = "# #"
  matriz[0][2] = "# #"
  matriz[0][3] = "# #"
  matriz[0][4] = "###"

  # Digito 1
  matriz[1][0] = "  #"
  matriz[1][1] = "  #"
  matriz[1][2] = "  #"
  matriz[1][3] = "  #"
  matriz[1][4] = "  #"

  # Digito 2
  matriz[2][0] = "###"
  matriz[2][1] = "  #"
  matriz[2][2] = "###"
  matriz[2][3] = "#  "
  matriz[2][4] = "###"

  # Digito 3
  matriz[3][0] = "###"
  matriz[3][1] = "  #"
  matriz[3][2] = "###"
  matriz[3][3] = "  #"
  matriz[3][4] = "###"

  # Digito 4
  matriz[4][0] = "# #"
  matriz[4][1] = "# #"
  matriz[4][2] = "###"
  matriz[4][3] = "  #"
  matriz[4][4] = "  #"

  # Digito 5
  matriz[5][0] = "###"
  matriz[5][1] = "#  "
  matriz[5][2] = "###"
  matriz[5][3] = "  #"
  matriz[5][4] = "###"

  # Digito 6
  matriz[6][0] = "###"
  matriz[6][1] = "#  "
  matriz[6][2] = "###"
  matriz[6][3] = "# #"
  matriz[6][4] = "###"

  # Digito 7
  matriz[7][0] = "###"
  matriz[7][1] = "  #"
  matriz[7][2] = "  #"
  matriz[7][3] = "  #"
  matriz[7][4] = "  #"

  # Digito 8
  matriz[8][0] = "###"
  matriz[8][1] = "# #"
  matriz[8][2] = "###"
  matriz[8][3] = "# #"
  matriz[8][4] = "###"

  # Digito 9
  matriz[9][0] = "###"
  matriz[9][1] = "# #"
  matriz[9][2] = "###"
  matriz[9][3] = "  #"
  matriz[9][4] = "###"
  
  for i in range(0,len(numeros)):
    caracter = numeros[i:i+1]
    digito = int(caracter)
    print_matriz[0][0] = print_matriz[0][0] + matriz[digito][0] + "  "  
    print_matriz[1][0] = print_matriz[1][0] + matriz[digito][1] + "  "  
    print_matriz[2][0] = print_matriz[2][0] + matriz[digito][2] + "  "  
    print_matriz[3][0] = print_matriz[3][0] + matriz[digito][3] + "  "  
    print_matriz[4][0] = print_matriz[4][0] + matriz[digito][4] + "  "  
    
  print(print_matriz[0][0])    
  print(print_matriz[1][0])    
  print(print_matriz[2][0])    
  print(print_matriz[3][0])    
  print(print_matriz[4][0])    

    
# cad_num = input("Introduzca los Digitos : ")

# digitos(cad_num)
    







# limpiar()

# print("\n\n Demo de Tabla",end='\n\n')


# campos = ["No.", "ID", "TIPO_ID", "NOMBRE", "APELLIDO", "TELEFONO", "DIRECCION"]
# datos = [
#          ["01","54321","Pasaporte", "Clark", "Kent", "555555555", "USA"],
#          ["02","12345","Pasaporte", "Bruce", "Wayne", "444444444", "USA"], 
#          ["03","67890","Pasaporte", "Tony", "Stark", "111111111", "USA"],
#          ["04","09876","Pasaporte", "Natasha", "Romanof", "222222222", "RUSSIA"],
#          ["05","12389","Pasaporte", "Dayana", "Prince", "333333333", "USA"], 
#          ["06","32198","Pasaporte", "Jane", "Foster", "777777777", "USA"],
#          ["07","567098","Pasaporte", "Tony", "Stark", "000000000", "USA"],
#          ["08","654105","Pasaporte", "Bruce", "Banner", "666666666", "USA"],
#          ["09","446699","Pasaporte", "T", "Challa", "888888888", "WAKANDA"], 
#          ["10","110055","Pasaporte", "Logan", "Wolverine", "999999999", "CANADA"],
#          ]


# printgrid(campos,datos)

# print("\n\n numero de registros",end='\n\n')

# digitos(str(len(datos)))
