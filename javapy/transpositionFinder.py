from slippi import Game
import os
import re
import comboparser




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



'''
@param p1 - a tuple where the first value is the port of char 1 in framea and the second value is that on frame b 
@param p2 - a tuple where the first value is the port of char 2 in framea and the second value is that on frame b 


'''
def framechecker(ranges, framea, frameb, p1, p2):
	#print(p1, p2)
	#getting all information from framea to check will add more when want more
	p1_pos = framea.ports[p1[0]].leader.post.position
	p2_pos = framea.ports[p2[0]].leader.post.position
	p1_air = framea.ports[p1[0]].leader.post.airborne
	p2_air = framea.ports[p2[0]].leader.post.airborne
	p1_jumps = framea.ports[p1[0]].leader.post.jumps
	p2_jumps = framea.ports[p2[0]].leader.post.jumps
	p1_state = framea.ports[p1[0]].leader.post.state
	p2_state = framea.ports[p2[0]].leader.post.state





	#getting same info from frameb
	check_pos_1 = frameb.ports[p1[1]].leader.post.position
	check_air_1 = frameb.ports[p1[1]].leader.post.airborne == p1_air
	check_jumps_1 = frameb.ports[p1[1]].leader.post.jumps == p1_jumps
	check_state_1 = frameb.ports[p1[1]].leader.post.state == p1_state
	check_pos_2 = frameb.ports[p2[1]].leader.post.position 
	check_air_2 = frameb.ports[p2[1]].leader.post.airborne == p2_air
	check_jumps_2 = frameb.ports[p2[1]].leader.post.jumps == p2_jumps
	check_state_2 = frameb.ports[p2[1]].leader.post.state == p2_state


	check_state_2 = True
	check_state_1 = True
	#preforming checks
	pos1_check_x = (p1_pos.x - ranges < check_pos_1.x) and (check_pos_1.x < p1_pos.x+ranges)
	pos1_check_y = (p1_pos.y -ranges < check_pos_1.y) and (check_pos_1.y < p1_pos.y+ranges)

	pos2_check_x = (p2_pos.x -ranges < check_pos_2.x) and (check_pos_2.x < p2_pos.x+ranges)
	pos2_check_y = (p2_pos.y -ranges < check_pos_2.y) and (check_pos_2.y < p2_pos.y+ranges)

	all_check = (pos1_check_x and pos1_check_y and pos2_check_x and 
				 pos2_check_y and check_air_1 and check_air_2 and check_jumps_1 
				 and check_jumps_2 and check_state_1 and check_state_2)

	#print('\nall_check: ' + str(all_check) + '\ncheck_jumps: ' + str(check_jumps_1) + str(check_jumps_2))
	
	return (all_check)

def MetaCheckerMover(initial_game, folder):
	dest_folder = '../matching_slps/'
	os.chdir(folder)
	all_slps = os.listdir()
	for slp in all_slps:
		try:
			game2 = Game(slp)
		except:
			continue

		stages = False
		characters = False
		game1stats = metagetter(initial_game)
		game2stats = metagetter(game2)
		if game1stats[0] == game2stats[0]:
			stages = True
		if game1stats[1] in game2stats:
			index = game2stats.index(game1stats[1])
			game2stats[index] = 'FOUND'
			if game1stats[2] in game2stats:
				characters = True
		if characters and stages:
			os.system('cp '+slp+ ' ' + dest_folder + slp)
			print(slp)
	os.chdir('..')



def SimilarStater(init_game, frame_num, ranges, searchfolder):
	init_stats = metagetter(init_game)
	search_frame = init_game.frames[frame_num]
	found_frames=[]

	os.chdir(searchfolder)
	slpfiles = os.listdir()
	for slp in slpfiles:
		#print(slp)
		currgame = Game(slp)
		currstats = metagetter(currgame)
		#corresponding which ports to similar characters
		if(init_stats[1] == currstats[1]):
			p1 = (init_stats[3][0], currstats[3][0])
			p2 = (init_stats[3][1], currstats[3][1])
		else:
			p1 = (init_stats[3][0], currstats[3][1])
			p2 = (init_stats[3][1], currstats[3][0])
		for frame in currgame.frames:

			same = framechecker(ranges, search_frame, frame, p1, p2)
			if(same):
				found_frames.append([frame,int(frame.index)//60,slp])
	return found_frames


if __name__ == "__main__":
	init_game = Game('Game_20221112T224039.slp')
	#all_frames = SimilarStater('Game_20210716T015410.slp', 382, 5, 'Summit-11')
	'''
	Run this if you want to find all the matching files first
	
	
	os.system('rm -r matching_slps')
	os.system('mkdir matching_slps')
	
	MetaCheckerMover(init_game, 'Summit-11')
	'''
	'''
	Run this to get matching frames
	'''
	all_frames = SimilarStater(init_game, 2868, 1, 'matching_slps')
	print('Printing All Frames:')
	for each_frame in all_frames:
		print(str(each_frame[1]) + ' ' + str(each_frame[2]))






	

