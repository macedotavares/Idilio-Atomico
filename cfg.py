# -*- coding: utf-8 -*-

import random

substitutions = {
			' . ':'. ',
			' ?':'?',
			' : ':': '
			}

grammar = {
			'ARTD_MS':['o', 'aquele'],
			'ARTI_MS':['um', 'certo'],
			'ARTD_FS':['a', 'aquela'],
			'ARTI_FS':['uma', 'alguma', 'certa'],
			'N_MS':['homem', 'cão', 'palácio', 'papel', 'falcão', 'bispo'],
			'N_FS':['mulher', 'princesa', 'rainha', 'pedra'],
			'ADJ_MS':['feio', 'bonito', 'grande', 'pequeno'],
			'ADJ_FS':['serena', 'ávida', 'branca'],
			'VTRA':['come', 'mata', 'vê', 'ama', 'chama', 'ouve', 'larga'],
			'VINT':['dorme', 'acorda', 'corre', 'foge', 'chora'],
			'VPLU':['dormem', 'choram', 'planam', 'caem', 'murcham'],
			'VINF':['ver', 'tocar', 'ouvir'],
			'N_IND':['mágoas', 'nuvens', 'sinfonias'],
			'CO':['e', 'mas','só que', 'enquanto'],
			'LOC':['na floresta', 'em alto mar', 'no cimo da montanha'],
			'INTRO':['alguém diz', 'ouve-se ao longe', 'dizem', 'ouve'],
			'USO': ['VINF N_IND'],

			'FN':['ARTD_MS N_MS', 'ARTD_FS N_FS','ARTI_MS N_MS ADJ_MS', 'ARTI_FS N_FS ADJ_FS'],
			'FV':['VINT', 'VTRA FN', 'VINT LOC', 'VTRA FN LOC'],
			'QUEST':['será que AFIRM ?', 'AFIRM ?'],
			'AFIRM':['FN FV','FN encontra FN que serve para USO'],
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
	global sentence
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
		sentence = symbol_list

def clean(text):
	for pair in substitutions:
		text = text.replace(pair,substitutions[pair])
	text = text.capitalize()
	if text[-1:] != ('?' or '!'):
		text += '.'
	return text

def make(start_symbol,n_sentences):
	global sentence
	for _ in range(n_sentences):
		parse(start_symbol)
		sentence = clean(sentence)
		print(sentence)

make('F', 5)
