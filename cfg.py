# -*- coding: utf-8 -*-

import random, json, re

with open('grammar.json') as json_file:
    grammar = json.load(json_file)
	
with open('substitutions.json') as json_file:
    substitutions = json.load(json_file)

taglist = grammar.keys()

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

make('F', 10)
