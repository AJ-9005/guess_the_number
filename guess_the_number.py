from random import randint
def user_guess():
    x = int(input("Enter range: "))
    num = randint(1, x)
    n = 0
    count=1
    while(n != num):
        n = int(input("Enter ur guess: "))
        if n > num:
            print("Number guessed is too high!")
            count+=1
        elif n < num:
            print("Number guessed is too low!")
            count+=1
    print("Bingo! You got the target!")
    print(f"\nIt took you {count} tries!")
def comp_guess():
    a = False
    while a==False:
        num = int(input("Enter a 2-digit no: "))
        if len(str(num)) > 2:
            print("Please input a 2-digit number!")
        else:
            a = True
    count=1
    guess=randint(0,99)
    while guess!=num:
        guess=randint(0,99)
        if guess==num:
            print(f"The computer found ur number. Its {guess}!")
            print(f"It took the computer {count} tries! ")
        elif guess<num:
            print(f"The computer guessed {guess}!")
            l=guess+1
            count+=1
        elif guess>num:
            print(f"The computer guessed {guess}!")
            r=guess-1
            count+=1
def main():
    x=False
    while x==False:
        game = int(input("Enter which game you wish to play?\n1. Human guesses the no.\n2. Computer guesses the no.\n3. Exit\nYour choice: "))
        if game==1:
            user_guess()
            print("\n")
        elif game==2:
            comp_guess()
            print("\n")
        elif game==3:
            x=True
        else:
            print("\nPlease enter valid choice!")
main()