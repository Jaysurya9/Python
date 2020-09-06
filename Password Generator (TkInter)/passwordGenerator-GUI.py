'''
Author: Jaysurya9
'''
# Python program to generate random 
# password using Tkinter module
import random
from tkinter import *
from tkinter.ttk import *
import time
import datetime

def qwe(len,ch):
	def copy():
		import pyperclip
		c=""
		s=(lis.get(0,END))
		for i in s:
			c=c+i+"\n"
		pyperclip.copy(c)
		
		
	# Function to reset the window 
	def Reset():
		lis.delete(0,END)
		E1.delete(0,END)
		entry5.delete(0,END)
		entry5.insert(0,"Enter the count")

	def msg(s):  
		entry5.insert(END, s)
		
	def reqpw_except(cc):
	    reqPWs=cc
	    try:
		    aa=int(reqPWs)
		    if(aa==0):
			    si="Enter count greater than 0"
			    return msg(si)
		    elif aa<0:
			    si="Error:Negative value!"
			    return msg(si)
		    else:return aa
	    except ValueError:
		    si="Error:Invalid Input count"
		    return msg(si)
	def qExit(): 
		root1.destroy()
	
	def multiple(len,ch):
		entry5.delete(0,END)
		count=E1.get()
		count4=reqpw_except(count)
		password=""
		for i in range(0, count4):
			for j in range(len):
				password+=random.choice(ch)
			password+="\n"
		entry5.insert(0,"Copy your passwords")
		lis.delete(0,END)
		for index,i in enumerate(password.split("\n")):
			lis.insert(index,i)
		
	#GUI for multiple password generator
	root1=Tk()
	root1.title("Multiple Password generator")
	
	fm1 = Frame(root1, width = 20, relief = SUNKEN) 
	fm1.pack(side = TOP,padx=10,pady=10)

	fm = Frame(root1, width = 20, relief = SUNKEN) 
	fm.pack(side = TOP,padx=10,pady=10)

	fm2 = Frame(root1, width = 20, relief = SUNKEN) 
	fm2.pack(side = TOP,padx=10,pady=10)

	fm3 = Frame(root1, width = 20, relief = SUNKEN) 
	fm3.pack(side = TOP,padx=10,pady=10)

	fm4 = Frame(root1, width = 20, relief = SUNKEN) 
	fm4.pack(side = TOP,padx=10,pady=10)
	
	#label
	password_count = Label(fm1, text=" Password Count: ",font = ('timesnewroman', 12,'bold'))
	password_count.pack(side=LEFT,padx=2,pady=2)
	E1 = Entry(fm1,font = ('timesnewroman', 15))
	E1.pack(side = LEFT)
		

	lblInfo =Label(fm, font=('timesnewroman',12,'bold'),text = " Message: ") 						
	lblInfo.pack(side=LEFT,padx=2,pady=2)
	entry5 =Entry(fm,width=35,font = ('timesnewroman', 15, 'bold'))
	entry5.pack(side=LEFT)
	entry5.insert(0,"Enter password count")

	
	scrollbar=Scrollbar(fm2)
	scrollbar.pack(side=RIGHT, fill=Y)
	lis=Listbox(fm2,width=50,height=10,font=('timesnewroman,14,bold'))
	lis.pack(side=LEFT,padx=5,pady=5,expand=1)
	lis.config(yscrollcommand=scrollbar.set)
	scrollbar.config(command=lis.yview)

	#buttons
	generate_button = Button(fm3,text="Generate",command=lambda:multiple(len,ch))
	generate_button.pack(side=LEFT)
	
	copy_button1 = Button(fm3, text="Copy",command=copy)
	copy_button1.pack(side=LEFT)

	reset1= Button(fm3, text="Reset",command=Reset) 
	reset1.pack(side=LEFT)
	
	exit1= Button(fm3, text="Exit",command=qExit) 
	exit1.pack(side=LEFT)

	#TIME 
	localtime = time.asctime(time.localtime(time.time()))
	lblInfo = Label(fm4, font=('timesnewroman',12,'bold'),text = localtime) 						
	lblInfo.pack(side=BOTTOM)

	
	root.mainloop()


#single password generator		

def length_except(a):
	length=a
	try:
		bb=int(length)
		if(bb==0 or bb==1 or bb==2 or bb==3):
			si="Select length(4-32)"
			return msg(si)
		elif bb>32:
			si="Enter the Length less than 32"
			return msg(si)
		elif bb<0:
			si="Error:Negative Value Length"
			return msg(si)
		else:
			return bb
	except ValueError:  
		si="Error:Invalid Input Length"
		return msg(si)

def msg(s):  
	entry1.insert(END, s+"\n                               ")


def single(length,ch):
	password=""
	for i in range(0, length):
			password +=random.choice(ch) 
	return password


	if value==1:
		return single(length,ch)
	else:
		s="select single/multiple"
		return msg(s)

# Function for calculation of password

