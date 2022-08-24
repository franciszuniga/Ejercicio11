numero = float(input("Ingrese un numero"))  #pide ingresar numero y como es string lo llevamos a float
while numero%1 !=0 or numero == 0 :         #mientras el residuo de (numero/1) es diferente de 0 o numero sea igual a 0 se repite el bucle
    print("El numero ingresado es 0 o no es entero")
    numero = float(input("Ingrese un numero entero diferernte de 0: "))

numerostr = str(numero)                     #convertimos numero a un string y lo almacenamos en la variable numerostr
if numero%2==0:                             #si el residuo de numero/2 es 0 el numero es par, sino es impar
    print("El numero "+numerostr+" es par")
else:
    print("El numero "+numerostr+" es impar")
