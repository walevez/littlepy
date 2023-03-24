import random

list_word = []
reintent = 10

with open('./source/words.txt', 'r', encoding='utf-8') as archivo_lectura:
    line_number = 0
    for word in archivo_lectura:
        word = word.rstrip().lower()
        list_word.append(word)

#selection word random
word_random = list_word[random.randint(0,len(list_word))]

#Transformation from string to list
word_random = list(word_random)
word_random_string = "".join(word_random)

unknown_word = []
for x in range(len(word_random)):
    unknown_word.append('-')

def show_word():
    global unknown_word_string
    unknown_word_string = ''.join(unknown_word)
    print(unknown_word_string)

show_word()

while True:
    if unknown_word != word_random:
        
        print(f"Tienes {reintent} intentos.")
        pregunta = input('una letra: ')
        
        counter_index = 0
        punch = False
        
        for i in word_random:
            if i == pregunta:
                unknown_word[counter_index] = i
                punch = True
            counter_index +=1
        
        if punch is False:
            reintent -=1
        
        show_word()
        
        if reintent == 0:
            print(f'Gamer Over la palabra era {word_random_string.upper()}')
            break
    else:
        print(f'Ganaste la palabra era {unknown_word_string.upper()}')
        break