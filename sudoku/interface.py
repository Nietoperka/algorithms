# Import Module
#from tkinter import *
import tkinter as tk

# create root window
root = tk.Tk()

# root window title and dimension
root.title("Sudoku")
# Set geometry(widthxheight)
root.geometry('350x350')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding  items in the menu bar 
# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File', menu=item)
# root.config(menu=menu)

# adding a label to the root window
#lbl = Label(root, text = "Are you a Geek?")
#lbl.grid()

# adding Entry Field
# a="0"
# s=[]
# for i in range(1,5):
# 	for j in range(1,5):
# 		x="s"+str(i)+str(j)
# 		s.append(x)
# 		x=Entry(root, width=3, textvariable=a)
# 		x.grid(column =j+1, row =i)
s11=tk.StringVar()
s12=tk.StringVar()
s13=tk.StringVar()
s14=tk.StringVar()
s21=tk.StringVar()
s22=tk.StringVar()
s23=tk.StringVar()
s24=tk.StringVar()
s11.set("0")
s12.set("0")
s13.set("0")
s14.set("0")
s21.set("0")
s22.set("0")
s23.set("0")
s24.set("0")

#print(s)


# function to display user text when
# button is clicked
def clicked():
	#PROGRAM
	#r1=Label(root,width=3)
	#r1.grid(column =2, row =1)
	#r1.configure(text = "A")
	n11=s11.get()
	n12=s12.get()
	n13=s13.get()
	n14=s14.get()
	n21=s21.get()
	n22=s22.get()
	n23=s23.get()
	n24=s24.get()

	data=[n11,n12,n13,n14,n21,n22,n23,n24]
	print(data)
	
	# for i in range(1,5):
	# 	for j in range(1,5):
	# 		print(s)

entry11 = tk.Entry(root,textvariable = s11,width=2, font=('calibre',20,'normal'),justify="center")
entry12 = tk.Entry(root,textvariable = s12,width=2, font=('calibre',20,'normal'),justify="center")
entry13 = tk.Entry(root,textvariable = s13,width=2, font=('calibre',20,'normal'),justify="center")
entry14 = tk.Entry(root,textvariable = s14,width=2, font=('calibre',20,'normal'),justify="center")
entry21 = tk.Entry(root,textvariable = s21,width=2, font=('calibre',20,'normal'),justify="center")
entry22 = tk.Entry(root,textvariable = s22,width=2, font=('calibre',20,'normal'),justify="center")
entry23 = tk.Entry(root,textvariable = s23,width=2, font=('calibre',20,'normal'),justify="center")
entry24 = tk.Entry(root,textvariable = s24,width=2, font=('calibre',20,'normal'),justify="center")

entry11.grid(row=1,column=1)
entry12.grid(row=1,column=2)
entry13.grid(row=1,column=3)
entry14.grid(row=1,column=4)
entry21.grid(row=2,column=1)
entry22.grid(row=2,column=2)
entry23.grid(row=2,column=3)
entry24.grid(row=2,column=4)

# button widget with red color text inside
btn = tk.Button(root, text = "SOLVE" ,activebackground="grey",
			fg = "black", command=clicked)
# Set Button Grid
btn.grid(column=10, row=10)

# Execute Tkinter
root.mainloop()
