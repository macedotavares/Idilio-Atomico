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
	construction = expand(start)
	print ('contruction: '+construction)
	expanded = ''
	
	for i in range(0,5):
		print('expanded construction '+str(i)+': '+expanded)
		split_const=construction.split(' ')
		for i in range(0,len(split_const)):
			word=split_const[i]
			if word in taglist:
				expansion=(expand(word)+' ')
				expanded+=expansion
				print (word+' '+str(i)+' expanded to '+expansion)
			else:
				pass
			construction=expanded

parse('S')

