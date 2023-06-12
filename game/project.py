from colorama import Fore
import sys
import re
import csv
from tabulate import tabulate
import time
import random
from datetime import date

lifes =  5
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla',
             'Antarctica', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria',
             'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Botswana',
             'Brazil', 'Brunei', 'Bulgaria', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
             'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Croatia', 'Cuba',
             'Curaçao', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica',
             'Ecuador', 'Egypt', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji',
             'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
             'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
             'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
             'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
             'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan',
             'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
             'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
             'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
             'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
             'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat',
             'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
             'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norway', 'Oman', 'Pakistan',
             'Palau', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
             'Qatar', 'Réunion', 'Romania', 'Russia', 'Rwanda', 'Samoa', 'Senegal',
             'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia',
             'Spain', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
             'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau',
             'Tonga', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
             'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen',
             'Zambia', 'Zimbabwe']
name = ""
score = 0
streak = 0
def prompt():
    print("\033c")
    print(Fore.CYAN + "==========================================")
    print("==========================================")
    print("==                                      ==")
    print("==                                      ==")
    print("== 🏳️ 🏳️ 🏳️ 🏳️ 🏳️🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️🏳️ 🏳️ 🏳️ 🏳️ 🏳️    ==")
    print("==                                      ==")
    print("==                                      ==")
    print("==    WELCOME TO COUNTRY GUESSING GAME  ==")
    print("==                                      ==")
    print("==       Press 1 to start new game      ==")
    print("==       Press 2 to check score board   ==")
    print("==       Press Q to exit                ==")
    print("==                                      ==")
    print("== 🏳️ 🏳️ 🏳️ 🏳️ 🏳️🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️ 🏳️🏳️ 🏳️ 🏳️ 🏳️ 🏳️    ==")
    print("==                                      ==")
    print("==                                      ==")
    print("==                                      ==")
    print("==========================================")
    print("==========================================")

    print(Fore.YELLOW, end="")
    value = check_choice(input().strip())
    if not value:
        print("Invalid Input")
        time.sleep(1)
        prompt()
    action(value)



def Sort(sub_li):
    return(sorted(sub_li, key=lambda x: x[2]))
def action(value):
    match value:
        case "1":
            new_game()
        case "2":
            high_score()
        case _:
            quit()
def check_choice(a):
    if match := re.match(r"^([1-2]|Q|q)$", a):
        return match.group(1)
def high_score():
    all_score = []
    with open("leaderboard.csv") as file:
        scores = csv.reader(file)
        for row in scores:
            all_score.append(row)
        unsorted_score = all_score[1:]
        sorted_scores = Sort(unsorted_score)
        print("\033c")
        all_score = [all_score[0]]
        all_score += sorted_scores
        print(Fore.LIGHTYELLOW_EX + "HALL OF FAME")
        print(tabulate(all_score, headers="firstrow", tablefmt="heavy_grid"))
    print()
    check = input("press any key to return Home, 9 to reset leadership board: ").strip()
    if check == "9":
        print()
        confirm = input("press 1 to confirm, any other key to go home: ").strip()
        if confirm == "1":
            reset_board()
            time.sleep(2)
            prompt()
            return
    prompt()
def new_game():
    global name
    name = start()
    while True:
        if len(name) > 2:
            break
        else:
            print("Name is too short")
            time.sleep(1)
            new_game()
            return
    play(1)
    
