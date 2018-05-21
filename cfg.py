import random

NN = ['man', 'dog', 'box']

DT = ['the', 'a', 'some']

JJ = ['red', 'green', 'large']

NP = ['DT NN' ,'DT JJ NN']

VP = ['sleeps', 'walks']

S = ['NP VP']

taglist = {'NN':NN, 'VP':VP, 'DT':DT, 'JJ':JJ, 'NP':NP, 'S':S}

def parse(start):
	construction = random.choice(start)
	
	for symbol in construction.split(' '):
		if symbol in taglist:
			parse(taglist[symbol])

	print construction		


parse(S)
