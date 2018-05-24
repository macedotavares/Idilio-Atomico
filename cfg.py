import random

grammar = {
			'NN':['man', 'dog', 'park', 'box', 'car', 'pigeon'],
			'NNS':['telescopes', 'houses', 'roads'],
			'NNP':['Bill', 'Wendy'],
			'VI':['sleeps', 'walks'],
			'VT':['kills', 'touches'],
			'VD':['gave'],
			'DT':['the', 'a', 'some', 'that', 'every'],
			'IN':['in', 'under', 'of', 'on', 'with'],
			'JJ':['red', 'green', 'large', 'idealistic', 'fast', 'serious', 'clay', 'metal'],
			'COMP':['that'],
			'CC': ['and', 'or', 'but'],

			'NBAR':['NN', 'NN NBAR', 'JJ NBAR', 'NBAR NBAR', 'NBAR PP', 'NBAR CC NBAR'],
			'PP':['IN NP'],
			'NP':['DT NBAR', 'NP CC NP'],
			'VP':['VI', 'VT NP', 'VD NP NP', 'VD PP', 'NP NP SBAR'],
			'NP':['DT NN' ,'DT JJ NN'],
			'A':['NP VT NP'],
			'Q':['what if A ?'],
			'S':['NP VP', 'S CC S'],
			'SBAR':['COMP S','SBAR CC SBAR']
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
	print(symbol_list)
	for i in range(0,len(symbol_list)):
		if symbol_list[i] in taglist:
			symbol_list[i]=expand(symbol_list[i])
	symbol_list=' '.join(symbol_list)
	if check_for_keys(symbol_list):
		parse(symbol_list)
	else:
		print(symbol_list)

parse('S')


