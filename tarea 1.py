#Tarea de los ejercicios 
# Luis Fernando Soria Guaranga
# Ingeniería en Software
#!ejercicio de la superficie de un circulo
class superficie:
    def __init__(self):
        pass
    def calculo(self):
        r=int(input("***Ingrese un Numero Real***: "))
        s=r*3.1416
        print("La superficie de un circulo con un Radio de:{}: es igual a:{}".format(r,s))

cal1=superficie()
cal1.calculo()

#!compra con descuento del 15 %
class ejecicios:
    def __init__(self):
        pass

    def calculo(self):
        tc=int(input("*Ingrese EL Total de las compras*: "))
        d=tc*0.15
        cp=tc-d
        print("El total de la compra es:{}".format(cp))


cal1=ejecicios()
cal1.calculo()

#!concepto de comiciones
class comision:
    def __init__(self):
        pass
    
    def calculo(self):
        suelB=float(input("Por favor mi estimado usuario Ingrese su sueldo base : "))
        v1=float(input("Ingrese el valor de la venta 1: "))
        v2=float(input("Ingrese el valor de la venta 2: "))
        v3=float(input("Ingrese el valor de la venta 3: "))

        TotalV=v1+v2+v3
        com=TotalV+0.1
        TotalR=suelB+com

        print("EL total a recibir sera de:{} dolares".format(TotalR))

cal1=comision()
cal1.calculo()

#!cafilicacion de un examen
class calificacion:
    def __init__(self):
        pass

    def calculo(self):
       cal=float(input("Ingrese su calificacion: "))
       if cal >= 7:
            print("Usted ha Aprovado, felicidades")
      

cal1=calificacion()
cal1.calculo()

#!calificacon de un examen con doble salida
class calificacion2:
    def __init__(self):
        pass

    def calculo(self):
       cal=float(input("Ingrese su calificacion: "))
       if cal >= 7:
            print("Usted ha Aprovado, felicidades")
       else:
            print("Usted Reprobo")

cal1=calificacion2()
cal1.calculo()
        

#!nuevo sueldo si es menor a $600
class sueldo:
    def __init__(self):
        pass

    def calculo(self):
        sueldI=float(input("Ingrese el sueldo Inicial: "))
        if sueldI < 600:
            sueldN=sueldI+(sueldI*0.10)
        else:
            sueldN=sueldI
            print("su nuevo sueldo es de:{} dolares".format(sueldN))       

cal1=sueldo()
cal1.calculo()

#!sueldo de un trabajador considerando horas extra
class HExtra:
    def __init__(self):
        pass

    def calculo(self):
        ht=int(input("Ingrese las horas Trabajadas: "))
        ph=float(input("Ingrese el pago por hora: "))

        if ht > 40:
            he=ht-40
            if he > 8:
                het=he-8
                phe=ph*2*8+ph*3*het
            else:
                phe=ph*2*he

            pt=ph*40+phe
        else:
            pt=ph*ht
            print("EL pago total de horas trabajadas es de:{}".format(pt))

clas1=HExtra()
clas1.calculo()

#!leer los 3 numeros enteros entres si y determinar el mayor de los 3
class Mayor:
    def __init__(self):
        pass

    def calculo(self):
        N1=int(input("Ingrese el Numero 1: "))
        N2=int(input("Ingrese el Numero 2: "))
        N3=int(input("Ingrese el Numero 3: "))

        if (N1 > N2) and (N1 > N3):
            NM=N1
        else:
            if N2 > N3:
                NM=N1
            else:
                NM=N3
        
        print("EL numero mayor es:{}".format(NM))

clas1=Mayor()
clas1.calculo()

#!resultado de una funcion
class funcion:
    def __init__(self):
        pass

    def calculo(self):
        num=int(input("Favor Ingresar un numero: "))
        v=int(input("Ingrese un valor"))

        if num == 1:
            resp=100*v
        elif num == 2:
            resp=100**v
        elif num == 3:
            resp=100/v
        else:
            resp=0

        print("El resultado de la funcion seleccionada es:{}".format(resp))

clas1=funcion()
clas1.calculo()
        
