import random
winning_number = random.randint(1,100)
count = 1
guess_number = int(input('Enter your Guessed number between 1 to 100 '))
while True:
    if winning_number == guess_number:
        print(f'You win! Finally You Guessed the right number in {count} efforts')
        print(f'winning_number : {winning_number}\tguessed_number {guess_number}')
        break
    elif guess_number > winning_number:
        print(f'Too High  {guess_number}')
        print(f'winning_number : {winning_number}\tguessed_number {guess_number}')
    elif guess_number < winning_number:
        print(f'Too Low {guess_number}')
        print(f'winning_number : {winning_number}\tguessed_number {guess_number}')
    guess_number = int(input('Enter your guessed Number between 1 to 100 '))
    winning_number = random.randint(1,100)
    count = count +1 