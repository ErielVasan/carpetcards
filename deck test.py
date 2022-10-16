import random


suit = ["C", "H", "S", "D"]
number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
jokers = 2
grid = 5

class Card():

	def __init__(self, number, suit):
		self.number = number 
		self.suit = suit if not self.number == "Joker" else "*"
		self.colour = "red" if self.suit == "H" or self.suit == "D" else "neutral" if self.suit == "*" else "black" 
		self.points = 10 if self.number == "J" or self.number == "Q" or self.number == "K" else 0 if self.number == "Joker" else 11 if self.number == "A" else int(self.number)  

	def __str__(self):
				return f"The {self.number} of {self.suit}. It's a {self.colour} card with a worth of {self.points} points."	


class Deck():

	def __init__(self):
		self.cardlist = []
		for x in range(len(suit)):
			for y in range(len(number)):
				self.cardlist.append(Card(number[y], suit[x])) 
		for x in range(jokers):
			self.cardlist.append(Card("Joker", ""))
		self.current = 0
	
	def shuffle(self):
		random.shuffle(self.cardlist)
		self.current = 0

	def deal(self):
		self.current += 1
		return self.cardlist[self.current]

		
	def __str__(self):
			for x in range(len(self.cardlist)):
					print(self.cardlist[x])	


deck = Deck()
totalPoints = 0
totalReds = 0
totalBlacks = 0
totalNeutrals = 0
totalHis = 0

totalTests = 100000000

def game():
	global totalPoints, totalReds, totalBlacks, totalNeutrals, totalHis
	deck.shuffle()
	dealt = []
	for x in range(grid**2):
		dealt.append((deck.deal()))
	
	blacks = 0
	reds = 0
	neutrals = 0
	points = 0
	his = 0

	for x in range(len(dealt)):
		points += dealt[x].points
		if dealt[x].colour == "red":
			reds += 1
		elif dealt[x].colour == "black":
			blacks += 1
		elif dealt[x].colour == "neutral": 
			neutrals += 1
		if dealt[x].points >= 7:
			totalHis += 1

	totalPoints += points
	totalReds += reds
	totalBlacks += blacks
	totalNeutrals += neutrals


def routine(amount):
	for x in range(amount):
		game()

routine(totalTests)
print("Average points:", totalPoints/totalTests, "Average his:", totalHis/totalTests, "Average reds:", totalReds/totalTests, "Average blacks:", totalBlacks/totalTests, "Average neutrals:", totalNeutrals/totalTests)
