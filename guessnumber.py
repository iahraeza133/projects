import random
def guess_number():
    count = 0
    max_count = 5
  
    while count < max_count:
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
        
        if lower >= upper:
            print("Invalid range! The lower bound must be less than the upper bound.")
            continue
        
        generated_input = random.randint(lower, upper)
        guess = int(input("Guess the number: "))
        
        if guess == generated_input:
            print("Correct! You guessed it.")
        else:
            print(f"Wrong! The correct number was {generated_input}.")
        
        count += 1
        print(f"Attempt {count}/{max_count} finished.\n")

    print("Game over! Try again.")

# Run the game
print(guess_number())
