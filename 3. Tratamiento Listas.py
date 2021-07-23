import os 
class Menu: 
    def __init__(self,titulo="",opciones= []):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1....{}]: ".format(len(self.opciones)))
        return opc  

opc = ""
while opc != "11": 
    os.system("cls") 
    men1 = Menu("--------------------- Menú Tratamiento Listas ---------------------",[" 1. Recorrer y presentar los datos de una lista",
        " 2. Buscar un valor en una lista"," 3. Retornar una lista con los factoriales"," 4. Retornar una lista de números primos",
        " 5. Recorrer una lista de diccionario con notas de alumnos"," 6. Insertar un dato en una Lista dada lo Posición"," 7. Eliminar todas las ocurrencias en una Lista",
        " 8. Retornar cualquier valor de una lista eliminándolo"," 9. Copiar cada elemento de una tupla en una lista"," 10. Dar el vuelto a varios clientes",
        " 11. Salir" ])  
    opc = men1.menu()  
    if opc == "1":
        opci1 = " "
        while opci1 != "3":
            os.system("cls") 
            menu1 = Menu("-----. Recorrer y presentar los datos de una lista .----",["1. Días de la semana","2. Meses del año","3. Salir"])
            opci1 = menu1.menu()
            if opci1 == "1":
                os.system("cls") 
                menu2=Menu("_* Días de la semana *_",["1. Lunes","2. Martes","3. Miercoles","4. Jueves","5. Viernes","6. Sabado","7. Domingo"])
                dias = menu2.menu()
                os.system("cls") 
                if dias == "1": print ("Lunes") 
                elif dias == "2": print( "Martes")
                elif dias == "3": print( "Miércoles") 
                elif dias == "4": print( "Jueves")
                elif dias == "5": print( "Viernes")
                elif dias == "6": print( "Sábado")
                elif dias == "7": print( "Domingo")
                else: print ("El día solicitado no existe")
            input("Presione una tecla para continuar...") 

            if opci1 == "2":  
               os.system("cls") 
               menu3 = Menu("________* Meses del año *________",["1. Enero ","2. Febrero ","3. Marzo "," 4. Abril ","5. Mayo ","6. Junio ","7. Julio ","8. Agosto ","9. Septiembre ","10. Octubre ","11. Noviembre ","12 Diciembre "])
               meses = menu3.menu() 
               os.system("cls") 
               if meses == "1": print ("Enero") 
               elif meses == "2": print( "Febrero")
               elif meses == "3": print( "Marzo") 
               elif meses == "4": print( "Abril")
               elif meses == "5": print( "Mayo")
               elif meses == "6": print( "Junio")
               elif meses == "7": print( "Julio") 
               elif meses == "8": print( "Agosto")
               elif meses == "9": print( "Septiembre") 
               elif meses == "10": print( "Octubre")
               elif meses == "11": print( "Noviembre")
               elif meses == "12": print( "Diciembre") 
               else: print ("El mes solicitado no existe")
            input("Presione una tecla para continuar...") 
            if opci1 == "3": 
               resp= " "
               print("___________ Fin del proceso Recorrer y presentar los datos de una lista ___________")
               print(" ")
               print("Retornar a :\n1. Menu Principal ""\n2. Programa Actual""\nRespuesta: ")
               resp = input()
               if resp == "1": opci = Menu()
               elif resp == "2": menu1.menu()

    def  buscarLista(valor):
        pass

    def  listaFactorial():
        pass 

    def listaPrimo():
        pass

    def listaNotas(listaNotasDicccionario):
        pass

    def insertarLista(valor,posicion):
        pass
    
    def eliminarLista(valor):
        pass

    def retornaValorLista(posicion):
        pass

    def copiarTuplaLista(tupla):
        pass

    def vueltoLista(listaClientesDiccionario):
        pass 
    
ejercicio = Menu()


