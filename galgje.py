print("Tomas de Jonge / 1043773 ")

HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  |   |
  0   |
 /|\  |
 / \  |
========='''
]

woord = input("Vul een woord in: ")
print(woord)

spelen = True
fouten = 0
woordenlijst = []
for index in woord: 
    woordenlijst += "_"
    
while spelen: 
    letter = input("Vul een letter in: ")
    
    letterinwoord = letter in woord 
    if letterinwoord == False:
        print(HANGMANPICS[fouten])
        fouten = fouten + 1
        print("Je heb een fout gemaakt. Probeer het op nieuw!")
        
        if fouten >= 9:
            print("Je heb verloren game over. Probeer het nog een keer!")
            spelen = False
    
    else:
        for index in range(len(woord)):
            if woord[index] == letter:
                woordenlijst[index] = letter
            
        geraden_woord = ''.join(woordenlijst)
        if(geraden_woord == woord):
            print("Gefeliciteerd je heb gewonnen!")
            spelen = False
        print(woordenlijst)