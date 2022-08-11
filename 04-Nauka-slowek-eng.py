import json
import sys

points = 0

def game_rules(rules):
    print("Zasdady: ")
    print("odpowiedzi podawaj używając tylko małych liter,")
    print("Zbieraj punkty i rywalizuj,")
    print("Baw się dobrze i naucz się jak najwięcej! :)")
    rules = input("Akceptujesz zasady gry? tak / nie: ")

    if rules == "tak":
        print("Powodzenia!")
    elif rules == "nie":
        print("Przez brak akceptacji reguł, gra zakończona.")
        sys.exit(0)
    else:
        print("Nieprawidłowa odpowiedź. Podaj odpowiedź tak lub nie.")
        return

def show_question(question):
    global points
    
    print()
    print(question["pytanie"])
    print()

    answer = input("Odpowiedź: ")

    if answer == question["odpowiedź"]:
        points += 1
        print("To prawidłowa odpowiedź, brawo! Masz już", points, "punktów.")
    else:
        points -= 1
        print("Niestety to zła odpowiedź. Prawidłowa odpowiedź to " + question["odpowiedź"] + ". Masz już " + str(points) +".")

with open("nauka-eng.json", encoding = "utf-8") as json_file:
    questions = json.load(json_file)
    print(questions)

    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("Koniec gry, zdobyta liczba punktów to " + str(points) + ".")