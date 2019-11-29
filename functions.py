import random


def gen_random_ord():
    with open('words.txt', 'r', encoding='utf-8') as words:
        list_words = words.read().split()
    randomword = random.choice(list_words)
    return randomword


def check_correct(guess, random_word):
    if guess == random_word:
        return True
    else:
        return False

def hints(guess, random_word):
    '''returnerar antalet rätta bokstäver på rätt plats
    och antal rätta bokstäver men på fel plats'''
    correct_letter = 0
    wrong_letter = 0

    for letter in random_word:
        try:
            if random_word.index(letter) == guess.index(letter):
                correct_letter += 1
            elif letter in guess:
                wrong_letter += 1
        except:
            pass
    return f'bokstäver på rätt plats: {correct_letter} bokstäver på fel plats: {wrong_letter}'

    