def low():
	entry.delete(0, END)
	entry1.delete(0,END)
	# Get the length of password
	length=var1.get()
	value=var.get()
	length=length_except(length)        
	
	password=""
	num='0123456789'
	SLet='abcdefghijklmnopqrstuvwxyz'
	CLet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	punc="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	if v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
		ch=num
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 0 and v2.get() == 0 and v3.get() == 0 and v4.get() == 4: 
		ch=punc
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 0 and v2.get() == 0 and v3.get() == 3 and v4.get() == 0: 
		ch=SLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)   
	elif v1.get() == 0 and v2.get() == 2 and v3.get() == 0 and v4.get() == 0: 
		ch=CLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 1 and v2.get() == 2 and v3.get() == 3 and v4.get() == 4: 
		ch=num+punc+SLet+CLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 0 and v2.get() == 2 and v3.get() == 3 and v4.get() == 0: 
		ch=CLet+SLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)  
	elif v1.get() == 1 and v2.get() == 0 and v3.get() == 3 and v4.get() == 0: 
		ch=num+SLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 1 and v2.get() == 2 and v3.get() == 0 and v4.get() == 0: 
		ch=num+CLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 0 and v2.get() == 0 and v3.get() == 3 and v4.get() == 4: 
		ch=punc+SLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s) 
	elif v1.get() == 0 and v2.get() == 2 and v3.get() == 0 and v4.get() == 4: 
		ch=punc+CLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 4:
		ch=punc+num
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 1 and v2.get() == 0 and v3.get() == 3 and v4.get() == 4: 
		ch=punc+num+SLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s) 
	elif v1.get() == 1 and v2.get() == 2 and v3.get() == 0 and v4.get() == 4: 
		ch=punc+CLet+num
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 1 and v2.get() == 2 and v3.get() == 3 and v4.get() == 0: 
		ch=num+CLet+SLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	elif v1.get() == 0 and v2.get() == 2 and v3.get() == 3 and v4.get() == 4: 
		ch=punc+SLet+CLet
		if value==1:
			return single(length,ch)
		elif value==2:
			if length>=4 and length<=32:
				qwe(length,ch)
		else:
			s="select single/multiple"
			return msg(s)
	else: 
		return msg("Tick options")
	

# Function for generation of password 
def generate(): 
	password1 = low()
	entry.insert(END, password1)
	msg("copy your password")

# Function for copying password to clipboard 
def copy1():
	import pyperclip
	random_password = entry.get()
	pyperclip.copy(random_password)
	
# exit function 
def qExit(): 
	root.destroy()
	exit(0)

# Function to reset the window 
def Reset(): 
	v1.set(0) 
	v2.set(0) 
	v3.set(0) 
	v4.set(0) 
	var.set(0)
	var1.set("4")
	entry.delete(0,END)
	entry1.delete(0,END)


# Main Function 

# create GUI window 
root = Tk()

# defining size of window 
root.geometry("590x370")


top = Frame(root, width = 20, relief = SUNKEN) 
top.pack(side = TOP,padx=10,pady=10)

tops = Frame(root, width = 20, relief = SUNKEN) 
tops.pack(side = TOP,padx=10,pady=10)

radio = Frame(root, width = 20, relief = SUNKEN) 
radio.pack(side = TOP,padx=10,pady=10)


f2 = Frame(root, width = 20, height = 20,relief = SUNKEN) 
f2.pack(side = TOP,padx=10,pady=10)


fw = Frame(root, width = 20, height = 20,relief = SUNKEN) 
fw.pack(side = TOP,padx=10,pady=10)

last = Frame(root, width = 20, height = 20,relief = SUNKEN) 
last.pack(side = TOP,padx=10,pady=10)

f5 = Frame(root, width = 20, height = 20,relief = SUNKEN) 
f5.pack(side = TOP,padx=10,pady=10)

f4= Frame(root, width = 20, height = 20,relief = SUNKEN) 
f4.pack(side = TOP,padx=10,pady=10)


var=IntVar()
v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
var1=StringVar()


# Title of your GUI window 
root.title("Password Generator")

Random_password = Label(last, text="Generated Password: ",font = ('timesnewroman', 12,'bold'))
Random_password.pack(side=LEFT,padx=5)
entry =Entry(last,width=30,font = ('timesnewroman', 15, 'bold'))
entry.pack(side=LEFT,padx=2,fill=Y)


c_label = Label(top, text="Length: ",font = ('timesnewroman', 12, 'bold'))
c_label.pack(side=LEFT,padx=5)
combo = Combobox(top, textvariable=var1,font = ('timesnewroman', 15))
combo['values'] = (4,5,6,7,8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32) 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.pack(side=LEFT,padx=2)

#checkButtons

a=Checkbutton(tops, text="DIGITS",variable=v1,onvalue=1,offvalue=0)
a.pack(side=LEFT,fill=BOTH)

b=Checkbutton(tops, text="UPPER", variable=v2,onvalue=2,offvalue=0)
b.pack(side=LEFT,fill=BOTH)

c=Checkbutton(tops, text="LOWER", variable=v3,onvalue=3,offvalue=0)
c.pack(side=LEFT,fill=BOTH)

d=Checkbutton(tops, text="SYMBOLS", variable=v4,onvalue=4,offvalue=0)
d.pack(side=LEFT,fill=BOTH)


#radioButtons

radio_low = Radiobutton(radio,text="SINGLE PASSWORD", variable=var, value=1) 
radio_low.pack(side=LEFT,fill=BOTH)

radio_strong = Radiobutton(radio, text="MULTIPLE PASSWORDS", variable=var, value=2) 
radio_strong.pack(side=LEFT,fill=BOTH)


#buttons

generate_button = Button(f2,text="Generate",command=generate) 
generate_button.pack(side=LEFT,fill=BOTH)

copy_button = Button(f5, text="Copy",command=copy1) 
copy_button.pack(side=LEFT)

copy_button1 = Button(f5, text="Exit",command=qExit) 
copy_button1.pack(side=RIGHT)

btnReset = Button(f5,text = "Reset",command = Reset).pack(side=RIGHT)

lblInfo =Label(fw,font=('timesnewroman',12,'bold'),text = " Message: ") 						
lblInfo.pack(side=LEFT,padx=2,pady=2)
entry1 =Entry(fw,width=36,font = ('timesnewroman', 15, 'bold'))
entry1.pack(side=LEFT)

#TIME 
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(f4, font=('timesnewroman',12,'bold'),text = localtime) 						
lblInfo.pack(side=BOTTOM)


# start the GUI 
root.mainloop() 
