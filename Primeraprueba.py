def nuevoTema(tema):
    print ("\n======", tema, "=====\n")

#MatinezUrzuaSebastianEsdras 09/02/23
nuevoTema("Operador aritmetico")
print ("Operador dvision entero(10//3):",10//3)
print ("Operador potencia (5*3):", 5*3)

nuevoTema("Operadores logicos")
print ("Operador and (True and False):",True and False) #True y False siempre seran en mayuscula

#Imprimir la tabla de verdad de los operadores logicos.

nuevoTema("Operadores con and")
print ("Operador and (True and False):",True and False)
print ("Operador and (True and True):",True and True)
print ("Operador and (False and True):",False and True)
print ("Operador and (False and False):",False and False)

nuevoTema("Operadores con not")
print ("Operador not (True ):", not True)
print ("Operador not (False ):",not False)

nuevoTema("Operadores con or")
print ("Operador or (True or True):",True or True)
print ("Operador or (True or False):",True or False)
print ("Operador or (False or True):",False or True)
print ("Operador or (False or False):",False or False)

nuevoTema("Operadores de comparacion")

print ("4==9",2==3)
print ("4!=9",4!=9)
print ("4<9",4<9)
print ("4<=9",4<=9)
print ("4>9", 4>9)
print ("4>=9",4>=9)

nuevoTema("Variables")
variable1=10
_variable2=6.2456
Variable3="Juancho"
dosPalabras="Hola"
dos_Palabras="Hello"

print (variable1,_variable2,Variable3,dosPalabras,dos_Palabras)

a, b, c=10, 5.16, "Palabra"
print (a,b,c)

nuevoTema("Enteros")
w=105
x=99999999
y=-999
z=0b00110011
h=0xffa

print(w,type(w))
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(h,type(h))

nuevoTema("Flotantes")
x=1243.50
print (x,type (x))
y=0.56789
print(y,type(y))

nuevoTema("Numeros complejos")
x=-46j
y=12+45j
z=2j

print(x, type (x))
print(y, type (y))
print(z, type (z))

nuevoTema("Numero boleano")
lis= [8]
print(lis, "es", bool(lis))
t= ()
print(t, "es", bool(t))
new="Hello"
print(new,"es",bool(new))
num=99
print(num,"es",bool(num))
comp=1+0j
print(comp,"es",bool(comp))
val=None
print(val,"es",bool(val))

nuevoTema("Listas") #No son arreglos
a=[10,20.5,"Python list"]
print(a)
print(a[1])
a[0]="Hola"
print(a)

nuevoTema("Tuplas")

t= (25, "Tupla",1+10j,3.1416)
print (t)
print(t[2])
print("t[1:4", t[1:4])

nuevoTema("Conjuntos")

t= {50, 20, 30, 40, 10, 50}
print ("Conjunto t=", t, type(t))


nuevoTema("Diccionarios")

d={1:"Valor", "Valor2":2j}
print(d,type(d))
print ("d[Valor2]:", d["Valor2"])

nuevoTema("Cadenas")
cadena1="Cadena con comillas dobles"
cadena2='Cadena con comillas simples'

print  (cadena1, type(cadena1))
print  (cadena2, type (cadena2))

cadenaMultilinea='''Esta es una cadena de
varias lineas con tabulares y
saltos
de
linea'''

print (cadenaMultilinea)
print("Segmentacion de cadenas")
print(cadena1[5:11])
print (cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1= "Hola"
cadena4 = (cadena1+"")*5
print (cadena4)
cadena5=cadena4.capitalize()
print(cadena5)
