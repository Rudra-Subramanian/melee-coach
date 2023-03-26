import os
import re

class ACombo:
	def __init__(self, combotext):
		'''
		self.player = 
		self.character = 
		self.sframe = 
		self.eframe = 
		self.didkill = 
		self.damage = 
		self.moves = 
		self.sloc = 
		self.eloc = 
		self.first_move = 
		self.las_move = 
		'''
		self.text = [x.strip('\n') for x in combotext]

	def printtext():
		i = 0
		for line in combotext:
			print('line ' + str(i) + ': ' + line)






def dictmaker(combotext):
	#print('________COMBO________')
	#print(combotext)
	combodict = {}
	combotext = [x.strip('\n') for x in combotext]
	player = int(combotext[3][-2:-1])
	sframe = combotext[4].split(':')[1]
	sframe = sframe.strip()
	sframe = int(sframe.strip(','))
	eframe = combotext[5].split(':')[1]
	eframe = eframe.strip()
	eframe = int(eframe.strip(','))
	didkill = combotext[-4]
	if 'false' in didkill:
		didkill = False
	else:
		didkill = True
	#getting moves
	moves_full = []
	i = 9
	move = combotext[i]
	while(']' not in move):
		moves_full.append(move)
		i = i+1
		move = combotext[i]
	all_moves = []
	full = ''
	start = False
	for tag in moves_full:
		if '{' in tag:
			temp = tag
			full = full + temp.strip() + ' '
			start = True
		if '}' in tag:
			if temp != tag:
				full = full + tag
			start = False
			all_moves.append(full)
			full = ''
		elif start == True:
			temp = tag
			full = full + temp.strip() + ' ' 
	#MAKING DICTIONARY FROM MOVES
	moves_full = []
	for move in all_moves:
		frame = int(re.search('frame: (.+?),', move).group(1))
		moveid = int(re.search('moveId: (.+?),', move).group(1))
		moves_full.append({'Frame': frame, 'ID': moveid})
	combodict['Player'] = player
	combodict['Sframe'] = sframe
	combodict['Eframe'] = eframe
	combodict['Kill'] = didkill
	combodict['Moves'] = moves_full
	return combodict

'''
Need to make ComboParser be able to get player ids and character ids for certain combos 
(array where 0th value is name of character of player 0 and 1st value is name of player 1 character) (or whichever the ports are assign character to port)
'''

def ComboParser(slpfile):
	os.system('node script.js '+ slpfile +' > out.txt')
	combos = []
	raw_combos = []
	#parsing txt file
	started = False
	f = open('out.txt', 'r')
	lines = f.readlines()
		#look for combo start
	startframes = []
	for i in range(len(lines)):
		if started == False and "@COMBO START@" in lines[i]:
			started = i
			while '@COMBO END@' not in lines[i]:
				i = i + 1
			combo = dictmaker(lines[started:i])
			raw_combos.append(lines[started:i])
			started = False
			startframes.append(combo['Sframe'])
			combos.append(combo)
		i = i + 1
	return combos, startframes, raw_combos



def main():
	combolist , startframelist, rawcombolist = ComboParser('test.slp')
	outfile = open('out.txt', 'w')
	for line in rawcombolist:
		
		x = ''
		for word in line:
			x = x + str(word)
		outfile.write(x)










if __name__ == '__main__':
	main()

