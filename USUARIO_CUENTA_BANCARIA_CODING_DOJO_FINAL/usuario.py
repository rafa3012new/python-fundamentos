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
      self.sobregiro = 0
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
      
        print("Usuario : " + self.iduser + " - " + self.name,end='\n\n')

        print(bcolors.CYAN+"Listado de cuentas del Cliente"+bcolors.ENDC,end="\n\n")
        utilidades_basicas.printgrid(listacampos,listacuentas,'*',17)
        print("\n\n")
      else:
        print(bcolors.YELLOW+"no hay registros para mostrar..."+bcolors.ENDC,end='\n\n')        


    def newcuenta(self, apertura):  
      #se agregar un item diccionario de cuenta nueva a la listas de cuentas de ese cliente
      try:
        self.cuentas.append(apertura)
        return True
      except:
        return False
    
    def creditcuenta(self, tipo_operacion, montoop, indice_cuenta, realizado_por):  
      try:
        
        #se actualiza el saldo de la cuenta que es el anterior mas
        monto_anterior = float(self.cuentas[indice_cuenta]['saldo'].strip())
        monto_registrar = "{:0.2f}".format(monto_anterior+float(montoop.strip()))
        self.cuentas[indice_cuenta]['saldo'] = monto_registrar
        
        #se agregan los movimientos
        operacion = {'fecha':str(datetime.date.today()),'tipo':tipo_operacion,'monto':"{:0.2f}".format(float(montoop.strip())),'realizado':realizado_por}             
        self.cuentas[indice_cuenta]['operaciones'].append(operacion)
        
        #para que funcionen los metodos encadenados
        return self
      except Exception as e:
        print(bcolors.RED+"hubo una excepcion... no se pudo efectuar el credito a la cuenta"+bcolors.ENDC)
        print(str(e))
        input()
        return None

    def debitcuenta(self, tipo_operacion, montoop, indice_cuenta, realizado_por):  
      try:
        
        #se actualiza el saldo de la cuenta que es el anterior mas
        monto_anterior = float(self.cuentas[indice_cuenta]['saldo'].strip())
        if float(montoop.strip()) > monto_anterior:
          print("Saldo insuficiente para realizar esta operacion")
          return False
        else:
          monto_registrar = "{:0.2f}".format(monto_anterior-float(montoop.strip()))
          self.cuentas[indice_cuenta]['saldo'] = monto_registrar
        
          #se agregan los movimientos
          operacion = {'fecha':str(datetime.date.today()),'tipo':tipo_operacion,'monto':"{:0.2f}".format(float(montoop.strip())),'realizado':realizado_por}             
          self.cuentas[indice_cuenta]['operaciones'].append(operacion)
        
        #para que funcionen los metodos encadenados
        return self
      except:
        print(bcolors.RED+"hubo una excepcion... no se pudo efectuar el debito a la cuenta"+bcolors.ENDC)
        input()
        return False


    #metodo del objeto usuario que permite eliminar una cuentas
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


        print(bcolors.CYAN+"Usuario Actual "+bcolors.ENDC,end="\n\n")
        print(self.iduser + " " + self.name,end='\n\n')

        print(bcolors.CYAN+"Listado de cuentas del Cliente"+bcolors.ENDC,end="\n\n")
        utilidades_basicas.printgrid(listacampos,listacuentas,'*',17)
        print("\n\n")
     
        cond2 = False
        print("\n")        
        while cond2 == False:
          print("Seleccione la cuenta (No.) que desea eliminar, o presione 0 para cancelar la eliminacion :",end='')
          Ncuenta = input()
          
          if Ncuenta.strip() == '0':
            return None

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
   
    
def validardoscuentas(listausuarios, imprimir = False):
  contador = 0
  print("\n\n")
  print("antes del for",end='\n\n')
  for i in listausuarios:   
    if len(i.cuentas) > 0:
      print("imprimiendo cuentas",end='\n\n')
      contador+= len(i.cuentas)
      if imprimir:
        print("el usuario " + i.iduser + " tiene las siguientes cuentas : ",end='\n\n')
        print(i.cuentas,end='\n\n')
      if contador >= 2:
        return True  
    else:
       if imprimir:
         print("el usuario " + i.iduser + " no tiene cuentas",end='\n\n')  
  return False



