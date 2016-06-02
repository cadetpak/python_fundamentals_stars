# create function that takes list of numbers and prints that many '*'

def draw_stars(list): 
	for each in list: 
		print each * "*"

x = [4, 6, 1, 3, 5, 7, 26]
draw_stars(x)

# create function that takes list of strings and numbers and prints that many "*" if int, first letter lower case if str. 

def draw_stars2(list): 
	for each in list: 
		if type(each) == int: 
			print each * "*"
		elif type(each) == str: 
			# this splits the word (each) and pulls the first letter, makes it lower case
			for letter in each.lower().split()[0][0]: 
				value = letter
				# len(each) - counts the length of word
				print value * len(each)
y = [4, "Tina", 1, "Michelle", 5, 7, "Danielle Smith"]
draw_stars2(y)