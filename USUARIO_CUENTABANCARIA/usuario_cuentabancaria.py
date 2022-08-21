import datetime
import utilidades_basicas

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BACKGROUNDWHITE = '\033[35;47m'

class usuario:
    #atriuto de la clase
    tipo_usuario = 'Regular'
    
    #contructor de objetos de la clase
    def __init__(self,iduser,name,email,cuentas,operacion):
      self.iduser = iduser
      self.name = name
      self.email = email
      self.cuentas = cuentas
      self.maxcuentas = 10
      self.operacion = operacion

    def verificarcuenta(self,campo,valor):
      for i in self.cuentas:
        if i[campo] == valor:
          return True
      else:
        return False    


    #metodo del objeto usuario que permite consultar cuentas
    def listarcuentas(self):
      if len(self.cuentas) > 0:
        listacuentas = []
        listatemp = []
        listacampos = ['No.','num cuenta','tipo cuenta','fecha apertura','saldo']
        x = 1
        for i in self.cuentas:
          listatemp = list(i.values())
          listatemp.insert(0,str(x))
          listatemp.pop(len(listatemp)-1)
          listacuentas.append(listatemp)     
          x+= 1
        print(bcolors.CYAN+"Listado de cuentas del Cliente"+bcolors.ENDC,end="\n\n")
        utilidades_basicas.printgrid(listacampos,listacuentas,'*',17)
        print("\n\n")
      else:
        print(bcolors.YELLOW+"no hay registros para mostrar..."+bcolors.ENDC,end='\n\n')        


    #metodo del objeto usuario que permite agregar nueva cuenta
    def newcuenta(self, apertura):  
      try:
        self.cuentas.append(apertura)
        return True
      except:
        return False

    #funcion que permite eliminar una cuentas
    def eliminarcuentas(self):
      if len(self.cuentas) > 0:
        listacuentas = []
        listatemp = []
        listaindices = []
        listacampos = ['No.','num cuenta','tipo cuenta','fecha apertura','saldo']
        x = 1
        for i in self.cuentas:
          listatemp = list(i.values())
          listatemp.insert(0,str(x))
          listatemp.pop(len(listatemp)-1)
          listacuentas.append(listatemp)
          listaindices.append(listatemp[0])
          x+= 1
        print(bcolors.CYAN+"Listado de cuentas del Cliente"+bcolors.ENDC,end="\n\n")
        utilidades_basicas.printgrid(listacampos,listacuentas,'*',17)
        print("\n\n")
     
        cond2 = False
        print("\n")        
        while cond2 == False:
          print("Seleccione la cuenta (No.) que desea eliminar :",end='')
          Ncuenta = input()
          cond2 = Ncuenta in (listaindices)
          if cond2 == False:
            print(bcolors.RED+"debe seleccionar una cuenta de la lista para eliminar..."+bcolors.ENDC)
          else:
            print("se eliminara la cuenta : " + Ncuenta + " Realmente desea eliminarla? S/N")
            if input() in ['S','s']:
              del self.cuentas[int(Ncuenta.strip())-1]
              print(bcolors.YELLOW+"La Cuenta " + Ncuenta + " fue eliminada..."+bcolors.ENDC)
              input()
              return True
        print("\n")
      else:
        print(bcolors.YELLOW+"no hay registros para eliminar..."+bcolors.ENDC,end='\n\n')        
   
    

