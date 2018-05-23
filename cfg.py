import random

taglist = {
			'NN':['man', 'dog', 'box'],
			'VP':['sleeps', 'walks'],
			'DT':['the', 'a', 'some'],
			'JJ':['red', 'green', 'large'],
			'NP':['DT NN' ,'DT JJ NN'],
			'S':['NP VP NP']
			}

def expand(symbol):
	expanded = random.choice(taglist[symbol])
	return expanded

def parse(start):
	start = expand(start)
	construction = start.split(' ')
	expanded = []
	
	for i in range(0,len(construction)):
		print('expanded construction '+str(i)+': '+str(expanded))
		expanded = list(construction)
		
		word=construction[i]
		
		if word in taglist:
			expansion = expand(word)
			expanded[i] = str(expansion)
			print (word+' '+str(i)+' expanded to '+str(expansion))
		else:
			pass
		for i in range(0,len(expanded)):
			construction += expanded[i]+' '


parse('S')

