import random

NN = ['man', 'dog', 'box']

DT = ['the', 'a', 'some']

JJ = ['red', 'green', 'large']

NP = ['DT NN' ,'DT JJ NN']

VP = ['sleeps', 'walks']

S = ['NP VP', 'NP VP NP', 'NN VP NN']

taglist = {'NN':NN, 'VP':VP, 'DT':DT, 'JJ':JJ, 'NP':NP, 'S':S}

def parse(start):
	construction = random.choice(start).split(' ')
	print(construction)
	repeat = True
	
	while repeat:
		for i in range(0,len(construction)):
			

			symbol = construction[i]
			flat=[]			
			if symbol in taglist:
				construction[i] = random.choice(taglist[symbol])
				for x in construction:
					for y in x.split(' '):
						flat.append(y)
				construction = flat
				
				
			else:
				repeat=False

	print(construction)


parse(S)
