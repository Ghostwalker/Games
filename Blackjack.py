import random

def shuffledDeck():
  
  suits = {"\u2663", "\u2662", "\u2661", "\u2660"}
  ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
  
  deck = []
  
  for suit in suits:
    for rank in ranks:
      deck.append(rank + " " + suit)
      
      
  random.shuffle(deck)
  return deck
  
  
def dealCard(deck, participant):
  
  card = deck.pop()
  participant.append(card)
  return card
  
  
def total(hand):
  values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '1':10, 'J':10, 'Q':10, 'K':10, 'A':11}
  result = 0
  numAces = 0
  
  for card in hand:
    result += values[card[0]] 
    if card[0] == "A":
      numAces += 1
      
  while result > 21 and numAces > 0:
    result -= 10
    numAces -= 1
  
  return result
  
def compareHands(house, player):

  houseTotal, playerTotal = total(house), total(player)

  if houseTotal > playerTotal:
    print('You lose.')
    
  elif houseTotal < playerTotal:
    print('You win.')
    
  elif houseTotal == 21 and 2 == len(house) < len(player):
    print('You lose.')
    
  elif playerTotal == 21 and 2 == len(player) < len(house):
    print('You win.') 
    
  else:
    print('A tie.')  
    
    
    
    
def blackjack():
  
  deck = shuffledDeck()
  player = []
  house = []
  
  for i in range(2):
    dealCard(deck, house)
    dealCard(deck, player)
    
  print('House:{:>7}{:>7}'.format(house[0] , house[1]))
  print(' You:{:>7}{:>7}'.format(player[0], player[1]))
  
  
  answer = input('Hit or stand? (default: hit): ')
  
  while answer in {'', 'h', 'hit'}:
    card = dealCard(deck, player)
    print('You got{:>7}'.format(card))
    
    if total(player) > 21:
      print('You went over... You lose.')
      return
    
    answer = input('Hit or stand? (default: hit): ')
  
  while total(house) < 17:
    card = dealCard(deck, house)
    print('House got{:>7}'.format(card))
    
    if total(house) > 21:
      print('House went over... You win.')
      return
  
  compareHands(house, player)
    
    
blackjack()
