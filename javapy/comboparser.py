import os
import re
from slippi import Game


class ACombo:
	#initialilzes for the player who hit the combo (player index in the combo text)
	def __init__(self, combotext, char_dict):
		#combo text
		self.text = [x.strip('\n') for x in combotext]
		#initial percent
		initpercent = self.text[6].split(':')[1]
		initpercent = initpercent.strip(',').strip()
		self.initpercent = float(initpercent)
		#final percent
		endpercent = self.text[6].split(':')[1]
		endpercent = endpercent.strip(',').strip()
		if 'null' in endpercent:
			self.endpercent = None
			#setting total combo damage to None
			self.combodamage
		else:
			self.endpercent = float(endpercent)
			#setting combo damage to difference
			self.combodamage = self.endpercent - self.initpercent
		


		#port
		self.port = int(self.text[3][-2:-1])
		#character the combo
		self.character = char_dict[self.port]
		#the opponent character
		keys = list(char_dict.keys())
		if keys[0] == self.port:
			opp_port = keys[1]
		else:
			opp_port = keys[0]
		self.vs = [char_dict[opp_port]]
		#first frame of the combo
		sframe = self.text[4].split(':')[1]
		sframe = sframe.strip()
		self.sframe = int(sframe.strip(','))
		#last frame of the combo, could be null
		eframe = self.text[5].split(':')[1]
		eframe = eframe.strip()
		if 'null' in eframe:
			self.eframe = None
		else:
			self.eframe = int(eframe.strip(','))
		#finding if it killed
		didkill = self.text[-4]
		if 'false' in didkill:
			self.didkill = False
		else:
			self.didkill = True
		moves_full = []
		i = 9
		move = self.text[i]
		while(']' not in move):
			moves_full.append(move)
			i = i+1
			move = self.text[i]
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
		moves_full = []
		for move in all_moves:
			moveid = int(re.search('moveId: (.+?),', move).group(1))
			moves_full.append(moveid)
		self.moves = moves_full



	def printtext():
		i = 0
		for line in combotext:
			print('line ' + str(i) + ': ' + line)





def metagetter(game):
	stage = game.start.stage
	chars = game.start.players
	chars = [x for x in chars if x != None]
	char1 = str(chars[0].character).split('.')[1]
	char2 = str(chars[1].character).split('.')[1]
	#trying to associate ports to character
	all_ports = game.frames[0].ports
	named_ports = []
	port_cor = []
	for port in all_ports:
		if port != None:
			named_ports.append(str(port.leader.post.character))
		else:
			named_ports.append('InGameCharacter.None')

	named_ports = [x.split('.')[1] for x in named_ports] 
	try:
		port_cor.append(named_ports.index(char1))
	except:
		port_cor.append(0)
	named_ports[port_cor[0]] = 5
	try:
		port_cor.append(named_ports.index(char2))
	except:
		port_cor.append(5)
	return [stage, char1, char2, port_cor]

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

	'''
	Make try except for the slp_game = Game(slpfile), if it doesnt work delete the with os and continue

	'''
	slp_game = Game(slpfile)
	metadata = metagetter(slp_game)
	#creating character dict where port is key to character name
	char_dict = {metadata[3][0]:metadata[1] , metadata[3][1]:metadata[2]}
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
			#combo = dictmaker(lines[started:i])

			#making the combo
			combo = ACombo(lines[started:i],char_dict)
			raw_combos.append(lines[started:i])
			started = False
			startframes.append(combo.sframe)
			#appending combos
			combos.append(combo)
		i = i + 1
	return combos, startframes, raw_combos



def main():
	slpfiles = os.listdir('Summit-11')
	slpfiles = [x for x in slpfiles if '.slp' in x]
	allcombos = []
	for slp in slpfiles:
		print(slp)
		combolist , startframelist, rawcombolist = ComboParser('Summit-11/' + slp)
		allcombos.extend(combolist) 
		#outfile.write(x)
	newcombolist = [x for x in allcombos if (len(x.moves) > 5)]
	print('number of combos with more than 5 hits: ' + str(len(newcombolist)))










if __name__ == '__main__':
	main()

