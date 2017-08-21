import re

class Mastermind():
	def __init__(self):
		self.code = []
		self.code_counts = {}
		self.num = 10
		self.guesses = []
		self.evaluations = []

	def evaluateGuess(self, guess):
		self.guesses.append(guess)

		counts = dict(self.code_counts)
		result = [0, 0, 0, 0]
		
		for i in range(4):
			if guess[i] == self.code[i]:
				result[i] = 2
				counts[guess[i]] -= 1

		for i in range(4):
			if result[i] != 2:
				if guess[i] in self.code and counts[guess[i]] > 0:
					result[i] = 1
					counts[guess[i]] -= 1


		result = list(map(str, result))
		self.evaluations.append(result)

		print("your guess: " + " ".join(guess))
		print("evaluation: " + " ".join(result))


	def formatCode(self, code):
		code = re.sub("[^a-zA-Z]+", "", code)
		code = code.replace(" ", "")
		return code

	def validCode(self, code):
		for char in code:
			if char not in ["a", "b", "c", "d", "e", "f"]:
				return False

		return len(code) == 4


	def ongoing(self):
		if len(self.guesses) >= self.num:
			return "codemaker wins, codebreaker loses!"
		if self.guesses != [] and self.guesses[-1] == self.code:
			return "codebreaker wins, codemaker loses!"
		else:
			return "ongoing"


	def __main__(self):
		print("Welcome to Mastermind!")
		print("")
		print("There are six possible symbols: a, b, c, d, e, f")
		print("0 means the symbol in the same position is not contained the code,")
		print("1 means the symbol in the same position is contained in the code but is in an incorrect position")
		print("2 means the symbol in the same position is in the correct position in the code")

		print("")
		self.code = self.formatCode(input("Codemaker, please input a 4 symbol sequence: "))

		while not self.validCode(self.code):
			self.code = self.formatCode(input("Please input a valid 4 symbol sequence: "))
		
		self.code = list(self.code)
		print("Entered code: " + " ".join(self.code))
		print("")
		for char in self.code:
			if char not in self.code_counts:
				self.code_counts[char] = 1
			else:
				self.code_counts[char] += 1

		self.num = input("Input the maximum number of guesses allowed (no leading zeros): ")
		while not self.num.isdigit() or self.num[0] == '0':
			self.num = input("Input a valid number greater than 0: ")
		self.num = int(self.num)
		print("")

		while self.ongoing() == "ongoing":
			guess = self.formatCode(input("Codebreaker, please input a guess: "))
			while not self.validCode(guess):
				guess = input("Please input a valid 4 symbol sequence: ")
			guess = list(guess)
			self.evaluateGuess(guess)
			print("guesses left: " + str(self.num-len(self.guesses)))
			print("")
		
		print(self.ongoing())

m = Mastermind()
m.__main__()
		