import tkinter as tk

# -------------------
# GUI Setup
# -------------------

root = tk.Tk()
root.title("Calculator")
root.geometry("415x575")

# -------------------
# Adding in background to hold numbers
# -------------------


# -------------------------------------
def xyz(number):
  global answerVariable
  aVarTen = answerVariable*10
  subNumber = aVarTen+number
  return subNumber

# This just sets the new number to
# add a digit to the end. Didnt feel
# like changing the name everywhere.

# -------------------------------------

def tenthsPlace(number):
  if number == 0:
    return 0
  else:
    return len(str(abs(number)))-1
  
def onClick(number):
  global answerVariable
  answerVariable = xyz(number)
  textBox.config(text=str(answerVariable))

def onClickBackspace():
  global answerVariable
  tempNo = answerVariable%10
  answerVariable = answerVariable-tempNo
  answerVariable = int(answerVariable/10)
  textBox.config(text=str(answerVariable))

def onClickAdd():
  global nextVariable
  global answerVariable
  global device
  device = 'a'
  # Swap answerVariable to a placeholder second variable, then answer variable to 0 again to put in second variable.
  nextVariable = answerVariable
  answerVariable = 0
  textBox.config(text=str(answerVariable))

def onClickSubtract():
  global nextVariable
  global answerVariable
  global device
  device = 's'
  nextVariable = answerVariable
  answerVariable = 0
  textBox.config(text=str(answerVariable))

def onClickMultiply():
  global nextVariable
  global answerVariable
  global device
  device = 'm'
  nextVariable = answerVariable
  answerVariable = 0
  textBox.config(text=str(answerVariable))

def onClickDivide():
  global nextVariable
  global answerVariable
  global device
  device = 'd'
  nextVariable = answerVariable
  answerVariable = 0
  textBox.config(text=str(answerVariable))

def onClickEqual():
   global answerVariable
   global nextVariable
   global device
   if device == 'a':
      answerVariable = nextVariable+answerVariable
   if device == 's':
      answerVariable = nextVariable-answerVariable
   if device == 'm':
      answerVariable = nextVariable*answerVariable
   if device == 'd':
      answerVariable = nextVariable/answerVariable
   if answerVariable%1==0:
      answerVariable = int(answerVariable)
   textBox.config(text=str(answerVariable))

      
def onClickClear():
   global answerVariable
   global nextVariable
   global device

   answerVariable = 0
   nextVariable = 0
   device = 'a'
   textBox.config(text=str(answerVariable))




# -------------------
# Adding in numbers and results widgets
# -------------------

answerVariable = 0
nextVariable = 0
device = 'a'


def columnC(number):
  if number%3!=0:
     return abs((number%3)-1)
  else:
     return 2
    
def rowC(number):
   if number%3!=0:
      return int((number/3))+1
   else:
      return int(number/3)


def numberCreate(name, number):
    name = tk.Button(root, text=str(number), width=7, height=5, command=lambda num=number: onClick(num))
    name.grid(column=abs(int(columnC(number))), row=int(rowC(number)))

numberCreate('one',1)
numberCreate('two', 2)
numberCreate('three',3)
numberCreate('four',4)
numberCreate('five',5)
numberCreate('six', 6)
numberCreate("seven", 7)
numberCreate('eight', 8)
numberCreate('nine', 9)
numberCreate('zero', 0)


# Text Box Below
textBox = tk.Label(root, text = answerVariable, height=5, width=7, borderwidth=5, relief='solid')
textBox.grid(row=0, column=0, sticky='s')

backspace = tk.Button(root, text = "Backspace", height=5,width = 7, command=lambda: onClickBackspace())
backspace.grid(row=4,column=0, sticky='e')

clearSign = tk.Button(root, text='Clear', height=5, width=7, command = lambda: onClickClear())
clearSign.grid(row=4, column=1, sticky='e')

equalSign = tk.Button(root, text='=', height=5, width=7, command = lambda: onClickEqual())
equalSign.grid(row=4, column = 2)

plusSign = tk.Button(root, text='+', height=5,width=7, command = lambda: onClickAdd())
plusSign.grid(row=5, column=0, sticky='e')

minusSign = tk.Button(root, text='-',height=5, width=7,command=lambda: onClickSubtract())
minusSign.grid(row=5,column=1,sticky='e')

multiplySign = tk.Button(root, text='x',height=5, width=7,command=lambda: onClickMultiply())
multiplySign.grid(row=5,column=2,sticky='e')

divideSign = tk.Button(root, text='/',height=5, width=7,command=lambda: onClickDivide())
divideSign.grid(row=5,column=3,sticky='e')

root.mainloop()