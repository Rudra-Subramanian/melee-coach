import os
import re
from slippi import Game


class ACombo:
	#initialilzes for the player who hit the combo (player index in the combo text)
	#STILL NEED TO ADD LOCATION DATA TO MOVES


	'''
	Variables
	self.text = combotext raw version
	self.initpercent = initial percent
	self.endperceent = end percent after final hit
	self.combodamage = total damage combo did
	self.stage = the stage
	self.port = the port of the character doing the combo
	self.character = the name of the character in the combo
	self.vs = opponents character
	self.sframe = first frame of combo
	self.eframe = last frame of combo
	self.didkill = did the combo kill?
	self.moves = the moves in the combo with the locatin of each move. Must call SetMoves
	'''

	def __init__(self, combotext, char_dict, stage):
		#combo text
		self.text = [x.strip('\n') for x in combotext]
		#initial percent
		initpercent = self.text[6].split(':')[1]
		initpercent = initpercent.strip(',').strip()
		self.initpercent = float(initpercent)
		#final percent
		endpercent = self.text[8].split(':')[1]
		endpercent = endpercent.strip(',').strip()
		if 'null' in endpercent:
			self.endpercent = None
			#setting total combo damage to None
			self.combodamage = None
		else:
			self.endpercent = float(endpercent)
			#setting combo damage to difference
			self.combodamage = self.endpercent - self.initpercent
		
		#stage
		self.stage = stage

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
		self.vs = char_dict[opp_port]
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
			frame = int(re.search('frame: (.+?),', move).group(1))
			moveid = int(re.search('moveId: (.+?),', move).group(1))
			#moves is a tuple unnasigned
			moves_full.append([moveid, frame])
		self.moves = moves_full



	def printtext(self):
		i = 0
		for line in combotext:
			print('line ' + str(i) + ': ' + line)

	#takes in a list of coordinates that should be the same length as moves
	#checks if same length
	#reassigns second value of each move list to the coord and makes it a tuple with tuple() to finalize it
	#returns False if didnt work, is a flag to remove combo from list
	def FinalizeMoves(self, coords):
		if len(coords) != len(self.moves):
			return False
		for i in range(len(coords)):
			self.moves[i] = (self.moves[i][0], coords[i])
		return True

	









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
Combo Parser
@param - the directory of a slippi file
@output - 
		list of combos
		list of the first frame of every combo
		the raw combos
'''

def ComboParser(slpfile):

	'''
	Make try except for the slp_game = Game(slpfile), if it doesnt work delete the with os and continue

	'''
	#TRY except for SLP files (just incase some files are too small and arent loaded correctly)
	#Tries to load file, except will delete file from directory and return none for everything
	try:
		slp_game = Game(slpfile)
	except:
		print(slpfile + ' Cannot be added\n\nSKIPPING: ' +slpfile)
		#os.system('rm -r '+slpfile)
		return None, None, None
	metadata = metagetter(slp_game)

	#loading the frames of the slp file to get location info into all_frames
	all_frames = slp_game.frames
	#creating character dict where port is key to character name
	char_dict = {metadata[3][0]:metadata[1] , metadata[3][1]:metadata[2]}
	stage = metadata[0]
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

			'''
				--------------------------------------------------------
				Add character locations to Acombo

				with combo make 

			'''




			combo = ACombo(lines[started:i],char_dict,stage)
			raw_combos.append(lines[started:i])
			started = False
			startframes.append(combo.sframe)

			#calculating the coordinates of the combo
			coord_list = []

			for each_move in combo.moves:
				theframe = all_frames[each_move[1]]
				comboer = theframe.ports[combo.port].leader
				move_coord = comboer.post.position
				coord_list.append(move_coord)
			#re add to list of combo
			combo.FinalizeMoves(coord_list)



			#appending combos
			combos.append(combo)
		i = i + 1
	return combos, startframes, raw_combos


'''
main function of comboparser (what to call if you want to run)
@input dire - the directory of files you want to check
@input character - character of comboer
@input vs_char - list of characters to combo against
@input stage - stage to combo on
@input hits - number of hits in combo
'''
def main_specific(dire, character, stage, hits, vs_char=['all']):
	slpfiles = os.listdir(dire)
	slpfiles = [x for x in slpfiles if '.slp' in x]
	slpfiles = slpfiles[4:100]
	allcombos = []
	for slp in slpfiles:
		print(slp)
		combolist , startframelist, rawcombolist = ComboParser(dire + "/" + slp)
		if combolist != None:
			allcombos.extend(combolist) 
		#outfile.write(x)
	newcombolist = allcombos
	if hits != None:
		newcombolist = [x for x in newcombolist if (len(x.moves) >= hits)]
	newcombolist= [x for x in newcombolist if (str(x.character) == character)]
	if (vs_char != 'all'):
		newcombolist = [x for x in newcombolist if (str(x.vs) in vs_char)]
	try:
		newcombolist = [x for x in newcombolist if (str(x.stage) == stage)]
	except:
		print('NO STAGE SPECIFIED, THIS WONT WORK WITH THE UI')
	#print('number of combos with more than '+str(hits)+' hits: ' + str(len(newcombolist)))
	return allcombos, newcombolist

def main():
	slpfiles = os.listdir('Summit-11')
	slpfiles = [x for x in slpfiles if '.slp' in x]
	slpfiles = slpfiles[4:100]
	allcombos = []
	for slp in slpfiles:
		print(slp)
		combolist , startframelist, rawcombolist = ComboParser('Summit-11/' + slp)
		if combolist != None:
			allcombos.extend(combolist) 
		#outfile.write(x)
	newcombolist = allcombos
	print('MAIN VERSION, NOTHING SPECIFIED, THIS WONT WORK WITH THE UI')
	#print('number of combos with more than '+str(hits)+' hits: ' + str(len(newcombolist)))
	return allcombos, newcombolist








if __name__ == '__main__':
	directory = 'Summit-11'
	main()

