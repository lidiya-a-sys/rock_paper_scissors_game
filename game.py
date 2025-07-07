import random
import os

# ASCII Art for Visuals
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    clear_screen()
    print("🎮 Welcome to Rock-Paper-Scissors! 🎮")
    print("----------------------------------")
    
    player_score = 0
    computer_score = 0
    round_num = 1
    
    while True:
        print(f"\n=== Round {round_num} ===")
        print(f"Score: You {player_score} - {computer_score} Computer")
        
        player_choice = input("\nChoose: rock, paper, or scissors? (or 'quit'): ").lower()
        
        if player_choice == 'quit':
            break
            
        if player_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Try again.")
            continue
            
        # Computer's random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        # Display choices with ASCII art
        print(f"\nYou chose:\n{game_images[['rock', 'paper', 'scissors'].index(player_choice)]}")
        print(f"Computer chose:\n{game_images[['rock', 'paper', 'scissors'].index(computer_choice)]}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            print("🎉 You win this round!")
            player_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1
        
        round_num += 1
        
        # Ask to play again
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    # Final results
    print("\n=== Game Over ===")
    print(f"Final Score: You {player_score} - {computer_score} Computer")
    if player_score > computer_score:
        print("🔥 You are the champion! 🔥")
    elif player_score < computer_score:
        print("😢 Computer wins. Better luck next time!")
    else:
        print("🤷 It's a draw!")
    
    print("\nThanks for playing! 🎮")

# Start the game
if __name__ == "__main__":
    play_game()