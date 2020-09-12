import random
import tkinter as tk
from tkinter import *
from random import randint

window = tk.Tk()
window.geometry("650x300")
window.title("Rock Paper Scissors Game")

window.configure(background = "black")

Label1 = Label(window, text="Rock Paper Scissors Game",font=("Arial Bold", 20),background="black",foreground="white")
Label1.grid(row=0, column=1)



#create a list of play options
t = ["Rock", "Paper", "Scissors"]


def rock():
    computer = t[randint(0,2)]
    Comp.config(text="Computer = "+computer)
    player = 'Rock'
    if player == computer:
        output = "Tie!"
        Result.config(text=output)
    elif computer == "Paper":
        output = "You lose! paper covers rock."
        Result.config(text=output)
    else:
        output = "You win! rock smashes scissors."
        Result.config(text=output)
    computer = t[randint(0,2)]
        
def paper():
    computer = t[randint(0,2)]
    Comp.config(text="Computer = "+computer)
    player = 'Paper'
    if player == computer:
        output = "Tie!"
        Result.config(text=output)
    elif computer == "Scissors":
        output ="You lose! Scissors cut paper."
        Result.config(text=output)
    else:
        output = "You win! paper covers rock."
        Result.config(text=output)
    computer = t[randint(0,2)]

def scissor():
    computer = t[randint(0,2)]
    Comp.config(text="Computer = "+computer)
    player = 'Scissors'
    if player == computer:
        output = "Tie!"
        Result.config(text=output)
    elif computer == "Rock":
        output = "You lose! rock smashes scissors."
        Result.config(text=output)
    else:
        output = "You win! Scissors cut paper."
        Result.config(text=output)
    computer = t[randint(0,2)]
    

Rock = Button(window, text="Rock", width = 20, background="blue", command=rock).grid(row=1,column=0)

Paper = Button(window, text="Paper", width = 20, background="green", command=paper).grid(row=1,column=1)

Scissor = Button(window, text="Scissor", width = 20, background="yellow", command=scissor).grid(row=1,column=2)

Comp = Label(window, text=" ",font=("Arial Bold", 15),background="black",foreground="white")
Comp.grid(row=9, column=1)

Result = Label(window, text=" ",font=("Arial Bold", 15),background="black",foreground="white")
Result.grid(row=10, column=1)
