from tkinter import *
import comboparser as cp


def create_circle(x, y, r, canvas):
	x_max = 198.75
	y_max = 202.5
	x_min = -198.75
	y_min = -84.75
	x0 = x+x_max - r
	y0 = -y+y_max - r
	x1 = x+x_max + r
	y1 = -y+y_max + r
	return canvas.create_oval(x0, y0, x1, y1, width = 2)


def load_all(percent, allcombos,canvas,circles):
	if circles != []:
		for circle in circles:
			canvas.delete(circle)
	x_max = 198.75
	y_max = 202.5
	x_min = -198.75
	y_min = -84.75
	newcombolist = [x for x in allcombos if (x.combodamage != None)]
	newcombolist = [x for x in newcombolist if ((x.combodamage> percent -2) and (x.combodamage < percent + 2)) ]
	all_circles = []
	for combo in newcombolist:
		combox = combo.moves[0][1].x
		comboy = combo.moves[0][1].y
		combox = combox + x_max
		comboy = -comboy + y_max
		newcircle = create_circle(combox,comboy,len(combo.moves), canvas)
		all_circles.append(newcircle)
	return all_circles




def main():
	directory = 'Summit-11'
	#character = 'FOX'
	stage = 'Stage.FOUNTAIN_OF_DREAMS'
	#allcombos, newcombolist = cp.main_specific(directory,character, stage, None)
	allcombos = []
	newcombolist = []


	# Create an instance of tkinter frame or window
	x_max = 198.75
	y_max = 202.5
	x_min = -198.75
	y_min = -84.75
	stage=Tk()
	popups = Toplevel(stage)
	width = int(x_max-x_min)
	height = int(y_max-y_min)
	# Set the size of the tkinter window
	stage.geometry(str(width) + "x"+str(height) )

	# Create a canvas widget
	canvas=Canvas(stage, width=x_max-x_min, height=y_max-y_min)
	canvas.pack()

	a= (-8.6809 + x_max, -1*-71.8312 + y_max)
	b= (-18.9105+ x_max, -1*-48.6670 +y_max)
	c= (-41.1778+ x_max, -1*-41.9127+ y_max)
	d= (-56.8736+ x_max, -1*-19.5537+ y_max)
	e= (-63.2570+ x_max, -1*-4.3985+ y_max)
	f= (-63.3500+ x_max, -1*0.6214+ y_max)
	g= (-53.5835+ x_max, -1*0.6214+ y_max)
	h= (-51.2608+ x_max, -1*0.0000+ y_max)
	i= (51.2608+ x_max, -1*0.0000+ y_max)
	j= (53.5835+ x_max, -1*0.6214+ y_max)
	k= (63.3500+ x_max, -1*0.6214+ y_max)
	l= (63.2570+ x_max, -1*-4.3985+ y_max)
	m= (56.8736+ x_max, -1*-19.5537+ y_max)
	n= (41.1778+ x_max, -1*-41.9127+ y_max)
	o= (18.9105+ x_max, -1*-48.6670+ y_max)
	p= (8.6809+ x_max, -1*-71.8312+ y_max)







	# creating stage
	canvas.create_line(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p, fill="green", width=8)
	#top platfrom
	canvas.create_line(-14.25+x_max, -42.75+y_max, 14.25+x_max, -42.75+y_max, fill = 'green', width = 5      )
	#left side plat
	#canvas.create_line(-57.60+x_max, -27.20+y_max, -20+x_max, - 27.20+y_max, fill = 'green', width = 5      )
	#ride side plat
	#canvas.create_line(20+x_max, -27.20+y_max, 57.6+x_max, - 27.20+y_max, fill = 'green', width = 5      )

	'''
	widget to help calculate locations

	'''





	#make scale to choose percent
	circles = []
	w1 = Scale(popups, from_=0, to=100, tickinterval=10, length = 200)
	but1 = Button(popups,text="Show Combos",command= lambda: circles==load_all(w1.get(), allcombos,canvas,circles))
	but1.grid()
	w1.grid()
	stage.mainloop()

if __name__ == "__main__":

	main()