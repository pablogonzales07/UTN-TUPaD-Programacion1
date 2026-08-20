""" contador = 0
while contador < 10:
    contador+=1
    print(f"Vuelta Numero {contador}") """

""" for i in range(5, 0, -1):
    print(i, "Debo aprender ciclos")
 """

#Actividad: Encontrar Maximo y Minimo
""" cant_numeros = 4

print("Ingrese numero 1")
num = int(input())

num_max = num
num_min = num
pos_max = 1
pos_min = 1

for cont in range(2, cant_numeros+1):
    print("Ingrese numero 2")
    num = int(input())

    if num > num_max:
        num_max = num
        pos_max = cont
    elif num < num_min:
        num_min = num
        pos_min = cont

print(f"El numero maximo hasta el momento es: {num_max} y esta en la posicion {pos_max}")
print(f"El numero minimo hasta el momento es: {num_min} y esta en la posicion {pos_min}")
 """
""" numero = 0
while True:
    numero = input("Ingrese un numero entero positivo ==> ")
    if numero.isdigit() and int(numero) > 0:
        print("Numero ingresado")

        break
    print("Debe ingresar un numero entero positivo")

numero = int(numero)
for i in range(numero, 0 - 1, -1):
    if i % 2 == 0: 
        print(i, end= " ") 
 """

for i in range (3):
     for j in range (2):
          print(i,j)