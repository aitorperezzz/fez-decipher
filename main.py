def main():
	# Load symbols to memory.
	symbols = loadSymbols()
	if symbols == None:
		print('Could not load symbols to memory')
		return -1
	print('Symbols loaded to memory')

	# Rotate all symbols into the 4 directions to obtain
	# all the letters of the alphabet.
	alphabet = []
	for symbol in symbols:
		alphabet.append(symbol)
		for i in range(3):
			alphabet.append(rotateSymbol(alphabet[-1]))

	# Print the help guide (association of letters to numbers).
	i = 0
	while i < len(alphabet):
		printLettersWithCode(alphabet, i, i + 4)
		i += 4


def loadSymbols():
	symbols = []
	for i in range(6):
		with open('./symbols/s' + str(i) + '.txt', 'r') as symbol:
			symbols.append([list(line.rstrip('\n')) for line in symbol])

	# Check all the symbols have the right dimensions.
	for symbol in symbols:
		for line in symbol:
			if len(line) != 5:
				print('ERROR: one of the symbols does not have proper dimensions')
				return None
	print('All symbols have proper dimensions')

	return symbols


def rotateSymbol(symbol):
	newSymbol = []
	for i in range(5):
		newSymbol.append([])
		for j in range(5):
			newSymbol[i].append(symbol[4 - j][i])
	return newSymbol


def printLetter(letter):
	for line in letter:
		for element in line:
			print(element, end='')
		print()


def printLettersWithCode(alphabet, start, end):
	for i in range(4):
		displayLine = ''
		for j in range(end - start):
			for k in range(5):
				displayLine += alphabet[start + j][i][k]
			displayLine += '        '
		print(displayLine)
	displayLine = ''
	for j in range(end - start):
		for k in range(5):
			displayLine += alphabet[start + j][4][k]
		displayLine += '  ' + str(start + j).rjust(2, ' ') + '    '
	print(displayLine)
	print()

if __name__ == '__main__':
	main()
