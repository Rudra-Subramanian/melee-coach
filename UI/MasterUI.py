from tkinter import *
import FOD_tkinter
import BF_tkinter



rootsc = Tk()
rootsc.geometry("448x308")
stage_decision = IntVar(rootsc)

def demoColorChange(abutton):
	global fd
	global fod
	global ys
	global stadium
	global bf
	global dl
	fd.configure(bg="gray")
	fod.configure(bg="gray")
	dl.configure(bg="gray")
	ys.configure(bg="gray")
	stadium.configure(bg="gray")
	bf.configure(bg="gray")
	abutton.configure(bg="blue")

bf = Button(rootsc, text="Battlefield", bg="white")
bf.configure(command=lambda: demoColorChange(bf))
bf.pack()
fd = Button(rootsc, text="Final Destination", bg="white")
fd.configure(command=lambda: demoColorChange(fd))
fd.pack()
dl = Button(rootsc, text="Dreamland", bg="white")
dl.configure(command=lambda: demoColorChange(dl))
dl.pack()
ys = Button(rootsc, text="Yoshi's Story",bg="white")
ys.configure(command=lambda: demoColorChange(ys))
ys.pack()
fod = Button(rootsc, text="Fountain Of Dreams", bg = 'white')
fod.configure(command=lambda: demoColorChange(fod))
fod.pack()
stadium = Button(rootsc, text="Stadium", bg = 'white')
stadium.configure(command=lambda: demoColorChange(stadium) )
stadium.pack()






rootsc.mainloop()