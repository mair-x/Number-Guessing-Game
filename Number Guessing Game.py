import random

def difficulty():
    while True:
        try:
            number_of_guesses = int(input("Difficulty: Number of attempts! "))
            if number_of_guesses <= 0:
                print("Number of attempts must be positive!")
            else:
                return number_of_guesses
        except ValueError:
            print("Please enter a valid number!")

def minimal_value():
    while True:
        try:
            minimal = int(input("Minimal range value: "))
            if minimal < 0:
                print("Minimal value must be positive!")
            else:
                return minimal
        except ValueError:
            print("Please enter a valid number!")

def maximal_value():
    while True:
        try:
            maximal = int(input("Maximal range value: "))
            if maximal <= 0:
                print("Maximal value must be positive!")
            else:
                return maximal
        except ValueError:
            print("Please enter a valid number!")

def main():
    best_score = None
    results = []
    
    while True:
        maximal = maximal_value()
        minimal = minimal_value()
        
        while minimal > maximal:
            print("Minimum value must be less than maximum value.")
            minimal = minimal_value()
            maximal = maximal_value()
        
        attempts = difficulty()
        guessed_number = random.randint(minimal, maximal)
        counter = 0
        
        while True:
            try:
                number = int(input(f"Guess the number (between {minimal} and {maximal}): "))
                if number < minimal or number > maximal:
                    print(f"Please enter a number within the range of {minimal} to {maximal}.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            counter += 1
            if number > guessed_number:
                print(f"Too high! Try again. Number of attempts remaining: {attempts - counter}")
            elif number < guessed_number:
                print(f"Too low! Try again. Number of attempts remaining: {attempts - counter}")
            elif number == guessed_number:
                print(f"Congratulations! You guessed the number in {counter} attempts.")
                
                # Update best score
                if best_score is None or counter < best_score:
                    best_score = counter
                
                # Store result
                results.append(counter)
                if len(results) > 5:
                    results.remove(max(results))
                
                print(f"Top 5 scores: {sorted(results)}")
                print(f"Best score: {best_score} attempts")
                
                choice = input("Do you want to play again? (y/n): ")
                if choice == "n":
                    return
                else:
                    break
            
            if counter >= attempts:
                print(f"Game over! The number was {guessed_number}.")
                print(f"Best score: {best_score} attempts.")
                choice = input("Do you want to start again? (y/n): ")
                if choice == "n":
                    return
                else:
                    break

if __name__ == "__main__":
    main()
