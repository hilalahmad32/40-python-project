class MedLibsGame:
    def __init__(self):
        global gameName,gameType
        print('President ', 'Vacations ', 'Party Time ', 'Selecting a Tree')
        gameName=['President', 'Vacations', 'Party Time', 'Selecting a Tree']


    def palyGame(self):
        gameType=input('Which game you want to play  > ')
        if gameType in gameName:
            if gameType == 'President':
                print('IF I WERE A PRESIDENT')
                name=input('Your Name (noun) > ')
                number=input('Your Age (noun) > ')
                adjactive=input('Adjactive > ')
                color=input('Color > ')
                noun1=input('Noun > ')
                typeOfFood=input('Food Noun > ')
                noun2=input('Noun > ')
                verb=input('Verb With End ing > ')
                number1=input('Number > ')
                output=f"My name is {name} and i am {number}. If I were president , I'd do a whole bunch of {adjactive} things: \n 1. I would dive the biggest {color} car in the country.And that car would go faster then any other {noun1} in the world! \n 2. Everyone would eat pepperoni  {typeOfFood} for diner. \n 3. I would live in the statue of  {noun2} and build a {verb} pool at her feet 4. School would be open only {number1} days a year"
                print(output)

            elif gameType == 'Party Time':
                print('PARTY TIME')
                adj = input('Adjactive > ')
                noun = input('Noun > ')
                verb = input('verb  > ')
                noun1 = input('Noun > ')
                cl = input('Celebrtoy  > ')
                male = input('person in a Room > ')
                sillyword = input('Silly World > ')
                verb1 = input('Type of food > ')
                food = input('Type of Food > ')
                noun2 = input('Noun > ')

                output=f'''One of the most {adj} things about graduating is that my {noun} are {verb} a huge party! I decided to have a backyard barbecue for all of my family and {noun1} I've invited my best friends {cl} , {male} 
and of course my teacher Mrs.{sillyword}. My dad is going {verb1} hamburgers and {food} on his shiny new {noun2}.
'''
                print(output)

            elif gameType == 'Selecting a Tree':
                print(f'{gameType} game is pending.....')
            else:
                print(f'{gameType} game is also in pending....')
        else:
            print("not in list")

gameMed=MedLibsGame()
gameMed.palyGame()
while True:
    again=input('Are you want to paly again y / n ')
    if again == 'y' or again == 'Y':
        gameMed.palyGame()
    else:
        exit()
        print("Thank You")
