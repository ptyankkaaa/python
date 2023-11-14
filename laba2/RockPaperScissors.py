import random


class switch(object):
    def __init__(self, value):
        self.value = value  # значение, которое будем искать
        self.fall = False   # для пустых case блоков

    def __iter__(self):     # для использования в цикле for
        """ Возвращает один раз метод match и завершается """
        yield self.match
        raise StopIteration

    def match(self, *args):
        """ Указывает, нужно ли заходить в тестовый вариант """
        if self.fall or not args:
             # пустой список аргументов означает последний блок case
             # fall означает, что ранее сработало условие и нужно заходить 
             #   в каждый case до первого break
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False

def game1():
    print("\nChoose:\n1 - ROCK\n2 - PAPER\n3 - SCISSORS\n")
    y = int(input())

    variables = [1,2,3]
    random.shuffle(variables)
    z = random.choice(variables)

    if (y == 1 and z == 1):
        print("\nRock and rock\nDraw!\n")
    if (y == 2 and z == 2):
        print("\nPaper and paper\nDraw!\n")
    if (y == 3 and z == 3):
        print("\nScissors and scissors\nDraw!\n")
    if (y == 1 and z == 2):
        print("\nRock and paper\nYou lose!\n")
    if (y == 1 and z == 3):
        print("\nRock and scissors\nYou won!\n")
    if (y == 2 and z == 1):
        print("\nPaper and rock\nYou won!\n")
    if (y == 2 and z == 3):
        print("\nPaper and scissors\nYou lose!\n")
    if (y == 3 and z == 1):
        print("\nScissors and rock\nYou lose!\n")
    if (y == 3 and z == 2):
        print("\nScissors and paper\nYou won!\n")
    if (y != 1 and y != 2 and y != 3):
        print("\nError, try again\n")
        game1() 
    
def game2():
    print("\nChoose:\n1 - ROCK\n2 - PAPER\n3 - SCISSORS\n")
    y = int(input())


    variables = [1,2,3]
    random.shuffle(variables)
    z = random.choice(variables)
    

    if (y == 1 and z == 1):
        print("\nRock and rock\nDraw!\n")
     
    if (y == 2 and z == 2):
        print("\nPaper and paper\nDraw!\n")
      
    if (y == 3 and z == 3):
        print("\nScissors and scissors\nDraw!\n")
        
    if (y == 1 and z == 2):
        print("\nRock and paper\nYou lose!\n")
        
    if (y == 1 and z == 3):
        print("\nRock and scissors\nYou won!\n")
       
    if (y == 2 and z == 1):
        print("\nPaper and rock\nYou won!\n")
        
    if (y == 2 and z == 3):
        print("\nPaper and scissors\nYou lose!\n")
       
    if (y == 3 and z == 1):
        print("\nScissors and rock\nYou lose!\n")
    
    if (y == 3 and z == 2):
        print("\nScissors and paper\nYou won!\n")
    
    if (y != 1 and y != 2 and y != 3):
        print("\nError, try again\n")
        game2()

def after_game1():
    import sys
    print("\nIf you don't want to play some more - enter 0\nif you want to play some more - enter 1\nIf you want to go to main menu - enter 2\n")
    answer = int(input())
    for case in switch(answer):
        if case(1):
            print("\nLet's continue!\n")
            game1()
        if case(2):
            main_menu()
        if case(0):
            print("\nThanks for the game! See you!")
            sys.exit()

def after_game2():
    import sys
    print("\nIf you don't want to play some more - enter 0\nif you want to play some more - enter 1\nIf you want to go to main menu - enter 2\n")
    answer = int(input())
    for case in switch(answer):
        if case(1):
            print("\nLet's continue!\n")
            game_settings()
            game2()
        if case(2):
            main_menu()
        if case(0):
            print("\nThanks for the game! See you!\n")
            sys.exit()

def game_settings():
    print("\nHow many rounds do you want to play?\n")
    s = int(input())
    while s!=0:
        game2()
        s-=1


def rules():
    print("\nStone dulls scissors\nPaper covers stone\nScissors cutting paper\n")
    main_menu()

def grittings():
    print("\nWelcome in Rock Paper Scissors!\n")

def main_menu():
    print("\nIf you want a one time game - enter 1\nIf you want to set the number of rounds - enter 2\nIf you want to know the rules of the game - enter 3\n")
    answer = int(input())
    if answer == 1:
        game1()
        after_game1()
    if answer == 2:
        game_settings()
        after_game2()
    if answer == 3:
        rules()



grittings()
main_menu()

