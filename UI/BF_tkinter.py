from tkinter import *


def create_random_moves():
	random_move_list = [[(13, (11.02, 58.07)), (52, (-1.54, 51.43)), (55, (-21.34, 51.20))],
	[(16, (-69.98, 0.01)), (52, (-65.41, 54.90)), (56, (17.84, 51.43))],
	[(3, (-28.33, 0.01))],
	[(14, (4.44, 51.43))],
	[(2, (147.32, -4.78))],
	[(14, (63.73, 0.01))],
	[(13, (79.19, 18.46)), (13, (80.71, -5.20))],
	[(12, (51.49, 0.01))],
	[(14, (37.88, 0.01))],
	[(13, (8.00, 8.48))],
	[(13, (-49.86, 0.01))],
	[(8, (-6.84, 30.47)), (14, (-40.74, 6.83))]
	,[(52, (-36.70, 0.01)), (56, (-5.54, 27.38)), (52, (24.30, 0.01)), (56, (0.47, 0.01)), (52, (-46.56, 0.01)), (55, (-46.56, 0.01)), (55, (-46.36, 0.01)), (52, (-19.80, 0.01)), (52, (-16.03, 18.86)), (56, (-11.71, 0.01)), (52, (16.97, 0.01)), (56, (16.97, 0.01)), (52, (41.31, 0.01)), (55, (21.69, 0.01)), (55, (-5.45, 0.01))], [(21, (4.91, 9.67)), (13, (17.41, 0.01))], [(55, (-56.17, 0.01)), (8, (-44.33, 0.01)), (15, (-34.95, 0.01))], [(16, (-19.20, 0.01)), (13, (41.94, 0.01)), (16, (98.52, 22.99))], [(21, (30.27, 0.01))], [(13, (63.05, 14.57)), (55, (19.40, 0.01)), (13, (2.66, 18.88)), (15, (-5.19, 0.01))], [(17, (-146.64, -15.76)), (21, (-108.41, -33.11))], [(2, (-63.55, 0.01)), (11, (-69.37, 10.58))], [(15, (3.27, 51.43))], [(13, (-4.29, 0.82)), (21, (-16.97, 14.23))], [(15, (-2.37, 0.01)), (21, (48.17, 0.01)), (11, (63.51, 7.56))], [(15, (44.49, 0.01))], [(13, (-10.11, 0.01))], [(16, (54.24, 30.24))], [(8, (17.93, 6.08)), (15, (24.55, 29.71))], [(16, (-16.51, 35.55)), (53, (53.12, 0.01))], [(13, (51.14, 0.01))], [(2, (62.16, 10.36)), (3, (54.77, 30.24)), (4, (40.73, 30.24)), (55, (58.67, 0.01))], [(13, (1.89, 0.01))], [(55, (-85.52, -14.92)), (52, (16.09, 0.01)), (56, (16.09, 0.01)), (56, (16.09, 0.01))], [(13, (77.27, 0.01)), (56, (77.28, 1.35)), (55, (41.30, 0.01)), (55, (8.17, 10.21)), (15, (26.01, 6.18)), (14, (11.28, 0.01)), (16, (36.11, 0.01))]]
	return random_move_list







def draw_canvas(x, y, r, canvas):
	x_max = 224
	y_max = 200
	x_min = 224
	y_min = 108.8
	x0 = x+x_max - r
	y0 = -y+y_max - r
	x1 = x+x_max + r
	y1 = -y+y_max + r
	return canvas.create_oval(x0, y0, x1, y1, width = 2)


def main():


	# Create an instance of tkinter frame or window
	x_max = 224
	y_max = 200
	x_min = 224
	y_min = 108.8
	stage=Tk()
	popups = Toplevel(stage)
	#location_checker = Toplevel(stage)

	# Set the size of the tkinter window
	stage.geometry("448x308")

	# Create a canvas widget
	canvas=Canvas(stage, width=448, height=308.8)
	canvas.pack()


	# creating stage
	canvas.create_line((-68.4000+x_max), (0.0000+y_max),(68.4+x_max),(0+y_max), fill="green", width=10)
	#top platfrom
	canvas.create_line(-18.8+x_max, -54.40+y_max, 18.8+x_max, -54.40+y_max, fill = 'green', width = 5      )
	#left side plat
	canvas.create_line(-57.60+x_max, -27.20+y_max, -20+x_max, - 27.20+y_max, fill = 'green', width = 5      )
	#ride side plat
	canvas.create_line(20+x_max, -27.20+y_max, 57.6+x_max, - 27.20+y_max, fill = 'green', width = 5      )

	w1 = Scale(popups, from_=0, to=100, tickinterval=10, length = 200)
	w1.set(0)


	'''
	x1 = Scale(location_checker, from_=-224, to=224, tickinterval=10, length=600, orient=HORIZONTAL)
	x1.set(0)
	y1 = Scale(location_checker, from_=- 108.8, to=200, tickinterval=10, length=600)
	y1.set(0)
	#command= lambda: draw_canvas(x1.get(), y1.get(), 2,canvas)
	
	check_button = Button(location_checker, text='Make circle', command= lambda: draw_canvas(x1.get(), y1.get(), 2,canvas))
	#for some reason its packing on top too small, make next to each other
	check_button.pack()
	x1.pack()
	y1.pack()
	
	'''
	all_moves = create_random_moves()
	for moves in all_moves:
		draw_canvas(int(moves[0][1][0]), int(moves[0][1][1]), 2, canvas)

	w1.pack()
	stage.mainloop()

if __name__ == '__main__':
	main()