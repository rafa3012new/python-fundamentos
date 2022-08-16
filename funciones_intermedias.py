#se declaran funciones de los diccionarios
def iteratelistdictionary(lista):
  try:  
    for i in range(0,len(lista)):
      x= list(lista[i].items())
      print(x[0][0] + " - " + x[0][1] + " , " + x[1][0] + " - " + x[1][1] + " , " + x[2][0] + " - " + x[2][1],end='\n')
    
    return 'fin de la impresion de la Lista\n'
  except:
    return 'error al procesar la lista\n' 


def iteratelistdictionarykey(lista,clave):
  try:  
    for i in range(0,len(lista)):
      x= lista[i].get(clave)
      print(x,end='\n')
    
    return 'fin de la impresion de la Lista\n'
  except:
    return 'error al procesar la lista\n' 


def iteratedictionarylist(dictionary):
  try:  
    for x in (dictionary):
      print(str(len(dictionary[x])) + " " + x ,end='\n')
      for i in range(0, len(dictionary[x])):
        print(dictionary[x][i])
      print("\n\n") 
    print("\n")  
    
    return 'fin de la impresion del Diccionario\n'
  except:
    return 'error al procesar el Diccionario\n' 


#lista de diccionarios 1
consolasvideojuegos = [
    {'Marca':'Sony','Consola':'Playstation 5', 'Año':'2020'},
    {'Marca':'Microsoft','Consola':'Xbox Series X', 'Año':'2020'},
    {'Marca':'Nintendo','Consola':'Switch', 'Año':'2017'},
    {'Marca':'Sony','Consola':'Playstation 4', 'Año':'2013'},
    {'Marca':'Microsft','Consola':'Xbox One', 'Año':'2013'},
    {'Marca':'Nintendo','Consola':'Wii U', 'Año':'2012'}
]

#Diccionarios de Listas
dojo = {
    'ubicaciones':['San Jose','Seattle','Dallas','Chicago','Tulsa','DC','Burbank'],
    'instructores':['Michael','Amy','Eduardo','Josh','Graham','Patrick','Minh','Devon']
}

#Lista X
x = [ [5,2,3], [10,8,9] ] 

#Diccionario estudiantes
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#diccionario directorio_deportes
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

#diccionario z
z = [ {'x': 10, 'y': 20} ]


print("\n\n")

#se imprime la lista inicialmente
print("Lista x antes de la modificacion ", end='')
print(x, end='\n')

#se modifica la lista
x[1][0] = 15


#se imprime la lista despues de la modificacion
print("Lista x despues de la modificacion ", end='')
print(x,end='\n\n')



#se imprime la lista estudiantes incialmente, 
#el parametro end='' en print hace que la siguiente linea imprima al lado del print
print("Lista estudiantes antes de la modificacion ", end='')
print(estudiantes,end='\n')

#se modifica la lista
estudiantes[0].update({'last_name':'Bryant'})

#se imprime la lista despues de la modificacion
#el parametro end='' en print hace que la siguiente linea imprima al lado del print
print("Lista estudiantes despues de la modificacion ", end='')
print(estudiantes,end='\n\n')



#se imprime el diccionario directorio deportes incialmente, 
#el parametro end='' en print hace que la siguiente linea imprima al lado del print
print("Diccionario directorio deportes antes de la modificacion ", end='')
print(directorio_deportes,end='\n')

#se modifica el diccionario
# directorio_deportes[0].update({'last_name':'Bryant'})
directorio_deportes["fútbol"][0] = "Andres"

#se imprime el diccionario directorio deportes despues de la modificacion
#el parametro end='' en print hace que la siguiente linea imprima al lado del print
print("Diccionario directorio_deportes despues de la modificacion ", end='')
print(directorio_deportes,end='\n\n')



#se imprime la lista z incialmente, 
#el parametro end='' en print hace que la siguiente linea imprima al lado del print
print("Lista z antes de la modificacion ", end='')
print(z,end='\n')

#se modifica la lista
z[0]['y'] = 30

#se imprime la lista z despues de la modificacion
#el parametro end='' en print hace que la siguiente linea imprima al lado del print
print("lista z despues de la modificacion ", end='')
print(z, end='\n\n')


#imprimiendo la lista de diccionarios
print("lista de diccionarios consolasvideojuegos antes de ser iterada", end='\n\n')
print(consolasvideojuegos,end='\n\n')

#se itera la lista de diccionarios consolasvideojuegos
procesar = iteratelistdictionary(consolasvideojuegos)

print("\n")
print(procesar, end = '\n\n')

print("imprimiendo el contenido del key 'Marca' en el diccionario",end='\n\n')

#se itera la lista de diccionarios consolasvideojuegos
procesar = iteratelistdictionarykey(consolasvideojuegos,'Marca')

print("\n")
print(procesar, end = '\n\n')

print("imprimiendo el contenido del key 'Consola' en el diccionario",end='\n\n')

#se itera la lista de diccionarios consolasvideojuegos
procesar = iteratelistdictionarykey(consolasvideojuegos,'Consola')

print("\n")
print(procesar, end = '\n\n')


print("imprimiendo el contenido del key 'Año' en el diccionario",end='\n\n')

#se itera la lista de diccionarios consolasvideojuegos
procesar = iteratelistdictionarykey(consolasvideojuegos,'Año')

print("\n")
print(procesar, end = '\n\n')


#imprimiendo el diccionario de lista
print("diccionario de listas dojo antes de ser iterado", end='\n\n')
print(dojo,end='\n\n')

print(iteratedictionarylist(dojo),end='\n\n')

print("\n\n presione una tecla para finalizar el programa...")
input()
