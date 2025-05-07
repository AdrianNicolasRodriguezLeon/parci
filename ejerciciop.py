##primer punto
def suma(a,b,c,d,e):   #definir variables
    total= a+b+c+d+e
    return total

# ingresar los datos enteros
entero1= int(input("ingrese un  numero: "))
entero2= int(input("ingrese un  numero: "))
entero3= int(input("ingrese un  numero: "))
entero4= int(input("ingrese un numero: "))
entero5= int(input("ingrese un  numero: "))


#condicionales
# si los enteros son diferentes de 2 y negativos se definnen como 0 para no afectar la suma 
if entero1 % 2 != 0 or entero1 < 0:
        entero1=0
if entero2 % 2 != 0 or entero1 < 0:
        entero2=0
if entero3 % 2 != 0 or entero1 < 0:
        entero3=0

if entero4 % 2 != 0 or entero1 < 0:
        entero4=0

if entero5 % 2 != 0 or entero1 < 0:
        entero5=0
#impresion 
print (f"la suma de los positivos y pares es {suma(entero1,entero2,entero3,entero4,entero5)}")



# segundo punto
edad= int(input("ingrese la edad de la persona "))
if edad < 13:
    print("Es niño")
if edad >= 13 and edad < 17:
    print("Es adolecente")
if edad >= 13 and edad <= 17:
    print("Es adolecente")
if edad >= 18 and edad <=59:
    print("Es adulto")
if edad >= 60:
    print("Es adulto mayor")

##ciclo

#en caso que se ingrese una edad negativa se vuelve a repetir el programa
while edad< 0:
    print ("numero negativo. Vuelva ingresar la edad")
    edad= int(input("ingrese la edad de la persona "))
    if edad < 13:
        print("Es niño")
    if edad >= 13 and edad < 17:
        print("Es adolecente")
    if edad >= 13 and edad <= 17:
        print("Es adolecente")
    if edad >= 18 and edad <=59:
        print("Es adulto")
    if edad >= 60:
        print("Es adulto mayor")

#tercer punto


palabra= (input("ingrese la palabra:"))


