import random
try:
    class GuessNumber:
        def __init__(self):
            print('-------------    ||                   || ||---------------   -----------------')
            print('-------------    ||                   || ||---------------   -----------------')
            print('||               ||                   || ||                  ||')
            print('||               ||                   || ||                  ||')
            print('||               ||                   || ||                  ||')
            print('||       ---     ||                   || ||---------------   ||---------------')
            print('||       ---     ||                   || ||---------------   ||---------------')
            print('||         | |   ||                   || ||                                  ||')
            print('||         | |   ||                   || ||                                  ||')
            print('||         | |   ||                   || ||                                  ||')     
            print('-----------      ||-------------------|| ||---------------   ----------------||')
            print('-------------    ||-------------------|| ||---------------   ----------------||')

            global name
            name=input('Enter your name  > ')

        def guess(self,x):
            input_number=int(input(f"Enter the number between 1 and {x} > "))
            number=random.randint(1,x)

            if input_number == number:
                print(f"{name} are number {input_number} is equal to {number}")
                print(f"{name} won the game")
            elif input_number > number:
                print(f"{name} Number {input_number} is Heigh")
                print("Computer won the game")
            elif input_number < number:
                print(f"{name} Number {input_number} is Low")
                print(f"{name} loss the game")
            else:
                print("Your number is not in 1 to 10")

    guess_number=GuessNumber()
    guess_number.guess(10)
    while True:
        again=input('you want to paly again yes / no ')
        if again == 'yes':
            guess_number.guess(10)
        else:
            exit()
    exit()
except:
    pass
finally:
    print("Your Game is exit Thank you")
