#declaraciones de las funciones

def countdown(num):
    list = []
    for i in range(num,-1,-1):
      list.append(i)
    return list

def printreturn(list):
    if len(list) > 1:
      print("imprimiendo el primer valor de la lista : " + list[0])
      return list[1]
    else:
        print("introduzca una lista con al menos 2 elementos")  

def firstpluslen(list):
    if len(list) > 1:
      return int(list[0]) + len(list)
    else:
        print("introduzca una lista con al menos 2 elementos")  

def valminussecond(list):
    newlist = []
    comparevalue = 0
    
    if len(list) > 1:
      #second value of the list
      comparevalue = list[1]
      if list[0] > list[1]:
        newlist.append(list[0])
      if len(list) > 2:  
        for i in range(2, len(list)):
          if list[i] > list[1]:
            newlist.append(list[i])
      if len(newlist) > 2:
        return newlist
      else:
        return False      
    else:
        print("por favor introduzca uana lista con mas de un valor")
        return False    

def lenvalue(len, value):
  lista = []
  for i in range(0, len):
    lista.append(value)
  return lista

#ejecuciones de la funciones


#funcion countdown() - cuenta regresiva
print("introduzca un numero")
valor = int(input().strip())
print("imprimiendo el valor devuelto por la funcion countdown : " + str(countdown(valor)))

#funcion printreturn() - imprimir y devolver
print("\nintroduzca dos numeros")
valor1 = input().strip()
valor2 = input().strip()
lista = []
lista.append(valor1)
lista.append(valor2)
print("imprimiendo el valor devuelto por la funcion printreturn : " + printreturn(lista))

#funcion firstpluslen() - primero mas longitud
print("\nintroduzca dos numeros")
valor1 = input().strip()
valor2 = input().strip()
lista = []
lista.append(valor1)
lista.append(valor2)
print("imprimiendo el valor devuelto por la funcion firstpluslen : " + str(firstpluslen(lista)))

#funcion valminussecond - valores mayores que el segundo

#lista de valores a comparar con el segundo valor
listavalores = [56,3,1,0,2,45,84,11,5]
#agregando este caracter al final hara que el proximo print se haga en la misma linea
print("\nla lista de valores : ", end='')
#se imprime la misma lista de valores
print(listavalores)
#se imprime la ista despues de procesada
print("\nimprimiendo el valor devuelto por la funcion valminussecond : " + str(valminussecond(listavalores)))

#funcion largo valor
print("\nintroduzca el largo de la lista")
valor1 = input().strip()
print("\nintroduzca el valor de la lista")
valor2 = input().strip()
print("imprimiendo el valor devuelto por la funcion firstpluslen : " + str(lenvalue(int(valor1),int(valor2))))


#fin del programa
print("\n\n\n fin del programa presione una tecla para finalizar")
input()
