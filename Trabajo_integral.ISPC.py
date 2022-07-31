'''
Consigna:
Codificar en Python un programa que contenga las siguientes condiciones:
● El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una
lista.
● Función Suma: recibe como parámetro la lista y devuelve la suma total de todos
sus elementos.
● Función Promedio: recibe como parámetro la lista y devuelve el promedio de sus
elementos.
● Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de
todos los elementos que contiene.
● Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de
todos los elementos que contiene.

'''

lista =[]
n = 0

print()

while n < 5:
     lista.append(int(input("Ingrese el valor que desea calcular: ")))
     n += 1
print()
print("\t MENU: ")
print("1- Sumar la lista.")
print("2- Promedio de la lista.")
print("3- Máximo valor en la lista.")
print("4- Mínimo valor en la lista.")
print()
vari = int(input("Que operación desea realizar: "))
print()

def suma(lista):
     for elemento in lista:
          suma_total = sum(lista)
          return suma_total

def promedio(lista): 
    promedio_total = sum(lista) / 5
    return promedio_total

def máximo(lista):
     máx_lista = max(lista)    
     return máx_lista

def mínimo (lista):
     mín_lista = min(lista)
     return mín_lista


if vari== 1:
     print(f"La suma total es: {suma(lista)}")

elif vari== 2:
     print(f"El promedio de la lista es: {promedio(lista)}")

elif vari== 3:
     print(f"El valor máximo es: {max(lista)}")

elif vari== 4:
     print(f"El valor mínimo de la lista es: {min(lista)} ") 
else:
     print("El valor tipeado no corresponde a una opción del menú.")

print()
print("\t Gracias por usar esta calculadora.")      
print()  