import random

grammar = {
			'NN':['man', 'dog', 'box'],
			'VP':['sleeps', 'walks'],
			'DT':['the', 'a', 'some', 'that'],
			'JJ':['red', 'green', 'large', 'JJ JJ'],
			'NP':['DT NN' ,'DT JJ NN'],
			'S':['NP VP NP'],
			'Q':['Does S ?']
			}

taglist = grammar.keys()

def expand(symbol):
	expanded = random.choice(grammar[symbol])
	return expanded

def check_for_keys(string):
	intersect = set(string.split(' ')).intersection(set(taglist))
	return intersect

def parse(start_symbols):
	global symbol_list
	symbol_list=start_symbols.split(' ')
	for i in range(0,len(symbol_list)):
		if symbol_list[i] in taglist:
			symbol_list[i]=expand(symbol_list[i])
	symbol_list=' '.join(symbol_list)
	if check_for_keys(symbol_list):
		parse(symbol_list)
	else:
		print(symbol_list)

parse('Q')


