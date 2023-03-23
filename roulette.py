class Roulette:
	def __init__(self):
		self.displayPossibleBets = ["Number (0, 00 - 36)", "Red", "Black", "Even", "Odd"]
		self.possibleBets = ["00"] + str(range(0,37)) + ["Red", "Black", "Even", "Odd"]
		self.possibleRolls = ["00"] + str(range(0,37))
		self.blackNumbers = [str(i) for i in range(1,36) if (i in list(range(1,11)) + list(range(19,29)) and i%2==0) or (i in list(range(11, 19)) + list(range(29, 37)) and i%2==1)]
		self.redNumbers   = [str(i) for i in range(1,36) if (i in list(range(1,11)) + list(range(19,29)) and i%2==1) or (i in list(range(11, 19)) + list(range(29, 37)) and i%2==0)]

	def play():
		print("Welcome to Roulette!")
		game = True

		while game:
			print("What would you like to bet on?")
			for possibleBet in displayPossibleBets:
				print(possibleBet)
			bet = input(">>> ")
			
			roll = possibleRolls[random.randint(0,38)]

			print(f"The roll was a {roll}!")

			if bet == str(roll):
				print("You guessed the number exactly! You win ")