import random
import math


# call this everywhere
def ask_for_int(prompt, low, high):
    while True:
        try:
            x = int(input(prompt))
            if x >= low and x <= high:
                return x
            else:
                print("Invalid input. Please enter an integer between", low, "and", high)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# call this in math calc
def ask_for_float(prompt):
    while True:
        try:
            x = float(input(prompt))
            return x
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# option 1 in the menu
def math_calc():
    radius = ask_for_float("Enter the radius of the circle in inches: ")
    area = math.pi * (radius ** 2)
    print("The area is {:.2f}".format(area))
    print()


def get_computer_choice():
    return random.randint(1, 3)


def get_winner(user, computer, outcomes):
    return outcomes[user][computer]


# option 2 in the menu
def play_rps():
    user_score = 0
    computer_score = 0

    num_times = ask_for_int("Enter the number of times you want to play: ", 1, 5)

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    outcomes = {
        1: {1: "It's a tie!", 2: "Computer wins!", 3: "You win!"},
        2: {1: "You win!", 2: "It's a tie!", 3: "Computer wins!"},
        3: {1: "Computer wins!", 2: "You win!", 3: "It's a tie!"}}

    for x in range(num_times):
        user_choice = ask_for_int("Enter 1 for rock, 2 for paper, or 3 for scissors: ", 1, 3)
        while user_choice not in [1, 2, 3]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            user_choice = ask_for_int("Enter 1 for rock, 2 for paper, or 3 for scissors: ", 1, 3)

        computer_choice = get_computer_choice()

        print("You chose ", choices[user_choice])
        print("Computer chose", choices[computer_choice])

        result = get_winner(user_choice, computer_choice, outcomes)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    print("Final score was User:", user_score, "Computer:", computer_score)
    print("Thanks for playing.")
    print()


# tie it all together
def display_menu():
    while True:
        print("Menu:")
        print("1)Find the area of a circle")
        print("2)Play Rock Paper Scissors")
        print("3)Quit this program")
        print()
        # ask for int function
        choice = ask_for_int("Enter number for choice: ", 1, 3)
        print()

        if choice == 1:
            math_calc()
        elif choice == 2:
            play_rps()
        elif choice == 3:
            break
        else:
            print("Invalid option. Try again.")


def main():
    display_menu()


# don't forget to call your main function!
main()
print("Have a nice day!")