#funcion que permite depositar en una cuenta
def depositarcuentas(objetousuario):
  if len(objetousuario.cuentas) > 0:
    listacuentas = []
    listatemp = []
    listaindices = []
    listacampos = ['No.','num cuenta','tipo cuenta','fecha apertura','saldo']
    x = 1
    for i in objetousuario.cuentas:
      listatemp = list(i.values())
      listatemp.insert(0,str(x))
      listatemp.pop(len(listatemp)-1)
      listacuentas.append(listatemp)     
      listaindices.append(listatemp[0])
      x+= 1
    

    print(bcolors.CYAN+"Listado de cuentas del Cliente"+bcolors.ENDC,end="\n\n")
    utilidades_basicas.printgrid(listacampos,listacuentas,'*',17)
    print("\n\n\n")
     
    cond = False
    while cond == False:
      print("Seleccione la cuenta (No.) a la que le desea depositar (0 para salir) : ",end='')
      Ncuenta = input()
      if Ncuenta == '0':
        print("Se cancelo el deposito...",end='\n\n')
        return
      else:  
        cond = Ncuenta in (listaindices)
        if cond == False:
          print(bcolors.RED+"debe seleccionar una cuenta de la lista para depositar..."+bcolors.ENDC)
        else:
          #se debe borrar la pantalla
          utilidades_basicas.limpiar()    
          print("\n\n")
          
          #id usuario y nombre de usuario
          print("Usuario : " + objetousuario.iduser + "   -   " + objetousuario.name, end = '\n\n')
          #se debe mostrar la info cuenta a la que se va a depositar
          print("Cuenta No. : " + objetousuario.cuentas[int(Ncuenta.strip())-1]['num_cuenta'] + "   Saldo : " + objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'],end="\n\n")
          #se imprime la fecha del deposito
          print("La fecha de deposito es : " + str(datetime.date.today()),end='\n\n')
          #se debe mostrar la info cuenta a la que se va a depositar
          montodeposito = validar_lectura("Introduzca el Monto a Depositar : ","numero")
          print("\n\n")
          #print("Introduzca la Fecha del Deposito")
          cond2 = False
          while cond2 == False:
            print("Esta seguro que desea realizar el deposito S/N?")
            respuesta = input()
           
            if respuesta in ["S","s"]:
              montotemp = objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'].strip()
              montotemp = float(montotemp) + float(montodeposito.strip())
              objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'] = str(montotemp)
              print("\n\n")
              print(bcolors.YELLOW+"El deposito fue realizado"+bcolors.ENDC)
            else:
              print("No se realizo el desposito...")
            cond2 = True        
        print("\n")
    

#funcion que permite retirar de una cuenta
def retirarcuentas(objetousuario):
  if len(objetousuario.cuentas) > 0:
    listacuentas = []
    listatemp = []
    listaindices = []
    listacampos = ['No.','num cuenta','tipo cuenta','fecha apertura','saldo']
    x = 1
    for i in objetousuario.cuentas:
      listatemp = list(i.values())
      listatemp.insert(0,str(x))
      listatemp.pop(len(listatemp)-1)
      listacuentas.append(listatemp)     
      listaindices.append(listatemp[0])
      x+= 1
    

    print(bcolors.CYAN+"Listado de cuentas del Cliente"+bcolors.ENDC,end="\n\n")
    utilidades_basicas.printgrid(listacampos,listacuentas,'*',17)
    print("\n\n\n")
     
    cond = False
    while cond == False:
      print("Seleccione la cuenta (No.) de la que desea hacer el retiro, presione 0 para salir : ",end='')
      Ncuenta = input()
      if Ncuenta == '0':
        print("Se saldra del modulo de retiros")
        input()
        return
      else:  
        cond = Ncuenta in (listaindices)
        if cond == False:
          print(bcolors.RED+"debe seleccionar una cuenta de la lista para retirar..."+bcolors.ENDC)
        else:
          #se debe borrar la pantalla
          utilidades_basicas.limpiar()    
          print("\n\n")
          
          #id usuario y nombre de usuario
          print("Usuario : " + objetousuario.iduser + "   -   " + objetousuario.name, end = '\n\n')
          #se debe mostrar la info cuenta a la que se va a depositar
          print("Cuenta No. : " + objetousuario.cuentas[int(Ncuenta.strip())-1]['num_cuenta'] + "   Saldo : " + objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'],end="\n\n")
          #se imprime la fecha del deposito
          print("La fecha del retiro es : " + str(datetime.date.today()),end='\n\n')
          #se debe mostrar la info cuenta a la que se va a depositar
          montoretiro = validar_lectura("Introduzca el Monto a Retirar : ","numero")
          print("\n\n")
          montotemp = objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'].strip()
        
          if  float(montoretiro) > float(montotemp):
            print(bcolors.RED+"Saldo insuficiente"+bcolors.ENDC,end='\n\n')          
          else:
            cond2 = False
            while cond2 == False:
              print("Esta seguro que desea realizar el retiro S/N?")
              respuesta = input()
              if  respuesta in ["S","s"]:
                montotemp = float(montotemp) - float(montoretiro.strip())
                objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'] = str(montotemp)
                print("\n\n")
                print(bcolors.YELLOW+"El retiro fue realizado"+bcolors.ENDC,end='\n\n')
              else:
                print("No se realizo el retiro")  

              cond2 = True  
        print("\n")

#funcion que permite limpiar la pantalla y agregar una pausa
def micls():
    print("presione una tecla para continuar")
    input()
    utilidades_basicas.limpiar()    
    print("\n\n")


#funcion para validar lectura
def validar_lectura(etiqueta,tipo_validacion):
  cond = True
  while cond:

    print(etiqueta,end='')
    variable = input()

    if tipo_validacion == 'numero':
      try:
        float(variable)
        return variable       
      except:
        print(bcolors.RED + "error en lectura de numero, porfavor introducir un valor numerico correcto..." + bcolors.ENDC,end='\n\n')

    if tipo_validacion == 'fecha':
      try:
        day, month, year = variable.split('/')
        variable  = str(datetime.date(int(year),int(month),int(day)))
        return variable       
      except:
        print(bcolors.RED + "error en lectura de fecha, porfavor introducir un valor de fecha correcto..." + bcolors.ENDC,end='\n\n')

  return variable


#funcion para crerar una cuenta
def crearcuenta(objeto):
   numerocuenta = ''
   tipocuenta = ''
   montoapertura = 0.0
   fechaapertura = ''
   diccionario = {}
   cond = True
  
   while cond:
     print(bcolors.CYAN + "Menu de nueva cuenta" + bcolors.ENDC,end='\n\n')
     
     cond2 = True
     print("\n")
     while cond2:
       print("Introduzca el numero de cuenta : ",end='')
       numerocuenta = input()
       if numerocuenta.strip() == '':
         print(bcolors.RED+"\n\n Numero de cuenta no puede estar en blanco"+bcolors.ENDC,end="\n\n")
       else:         
         cond2 = objeto.verificarcuenta("num_cuenta",numerocuenta.strip())     
         if cond2:
           print(bcolors.RED+"\n\n Numero de cuenta ya existe"+bcolors.ENDC,end="\n\n")
  
     cond2 = False
     print("\n")        
     while cond2 == False:
       print("Introduzca el tipo de cuenta [1-corriente 2-ahorro] : ",end='')
       tipocuenta = input()
       cond2 = tipocuenta in (['1','2'])
       if cond2 == False:
         print("tipo de cuenta invalida, porfavor seleccione los tipos de cuentas indicados")
       else:
         if tipocuenta == '1':
           tipocuenta = 'corriente'  
         else:
           tipocuenta = 'ahorro'
     print("\n")

     montoapertura = validar_lectura("Introduzca el monto de apertura : ",'numero')
     print("\n")

     fechaapertura = validar_lectura("Introduzca la fecha de apertura en formato dd/mm/yyy : ",'fecha')
     print("\n\n")
     
     print("Datos correctos? [S/N]",end='')
     op = input()
     print("\n\n")
     if op in (['S','s']):
       print("\n\n")
       print("Desea crear la cuenta? S/N")
       op2 = input()
       if op2 in (['S','s']):
         print("\n\nCreando la cuenta...",end='\n\n')
         cantidad = str(len(objeto.cuentas)+1)
         listaoperaciones = []
         montoapertura = float(montoapertura.strip())
         montoapertura = str(montoapertura)
         operacion = {'fecha':fechaapertura,'tipo':'apertura','monto':montoapertura,'realizado':'titular'}
         listaoperaciones.append(operacion)
         diccionario = {'num_cuenta':numerocuenta,'tipo_cuenta':tipocuenta,'fecha_apertura':fechaapertura, 'saldo':montoapertura, 'operaciones':listaoperaciones}
       else:
         print(bcolors.RED +"No se creo la cuenta"+bcolors.ENDC,end='\n\n')
       cond = False  
     else:    
       print(bcolors.RED + "datos incorrectos - vuelva a introducir los datos" + bcolors.ENDC,end='\n\n')

   return diccionario

#funcion para seleccionar el usuario de los ya creados
def seleccionarusuario(listausuarios):
  
  if len(listausuarios) > 0:
    listacampos = ['No', 'Id Usuario','Usuario','Correo']
    superlista = []
    listaindices = []
    x = 1
    for i in listausuarios:
      nuevalista = []
      nuevalista.append(str(x))
      listaindices.append(str(x))
      nuevalista.append(i.iduser)
      nuevalista.append(i.name)
      nuevalista.append(i.email)
      superlista.append(nuevalista)
      x+=1
    else:
      print(bcolors.YELLOW+"no hay registros para mostrar..."+bcolors.ENDC,end='\n\n')        
  

    print(bcolors.CYAN+"Listado de Usuarios"+bcolors.ENDC,end="\n\n")
    utilidades_basicas.printgrid(listacampos,superlista,'*',22)
    print("\n\n")


    cond2 = False
    print("\n")        
    while cond2 == False:
      print("Seleccione el usuario (No.) con el que desea trabajar :",end='')
      Nousuario = input()
      cond2 = Nousuario in (listaindices)
      if cond2 == False:
        print(bcolors.RED+"debe seleccionar un usuario de la lista, porfavor seleccione el usuario correcto"+bcolors.ENDC)
      else:
        Nousuario = int(Nousuario) - 1
        break

    print("\n")
    
    return Nousuario


#cuerpo principal del programa
cadena_bienvenida = bcolors.PURPLE + "Menu de Dojo Bank" + bcolors.ENDC

lista_usuarios = []

#se instancia la clase usuario 
lista_usuarios.append(usuario('RAFFER1980','Rafael Fernandez',' rafa3012new@gmail.com',[],[]))
#se instancia la clase usuario 
lista_usuarios.append(usuario('ELOMSK1970','Elon Musk','ElonMuskw@gmail.com',[],[]))    
#se instancia la clase usuario 
lista_usuarios.append(usuario('BILGAT1960','Bill Gates','billgates@gmail.com',[],[]))

usuario_actual = lista_usuarios[0]

cond = True

utilidades_basicas.limpiar()        
print("\n\n")
    
while cond:
  

  print(cadena_bienvenida,end='\n\n')

  print("Usuario : " + usuario_actual.name + "  - Id : " + usuario_actual.iduser,end='\n\n')
      
  print(bcolors.BLUE + "[1] Para seleccionar usuario",end='\n')
  print("[2] Para consultar una cuenta",end='\n')
  print("[3] Para crear una cuenta",end='\n')
  print("[4] Para eliminar una cuenta",end='\n')
  print("[5] Para hacer un deposito",end='\n')
  print("[6] Para hacer un retiro",end='\n')
  print("[7] Para salir del sistema"+ bcolors.ENDC,end='\n\n')

  print("Indique la opcion que desea seleccionar : ",end='')
  
  opcion = input()
  
  if opcion not in(['1','2','3','4','5','6','7', '8', '9']):
    print ('\n'+bcolors.RED+"opcion invalida"+ bcolors.ENDC,end='\n\n')

    micls()
  
  #Se crea una cuenta
  if opcion == '3':
    utilidades_basicas.limpiar()    
    print("\n\n")
    diccionarioprueba = crearcuenta(usuario_actual)
    #se debe saber si el diccionario esta vacio o no  
    # si el diccionario no esta vacio se agraga a la instancia
    if len(diccionarioprueba) > 0:
      if usuario_actual.newcuenta(diccionarioprueba):
        print(bcolors.GREEN+"se creo la cuenta satisfactoriamente"+bcolors.ENDC,end='\n\n')
        micls()

      else:  
        print(bcolors.RED+"error al crear la cuenta"+bcolors.ENDC,end='\n\n')    
        micls()
    
  #Se consultan las cuentas
  if opcion == '2':
    utilidades_basicas.limpiar()    
    
    print("\n\n")
    usuario_actual.listarcuentas()

    micls()


  #Se selecciona el usuario
  if opcion == '1':
    utilidades_basicas.limpiar()    
    
    print("\n\n")
    nuevousuario = seleccionarusuario(lista_usuarios)

    usuario_actual = lista_usuarios[nuevousuario]

    micls()


  #Se elimina una cuenta
  if opcion == '4':
    utilidades_basicas.limpiar()    
    
    print("\n\n")
    usuario_actual.eliminarcuentas()

    micls()


  #Se deposita a una cuenta
  if opcion == '5':
    utilidades_basicas.limpiar()    
    
    print("\n\n")

    depositarcuentas(usuario_actual)

    micls()


  #Se deposita a una cuenta
  if opcion == '6':
    utilidades_basicas.limpiar()    
    
    print("\n\n")

    retirarcuentas(usuario_actual)

    micls()


  #Se sale del sistema
  if opcion == '7':
     cond = False  

print('\n\n'+ "presione un tecla para cerrar el programa...")   
input()


