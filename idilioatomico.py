# -*- coding: utf-8 -*-

import random, json, re

def load_dict(file): # Read a json file into a python dictionary
	with open(file) as json_file:
		dict = json.load(json_file)
	return dict

def expand(symbol): # Randomly choose a possible expansion from the grammar
	expanded = random.choice(grammar[symbol])
	return expanded

def check_for_symbols(string):
	symbols_present = set(string.split(' ')).intersection(set(symbols))
	return symbols_present

def parse(start_symbol):
	global sentence
	global word_list

	word_list = start_symbol.split(' ')

	for i in range(0,len(word_list)):
		if word_list[i] in symbols:
			word_list[i]=expand(word_list[i])
	expanded_word_list=' '.join(word_list)
	if check_for_symbols(expanded_word_list):
		parse(expanded_word_list) # RECURSION!
	else:
		sentence = expanded_word_list

def clean(text):
	for pair in substitutions:
		text = re.sub(pair,substitutions[pair], text)
	text = text.capitalize()
	if text[-1:] != ('?' or '!'):
		text += '.'
	return text

def make(start_symbol,n_sentences):
	global sentence
	for _ in range(n_sentences):
		parse(start_symbol)
		sentence = clean(sentence)
		print(sentence.encode("utf-8"))

grammar = load_dict('grammar.json')
substitutions = load_dict('substitutions.json')
symbols = grammar.keys() # Check the string and return all the tags

make('F', 20)
