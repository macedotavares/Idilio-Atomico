import random

taglist = {
			'NN':['man', 'dog', 'box'],
			'VP':['sleeps', 'walks'],
			'DT':['the', 'a', 'some', 'that'],
			'JJ':['red', 'green', 'large'],
			'NP':['DT NN' ,'DT JJ NN'],
			'S':['NP VP NP']
			}


def expand(symbol):
	expanded = random.choice(taglist[symbol])
	return expanded

def check_for_keys(string):
	keys_list = taglist.keys()
	intersect = set(string.split(' ')).intersection(set(keys_list))
	return intersect

def parse(start_symbols):
	symbol_list=start_symbols.split(' ')
	for i in range(0,len(symbol_list)):
		if symbol_list[i] in taglist:
			symbol_list[i]=expand(symbol_list[i])
	symbol_list=' '.join(symbol_list)
	if check_for_keys(symbol_list):
		parse(symbol_list)
	print(symbol_list)

parse('S')

