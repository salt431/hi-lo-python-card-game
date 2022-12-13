import random
#create initial deck
card_lst = ["2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d", "Jd", "Qd", "Kd", "Ad", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "Js", "Qs", "Ks", "As", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "Jh", "Kh", "Qh", "Ah", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc", "Ac"]

#define function to allow for easy restarting of the game
def start():
  #using substrings to determine the value of the cards being shuffled
  substring2 = "2"
  substring3 = "3"
  substring4 = "4"
  substring5 = "5"
  substring6 = "6"
  substring7 = "7"
  substring8 = "8"
  substring9 = "9"
  substring10 = "10"
  substringKing = "K"
  substringQueen = "Q"
  substringJack = "J"
  substringAce = "A"

  #shuffle the actual cards
  random.shuffle(card_lst)

  #the substring logic
  print("you got")
  for i in range(1):
    if substring2 in card_lst[i]:
      card = 2
    elif substring3 in card_lst[i]:
      card = 3
    elif substring4 in card_lst[i]:
      card = 4
    elif substring5 in card_lst[i]:
      card = 5
    elif substring6 in card_lst[i]:
      card = 6
    elif substring7 in card_lst[i]:
      card = 7
    elif substring8 in card_lst[i]:
      card = 8
    elif substring9 in card_lst[i]:
      card = 9
    elif substring10 in card_lst[i]:
      card = 10
    elif substringJack in card_lst[i]:
      card = 11
    elif substringQueen in card_lst[i]:
      card = 12
    elif substringKing in card_lst[i]:
      card = 13
    else: card = 14
    #print logic
    print(card_lst[i], "with a value of", card)
    #game logic
    game = input("higher or lower?")
  if game == "higher" or "lower":
      #Reshuffle required
      random.shuffle(card_lst)
  #substring logic for card2
  for i in range(1):
    if substring2 in card_lst[i]:
      card2 = 2
    elif substring3 in card_lst[i]:
      card2 = 3
    elif substring4 in card_lst[i]:
      card2 = 4
    elif substring5 in card_lst[i]:
      card2 = 5
    elif substring6 in card_lst[i]:
      card2 = 6
    elif substring7 in card_lst[i]:
      card2 = 7
    elif substring8 in card_lst[i]:
      card2 = 8
    elif substring9 in card_lst[i]:
      card2 = 9
    elif substring10 in card_lst[i]:
      card2 = 10
    elif substringJack in card_lst[i]:
      card2 = 11
    elif substringQueen in card_lst[i]:
      card2 = 12
    elif substringKing in card_lst[i]:
      card2 = 13
    else: card2 = 14
    #game outcome logic
    if game == "higher":
      if card2 > card:
        wingame = "you won the game bro!"
      elif card2 < card:
        wingame = "you lost the game bro!"
    if game =="lower":
      if card2 < card:
        wingame = "you won the game bro!"
      if card2 > card:
        wingame = "you lost the game bro!"
    #print the outcome of the game
    print("the next card is:", card_lst[i], "with a value of", card2, wingame)
    #play again? logic for it here
    playagain = input("would you like to play the game again?")
    if playagain == "yes":
      start()
    if playagain == "no":
      exit()
    
start()

    
