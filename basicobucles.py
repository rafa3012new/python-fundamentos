print("Todos los enteros entre 0 y 150:\n")
for i in range(0,151):
    print(str(i))
print("\n")

print("todos los multiplos de 5 entre 5 y 1000\n")
for i in range(5,1001):
    if i % 5 == 0:
        print(f"el numero {i} es multiplo de 5")
print("\n")

print("se imprimira coding para los multiplos de 5 y codingdojo para los multiplos de 10, para los numeros entre 1 y 100\n")
for i in range(1,101):
    if i % 10 == 0:
        print("coding dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print(i)    
print("\n")

print("Suma de los enteros impares entre 0 y 500000\n")
suma = 0
for i in range(0,500001):
    if i % 2 != 0:
      suma+= i
print(f"la suma de los numeros impares entre 0 y 500,000 es : {suma} \n")
print("\n")

print("Cuenta regresiva desde 2018 de 4 en 4 hasta 0\n")
for i in range(2018,0,-4):
    print(i)
print("\n")

print("Contador Flexible lownum = 1, highnum = 1000, mult = 7 :")
print("\n")
lownum = 1
highnum = 1000
mult = 7
for i in range(lownum,highnum+1):
    if i % mult == 0:
      print(i)
print("\n")
print("fin del programa ciclos")