#!expresiones logicas 2 examenes a sus aspirantes
class aspirantes:
    def __init__(self):
        pass
    #usando el operador and 
    def calculo(self):   
        c1=float(input("Ingrese la primmera calificacion: "))
        c2=float(input("Ingrese la segunda calificacion: "))
        if c1 >= 80 and c2 >= 80:
            print("aceptado")
        else:
            print("Rechazado")

    #usando el operador or

        if c1>=90 or c2>=90:
            print("aceptado")
        else:
            print("rechazado")

clas1=aspirantes()
clas1.calculo()

#!suma de los cuadrados de los primeros 100 enteros
class sumac:
    def __init__(self):
        pass

    def suma(self):
        sum=0
        for 1 in 100:
            sum=sum+1*1
        print("la suma es{}".format(sum))

clas1=sumac()
clas1.calculo()

#!escribir los numeros del 1 al 100
class numeros:
    def __init__(self):
        pass

    def numeros(self):
        i=1
        while 1 <= 100:
            print(i)
            i=i+1

clas1=numeros()
clas1.calculo()

#!calcular la suma y producto de numeros enteros
class bucle:
    def __init__(self):
        pass

    def calculo():
        suma=0
        prod=1
        resp=input("Ingrese Resp: ")
        while resp == s and resp == n:
            num=int(input("Ingrese un numero: "))
            suma=suma+num
            prod=prod*num
            print("desea continuar(s/n)?")

        print("Total de la suma es:{} ".format(suma))
        print("Total del producto es:{} ".format(prod))

clas1=bucle()
clas1.calculo() 

#!suma y producto de N números enteros, utilizando un bucle controlado por centinela
class enteros:
    def __init__(self):
        pass

    def calculo(self):
        num=int(input("Ingrese un numero: "))
        while num== -1:
            suma=suma+num
            prod=prod*num
            
        print("El Total de la suma es:{}".format(suma))
        print("EL total del producto es{}".format(prod))

clas1=enteros()
clas1.calculo()

#!Determinar si un número entero proporcionado por el usuario es primo

class primo:
    def __init__(self):
        pass

    def calculo(self):
        num=int(input("Ingrese el numero: "))
        primo=True
        divisor=2
        while ((divisor < num) and (primo == "t")):
            res= num % divisor
            if res==0:
                print("el numero es primo{}".format(primo))
            divisor=divisor+1

        if primo == "t":
            print("el numero:{} es primo".format(num))
        else:
            print("el numero:{} no es primo".format(num))

clas1=primo()
clas1.calculo()

#!leer un número entero N y calcular
class calcular:
    def __init__(self):
        pass

    def calculo(self):
        serie=0
        l=1
        N=int(input("Ingrese un Numero: "))
        band="T"
        while True:
            if band == "T":
                Serie=serie + (1/l)
                band="F"
            else:
                Serie=serie-(1/l)
                band="T"
            l=l+1
            if l > N:
                print(serie)

clas1=calcular()
clas1.calculo()

#!bucles anidados, calcular el factorial
class factorial:
    def __init__(self):
        pass

    def calculo(self):
        N=int(input("Ingrese la cantodad de numeros: "))
        for i in N:
            numero=int(input("Ingrese el numero: "))
            fact=1
            for j in numero:
                fact=fact*j
            print("EL factorial del numero:{} es:{}".format(numero,fact))

clas1=factorial()
clas1.calculo()

#!leer un vector de 20 numeros
class vector:
    def __init__(self):
        pass

    def calculo(self):
        j=1
        k=1
        num=20
        A=20
        B=20
        for i in 20:
            num=i
            if num>0:
                j=num
                j=j+1
            else:
                k=num
                k=k+1
            
            for i in j:
                print(A)
            
            for i in k:
                print(B)
            
clas1=vector()
clas1.calculo()


#!informacion sobre calificaciones
class infCal:
    def __init__(self):
        pass

    def calculo(self):
        for i in 30:
            for j in 6:
                print("Escriba la calificacion del alumno:{} en el examen{}".format(i,j))
                print(i,j)

        for j in 6:
            sum=0
            for i in 30:
                sum=sum+(i,j)
            prom=sum/30
            print("EL promedio del examane",j,prom)

        for i in 30:
            sum=0
            for j in 6:
                sum=sum+(i,j)

            print("El promedio del alumno es: ", i, sum/6)

        Examen=1
        promayor=prom
        for j in 6:
            if promayor<j:
                promayor=j
                Examen=j
        
        print("El examen:{} obtuvo el mayor promedio:{}".format(Examen,promayor))

clas1=infCal()
clas1.calculo()
                