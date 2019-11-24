import random

random_word = ''


def gen_random_ord():
    with open('words.txt', 'r', encoding='UTF-8') as words:
        list_words = words.read().split()
    random_word = random.choice(list_words)


def check_correct(guess):
    if guess == random_word:
        return True
    else:
        return False

def hints(guess):
    '''returnerar antalet rätta bokstäver på rätt plats
    och antal rätta bokstäver men på fel plats'''
    correct_letter = 0
    wrong_letter = 0

    for letter in random_word:
        try:
            if random_word.index(letter) == guess.index(letter):
                correct_letter += 1
            if letter in guess:
                wrong_letter += 1
        except:
            pass
    wrong_letter -= correct_letter
    return f'bokstäver på rätt plats: {correct_letter} bokstäver på fel plats: {wrong_letter}'


def main_guess(guess):
    pass
    