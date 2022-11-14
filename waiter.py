# Waiter

# W riting
# a n
# i nteresting
# t ext-type
# e solang
# r estaurant

import sys

listed = [[]]

#               I/O        I/O        INPUT     OUTPUT   OUTPUT    PUSH     PUSH      POP     POP     IF    IS    ISN'T      ADD        ADD       MINUS   MINUS     DIVIDE      DIVIDE      MULTIPLY     MULTIPLY    DUPE      DUPE      SWAP       SWAP     NULL    NULL      MOD      MOD      INFINITE   NO POP I/O NO POP I/O
dictionary = ["burger", "burgers", "coleslaw", "chips", "fries", "waters", "water", "salts", "salt", "if", "is", "isn't", "chicken", "chickens", "beef", "beefs", "mushroom", "mushrooms", "stuffings", "stuffing", "lemon", "lemons", "orange", "oranges", "plum", "plums", "crisp", "crisps", "infinite", "ketchup", "ketchups"]
punctuation = [" ", ",", ".", ":", ";"]

def lex(text):
	global listed
	tok = ""
	i = 0
	for char in text:
		tok += char
		if char in punctuation and (tok[:-1] in dictionary or tok[:-1].isnumeric() or tok[1:-1].isnumeric()):
			if tok[:-1] == "infinite":
				listed[i].append(sys.maxsize)
			else:
				listed[i].append(tok[:-1])
			tok = ""
		elif char in punctuation and not (tok[:-1] in dictionary or tok[:-1].isnumeric() or tok[1:-1].isnumeric()):
			tok = ""
		elif char == "\n":
			listed.append([])
			i += 1
			tok = ""
	#print(listed)

def parse(text):
	stack = []
	for i in range(len(listed)):
		for j in range(len(listed[i])):
			if listed[i][j] in ["burger", "burgers"]:
				for k in range(int(listed[i][j-1])):
					if listed[i][j + 1] == "coleslaw":
						stack += list(input().encode("ascii"))
					if stack[0] > 0:
						if listed[i][j + 1] in ["chips", "fries"]:
							try: 
								if listed[i][j+2]:
									print(chr(stack[0]), end="")
							except Exception:
								print(chr(stack[0]), end="")
								stack.pop(0)
					else:
						break;
			if listed[i][j] in ["water", "waters"]:
				stack.insert(0, int(listed[i][j-1]))
			if listed[i][j] in ["salt", "salts"]:
				stack.pop(int(listed[i][j-1]))
			if listed[i][j] in ["chicken", "chickens"]:
				stack.insert(0, stack[0] + stack[1])
				stack.pop(1)
				stack.pop(1)
			if listed[i][j] in ["beef", "beefs"]:
				stack.insert(0, stack[0] - stack[1])
				stack.pop(1)
				stack.pop(1)
			if listed[i][j] in ["mushroom", "mushrooms"]:
				stack.insert(0, stack[0] / stack[1])
				stack.pop(1)
				stack.pop(1)
			if listed[i][j] in ["crisp", "crisps"]:
				stack.insert(0, stack[0] % stack[1])
				stack.pop(1)
				stack.pop(1)
			if listed[i][j] in ["orange", "oranges"]:
				for k in range(int(listed[i][j-1])):
					stack = stack.reverse()
			if listed[i][j] == "if":
				if listed[i][j+1] == "is":
					if str(stack[0]) == listed[i][j+2]:
						stack.insert(0, 1)
					else:
						stack.insert(0, 0)
				if listed[i][j+1] == "isn't":
					if str(stack[0]) != listed[i][j+2]:
						stack.insert(0, 1)
					else:
						stack.insert(0, 0)
			if listed[i][j] in ["lemon", "lemons"]:
				for k in range(int(listed[i][j-1])):
					stack.insert(0, stack[0])
			if listed[i][j] in ["stuffing", "stuffings"]:
				stack.insert(0, stack[0] * stack[1])
				stack.pop(1)
				stack.pop(1)
	print(stack)

def main():
	try:
		parse(lex(open(sys.argv[1], "r").read()))
	except Exception:
		parse(lex(open("waiterTruthMachine.wtr", "r").read()))

if __name__ == '__main__':
	main()