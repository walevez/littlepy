import sys
import math

option = """Tipo Persona:

1-Empresa.
2-Mujer.
3-Hombre.

0-Salir.

Escoja un opcion (numero): """


while True:
    try:
        person = int(input(option))
        
        if person < 0 or person > 3:
            print('Elija una opcion correcta.')
        elif person == 0:
            sys.exit()
        elif person == 1:
            person = 30
            break
        elif person == 2:
            person = 27
            break
        elif person == 3:
            person = 20
            break        
        else:
            break
        
    except ValueError:
        print('Solo se adminten numeros!!!')

while True:
    try:
        number = int(input("Ingrese su numero de indentificacion: "))
        break
    except ValueError:
        print('Solo se adminten numeros!!!')
        
person_list = list(str(person))
person_list = [int(x) for x in person_list]

number_list = list(str(number))
number_list = [int(x) for x in number_list]
for i in range(8):
    if len(number_list) < 8:
        number_list.insert(0,0)

number_end = person_list + number_list

print(number_end)

key_validator = (5,4,3,2,7,6,5,4,3,2)
minumero = 0

if len(key_validator) == len(number_end):
    for i in range(len(key_validator)):
        cuit = number_end[i] * key_validator[i]
        minumero +=cuit
        print(minumero)

resto = (((minumero//11)*11)+11-minumero)

print(resto)