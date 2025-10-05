import random

computer_number = random.randint(1, 100)

print("Try to guess the number from 1 to 100:\n You have only 10 attempts!")
total_chances = 10
attempts = 0
while True:
    player_input = input("Guess the number: ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    if int(player_input) > 100:
        print("Invalid number. Try again...")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        attempts += 1
        print(f"Congratulations, you guessed the number in {attempts} attempts.")
        break
    elif player_number > computer_number:
        total_chances -= 1
        attempts += 1
        print(f"Your number is too High! You only have {total_chances} attempts left.")
    elif player_number < computer_number:
        total_chances -= 1
        attempts += 1
        print(f"Your number is too Low! You only have {total_chances} attempts left.")

    if total_chances <= 0:
        print("Sorry but you have no more attempts!")
        break