def play(num):
    global score
    global lifes
    if lifes == 0:
        add_score()
        print(Fore.RED, end="")
        print("==============================================")
        print("==============================================")
        print("==          GAME OVER                       ==")
        print("==============================================")
        print("==============================================")
        print("==                                          ==")
        print("==   👏👏👏👏👏👏👏👏👏👏👏👏👏👏           ==")
        print("==                                          ==")
        print("==                                          ==")
        print(f"You scored a total of {score} points in {num - 1} rounds")
        print("==                                          ==")
        print("==                                          ==")
        print("==   👏👏👏👏👏👏👏👏👏👏👏👏👏👏            ==")
        print("==                                           ==")
        print("==       Press any key to continue           ==")
        print("===============================================")
        print("===============================================")
        input()
        prompt()
    miss = 0
    print(f"Round {num} !!!")
    picked = list(random.choice(countries).lower())
    country2 = picked[:]
    dashes = ["-" for _ in picked]
    while miss < 5:
        print(f"\033c")
        print(Fore.LIGHTMAGENTA_EX, end="")
        print("==============================================")
        print(f"==          Score: {score}        ")
        print("==============================================")
        print(f"==              ROUND {num}                     ==")
        print("==                                          ==")
        print("==                                          ==")
        print(f"== {lifes} diadem(s) left           {miss} miss(es)    == ")
        print("==                                          ==")
        print("==                                          ==")
        print("==          Guess an alphabet:              ==")
        print("==                                          ==")
        print("==                                          ==")
        print("==============================================")
        print("==   Country name is "+ "".join(dashes))
        print("==============================================")
        
        guess = input("").lower()
        if len(guess) != 1:
            print("Guess must be 1 character long. Try again! \n")
            continue
        elif not guess.isalpha():
            print("Alphabets only please \n")
            continue
        else:
            if guess in country2:
                print("Your guess is correct!" + "\U0001F60D \n")
                score += 2
                pos = country2.index(guess)
                dashes[pos] = guess
                country2[pos] = '*'
                guessed = ''
                for i in dashes:
                    guessed = guessed + i
                
                # print(guessed)
                if guessed == "".join(picked).lower():
                    print("Hurray! You got the country, its " +
                          "".join(picked).title() + "\U0001F601 \n")
                    break
                time.sleep(1)
            else:
                print('You missed' + "\U0001F612 \n")
                time.sleep(1)
                miss += 1

    if miss == 5:
        print("5 wrong guesses already,  You lost this round!" + '\n')
        print("The Country is " + "".join(picked).title() + "\U0001F923 \n")
        lifes -= 1
    if miss == 0:
        print("FLAWLESS!!!!!")
        print("you got a reward of one life" + "\U0001F601 \n")
        lifes += 1
    score += 100 - (miss * 20)
    time.sleep(1)
    print("loading.....")
    time.sleep(3)
    play(num + 1)

def add_score():
    with open("leaderboard.csv", "a") as file:
        date_ = date.today()
        user = [name,date_,score]
        writer_obj = csv.writer(file)
        writer_obj.writerow(user)

def reset_board():
    with open("leaderboard.csv", "w") as file:
        heading = ["name","date","score"]
        writer_obj = csv.writer(file)
        writer_obj.writerow(heading)
    print("Leadership board resetted!!!")
def main():
    try:
        prompt()
    except KeyboardInterrupt:
        quit()
    except EOFError:
        quit()
def quit():
    print("\033c")
    print(Fore.GREEN + "==========================================")
    print("==========================================")
    print("==                                      ==")
    print("==                                      ==")
    print("==       👋 👋 👋 👋 👋 👋 👋 👋        ==")
    print("==                                      ==")
    print("==                                      ==")
    print("==       GOOD BYE                       ==")
    print("==                                      ==")
    print("==       Hope to see you soon           ==")
    print("==                                      ==")
    print("==       👋 👋 👋 👋 👋 👋 👋 👋        ==")
    print("==                                      ==")
    print("==                                      ==")
    print("==            ©️ Author Akinola Samson   ==")
    print("==========================================")
    print("==========================================")
    sys.exit()
def start():
    print("\033c")
    print(Fore.LIGHTBLUE_EX + "==========================================================")
    print("===========================================================")
    print("==                                                       ==")
    print("==                                                       ==")
    print("==   🎌 🎌 🎌 🎌 🎌 🎌 🎌 🎌 🎌 🎌🎌 🎌🎌 🎌🎌 🎌        ==")
    print("==                                                       ==")
    print("==                                                       ==")
    print("==                   INSTRUCTIONS                        ==")
    print("==                                                       ==")
    print("==       Each round presents you with a country          ==")
    print("==       randomly selected from a list of 177            ==")
    print("==       countries or you to guess its alphabets.        ==")
    print("==       You have a maximum of 4 wrong guesses           ==")
    print("==       for each roundbefore you lose the round.        ==")
    print("==                                                       ==")
    print("==       You lose a diadem for every round you lose      ==")
    print("==       and get a diadem for every round  no miss       ==")
    print("==                                                       ==")
    print("==       You start with a total of 5 diadems and         ==")
    print("==       the game ends when you run out of diadems       ==")
    print("==                                                       ==")
    print("==                                                       ==")
    print("==       Enter a name (min of 3 chars) to continue:      ==")
    print("==                                                       ==")
    print("==                                                       ==")
    print("==   🎌 🎌 🎌 🎌 🎌 🎌 🎌 🎌 🎌 🎌🎌 🎌🎌 🎌🎌 🎌        ==")
    print("==                                                       ==")
    print("==                                                       ==")
    print("==                                                       ==")
    print("===========================================================")
    print("===========================================================")
    return(input())

if __name__ == "__main__":
    main()
