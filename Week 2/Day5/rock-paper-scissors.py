from game import Game

def get_user_menu_choice():
    while True:
        print("Welcome to Rock-Paper-Scissors!")
        print("Please select an option:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")

        user_input = input("Enter your choice (1, 2, or 3): ")
        if user_input in ["1", "2", "3"]:
            return int(user_input)
        else:
            print("Invalid input. Please try again.")

def print_results(results):
    print("Game Results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("\nThanks for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == 1:
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == 2:
            print_results(results)
        elif choice == 3:
            print_results(results)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()