import random
import tkinter
from tkinter import *
from PIL import Image, ImageTk  # Import PIL modules

# Setting up the window
S = tkinter.Tk()
S.title("Rock Paper Scissor Game")
S.configure(background='Sky blue')
S.geometry('400x400')
S.resizable(0, 0)

# Labels for the display text
L1 = Label(S, text='Rock, Paper, Scissor', font=("COMIC SANS MS", 15, "bold"),bg = 'Sky Blue')
L1.place(x=95, y=10)

L2 = Label(S, text='Choose an option:', font=("COMIC SANS MS", 15, "bold"), bg = 'Sky Blue')
L2.place(x=110, y=70)

Result = StringVar()

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

L3 = Label(S, text='Result:', font=("COMIC SANS MS", 15, "bold"),bg = 'Sky blue')
L3.place(x=170, y=250)

R = Entry(S, font='arial 14', bd=3, textvariable=Result, bg='white', width=30)
R.place(x=30, y=300)

# Function to define the gameplay
def gameplay(user_choice):
    global choice_comp
    if user_choice == choice_comp:
        Result.set(f"Tie! Both selected {user_choice}")
    elif user_choice == 'Rock' and choice_comp == 'Paper':
        Result.set("You Lose, Computer selected Paper")
    elif user_choice == 'Rock' and choice_comp == 'Scissor':
        Result.set("You Win, Computer selected Scissor")
    elif user_choice == 'Paper' and choice_comp == 'Scissor':
        Result.set("You Lose, Computer selected Scissor")
    elif user_choice == 'Paper' and choice_comp == 'Rock':
        Result.set("You Win, Computer selected Rock")
    elif user_choice == 'Scissor' and choice_comp == 'Rock':
        Result.set("You Lose, Computer selected Rock")
    elif user_choice == 'Scissor' and choice_comp == 'Paper':
        Result.set("You Win, Computer selected Paper")
    else:
        Result.set("Invalid Choice")

# Function to reset the window
def Reset():
    Result.set("")  # Clear the result field
    comp_choice()   # Generate a new computer choice

# Function to exit the window
def Exit():
    S.destroy()

# Set the desired size for the images
image_size = (100, 100)

# Loading images for Rock, Paper, and Scissors using PIL and resizing them
rock_img = Image.open("C:/Users/aadit/OneDrive/Desktop/Code/Python-game/rock.png").resize(image_size, Image.Resampling.LANCZOS)
paper_img = Image.open("C:/Users/aadit/OneDrive/Desktop/Code/Python-game/paper.png").resize(image_size, Image.Resampling.LANCZOS)
scissor_img = Image.open("C:/Users/aadit/OneDrive/Desktop/Code/Python-game/scissor.png").resize(image_size, Image.Resampling.LANCZOS)

# Convert the images to PhotoImage
rock_img = ImageTk.PhotoImage(rock_img)
paper_img = ImageTk.PhotoImage(paper_img)
scissor_img = ImageTk.PhotoImage(scissor_img)

# Creating buttons for each choice with the resized images
B1 = Button(S, image=rock_img, command=lambda: gameplay('Rock'))
B1.place(x=30, y=130)

B2 = Button(S, image=paper_img, command=lambda: gameplay('Paper'))
B2.place(x=150, y=130)

B3 = Button(S, image=scissor_img, command=lambda: gameplay('Scissor'))
B3.place(x=270, y=130)

# Reset and Exit buttons
B4 = Button(S, text="Reset", command=Reset, width=10, bg='yellow', fg='Black')
B4.place(x=110, y=350)

B5 = Button(S, text="Exit", command=Exit, width=10, bg='yellow', fg='Black')
B5.place(x=210, y=350)

# Function to call the window
S.mainloop()
