from tkinter import *
import random

def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def result(human_choice, comp_choice):
    global user_score
    global comp_score
    if human_choice == comp_choice:
        print("Tie")
    elif (human_choice == "rock" and comp_choice == "scissors") or \
         (human_choice == "paper" and comp_choice == "rock") or \
         (human_choice == "scissors" and comp_choice == "paper"):
        print("You Win")
        user_score += 1
    else:
        print("Computer wins")
        comp_score += 1

def rock():
    global user_choice
    global comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def paper():
    global user_choice
    global comp_choice
    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def scissors():
    global user_choice
    global comp_choice
    user_choice = "scissors"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

# Create the Tkinter window
rps = Tk()
rps.geometry("300x300")
rps.title("Rock Paper Scissors")

# Initialize scores
user_score = 0
comp_score = 0

# Create buttons for each choice
button_rock = Button(text="Rock", bg="#888487", font=("arial", 15, "italic bold"), relief=RIDGE, 
                     activebackground="#059458", activeforeground="white", width=24, command=rock)
button_rock.grid(column=0, row=0)

button_paper = Button(text="Paper", bg="#808487", font=("arial", 15, "italic bold"), relief=RIDGE, 
                      activebackground="#85945B", activeforeground="white", width=24, command=paper)
button_paper.grid(column=0, row=1)

button_scissors = Button(text="Scissors", bg="#808487", font=("arial", 15, "italic bold"), relief=RIDGE, 
                         activebackground="#059458", activeforeground="white", width=24, command=scissors)
button_scissors.grid(column=0, row=2)

# Start the main event loop
rps.mainloop()