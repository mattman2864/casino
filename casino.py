# Casino simulator by mattman2864 on GitHub

import random
import time

games = ["Blackjack (N/A)", "Poker (N/A)", "Roulette", "Slots"]
coins = 100

class Roulette:
	def __init__(self):
		self.displayPossibleBets = ["Number (0, 00 - 36)", "Red", "Black", "Even", "Odd"]
		self.possibleBets = ["00"] + [str(i) for i in range(0,37)] + ["Red", "Black", "Even", "Odd"]
		self.possibleRolls = ["00"] + [str(i) for i in range(0,37)]
		self.blackNumbers = [str(i) for i in range(1,36) if (i in list(range(1,11)) + list(range(19,29)) and i%2==0) or (i in list(range(11, 19)) + list(range(29, 37)) and i%2==1)]
		self.redNumbers   = [str(i) for i in range(1,36) if (i in list(range(1,11)) + list(range(19,29)) and i%2==1) or (i in list(range(11, 19)) + list(range(29, 37)) and i%2==0)]

	def play(self, coins):
		print("Welcome to Roulette!")
		game = True

		while game:
			print("What would you like to bet on?")
			for possibleBet in self.displayPossibleBets:
				print(f"-{possibleBet}")
			print("-Quit")
			bet = input(">>> ")

			if bet.lower() == "quit":
				game = False
				print("Leaving Roulette...")
				return coins
			
			print(f"How many of your coins will you bet? (You have {coins})")
			coinsbet = input(">>> ")

			while float(coinsbet) > coins or float(coinsbet) <= 0 or "." in coinsbet:
				print(f"Invalid number of coins!")
				print(f"How many of your coins will you bet? (You have {coins})")
				coinsbet = input(">>> ")
			if coinsbet == "all":
				coinsbet = coins
			coinsbet = int(coinsbet)
			coins -= coinsbet
			
			roll = self.possibleRolls[random.randint(0,38)]

			print(f"The roll was a {roll}")

			if bet == roll:
				print("You guessed the number exactly! You win!")
				winratio = 35
			elif bet.lower() == "odd" and int(roll)%2==1:
				print("You guessed that the number was odd! You win!")
				winratio = 2
			elif bet.lower() == "even" and int(roll)%2==0:
				print("You guessed that the number was even! You win!")
				winratio = 2
			elif bet.lower() == "red" and roll in self.redNumbers:
				print("You guessed that the roll was red! You win!")
				winratio = 2
			elif bet.lower() == "black" and roll in self.blackNumbers:
				print("You guessed that the roll was black! You win!")
				winratio = 2
			else:
				print("Your bet was incorrect!")
				winratio = 0

			if winratio:
				print(f"You won {coinsbet*winratio} coins!")
			else:
				print("You lost all the coins you bet!")

			coins += coinsbet*winratio
			print(f"You now have {coins} coins")

class Slots:
	def __init__(self):
		self.ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]
	def play(self, coins):

		ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]

		print(f"Welcome to slots!")

		while 1:
			print(f"How many of your coins will you bet? (You have {coins})")
			coinsbet = input(">>> ")

			while float(coinsbet) > coins or float(coinsbet) <= 0 or "." in coinsbet:
				print(f"Invalid number of coins!")
				print(f"How many of your coins will you bet? (You have {coins})")
				coinsbet = input(">>> ")
			if coinsbet == "all":
				coinsbet = coins
			coinsbet = int(coinsbet)
			coins -= coinsbet

			input("PRESS [ENTER] TO SPIN")
			spins = []

			for i in range(3):
				for j in range(random.randint(20,40)):
					print("      \r", end="")
					print(ITEMS[(i + j)%len(ITEMS)], "\r", end="")
					time.sleep(0.05)
					spin = ITEMS[(i + j)%len(ITEMS)]
				spins.append(spin)
				print()

			if((spins[0] == "CHERRY") and (spins[1] != "CHERRY")):
				win = 2
			elif((spins[0] == "CHERRY") and (spins[1] == "CHERRY") and (spins[2] != "CHERRY")):
				win = 5
			elif((spins[0] == "CHERRY") and (spins[1] == "CHERRY") and (spins[2] == "CHERRY")):
				win = 7
			elif((spins[0] == "ORANGE") and (spins[1] == "ORANGE") and ((spins[2] == "ORANGE") or (spins[2] == "BAR"))):
				win = 10
			elif((spins[0] == "PLUM") and (spins[1] == "PLUM") and ((spins[2] == "PLUM") or (spins[2] == "BAR"))):
				win = 14
			elif((spins[0] == "BELL") and (spins[1] == "BELL") and ((spins[2] == "BELL") or (spins[2] == "BAR"))):
				win = 20
			elif((spins[0] == "BAR") and (spins[1] == "BAR") and (spins[2] == "BAR")):
				win = 250
			else:
				win = 0

			coinsbet *= win 
			coins += coinsbet

			print(f"You won {coinsbet} coins!")

			print(f"Would you like to play again? You now have {coins} coins.")
			playagain = input(">>> ")
			if not playagain.lower() in ["y", "yes"]:
				print("Leaving Slots...")
				break

		return coins

if __name__ == "__main__":

	print("Welcome to the Casino!")
	isRunning = True

	roulette = Roulette()
	slots = Slots()

	while isRunning:
		if not coins:
			print("You have 0 coins, you can not bet any more :(")
			break

		print(f"Which game would you like to play? You have {coins} coins.")
		for game in games:
			print(f"{games.index(game)+1}: {game}")
		print("Q: Quit")
		chosengame = input(">>> ")
		try:
			if chosengame.isnumeric():
				chosengame = games[int(chosengame)-1]
		except:
			print("\nThat number is not on the list!")
			continue

		if chosengame.lower() in ["quit", "q"]:
			print("Thanks for playing!")
			quit()

		if chosengame.lower() == "roulette":
			coins = roulette.play(coins)
		elif chosengame.lower() == "slots":
			coins = slots.play(coins)