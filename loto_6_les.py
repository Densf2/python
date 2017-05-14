# -*- coding: utf-8 -*-
import random
"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


# author Den Pavlyuk

class Meta:
    def __init__(self, lst):
        self.lst = lst

    # Mixing list of numbers(cards, barrel)
    def mixer(self):
        random.shuffle(self.lst)
        return self.lst

    # Get list from object
    def get_lst(self):
        res = [n for n in self.lst]
        return res


# Card class


class Card(Meta):
    def __init__(self, lst, name):
        self.lst = lst
        self.name = name

    # Get lists from numbers to cards
    def __str__(self):
        card = []
        for n in self.lst:
            card.append(str(n))
        return ''.join(['   '.join(card[0:5]), '\n', ' '.join(card[5:10]), '\n', '   '.join(card[10:15])])

    # Erase numbers, who indentend
    def erase(self, bar):
        for n in self.lst:
            if n == bar:
                i = self.lst.index(n)
                self.lst.remove(n)
                self.lst.insert(i, '-')
        return self.lst

    # Inspect card by erase numbers
    def revision(self):
        card = [str(n) for n in self.lst]
        card_st = [n for n in card if n.isdigit()]
        if len(card_st) == 0:
            res = True
        else:
            res = False
        return res

    # Get cards
    def view_card(self):
        return ''.join(['\n', '-' * 3, ' Cards ', self.name, ' ', '-' * 3, '\n', self.__str__(), '\n', '-' * 23])


# Dealer class


class Dealer:
    def __init__(self, bar, left):
        self.bar = bar
        self.left = left

    # Set showing numbers
    def new_number(self):
        return ''.join(['\n\n\n', 'Number fell ', str(self.bar), ' (at least ', str(self.left), ' barrels)',
                        '\nWant erase number? (y/n)'])

    # Response from dealer
    def unexpect_answer(self):
        return '\n\n---\n\n\n\nJoke...\nGo from the table!\n\n\n\n'

    def fortune(self):
        return '\n\n---\n\n\n\nGood, this numbers is!\n\n'

    def cheating(self):
        return '\n\n---\n\n\n\nCheating bad...\nGo from the table!\n\n\n\n'

    def wrong_answer(self):
        return '\n\n---\n\n\n\nRead rules again...\nGo from the table!\n\n\n\n'

    def failure(self):
        return '\n\n---\n\n\n\nFailure...\n\n'

    def win(self):
        return '\n\n---\n\n\n\nYou a winner!\nNice game.\n\n'

    def loss(self):
        return '\n\n---\n\n\n\nYou lose!\nBad game.\n\n'


# ----------
# Preparing to game
# ----------

# Making cards
numbers = Meta(list(range(1, 91)))
numbers.mixer()
card_player = Card(numbers.get_lst()[0:15], 'you')
numbers.mixer()
card_robot = Card(numbers.get_lst()[0:15], 'comp')

# Mixing barrels
barrels = Meta(list(range(1, 91)))
barrels.mixer()

# Counter for cards at least
left = len(barrels.get_lst()) - 1

# Game start

for bar in barrels.get_lst():
    if card_player.revision() == False and card_robot.revision() == False:
        card_robot.erase(bar)

        # Dealer coming
        dealer = Dealer(bar, left)
        print (dealer.new_number())

        print(card_player.view_card())
        print(card_robot.view_card())

        answer = raw_input()
        answer_lst = ['y', 'n']

        if answer not in answer_lst:
            print(dealer.unexpect_answer())
            break
        elif answer == 'y' and bar in card_player.get_lst():
            card_player.erase(bar)
            left -= 1
            print(dealer.fortune())
        elif answer == 'y' and bar not in card_player.get_lst():
            print(dealer.cheating())
            break
        elif answer == 'n' and bar in card_player.get_lst():
            print(dealer.wrong_answer())
            break
        elif answer == 'n' and bar not in card_player.get_lst():
            print(dealer.failure())
            left -= 1
            continue

        if card_player.revision() == True:
            print(dealer.win())
            break
        elif card_robot.revision() == True:
            print(dealer.loss())
        else:
            continue
