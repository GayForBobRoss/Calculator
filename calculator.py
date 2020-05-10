import tkinter as tk
from tkinter import font

waitForOp = False
strEquation = ""
strList = []

def addToString(): #This adds the strList into one string
    global strList, strEquation
    strEquation = ""
    for string in strList:
        strEquation = strEquation + string

def getOperator(op): #this gets called when the user enters an operator
    global strList, waitForOp
    if waitForOp:
        waitForOp = False
    strList.append(op)
    addToString()
    textVar.set(strEquation)

def getNumber(value): #this gets called when the user enters a number
    global strList, waitForOp
    if waitForOp:
        strList.clear()
        waitForOp = False
    strList.append(value)
    addToString()
    textVar.set(strEquation)
    
def getAnswere(): #This gets called when the user presses "="
    global strList, strEquation, waitForOp, answere
    strEquation = ""
    for index, string in enumerate(strList): #This adds an × next to any ANS and pi
        if string == "π" or string == "ANS":
            if index + 1 <= len(strList) - 1:
                if strList[index + 1] != "×" and strList[index + 1] != "+" and strList[index + 1] != "-" and strList[index + 1] != "÷" and strList[index + 1] != ")" and strList[index + 1] != "(" and strList[index + 1] != "^(":
                    strList.insert(index + 1, "×")
            if index - 1 >=  0: 
                if strList[index - 1] != "×" and strList[index - 1] != "+" and strList[index - 1] != "-" and strList[index - 1] != "÷" and strList[index - 1] != ")" and strList[index - 1] != "(" and strList[index - 1] != "^(":
                    strList.insert(index, "×")
    for index, string in enumerate(strList): #This changes every string that python can't calculate with into one that python can work with this is importent for eval()  
        if string == "×":
            strList.pop(index)
            strList.insert(index, "*")
        if string == "÷":
            strList.pop(index)
            strList.insert(index, "/")
        if string == "π":
            strList.pop(index)
            strList.insert(index, "3.14159265359")
        if string == "ANS":
            strList.pop(index)
            strList.insert(index, str(answere))
        if string == "^(":
            strList.pop(index)
            strList.insert(index, "(")
            strList.insert(index, "*")
            strList.insert(index, "*")

    for index, string in enumerate(strList): #This adds an * next to any ( and )
        if string == ")":
            if index + 1 <= len(strList) - 1:
                if strList[index + 1] != "*" and strList[index + 1] != "+" and strList[index + 1] != "-" and strList[index + 1] != "÷" and strList[index + 1] != ")" and strList[index + 1] != "(":
                    strList.insert(index + 1, "*")

        if string == "(":
            if index - 1 >=  0: 
                    if strList[index - 1] != "*" and strList[index - 1] != "+" and strList[index - 1] != "-" and strList[index - 1] != "÷" and strList[index - 1] != ")" and strList[index - 1] != "(":
                        strList.insert(index, "*")
    
    addToString()
    try:
        answere = eval(strEquation) #eval can calulate with numbers and operatores even if they are in a string
    except:
        answere = "math error"
    if answere % 1== 0:
        answere = str(int(answere))
    textVar.set(answere)
    strList.clear()
    strList.append("ANS")
    waitForOp = True

def clear(): #This clears the list
    global strList
    strList.clear()
    addToString()
    textVar.set(strEquation)

def remove(): #This clears one item from the list
    global strList
    try:
        strList.pop(len(strList) - 1)
        addToString()
        textVar.set(strEquation)
    except:
        pass


#---------------------------------------------------------GUI----------------------------------------------------------------
root = tk.Tk()

textVar = tk.StringVar()
textVar.set("Ready")

HEIGHT = 700
WIDTH = 500

root.title("Calculator")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

frame = tk.Frame(root, bg = "#000")
frame.place(relwidth = 1, relheight = 1)

topLabel = tk.Label(root, bg = "#222", fg = "#FFF", anchor = "e", textvariable = textVar, font = ("TkTextFont", 20))
topLabel.place(relwidth = 1, relheight = 0.2 )
#-----------------------------------Buttons----------------------------------
#vertical_row1
button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "7", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("7"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0, rely = 0.2)

button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "4", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("4"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0, rely = 0.4)

button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "1", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("1"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0, rely = 0.6)

button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = ".", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("."))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0, rely = 0.8)
#-----------------------------------------------------------------------------
#vertical_row2
button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "8", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("8"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.2, rely = 0.2)

button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "5", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("5"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.2, rely = 0.4)

button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "2", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("2"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.2, rely = 0.6)

button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "0", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("0"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.2, rely = 0.8)
#-----------------------------------------------------------------------------
#vertical_row3
button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "9", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("9"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.4, rely = 0.2)

button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "6", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("6"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.4, rely = 0.4)

button1 = tk.Button(root, bg = "#000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "3", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("3"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.4, rely = 0.6)
#-----------------------------------------------------------------------------
#vertical_row4
button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "÷", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getOperator("÷"))
button1.place(relwidth = 0.2, relheight = 0.1, relx = 0.6, rely = 0.2)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "×", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getOperator("×"))
button1.place(relwidth = 0.2, relheight = 0.1, relx = 0.6, rely = 0.3)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "-", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getOperator("-"))
button1.place(relwidth = 0.2, relheight = 0.1, relx = 0.6, rely = 0.4)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "+", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getOperator("+"))
button1.place(relwidth = 0.2, relheight = 0.1, relx = 0.6, rely = 0.5)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "π", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("π"))
button1.place(relwidth = 0.2, relheight = 0.1, relx = 0.6, rely = 0.6)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "(", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("("))
button1.place(relwidth = 0.2, relheight = 0.1, relx = 0.6, rely = 0.7)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = ")", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber(")"))
button1.place(relwidth = 0.2, relheight = 0.1, relx = 0.6, rely = 0.8)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "^(x)", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getOperator("^("))
button1.place(relwidth = 0.2, relheight = 0.1, relx = 0.6, rely = 0.9)
#-----------------------------------------------------------------------------
#vertical_row5

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "DEL", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: remove())
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.8, rely = 0.2)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "CE", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: clear())
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.8, rely = 0.4)

button1 = tk.Button(root, bg = "#444", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "ANS", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getNumber("ANS"))
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.8, rely = 0.6)

button1 = tk.Button(root, bg = "#FF0000", anchor = "center", fg = "#FFF", font = ("TkTextFont", 20), text = "=", bd = 0, activebackground = "#333", activeforeground = "#FFF", command = lambda: getAnswere())
button1.place(relwidth = 0.2, relheight = 0.2, relx = 0.8, rely = 0.8)

tk.mainloop()