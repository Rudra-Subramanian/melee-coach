from slippi import Game
from time import sleep
from colorama import Fore, Back, Style
import os
import re
from random import randrange



def dictmaker(combotext):
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



def ComboParser(slpfile):
	os.system('node script.js '+ slpfile +' > out.txt')
	combos = []
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
			started = False
			startframes.append(combo['Sframe'])
			combos.append(combo)
		i = i + 1
	return combos, startframes






def PrintList(count, list1, list2, locations):
	for i in range(len(list1) - 1 ,-1,-1):
		place = str(locations[i])
		print(count[i] + ' '*(6-len(count[i])) + list1[i] + ' '*(33-len(list1[i])) + list2[i] + ' '*(30-len(list2[i])) + place)





def Display(combos, starts):
	for i in range(3):
		print('press play in: ' + str(3-i))
		sleep(i)


	combocounter = 0
	#colour using colorama for and back
	print("\t Player 1 \t\t\t Player 2\n\n")
	newgame = Game('test.slp')
	frames = newgame.frames
	p1_states = ['None']*51
	p2_states = ['None']*51
	p_locations = ['None']*51
	pyr = 3
	length = len(p1_states) -1
	frame_count = ['None']*51

	#finding correct ports
	aframe = frames[0]
	ports = [aframe.ports.index(x) for x in aframe.ports if x != None]




	for frame in frames:
		combocounter = max(0 , combocounter-1)
		frame_num = frame.index
		#this port thing may be a problem
		p1 = frame.ports[ports[0]].leader
		p2 = frame.ports[ports[1]].leader
		p1_state = str(p1.post.state)
		p1_state = p1_state.split('.')[1]
		p2_state = str(p2.post.state)
		p2_state = p2_state.split('.')[1]
		locations = [p1.post.position, p2.post.position]



		p_locations.pop(0)
		frame_count.pop(0)
		p1_states.pop(0)
		p2_states.pop(0)
		p1_states.append(str(p1_state))
		p2_states.append(str(p2_state))
		frame_count.append(str(frame.index))
		p_locations.append(str(locations))



		#-----------------printing stuff-----------------------#
		if frame_num in starts:
			num = starts.index(frame_num)
			combocounter = combos[num]['Eframe'] - combos[num]['Sframe']
			if combos[num]['Player'] == 0:
				p1_states[length] = Back.GREEN + p1_states[length] + Style.RESET_ALL
				p2_states[length] = Back.RED + p2_states[length] + Style.RESET_ALL
				pyr = 1
			else:
				p1_states[length] = Back.RED + p1_states[length] + Style.RESET_ALL
				p2_states[length] = Back.GREEN + p2_states[length] + Style.RESET_ALL
				pyr = 2
		elif combocounter != 0 and pyr == 1:
			p1_states[length] = Back.GREEN + p1_states[length] + Style.RESET_ALL
			p2_states[length] = Back.RED + p2_states[length] + Style.RESET_ALL
		elif combocounter != 0 and pyr == 2:
			p1_states[length] = Back.RED + p1_states[length] + Style.RESET_ALL
			p2_states[length] = Back.GREEN + p2_states[length] + Style.RESET_ALL		




		PrintList(frame_count, p1_states, p2_states, p_locations)
		sleep(1/60)
		for i in range(len(p1_states)):
			print("\033[F", end='')#cursor up one line
			print("\033[K", end='')#clear line on cursor



combos, starts = ComboParser('test.slp')
Display(combos, starts)
