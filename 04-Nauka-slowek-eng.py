import json
import sys
import random

points = 0

def game_rules():
    print("\nZasdady: ")
    print("odpowiedzi podawaj używając tylko małych liter,")
    print("Zbieraj punkty i rywalizuj,")
    print("Baw się dobrze i naucz się jak najwięcej! :)\n")

    rules = ""
    while rules not in ["tak", "nie"]:
        rules = input("Akceptujesz zasady gry? tak / nie: ")

        if rules == "tak":
            print("\nPowodzenia!")
            print("----------------------------------------------------")
        elif rules == "nie":
            print("\nPrzez brak akceptacji reguł, gra zakończona.")
            sys.exit(0)
        else:
            print("Nieprawidłowa odpowiedź. Podaj odpowiedź tak lub nie.")

def show_question(question):
    global points
    
    print()
    print(question["pytanie"])
    print()

    answer = input("Odpowiedź: ")

    if answer == question["odpowiedź"]:
        points += 1
        print("\nTo prawidłowa odpowiedź, brawo! Masz już", points, "punktów.")
        print("----------------------------------------------------")
    else:
        points -= 1
        print("\nNiestety to zła odpowiedź. Prawidłowa odpowiedź to " + question["odpowiedź"] + ". Masz już " + str(points) +".")
        print("----------------------------------------------------")

with open("nauka-eng.json", encoding = "utf-8") as json_file:
    questions = json.load(json_file)
    game_rules()

    for i in range(0, len(questions)):
        show_question(questions[i])

print("\nKoniec gry, zdobyta liczba punktów to " + str(points) + ".")
