import random

the_number = random.randint(1,10)
attempt = 10

def my_number_def(again):
    while True:
        try:
            global my_number
            my_number = int(input(again))
            break
        except ValueError:
            print('Solo se admiten numeros. Reintente!!!')
    return my_number

def reintent(number_position):
    global attempt
    attempt -=1
    print(f'El numero es más {number_position}.')
    print(f'Te quedan: {attempt} intentos.')
    my_number_def('Ingresa otro numero: ')

game_over = lambda:print(f'Gamer Over, The number is {the_number}')

my_number_def('Ingrese el numero adivinar: ')

while my_number != the_number:
    if my_number < the_number:
        reintent('alto')
        if attempt == 1:
            game_over()
            break
    else:
        reintent('bajo')
        if attempt == 1:
            game_over()
            break
else:
    print(f'Ganaste el numero es {my_number}')