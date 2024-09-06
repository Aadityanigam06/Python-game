import random
import tkinter
from tkinter import *

# Setting up the window
S = tkinter.Tk()
S.title("My Window")
S.configure(background='Sky blue')
S.geometry('400x400')
S.resizable(0, 0)

# Labels for the display text
L1 = Label(S, text='Rock, Paper, Scissor', font=("COMIC SANS MS", 15, "bold")).place(x=80, y=10)

Choice = StringVar()
L2 = Label(S, text='Choose an option: Rock, Paper, Scissor', font=("COMIC SANS MS", 15, "bold")).place(x=3, y=100)

Text1 = Entry(S, font='arial 15', bd=3, textvariable=Choice, bg='white', width=25)
Text1.place(x=60, y=155)

# Random function to generate the computer choice
def comp_choice():
    global choice_comp
    choice_comp = random.randint(1, 3)
    if choice_comp == 1:
        choice_comp = 'Rock'
    elif choice_comp == 2:
        choice_comp = 'Paper'
    else:
        choice_comp = 'Scissor'

comp_choice()

L3 = Label(S, text='Result:-', font=("COMIC SANS MS", 15, "bold")).place(x=150, y=250)
Result = StringVar()
R = Entry(S, font='arial 14', bd=3, textvariable=Result, bg='white', width=30).place(x=30, y=300)

# Function to define the gameplay
def gameplay():
    global User_Choice
    User_Choice = Choice.get().capitalize()  # Capitalize to standardize input
    if User_Choice == choice_comp:
        Result.set("Tie, Both have the same choice")
    elif User_Choice == 'Rock' and choice_comp == 'Paper':
        Result.set("You Lose, Computer selected Paper")
    elif User_Choice == 'Rock' and choice_comp == 'Scissor':
        Result.set("You Win, Computer selected Scissor")   
    elif User_Choice == 'Paper' and choice_comp == 'Scissor':
        Result.set("You Lose, Computer selected Scissor")
    elif User_Choice == 'Paper' and choice_comp == 'Rock':
        Result.set("You Win, Computer selected Rock")
    elif User_Choice == 'Scissor' and choice_comp == 'Rock':
        Result.set("You Lose, Computer selected Rock")
    elif User_Choice == 'Scissor' and choice_comp == 'Paper':
        Result.set("You Win, Computer selected Paper")
    else:
        Result.set("Invalid Choice: Choose the correct option mentioned above")

# Function to reset the window
def Reset():
    Choice.set("")  # Clear the user input field
    Result.set("")  # Clear the result field
    comp_choice()   # Generate a new computer choice

# Function to exit the window
def Exit():
    S.destroy()

B1 = Button(S, text="Reset", command=Reset, width=10, bg='yellow', fg='Black').place(x=100, y=350)
B2 = Button(S, text="Exit", command=Exit, width=10, bg='yellow', fg='Black').place(x=200, y=350)
B3 = Button(S, text="Play", command=gameplay, width=10, bg='yellow', fg='Black').place(x=150, y=200)

# Function to call the window
S.mainloop()