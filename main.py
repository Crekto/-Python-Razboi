import tkinter as tk
import random
import sys
import settings
from PIL import Image, ImageTk
from tkinter import messagebox

## Global
deck = []
computerDeck = []
playerDeck = []
computerCard = playerCard = None
computerCardImage = playerCardImage = None


def getCardImage(card):
    cardImage = Image.open(card)
    resizedCardImage = cardImage.resize((225, 327))
    return ImageTk.PhotoImage(resizedCardImage)

def verifyGameOver():
    if len(computerDeck) == 0:
        messagebox.showinfo(title='Game Over', message = "Player won the game!")
        sys.exit()
    if len(playerDeck) == 0:
        messagebox.showinfo(title='Game Over', message = "Computer won the game!")
        sys.exit()

def updateNoOfCards():
    computer_cards.config(text=f"Cards: {len(computerDeck)}")
    player_cards.config(text=f"Cards: {len(playerDeck)}")
    verifyGameOver()

def razboi(noOfCards, cardsUsed):
    if len(computerDeck) > 0:
        for i in range(0,min(noOfCards,len(computerDeck))-1):
            cardsUsed.append(computerDeck.pop(0))
        global computerCard
        computerCard = computerDeck.pop(0)
        cardsUsed.append(computerCard)

        global computerCardImage
        computerCardImage = getCardImage(f'./images/{computerCard}.png')
        computer_label.config(image=computerCardImage)

    if len(playerDeck) > 0:
        for i in range(0,min(noOfCards,len(playerDeck))-1):
            cardsUsed.append(playerDeck.pop(0))
        global playerCard
        playerCard = playerDeck.pop(0)
        cardsUsed.append(playerCard)

        global playerCardImage
        playerCardImage = getCardImage(f'./images/{playerCard}.png')
        player_label.config(image=playerCardImage)

    computerCardValue = int(computerCard.split("_")[0])
    playerCardValue = int(playerCard.split("_")[0])

    if computerCardValue == playerCardValue:
        tempRazboi = playerCardValue
        if playerCardValue in [11, 12, 13]:
            tempRazboi = 10
        elif playerCardValue == 14:
            tempRazboi = 11
        messagebox.showinfo(title='Razboi', message=f'Razboi! Fiecare jucator va plasa {tempRazboi} carti, sau pe toate daca nu are destule.')
        razboi(tempRazboi, cardsUsed)
    elif computerCardValue > playerCardValue:
        round_winner_label.config(text="Computer won!")
        computerDeck.extend(cardsUsed)
    elif computerCardValue < playerCardValue:
        round_winner_label.config(text="Player won!")
        playerDeck.extend(cardsUsed)
    updateNoOfCards()
    

def shuffle():
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    random.shuffle(deck)
    global computerDeck, playerDeck
    computerDeck = deck[0:26]
    playerDeck = deck[26:52]
    nextRound()

def nextRound():
    razboi(1,[])
    print(f"{computerDeck} \nVS\n {playerDeck}\n")



root = tk.Tk()
root.title('Razboi')
root.geometry('1280x520')
root.configure(background=settings.BG)

my_frame = tk.Frame(root, bg=settings.BG)
my_frame.pack(pady=20)

computer_frame = tk.Frame(my_frame, width = 300, height = 600, bg=settings.BG)
computer_frame.grid(row = 0, column = 0)

computer_title = tk.Label(computer_frame, text = "Computer", font = settings.TITLE_FONT, bg = settings.BG, fg = settings.TEXT_COLOR)
computer_title.place(relx=0.5, rely=0.02, anchor='center')

# Cards left in computer deck
computer_cards = tk.Label(computer_frame, text = "", font = settings.CARDS_FONT, bg = settings.BG, fg = settings.TEXT_COLOR)
computer_cards.place(relx=0.5, rely=0.08, anchor='center')

# Current computer card
computer_label = tk.Label(computer_frame, text = "", bg = settings.BG)
computer_label.place(relx=0.5, rely=0.4, anchor='center')


player_frame = tk.Frame(my_frame, width = 300, height = 600, bg=settings.BG)
player_frame.grid(row = 0, column = 2)

player_title = tk.Label(player_frame, text = "Player", font = settings.TITLE_FONT, bg = settings.BG, fg = settings.TEXT_COLOR)
player_title.place(relx=0.5, rely=0.02, anchor='center')

# Cards left in player deck
player_cards = tk.Label(player_frame, text = "", font = settings.CARDS_FONT, bg = settings.BG, fg = settings.TEXT_COLOR)
player_cards.place(relx=0.5, rely=0.08, anchor='center')

# Current player card
player_label = tk.Label(player_frame, text = "", bg = settings.BG)
player_label.place(relx=0.5, rely=0.4, anchor='center')

round_winner_label = tk.Label(my_frame, text = "", width = 22, font = settings.MIDDLE_FONT, bg = settings.BG, fg = settings.TEXT_COLOR)
round_winner_label.grid(row = 0, column = 1)

next_button = tk.Button(my_frame, text='Next Round', font = settings.BUTTON_FONT, command=nextRound)
next_button.grid(row = 0, column = 1, pady=(300,0))


shuffle()
root.mainloop()