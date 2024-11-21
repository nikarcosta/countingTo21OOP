import random

class CountingTo21OOP:
    def __init__(self):
        self.currentPlayer = ""
        self.number = 0
        self.arr_of_numbers = []

    def define_who_plays_first(self):
        while True:
            answer = input("Do you want to start the game? (Y/N):").upper()
            if answer == 'Y':
                self.currentPlayer = "user"
                break
            elif answer == 'N':
                self.currentPlayer = "computer"
                break
            else:
                print("Invalid option! Please enter 'Y' or 'N'.")

    def computer_move(self):
        moves = random.randint(1, 3)
        new_numbers = [self.number + i + 1 for i in range(moves)]
        self.number = new_numbers[-1]
        self.arr_of_numbers.extend(new_numbers)
        print(f"Computer's move: {new_numbers}")
        print(f"Current sequence: {self.arr_of_numbers}")

    def validate_user_input(self):
        while True:
            user_input = input(
                    "Enter a sequence up to 3 numbers separated by comma or just enter a single number: ")
            try:
                user_numbers = [int(num.strip()) for num in user_input.split(",")]
                is_consecutive = all(
                    user_numbers[i] == user_numbers[i - 1] + 1 for i in range(1, len(user_numbers)))
                if user_numbers[0] == self.number + 1 and is_consecutive and len(user_numbers) <= 3:
                    return user_numbers
                else:
                    print("Invalid input. Make sure the numbers are consecutive and within the range.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")


    def play_game(self):
        print("====Welcome To Counting To 21 Game!====")
        self.define_who_plays_first()

        while self.number < 21:
            if self.currentPlayer == "computer":
                self.computer_move()
                if self.number == 21:
                    print("Computer loses! You win!")
                    break
                self.currentPlayer = "user"
            else:
               user_numbers = self.validate_user_input()
               self.arr_of_numbers.extend(user_numbers)
               self.number = user_numbers[-1]
               print(f"Your move: {user_numbers}")
               print(f"Current sequence: {self.arr_of_numbers}")
               if self.number == 21:
                   print("Computer wins! You lose!")
                   break
               self.currentPlayer = "computer"

game = CountingTo21OOP()
game.play_game()