def vercuentas(listausuarios):
  print("\n\n")
  print("antes del for",end='\n\n')
  for i in listausuarios:   
    if len(i.cuentas) > 0:
      print("imprimiendo cuentas",end='\n\n')
      print("el usuario " + i.iduser + " tiene las siguientes cuentas : ",end='\n\n')
      print(i.cuentas,end='\n\n')
    else:
      print("el usuario " + i.iduser + " no tiene cuentas",end='\n\n')  
  return False



def contarcuentas(listausuarios):  
  contador = 0

  for i in listausuarios:   
    if len(i.cuentas) > 0:
      contador+= len(i.cuentas)

  return contador


#funcion que permite seleccionar un usuario
def seleccionarusuario(listausuarios,usuarioactual):
  
  if len(listausuarios) > 0:
    listacampos = ['No', 'Id Usuario','Usuario','Correo']
    superlista = []
    listaindices = []
    x = 1
    for i in listausuarios:
      if i.iduser != usuarioactual.iduser:
        nuevalista = []
        nuevalista.append(str(x))
        listaindices.append(str(x))
        nuevalista.append(i.iduser)
        nuevalista.append(i.name)
        nuevalista.append(i.email)
        superlista.append(nuevalista)
        x+=1

    print(bcolors.CYAN+"Usuario Actual "+bcolors.ENDC,end="\n\n")
    print(usuarioactual.iduser + " " + usuarioactual.name,end='\n\n')
    
    print(bcolors.CYAN+"Listado de Usuarios"+bcolors.ENDC,end="\n\n")
    utilidades_basicas.printgrid(listacampos,superlista,'*',22)
    print("\n\n")
   

    cond2 = False
    print("\n")        
    while cond2 == False:
      print("Seleccione el usuario (No.) con el que desea trabajar, o presione 0 para continuar con el actual :",end='')
      Nousuario = input()
      Nousuario = Nousuario.strip()
      
     
      if Nousuario == '0':
        return None
      else:
        cond2 = Nousuario in (listaindices)
        if cond2 == False:
          print(bcolors.RED+"debe seleccionar un usuario de la lista, porfavor seleccione el usuario correcto"+bcolors.ENDC)
        else:
          x = 0
          for i in listausuarios:
            if superlista[int(Nousuario)-1][1].strip() == i.iduser.strip():
              Nousuario = str(x)
              break
            
            x+= 1

          break


    return int(Nousuario)




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
    

    print(bcolors.CYAN+"Usuario Actual "+bcolors.ENDC,end="\n\n")
    print(objetousuario.iduser + " " + objetousuario.name,end='\n\n')

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
          print("Usuario : " + objetousuario.iduser + "   -   " + objetousuario.name, end = '\n')
          #se debe mostrar la info cuenta a la que se va a depositar
          print("Cuenta No. : " + objetousuario.cuentas[int(Ncuenta.strip())-1]['num_cuenta'] + "   Saldo : " + objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'],end="\n\n")
          #se imprime la fecha del deposito
          print("La fecha de deposito es : " + str(datetime.date.today()),end='\n')
          #se debe mostrar la info cuenta a la que se va a depositar
          montodeposito = validar_lectura("Introduzca el Monto a Depositar : ","numero")
          print("\n")
          cond2 = False
          while cond2 == False:
            print("Esta seguro que desea realizar el deposito S/N?")
            respuesta = input()
           
            if respuesta in ["S","s"]:
              
              #se invoca el metodo que deposita
              objetousuario.creditcuenta('deposito',montodeposito,int(Ncuenta.strip())-1,'titular')
              
              print("\n\n" + bcolors.YELLOW+"El deposito fue realizado"+bcolors.ENDC)
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
    

    print(bcolors.CYAN+"Usuario Actual "+bcolors.ENDC,end="\n\n")
    print(objetousuario.iduser + " " + objetousuario.name,end='\n\n')

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
          #se debe mostrar la info cuenta a la que se va a retirar
          print("Cuenta No. : " + objetousuario.cuentas[int(Ncuenta.strip())-1]['num_cuenta'] + "   Saldo : " + objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'],end="\n\n")
          #se imprime la fecha del deposito
          print("La fecha del retiro es : " + str(datetime.date.today()),end='\n\n')
          #se debe mostrar la info cuenta a la que se va a retirar
          montoretiro = validar_lectura("Introduzca el Monto a Retirar : ","numero")
          print("\n\n")
                    
          cond2 = False
          while cond2 == False:
              print("Esta seguro que desea realizar el retiro S/N?")
              respuesta = input()
              if  respuesta in ["S","s"]:

                objetousuario.debitcuenta('retiro',montoretiro,int(Ncuenta.strip())-1,'titular')

                print("\n\n")
                print(bcolors.YELLOW+"El retiro fue realizado"+bcolors.ENDC,end='\n\n')
                cond2 = True  
              elif respuesta in ["N","n"]:
                print("No se realizo el retiro")  
                cond2 = True    
    print("\n")




def depositos_nomina(lista_usuarios, fecha,montonom,empresa):
  #se hace un ciclo para todos los usuarios y sus cuentas
  x = 0
  monto_anterior = 0
  for i in lista_usuarios:
    cadena_metodos_encadenados = ''
    cadenausuario = repr(i)
    cadena_metodos_encadenados = 'i'
    if len(i.cuentas) > 0:
      idcuenta = 0
      for j in i.cuentas:
        if j['tipo_cuenta'] == 'corriente':
          cadena_metodos_encadenados+=  '.creditcuenta(\'dep_nomina\',' + '\'' + str(montonom) + '\', ' + str(idcuenta)  + ',\'coding dojo\')'        
        idcuenta+=1     
    try:
      eval(cadena_metodos_encadenados)
    except:
      print(bcolors.RED+"error al hacer los metodos encadenados, presione una tecla para continuar..."+bcolors.ENDC)
      input()
      return None
  
  print(bcolors.YELLOW+"Se realizaron los depositos de nomina!..."+bcolors.ENDC)
      
  
def cobro_impuestos(lista_usuarios, fecha,porcentaje,organismo):
  #se hace un ciclo para todos los usuarios y sus cuentas
  x = 0
  montotax = 0
  for i in lista_usuarios:
    cadena_metodos_encadenados = ''
    cadenausuario = repr(i)
    cadena_metodos_encadenados = 'i'

    if len(i.cuentas) > 0:
      idcuenta = 0
      for j in i.cuentas:
        montotax = float(j['saldo']) * (float(porcentaje)/100)
        cadena_metodos_encadenados+=  '.debitcuenta(\'Impuesto\',' + '\'' + str(montotax) + '\', ' + str(idcuenta)  + ',\'' + organismo + '\')'        
        idcuenta+=1     
    try:
      eval(cadena_metodos_encadenados)
    except:
      print(bcolors.RED+"error al hacer los metodos encadenados, presione una tecla para continuar..."+bcolors.ENDC)
      input()
      return None
  
  print(bcolors.YELLOW+"Se realizaron los debitos por impuesto del SII!..."+bcolors.ENDC)



def generar_intereses(lista_usuarios, fecha,porcentaje,organismo):
  #se hace un ciclo para todos los usuarios y sus cuentas
  x = 0
  montointerest = 0
  for i in lista_usuarios:
    cadena_metodos_encadenados = ''
    cadenausuario = repr(i)
    cadena_metodos_encadenados = 'i'

    if len(i.cuentas) > 0:
      idcuenta = 0
      for j in i.cuentas:
        if j['tipo_cuenta'] == 'ahorro':
          montointerest = float(j['saldo']) * (float(porcentaje)/100)
          cadena_metodos_encadenados+=  '.creditcuenta(\'Impuesto\',' + '\'' + str(montointerest) + '\', ' + str(idcuenta)  + ',\'' + organismo + '\')'        
        idcuenta+=1     
    try:
      eval(cadena_metodos_encadenados)
    except:
      print(bcolors.RED+"error al hacer los metodos encadenados, presione una tecla para continuar..."+bcolors.ENDC)
      input()
      return None
  
  print(bcolors.YELLOW+"Se generaron los intereses en cada cuenta de ahorros!..."+bcolors.ENDC)







#funcion que permite transferir desde una cuenta
def transferircuenta(objetousuario,lista_usuarios):
  
  #sub funcion 
  def imprimirdatosorigen(titulo,objeto,id,monto=""):
    print(bcolors.YELLOW+"Tranferencia"+bcolors.ENDC,end='\n\n')
    #se imprime la fecha de la transferencia
    print("Fecha de transferencia : " + str(datetime.date.today()),end='\t\t')
    if monto != "":
      cad = monto.format('{:0.2f}')
      print("Monto a Transferir  :  " + cad,end='\n\n')
    else:
      print("\n")  

    print (bcolors.CYAN+titulo+bcolors.ENDC,end='\n\n')
    #id usuario y nombre de usuario
    print("Usuario : " + objeto.iduser + " - " + objeto.name, end = '\t\t')
    #se debe mostrar la info cuenta a la que se va a transferir
    print("Cuenta No. : " + objeto.cuentas[id]['num_cuenta'] + " - " + objeto.cuentas[id]['tipo_cuenta'] + " - Saldo : " + objeto.cuentas[id]['saldo'],end="\n\n")
  
  #sub funcion 
  def imprimirdatosdestino(titulo,objeto,id,tipo):
    print (bcolors.CYAN+titulo+bcolors.ENDC,end='\n\n')
    #id usuario y nombre de usuario
    print("Usuario : " + objeto.iduser + " - " + objeto.name, end = '\t\t')
    if tipo == '2':
      #se debe mostrar la info cuenta a la que se va a transferir
      print(" Cuenta No. : " + objeto.cuentas[id]['num_cuenta'] + " - " + objeto.cuentas[id]['tipo_cuenta'] + " - Saldo : " + objeto.cuentas[id]['saldo'],end="\n\n")


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
      print("Seleccione la cuenta (No.) de la que desea hacer la transferencia, presione 0 para salir : ",end='')
      Ncuenta = input()
      if Ncuenta == '0':
        print("Se saldra del modulo de transferencias")
        input()
        return
      else:  
        cond = Ncuenta in (listaindices)
        if cond == False:
          print(bcolors.RED+"debe seleccionar una cuenta de la lista para iniciar la transferencia..."+bcolors.ENDC)
        else:
          #se debe borrar la pantalla
          utilidades_basicas.limpiar()    
          
          #se llama a la subfuncion imprimir datos
          imprimirdatosorigen("Datos de Origen de la Transferencia",objetousuario,int(Ncuenta.strip())-1,"")

        
          #se debe mostrar la info cuenta a la que se va a transferir
          montotranf = validar_lectura("Introduzca el Monto a Transferir : ","numero")
          montotemp = objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'].strip()
        
          if  float(montotranf) > float(montotemp):
            print("\n"+bcolors.RED+"Saldo insuficiente"+bcolors.ENDC,end='\n\n')          
          else:

            print ("\n"+bcolors.GREEN+"Datos de Destino de la Transferencia"+bcolors.ENDC,end='\n\n')
            #se lista el usuario
           
            if len(lista_usuarios) > 0:
              
              listacampos = ['No', 'Id Usuario','Usuario','Correo']
              superlista = []
              listaindices = []
              x = 1
              
              for y in lista_usuarios:
                nuevalista = []
                nuevalista.append(str(x))
                listaindices.append(str(x))
                nuevalista.append(y.iduser)
                nuevalista.append(y.name)
                nuevalista.append(y.email)
                superlista.append(nuevalista)
                x+=1
              
              print(bcolors.YELLOW+"Seleccione el Usuario destino de la transferencia"+bcolors.ENDC,end="\n\n")
              utilidades_basicas.printgrid(listacampos,superlista,'*',22)

              cond2 = False
              print("\n")        
              while cond2 == False:
                print("Seleccione el usuario (No.) destino de la transferencia: ",end='')
                Nousuario = input()
                cond2 = Nousuario in (listaindices)
                if cond2 == False:
                  print(bcolors.RED+"debe seleccionar un usuario de la lista, porfavor seleccione el usuario correcto"+bcolors.ENDC)
                else:
                  Nousuario = int(Nousuario) - 1
               
              user = lista_usuarios[Nousuario]
              
              # print("antes de limpiar")
              utilidades_basicas.limpiar()
              # print("despues3 de limpiar")

              #se llama a la subfuncion imprimir datos
              imprimirdatosorigen(bcolors.CYAN+"Datos de Origen de la Transferencia"+bcolors.ENDC,objetousuario,int(Ncuenta.strip())-1,montotranf)

              # print("\n")
              
              imprimirdatosdestino(bcolors.GREEN+"Datos de Destino de la Transferencia"+bcolors.ENDC,user,Nousuario,'1')


              if len(user.cuentas) > 0:
                listacuentasd = []
                listatempd = []
                listaindicesd = []
                x = 1
                
                for i in user.cuentas:
                  listatempd = list(i.values())
                  listatempd.insert(0,str(x))
                  listatempd.pop(len(listatempd)-1)
                  listacuentasd.append(listatempd)     
                  listaindicesd.append(listatempd[0])
                  x+= 1

                print("\n")

                print(bcolors.YELLOW+"Listado de cuentas del Cliente Destino"+bcolors.ENDC,end="\n\n")
                listacampos = ['No.','num cuenta','tipo cuenta','fecha apertura','saldo']
                utilidades_basicas.printgrid(listacampos,listacuentasd,'*',17)
                print("\n")

                cond = False
                while cond == False:
                  print("Seleccione la cuenta (No.) a la que desea hacer la transferencia, presione 0 para salir : ",end='')
                  Ncuentad = input()
                  if Ncuentad == '0':
                    print("Se saldra del modulo de transferencias")
                    input()
                    return
                  else:  
                    cond = Ncuentad in (listaindicesd)
                    if cond == False:
                      print(bcolors.RED+"debe seleccionar una cuenta de la lista para iniciar la transferencia..."+bcolors.ENDC)
                    else:
                       utilidades_basicas.limpiar()
                       #se llama a la subfuncion imprimir datos
                       imprimirdatosorigen(bcolors.CYAN+"Origen de la Transferencia"+bcolors.ENDC,objetousuario,int(Ncuenta.strip())-1,montotranf)
                       imprimirdatosdestino(bcolors.GREEN+"Destino de la Transferencia"+bcolors.ENDC,user,int(Ncuentad.strip())-1,'2')
                       print("\n")
                       cond2 = False
                       while cond2 == False:
                         print("Esta seguro que desea realizar el Transferencia S/N?")
                         respuesta = input()
                         if  respuesta in ["S","s"]:
                           print("realizando la transferencia",end='\n\n')
                           #se descuenta de la cuenta origen
                           
                           objetousuario.debitcuenta('debit_tranf',montotranf,int(Ncuenta.strip())-1,'Titular')

                          #  saldocuentaorigen = float(objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo']) - float(montotranf)
                          #  objetousuario.cuentas[int(Ncuenta.strip())-1]['saldo'] = "{:0.2f}".format(saldocuentaorigen)
                           #se agrega el movimento al registro orgigen
                           #se abona en la cuenta destino
                           
                           user.creditcuenta('credit_transf', montotranf, int(Ncuentad.strip())-1, objetousuario.iduser)

                          #  saldocuentadestino = float(user.cuentas[int(Ncuentad.strip())-1]['saldo']) + float(montotranf)
                          #  user.cuentas[int(Ncuentad.strip())-1]['saldo'] = "{:0.2f}".format(saldocuentadestino)
                           #se agrega el registro de movimiento de destino
                           # print("\n\n")
                           print(bcolors.YELLOW+"La transferencia fue realizada..."+bcolors.ENDC,end='\n\n')

                           input()                           
                           # #se debe borrar la pantalla
                           # utilidades_basicas.limpiar()    
                           return

                         else:
                           print("No se realizo la transferencia")  
                           cond2 = True  
                           print("\n")
                           return
                            





#funcion que permite limpiar la pantalla
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



#funcion que permite crear una cuenta
def crearcuenta(objeto):
   numerocuenta = ''
   tipocuenta = ''
   montoapertura = 0.0
   fechaapertura = ''
   diccionario = {}
   cond = True
  
   while cond:

     print("Usuario : " + objeto.iduser + " - " + objeto.name,end="\n\n")

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
         montoapertura = "{:0.2f}".format(montoapertura)
         operacion = {'fecha':fechaapertura,'tipo':'apertura','monto':montoapertura,'realizado':'titular'}
         listaoperaciones.append(operacion)
         diccionario = {'num_cuenta':numerocuenta,'tipo_cuenta':tipocuenta,'fecha_apertura':fechaapertura, 'saldo':montoapertura, 'operaciones':listaoperaciones}
       else:
         print(bcolors.RED +"No se creo la cuenta"+bcolors.ENDC,end='\n\n')
       cond = False  
     else:    
       print(bcolors.RED + "datos incorrectos - vuelva a introducir los datos" + bcolors.ENDC,end='\n\n')

   return diccionario





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
  print("[7] Para hacer Transferencias",end='\n')
  print("[8] Para hacer Depositos de Nomina (metodos encadenados : deposita monto indicado a cuentas corrientes)",end='\n')
  print("[9] Para hacer Debitos por Impuestos (metodos encadenados : debita impuestos indicados a todas las cuentas)",end='\n')
  print("[0] Para generar intereses (metodos encadenados : deposita porcentaje de interes indicado a cuentas ahorro",end='\n')
  print("[i] Opcion de desarrollador : ver instancias (objetos) de la clase cuenta ",end='\n')
  print("[s] presione S para salir del sistema"+bcolors.ENDC,end='\n\n')
  
  print("Indique la opcion que desea seleccionar : ",end='')
  
  opcion = input()
  
  if opcion not in(['1','2','3','4','5','6','7', '8', '9', '0', 'i', 'I', 's', 'S']):
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
    nuevousuario = seleccionarusuario(lista_usuarios,usuario_actual)

    if nuevousuario != None:
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


  #Se retira de una cuenta
  if opcion == '6':
    utilidades_basicas.limpiar()    
    
    print("\n\n")

    retirarcuentas(usuario_actual)

    micls()

  #Se transfiere a una cuenta
  if opcion == '7':
    if validardoscuentas(lista_usuarios):
      utilidades_basicas.limpiar()    
    
      print("\n\n")

      transferircuenta(usuario_actual,lista_usuarios)
    else:
      print("no existen al menos dos cuentas creadas en el sistema",end='\n\n')
    micls()


  #Se sale del sistema
  if opcion == 's' or opcion == 'S':
     cond = False  

  if opcion == 'i' or opcion == 'I':
    vercuentas(lista_usuarios)

  if opcion == '8' :
    utilidades_basicas.limpiar()    
    
    print("\n")

    montodepo = validar_lectura("Introduzca el monto a depositar en todas las cuentas por Nomina : ",'numero')

    if float(montodepo) > 0:
      depositos_nomina(lista_usuarios,datetime.date.today(),float(montodepo),'coding dojo')    
    else:
      print(bcolors.RED+"Debe introducir un monto positivo \n\nno se realizo el deposito de Nomina"+bcolors.ENDC,end='\n\n')  
      input()

  if opcion == '9' :
    utilidades_basicas.limpiar()    
    
    print("\n")

    percenttaxes = validar_lectura("Introduzca el porcentaje de los impuestos : ",'numero')

    if float(percenttaxes) > 0:
      cobro_impuestos(lista_usuarios,datetime.date.today(),float(percenttaxes),'SII')    
    else:
      print(bcolors.RED+"Debe introducir un valor positivo para el porcentaje \n\nno se realizo debito por Impuestos llame al SII"+bcolors.ENDC,end='\n\n')  
      input()

  if opcion == '0' :
    utilidades_basicas.limpiar()    
    
    print("\n")

    percentinterest = validar_lectura("Introduzca el porcentaje de los intereses a generar : ",'numero')

    if float(percentinterest) > 0:
      generar_intereses(lista_usuarios,datetime.date.today(),float(percentinterest),'SII')    
    else:
      print(bcolors.RED+"Debe introducir un valor positivo para el porcentaje \n\nno se realizo el credito por intereses"+bcolors.ENDC,end='\n\n')  
      input()


print('\n\n'+ "presione un tecla para cerrar el programa...")   
input()


