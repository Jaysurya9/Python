'''
   Author: Jaysurya9
   ROJECT TITLE: PASSWORD GENERATOR 
   CODE LANGUAGE: PYTHON 3.7.0a3(32-bit)
   CREATION DATE: 12/02/2019'''

'''SOURCE CODE:'''

#importing random module
import random


#this a function choose() which displays the list of available combinations
def choose():
    '''Choose any one of the option given below which you want to generate passwords :
===============================================================================
 1.Include only Numbers
 2.Include only Symbols
 3.Include only Lowercase
 4.Include only Uppercase
 5.Include Numbers, Uppercase, Lowercase and Symbols
 6.Include Lowercase and Uppercase 
 7.Include Lowercase and Numbers
 8.Include Uppercase and Numbers
 9.Include Lowercase and Symbols
10.Include Uppercase and Symbols
11.Include Numbers and Symbols
12.Include Numbers, Lowercase and Symbols
13.Include Numbers, Uppercase and Symbols
14.Include Lowercase, Uppercase and Symbols
15.Include Lowercase, Uppercase and Numbers
===============================================================================
Press 0(zero) to exit'''
    print(choose.__doc__)   #to display multiple line comments present in the function choose()



#this a function generate() which takes 3 parameters
#i.e;count of passwords,length of passwords and combination characters
#and it generates passwords and displays to the user
def generate(reqPWs,length,ch):
    print("\n===========================GENERATED PASSWORDS===========================")
    for i in range(reqPWs):
        password=''
        for j in range(length):
          password+=random.choice(ch)
        print(i+1,": ",password)
    TogenMore()
    ToContinue()

def ToContinue():
    print("Press '1' Enter to continue\nPress 'any key' Enter to exit")
    inp=input()
    if inp=='1':
        try:
            va=int(inp)
            if(va==1):
                choose()
                n=input("Enter the choice you want: ")
                try:
                    value=int(n)
                    pwgen(value)
                except ValueError:
                    EnterAgain()
        except ValueError:
            EnterAgain()
    else:exit(0)

#this a function EnterAgain() shows the message
def EnterAgain():
    print("\nYou have entered an Invalid Input. Please enter the value (1 to 15)")
    ToContinue()

#this a function reqpw_except() which takes the count of passwords required for the user
def reqpw_except():
    reqPWs=input("Enter the number of passwords you want to generate: ")
    try:
        aa=int(reqPWs)
        if(aa==0):
            print("Passwords cannot be generated with the value 0(zero) Please enter the value greater than 0")
            return reqpw_except()
        elif aa<0:
            print("Invalid Input\nNumber of password cannot be Negative\nPlease enter the value greater than 0")
            return reqpw_except()
        else:
            return aa
    except ValueError:          
        print("\nYou have entered an Invalid Input\nPlease enter the input value of type number\n")
        return reqpw_except()

#this a function reqpw_except() which takes the count of passwords required for the user
def length_except():
    length=input("Enter the length of password you want (4 to 32): ")
    try:
        bb=int(length)
        if(bb==0 or bb==1 or bb==2 or bb==3):
            print("Length cannot be the value" ,bb, "Please enter the value (4 to 32)")
            return length_except()
        elif bb>32:
            print("Length of password should not be greater than 32")
            return length_except()
        elif bb<0:
            print("Invalid Input\nLength cannot be Negavtive\nEnter the length greater than or equal to 4")
            return length_except()
        else:
            return bb
    except ValueError:  
        print("\nYou have entered an Invalid Input\nPlease enter the input value of type number\n")
        return length_except()

#this is a function TogenMore() display the message to the user after generated passwords    
def TogenMore():
    print("\nDo you want to generate more passwords?")

#this is a function pwgen() which takes the  single parameter
#which is used to check the combination entered by the user
def pwgen(comb):
  if comb>15 or comb<0:
    EnterAgain()
  elif comb==0:exit(0)
  else:
    password=''
    reqPWs=int(reqpw_except())
    length=int(length_except())
    SLet='abcdefghijklmnopqrstuvwxyz'
    CLet='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    num='0123456789'
    punc="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    if comb==1:
      generate(reqPWs,length,num)
    elif comb==2:
      generate(reqPWs,length,punc)
    elif comb==3:
      generate(reqPWs,length,SLet)
    elif comb==4:
      generate(reqPWs,length,CLet)
    elif comb==5:
      ch=num+punc+CLet+SLet
      generate(reqPWs,length,ch)
    elif comb==6:
      ch=SLet+CLet
      generate(reqPWs,length,ch)
    elif comb==7:
      ch=num+SLet
      generate(reqPWs,length,ch)
    elif comb==8:
      ch=CLet+num
      generate(reqPWs,length,ch) 
    elif comb==9:
      ch=SLet+punc
      generate(reqPWs,length,ch)
    elif comb==10:
      ch=CLet+punc
      generate(reqPWs,length,ch) 
    elif comb==11:
      ch=num+punc
      generate(reqPWs,length,ch)
    elif comb==12:
      ch=SLet+num+punc
      generate(reqPWs,length,ch)
    elif comb==13:
      ch=CLet+num+punc
      generate(reqPWs,length,ch)
    elif comb==14:
      ch=CLet+SLet+punc
      generate(reqPWs,length,ch)
    elif comb==15:
      ch=CLet+num+SLet
      generate(reqPWs,length,ch)
      

#main function
if __name__=="__main__":                 
    print("\n================================PASSWORD GENERATOR=============================\n")                    
    choose()                    
    comb=input("Enter the choice you want: ")
    try:                    
        val=int(comb)
        pwgen(int(comb))
    except ValueError:      
        EnterAgain()
               
'''END CODE'''
