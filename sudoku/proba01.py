# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Sudoku")
# Set geometry(widthxheight)
root.geometry('350x350')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
#lbl = Label(root, text = "Are you a Geek?")
#lbl.grid()

# adding Entry Field
s=[]
for i in range(1,5):
	for j in range(1,5):
		x="s"+str(i)+str(j)
		s.append(x)
		x=Entry(root, width=3)
		x.grid(column =j+1, row =i)

print(s)


# function to display user text when
# button is clicked
def clicked():
	#PROGRAM
	r1=Label(root,width=3)
	r1.grid(column =2, row =1)
	r1.configure(text = "A")

# button widget with red color text inside
btn = Button(root, text = "Rozwiąż" ,activebackground="grey",
			fg = "black", command=clicked)
# Set Button Grid
btn.grid(column=10, row=10)

# Execute Tkinter
root.mainloop()
