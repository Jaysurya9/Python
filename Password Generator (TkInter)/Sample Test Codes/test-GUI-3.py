# Python program to generate random 
# password using Tkinter module 
import random 
#import pyperpclip 
from tkinter import *
from tkinter.ttk import *
import time
import datetime


def msg(s):  
	entry1.insert(10, s) 


# Function for calculation of password

def low(): 
	entry.delete(0, END)
	entry1.delete(0,END)
	# Get the length of password
	length= var1.get()
	try:
		length=int(length)
		if length<8 or length>32:
			si="select length(8-32)"
			return msg(si)
	except ValueError:
		si="select length(8-32)"
		return mgs(si)
	password=""
	num='0123456789'
	SLet='abcdefghijklmnopqrstuvwxyz'
	CLet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	punc="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	if v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(num) 
		return password 
	elif v1.get() == 0 and v2.get() == 0 and v3.get() == 0 and v4.get() == 4: 
		for i in range(0, length): 
			password = password + random.choice(punc) 
		return password
	elif v1.get() == 0 and v2.get() == 0 and v3.get() == 3 and v4.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(SLet) 
		return password   
	elif v1.get() == 0 and v2.get() == 2 and v3.get() == 0 and v4.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(CLet) 
		return password
	elif v1.get() == 1 and v2.get() == 2 and v3.get() == 3 and v4.get() == 4: 
		for i in range(0, length): 
			password = password + random.choice(num+punc+SLet+CLet) 
		return password
	elif v1.get() == 0 and v2.get() == 2 and v3.get() == 3 and v4.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(SLet+CLet) 
		return password   
	elif v1.get() == 1 and v2.get() == 0 and v3.get() == 3 and v4.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(num+SLet) 
		return password
	elif v1.get() == 1 and v2.get() == 2 and v3.get() == 0 and v4.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(CLet+num) 
		return password
	elif v1.get() == 0 and v2.get() == 0 and v3.get() == 3 and v4.get() == 4: 
		for i in range(0, length): 
			password = password + random.choice(SLet+punc) 
		return password  
	elif v1.get() == 0 and v2.get() == 2 and v3.get() == 0 and v4.get() == 4: 
		for i in range(0, length): 
			password = password + random.choice(CLet+punc) 
		return password
	elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 4:
		for i in range(0, length): 
			password = password + random.choice(num+punc) 
		return password 
	elif v1.get() == 1 and v2.get() == 0 and v3.get() == 3 and v4.get() == 4: 
		for i in range(0, length): 
			password = password + random.choice(SLet+num+punc) 
		return password  
	elif v1.get() == 1 and v2.get() == 2 and v3.get() == 0 and v4.get() == 4: 
		for i in range(0, length): 
			password = password + random.choice(CLet+num+punc) 
		return password
	elif v1.get() == 1 and v2.get() == 2 and v3.get() == 3 and v4.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(CLet+SLet+num) 
		return password
	elif v1.get() == 0 and v2.get() == 2 and v3.get() == 3 and v4.get() == 4: 
		for i in range(0, length): 
			password = password + random.choice(CLet+SLet+punc) 
		return password
	else: 
		return msg("select an option")


# Function for generation of password 
def generate(): 
	password1 = low() 
	entry.insert(10, password1) 


# Function for copying password to clipboard 
def copy1():
	random_password = entry.get()
	#pyperclip.copy(random_password)
	
# exit function 
def qExit(): 
	root.destroy()
	exit(0)



# Main Function 

# create GUI window 
root = Tk()

# defining size of window 
root.geometry("600x380")

top = Frame(root, width = 850, relief = SUNKEN) 
top.pack(side = TOP,padx=10,pady=10)

tops = Frame(root, width = 850, relief = SUNKEN) 
tops.pack(side = TOP,padx=10,pady=10)

f2 = Frame(root, width = 20, height = 20,relief = SUNKEN) 
f2.pack(side = TOP,padx=10,pady=10)


fw = Frame(root, width = 20, height = 20,relief = SUNKEN) 
fw.pack(side = TOP,padx=10,pady=10)

last = Frame(root, width = 20, height = 20,relief = SUNKEN) 
last.pack(side = TOP,padx=10,pady=10)

f5 = Frame(root, width = 20, height = 20,relief = SUNKEN) 
f5.pack(side = TOP,padx=10,pady=10)

f1 = Frame(root, width = 20, height = 20,relief = SUNKEN) 
f1.pack(side = TOP,padx=10,pady=10)

f4= Frame(root, width = 20, height = 20,relief = SUNKEN) 
f4.pack(side = TOP,padx=10,pady=10)



v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
var1=IntVar()

# Title of your GUI window 
root.title("Password Generator")

Random_password = Label(last, text="Generated Password: ",font = ('timesnewroman', 12,'bold'))
Random_password.pack(side=LEFT,padx=5)
entry =Entry(last,font = ('timesnewroman', 20, 'bold'))
entry.pack(side=LEFT)

c_label = Label(top, text="Length: ",font = ('timesnewroman', 12, 'bold'))
c_label.pack(side=LEFT,padx=5)
combo = Combobox(top, textvariable=var1,font = ('timesnewroman', 16))
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32) 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.pack(side=LEFT)


a=Checkbutton(tops, text="DIGITS",variable=v1,onvalue=1,offvalue=0)
a.pack(side=LEFT,fill=BOTH)

b=Checkbutton(tops, text="UPPER", variable=v2,onvalue=2,offvalue=0)
b.pack(side=LEFT,fill=BOTH)

c=Checkbutton(tops, text="LOWER", variable=v3,onvalue=3,offvalue=0)
c.pack(side=LEFT,fill=BOTH)

d=Checkbutton(tops, text="SYMBOLS", variable=v4,onvalue=4,offvalue=0)
d.pack(side=LEFT,fill=BOTH)


generate_button = Button(f2,text="Generate",width=20 ,command=generate) 
generate_button.pack(side=LEFT,fill=BOTH)

copy_button = Button(f5, text="Copy",command=copy1) 
copy_button.pack(side=LEFT)

copy_button1 = Button(f1, text="Exit",command=qExit) 
copy_button1.pack(side=RIGHT)

lblInfo =Label(fw, font=('timesnewroman',12,'bold'),text = "Message: ") 						
lblInfo.pack(side=LEFT,padx=5,pady=5)
entry1 =Entry(fw,font = ('timesnewroman', 15, 'bold'))
entry1.pack(side=LEFT)

#TIME 
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(f4, font=('timesnewroman',12,'bold'),text = localtime) 						
lblInfo.pack(side=BOTTOM)



# start the GUI 
root.mainloop() 
