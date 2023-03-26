import sys

def cuit_generator():
    option = "Tipo Persona:\n\n1-Empresa.\n2-Mujer.\n3-Hombre.\n\n0-Salir.\n\nEscoja un opcion (numero): "

    error_value = lambda:print("Solo de admiten numeros!")

    KEY_VALIDATOR = (5,4,3,2,7,6,5,4,3,2)

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
            error_value()

    while True:
        try:
            number = int(input("Ingrese su numero de indentificacion: ")) 
            break
        except ValueError:
            error_value()

    person_list = [int(d) for d in str(person)]
    number_list = [int(d) for d in str(number)]

    for i in range(8):
        if len(number_list) < 8:
            number_list.insert(0,0)

    number_end = person_list + number_list


    number_validator = 0
    if len(KEY_VALIDATOR) == len(number_end):
        for i in range(len(KEY_VALIDATOR)):
            result = number_end[i] * KEY_VALIDATOR[i]
            number_validator +=result

    number_validator = (((number_validator//11)*11)+11-number_validator)

    if number_validator == 10 and person == 20:
        person = 23
        number_validator = 9
    if number_validator == 10 and person == 27:
        person = 23
        number_validator = 4

    cuit = str(person) + str(number) + str(number_validator)

    print(f'El CUIT es: {cuit[0:2]}-{cuit[2:10]}-{cuit[10]}')

if __name__ == __name__:
    cuit_generator()