# Casino simulator by mattman2864 on GitHub

import random
import coloredtext

games = ["Blackjack", "Poker", "Roulette", "Slots"]

if __name__ == "__main__":

	print("Welcome to the Casino!")
	isRunning = True

	while isRunning:
		print("Which game would you like to play?")
		for game in games:
			print(f"{games.index(game)+1}: {game}")
		print("Q: Exit Casino")
		chosengame = input(">> ")
		try:
			if chosengame.isnumeric():
				chosengame = games[int(chosengame)-1]
		except:
			print("\nThat number is not on the list!")
			continue

		if chosengame.lower() in ["quit", "q"]:
			print("Thanks for playing!")
			quit()