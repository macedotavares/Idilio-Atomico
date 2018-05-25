import random

grammar = {
			'ART_MS':['o', 'aquele', 'um', 'algum', 'certo'],
			'ART_FS':['a', 'aquela', 'uma', 'alguma'],
			'N_MS':['homem', 'cão', 'palácio', 'papel', 'falcão', 'bispo'],
			'N_FS':['mulher', 'princesa', 'rainha', 'pedra'],
			'ADJ_MS':['feio', 'bonito', 'grande', 'pequeno'],
			'ADJ_FS':['serena', 'ávida', 'branca'],
			'VT':['come', 'mata', 'vê', 'ama', 'chama'],
			'VI':['dorme', 'acorda', 'corre', 'foge'],
			'CO':['e', 'mas','só que', 'enquanto'],
			'LOC':['na floresta', 'em alto mar', 'no cimo da montanha'],
			'INTRO':['alguém diz', 'ouve-se ao longe', 'dizem', 'ouve'],

			'FN':['ART_MS N_MS', 'ART_FS N_FS','ART_MS N_MS ADJ_MS', 'ART_FS N_FS ADJ_FS'],
			'FV':['VI', 'VT FN', 'VI LOC', 'VT FN LOC'],
			'QUEST':['será que AFIRM ?', 'AFIRM ?'],
			'AFIRM':['FN FV'],
			'F':['INTRO : AFIRM', 'AFIRM', 'QUEST']
			
			}

taglist = grammar.keys()
show_expansions = False

def expand(symbol):
	expanded = random.choice(grammar[symbol])
	return expanded

def check_for_keys(string):
	intersect = set(string.split(' ')).intersection(set(taglist))
	return intersect

def parse(start_symbol):
	global symbol_list
	symbol_list=start_symbol.split(' ')
	if show_expansions==True:
		print(symbol_list) 
	for i in range(0,len(symbol_list)):
		if symbol_list[i] in taglist:
			symbol_list[i]=expand(symbol_list[i])
	symbol_list=' '.join(symbol_list)
	if check_for_keys(symbol_list):
		parse(symbol_list)
	else:
		print(symbol_list)

def make(start_symbol,n_sentences):
	for _ in range(n_sentences):
		parse(start_symbol)

make('F', 5)
