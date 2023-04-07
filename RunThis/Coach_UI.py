from tkinter import *
import comboparser as cp



def confirmOptions(picked_stage,picked_char,vs_list_box,input_text):
	print("the stage picked is: " + str(picked_stage.get()))
	print("the character picked is: "+ str(picked_char.get()))
	all_chars = [vs_list_box.get(i) for i in vs_list_box.curselection()]
	for char in all_chars:
		print("a vs character is: " + str(char))
	print("the directory chosen is: " + str(input_text.get(1.0, "end-1c")))
	battlefieldDisplay(str(picked_char.get()), all_chars,str(input_text.get(1.0, "end-1c")),0)
	return None
# options for stages





def battlefieldDisplay(char, vs_char_list, directory, min_hits = 0):
	
	stage=Tk()
	popups = Toplevel(stage)
	#location_checker = Toplevel(stage)

	# Set the size of the tkinter window
	stage.geometry("448x308")

	# Create a canvas widget
	canvas=Canvas(stage, width=448, height=308.8)
	canvas.pack()
	#dimensions of battlefield CHANGE WHEN IMPLEMLENTING OTHER STAGES
	z = [224, 200,-224,-108.8]
	# creating stage
	canvas.create_line((-68.4000+z[0]), (0.0000+z[1]),(68.4+z[0]),(0+z[1]), fill="green", width=10)
	#top platfrom
	canvas.create_line(-18.8+z[0], -54.40+z[1], 18.8+z[0], -54.40+z[1], fill = 'green', width = 5)
	#left side plat
	canvas.create_line(-57.60+z[0], -27.20+z[1], -20+z[0], - 27.20+z[1], fill = 'green', width = 5)
	#ride side plat
	canvas.create_line(20+z[0], -27.20+z[1], 57.6+z[0], - 27.20+z[1], fill = 'green', width = 5)

	w1 = Scale(popups, from_=0, to=100, tickinterval=10, length = 200)
	w1.set(0)
	w1.pack()
	allcombos, newcombolist = cp.main_specific(directory,char, stage, min_hits, vs_char_list)
	for combos in newcombolist:
		if combos.moves != []:
			print("combo location: " + str(combos.moves[0][1]))
			coords = DrawCombo(combos, 0)
			canvas.create_oval(coords[0], coords[1],coords[2],coords[3], width = 2, fill = 'red')

	print("-----DONE SHOWING COMBOS---------")
	
	stage.mainloop()
	




	return None
#stage_dims is a list [x_max, y_max, x_min, y_min]
def DrawCombo(combo, moveindex):
	radius = 5
	z = [224, 200,-224,-108.8]
	x = combo.moves[moveindex][1].x
	y = combo.moves[moveindex][1].y
	x0 = x+combo.stage_dims[0] - radius
	y0 = y+combo.stage_dims[1] - radius
	x1 = x+combo.stage_dims[0] + radius
	y1 = y+combo.stage_dims[1] + radius
	return int(x0),int(y0),int(x1),int(y1)
	




def mainUI():
	options_list = ["Battlefield", "Stadium", "Dreamland", "Yoshis", "FD", "Fountain"]
	#options for characters
	character_list = ['Roy', 'Marth', 'Mr. Game & Watch', 'Mewtwo', 'Pichu' ,
	'Young Link','Falco','Ganondorf','Luigi','Dr. Mario','Jigglypuff',
	'Pikachu','Link','Zelda','Samus','Kirby','Ice Climbers','Ness',
	'Fox', 'Captain Falcon','Donkey Kong','Yoshi','Peach','Bowser','Mario']

	custom_characters = ['floaties', 'spacies']

	rootsc = Tk()
	rootsc.title=('Pick Your Combos')
	rootsc.geometry("800x800")

	#making stage variable
	picked_stage = StringVar(rootsc)
	picked_stage.set("Pick a Stage")
	#making character variable
	picked_char = StringVar(rootsc)
	picked_char.set("Pick a character")
	#making vs character variable
	selected_text_list = []
	#making stage menu
	stage_menu = OptionMenu(rootsc, picked_stage, *options_list)
	stage_menu.pack(side=BOTTOM)
	#making character pick menu
	my_char_menu = OptionMenu(rootsc, picked_char, *character_list)
	my_char_menu.pack(side=BOTTOM)
	#making vs list box
	vs_list_box = Listbox(rootsc,selectmode='multiple')
	for i in range(len(character_list)):
		vs_list_box.insert(i, character_list[i])
	vs_list_box.pack()
	#making the confirm button
	input_text = Text(rootsc, height = 2, width = 10)
	input_text.pack(side=BOTTOM)

	confirm = Button(rootsc, text="Confirm", bg="white",command=lambda: confirmOptions(picked_stage,picked_char,vs_list_box,input_text))
	confirm.pack(side=BOTTOM)


	rootsc.mainloop()




if __name__ == '__main__':
	mainUI()