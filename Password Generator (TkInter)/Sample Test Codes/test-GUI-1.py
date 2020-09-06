# Python program to generate random 
# password using Tkinter module 
import random 
#import pyperpclip 
from tkinter import *
from tkinter.ttk import *
# Function for calculation of password
def M1():
	password1 = "INVALID INPUT"
	entry1.insert(10, password1)
def low(): 
	entry.delete(0, END)
	entry1.delete(0,END)
	# Get the length of password
	length1= var1.get()
	try:
		length1=int(length1)
		if length1>=8 and length1<=32:
			length=length1
			password=""
			num='0123456789'
			SLet='abcdefghijklmnopqrstuvwxyz'
			CLet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
			punc="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
			if var.get() == 1: 
				for i in range(0, length): 
					password = password + random.choice(num) 
				return password 
			elif var.get() == 2: 
				for i in range(0, length): 
					password = password + random.choice(punc) 
				return password
			elif var.get() == 3: 
				for i in range(0, length): 
					password = password + random.choice(SLet) 
				return password   
			elif var.get() == 4: 
				for i in range(0, length): 
					password = password + random.choice(CLet) 
				return password
			elif var.get() == 5: 
				for i in range(0, length): 
					password = password + random.choice(num+punc+SLet+CLet) 
				return password
			elif var.get() == 6: 
				for i in range(0, length): 
					password = password + random.choice(SLet+CLet) 
				return password   
			elif var.get() == 7: 
				for i in range(0, length): 
					password = password + random.choice(num+SLet) 
				return password
			elif var.get() == 8: 
				for i in range(0, length): 
					password = password + random.choice(CLet+num) 
				return password
			elif var.get() == 9: 
				for i in range(0, length): 
					password = password + random.choice(SLet+punc) 
				return password  
			elif var.get() == 10: 
				for i in range(0, length): 
					password = password + random.choice(CLet+punc) 
				return password
			elif var.get() == 11:
				for i in range(0, length): 
					password = password + random.choice(num+punc) 
				return password 
			elif var.get() == 12: 
				for i in range(0, length): 
					password = password + random.choice(SLet+num+punc) 
				return password  
			elif var.get() == 13: 
				for i in range(0, length): 
					password = password + random.choice(CLet+num+punc) 
				return password
			elif var.get() == 14: 
				for i in range(0, length): 
					password = password + random.choice(CLet+SLet+punc) 
				return password
			elif var.get() == 15: 
				for i in range(0, length): 
					password = password + random.choice(CLet+SLet+num) 
				return password
			else: 
				return "Please choose an option"
		else:
			return M1()
	except ValueError:
		return M1()


# Function for generation of password 
def generate(): 
	password1 = low() 
	entry.insert(10, password1) 


# Function for copying password to clipboard 
def copy1(): 
	random_password = entry.get() 
	pyperpclip.copy(random_password) 


# Main Function 

# create GUI window 
root = Tk()
root.minsize(width=300,height=300) 
var = IntVar() 
var1 = IntVar() 

# Title of your GUI window 
root.title("Password Generator") 

# create label and entry to show 
# password generated 
Random_password = Label(root, text="Password")
Random_password.pack(fill=BOTH)
Random_password.grid(row=0,column=0,sticky='W',padx=10,pady=10) 
entry = Entry(root)
entry.grid(row=0, column=0,sticky='E',padx=10,pady=10)

# create label for length of password 
c_label = Label(root, text="Length") 
c_label.grid(row=1,column=0,sticky='W',padx=10,pady=10,)


# create Buttons Copy which will copy 
# password to clipboard and Generate 
# which will generate the password 
copy_button = Button(root, text="Copy", command=copy1) 
copy_button.grid(row=0,column=1,sticky='W')

generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=1,column=1,sticky='W')

# Radio Buttons for deciding the 
radio_low = Radiobutton(root,text="Numbers", variable=var, value=1) 
radio_low.grid(row=2,sticky='W')

radio_strong = Radiobutton(root, text="Symbols", variable=var, value=2) 
radio_strong.grid(row=3,sticky='W')

radio_upper = Radiobutton(root, text="Lowercase", variable=var, value=3) 
radio_upper.grid(row=4,sticky='W')

radio_digit = Radiobutton(root, text="Uppercase", variable=var, value=4) 
radio_digit.grid(row=5,sticky='W')

radio_digit = Radiobutton(root, text="Numbers, Uppercase, Lowercase and Symbols", variable=var, value=5) 
radio_digit.grid(row=2,column=1,sticky='W')

radio_digit = Radiobutton(root, text="Lowercase and Uppercase", variable=var, value=6) 
radio_digit.grid(row=3,column=1,sticky='W')

radio_digit = Radiobutton(root, text="Lowercase and Numbers", variable=var, value=7) 
radio_digit.grid(row=4,column=1,sticky='W')

radio_digit = Radiobutton(root, text="Uppercase and Numbers", variable=var, value=8) 
radio_digit.grid(row=5,column=1,sticky='W')

radio_digit = Radiobutton(root, text="Lowercase and Symbols", variable=var, value=9) 
radio_digit.grid(row=2,column=2,sticky='W')

radio_digit = Radiobutton(root, text="Uppercase and Symbols", variable=var, value=10) 
radio_digit.grid(row=3,column=2,sticky='W')

radio_digit = Radiobutton(root, text="Numbers and Symbols", variable=var, value=11) 
radio_digit.grid(row=4,column=2,sticky='W')

radio_digit = Radiobutton(root, text="Numbers, Lowercase and Symbols", variable=var, value=12) 
radio_digit.grid(row=5,column=2,sticky='W')

radio_digit = Radiobutton(root, text="Numbers, Uppercase and Symbols", variable=var, value=13) 
radio_digit.grid(row=6,sticky='W')

radio_digit = Radiobutton(root, text="Lowercase, Uppercase and Symbols", variable=var, value=14) 
radio_digit.grid(row=6,column=1,sticky='W')

radio_digit = Radiobutton(root, text="Numbers, Uppercase and Lowercase", variable=var, value=15) 
radio_digit.grid(row=6,column=2,sticky='W')

combo = Combobox(root, textvariable=var1)
# Combo Box for length of your password 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=0, row=1,sticky='E')

msg=Label(root,text="Message")
msg.grid(row=7,sticky='W',padx=10,pady=10)
entry1=Entry(root)
entry1.grid(row=7,column=0,sticky='E')




# start the GUI 
root.mainloop() 
