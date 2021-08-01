class Basico:
    def __init__(self):
        pass
    
    def numerosN(n):
        for i in range(n):
            print(str(i+1),end="   ")
        return n
    
    def multiplos(numero,multiplo):
        return numero % multiplo == 0

    def DivisoresNumero(numero):
        contador = 0
        print("Los divisores de {}".format(numero), "son: ")
        for divisor in range(1,numero+1):
            if (numero % divisor) == 0 :
                print(divisor,"es divisor de {}".format(numero))
                contador += 1
        return contador

    def primo(numero):
        for n in range(2, numero):
            if numero % n == 0:
                print("No es primo y {} es su divisor".format(n))
                return False
        print("Es primo")
        return True

    def perfecto(numero):
        perfect = 0
        numero2 = 1
        while numero2 < numero:
            if (numero % numero2 == 0):
                perfect = perfect + numero2
            numero2 = numero2 + 1
        if perfect == numero:
            print("El numero {}".format(numero),"si es perfecto")
        else:
            print("El numero {}".format(numero),"no es perfecto")
        return perfect
    

class Intermedio(Basico):
    def __init__(self):
        pass
    
    def suma(n):
        acum = 0
        for i in range (1,n+1):
            acum = acum +i
        return acum
  
    def factorial(numero):
        fact = 1
        if numero != 0:
            for i in range(1,numero +1):
                fact = fact * i
        return fact
    
    def fibonacci(n):
        a, b = 0,1
        for i in range(n):
            print(a, end="  ")
            a, b = b, a + b
        return i
        
    def primosgemelos(num1,num2):
        if num1 == (num2 - 2):
            print("Los numeros {} y {} son primos gemelos ".format(num1,num2))
        else :
            print("Los numeros {} y {} no son primos gemelos ".format(num1,num2))
        
    def  amigos(num1,num2):
        for i in range(2,num1):
            if(num1 % i==0):
                num2=num2+i
        return num2
