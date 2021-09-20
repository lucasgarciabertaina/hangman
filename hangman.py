import random
import os
import shutil

def getWord():
    data = [word[:-1] for word in open('data.txt','r').readlines()]
    return data[random.randint(0,len(data)-1)]

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def title():
    title = [
        " _    _                                                ",
        "| |  | |                                               ",
        "| |__| |  __ _  _ __    __ _  _ __ ___    __ _  _ __   ",                                                
        "|  __  | / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \  ",
        "| |  | || (_| || | | || (_| || | | | | || (_| || | | | ",
        "|_|  |_| \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_| ",
        "                        __/ |                          ",
        "                       |___/                           ",

             ]
    for part in title:
        print_centre(part)

def hangman():
    print_centre("    |_______________``")
    print_centre("    [/]           [  ]")
    print_centre("    [\]           | ||")
    print_centre("    [/]           |  |")
    print_centre("    [\]           |  |")
    print_centre("    [/]           || |")
    print_centre("   [---]          |  |")
    print_centre("   [---]          |@ |")
    print_centre("   [---]          |  |")
    print_centre("  oOOOOOo         |  |")
    print_centre(" oOO___OOo        | @|")
    print_centre("oO/|||||\Oo       |  |")
    print_centre("OO/|||||\OOo      |  |")
    print_centre("*O\ x x /OO*      |  |")
    print_centre("/*|  c  |O*\      |  |")
    print_centre("   \_O_/    \     |  |")
    print_centre("    \#/     |     |  |")
    print("                                                          |       |  |     | ||")
    print("                                                          |       |  |_____| ||__")
    print("                                                         _/_______\__|  \  ||||  \}")
    print("                                                         /         \_|\  _ | ||\  \}")
    print("                                                         |    V    |\  \//\  \  \  \}")
    print("                                                         |    |    | __//  \  \  \  \}")
    print("                                                         |    |    |\|//|\  \  \  \  \}")
    print("                                                         ------------\--- \  \  \  \  \}")
    print("                                                         \  \  \  \  \  \  \  \  \  \  \}")
    print("                                                         _\__\__\__\__\__\__\__\__\__\__\}")
    print("                                                         __|__|__|__|__|__|__|__|__|__|__|")
    print("                                                         |___| |___|")
    print("                                                         |###/ \###|")
    print("                                                         \##/   \##/")
    print("                                                          ``     `` \n")

def replace(letter,resolition,word, position):
    wordList = word.split()
    wordList[position] = letter
    returning = ''
    for i in range(len(resolition)):
        if i != len(resolition)-1:
            returning += wordList[i]
            returning += ' '
        else:
            returning += wordList[i]
    return returning

def game():
    os.system('clear')
    resolution = getWord()
    word = '_ '*len(resolution)
    hangman()
    print_centre(word)
    condition = word.find('_')
    while condition != -1:
        answer = input().upper()
        for position in range(len(resolution)):
            if answer == resolution[position].upper():
                word = replace(answer, resolution, word, position)
        os.system('clear')
        hangman()
        condition = word.find('_')
        print_centre(word)
        

def main():
    os.system('clear')
    title()
    if input('') == 'x':
        game()
    pass

if __name__ == '__main__':
    main()