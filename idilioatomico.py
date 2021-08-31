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
	symbols_present = set(string.split(' ')).intersection(set(symbols)) # Check if there are any symbols left in the expanded string
	return symbols_present

def parse(start_symbol):
	global sentence
	global word_list

	word_list = start_symbol.split(' ') # Create a list with words and symbols from the input string

	for i in range(0,len(word_list)): # For each item in the word list,
		if word_list[i] in symbols: # check if it's a symbol
			word_list[i]=expand(word_list[i]) # and if so, expand it inside the word list
	expanded_word_list=' '.join(word_list)
	if check_for_symbols(expanded_word_list): # Check if there are still any symbols left to expand
		parse(expanded_word_list) # If true, RECURSION! \o/
	else:
		sentence = expanded_word_list # Return the completed expansion

def clean(text): # I'm not proud of this
	for pair in substitutions:
		text = re.sub(pair,substitutions[pair], text) # But regex is so cool.
	text = text.capitalize()
	if text[-1:] != ('?' or '!'):
		text += '.'
	return text

def make(start_symbol,n_sentences): # Make n sentences starting with a given symbol.
	global sentence
	for _ in range(n_sentences):
		parse(start_symbol) # Parse one at a time
		sentence = clean(sentence) # clean it
		print(sentence.encode("utf-8")) # and finally print it.

grammar = load_dict('grammar.json') # Load a grammar file
substitutions = load_dict('substitutions.json') # Load a substitutions file
symbols = grammar.keys() # Build a list of all the symbols in the grammar

make('F', 20)
