#import necessory libraries
import tkinter as tk
import time

# Define questions and answers
questions = [
    ("What day is Sindhi culture Day?", "a) March 5", "b) July 33", "c) December 5", "d) Agust 17", ),
    ("What is culutural sign of sindhi people?", "a) Topi and Ajrak", "b) Bambo Hat", "c) Turban", "d) aporran"),
    ("How many rivers are flowing through sindh?", "a) 5", "b) 4", "c) 10", "d) 1"),
    ("Who is  National poet of Sindh?", "a) Shah Abdul Latif Bhittai", "b) Ahmed Faraz", "c) Mirza Ghalib ","d) John Ellya" )
]

# Initialize score
score = 0

# Define functions
def check_answer(question_num, choice):
    global score
    if choice == questions[question_num][4]:
        score += 1
    next_question()

def next_question():
    global current_question
    current_question += 1
    if current_question < len(questions):
        question_label.config(text=questions[current_question][0])
        for i in range(4):
            choice_labels[i].config(text=questions[current_question][i + 1])
    else:
        end_game()
#  Result performing here
def end_game():
    question_label.config()
    for button in choice_buttons:
        button.config(state=tk.DISABLED)
    if score >= 4:
        result_label.config(text="Well done! Your score was " + str(score))
    else:
        result_label.config(text="Better luck next time! Your score was " + str(score))

# Create a Tkinter window
root = tk.Tk()
root.title("Quiz App")
root.geometry("500x600")

# Set background color
root.configure(bg="light blue")

# Create a frame for the title
title_frame = tk.Frame(root, bg="light blue")
title_frame.grid(row=0, column=0, columnspan=2, pady=10)

# Create a label for the title
title_label = tk.Label(title_frame, text="Quiz App", font=("Arial", 18, "bold"), bg="light blue")
title_label.pack()

# Initialize current question
current_question = 0

# Create a frame for the question and options
question_frame = tk.Frame(root, bg="light blue")
question_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a label for the question
question_label = tk.Label(question_frame, text=questions[current_question][0], font=("Arial", 16), bg="light blue")
question_label.pack()

# Create labels for the options
choice_labels = []
for i in range(4):
    choice_label = tk.Label(question_frame, text=questions[current_question][i + 1], font=("Arial", 14), bg="light blue")
    choice_labels.append(choice_label)
    choice_label.pack(anchor="w")

# Create buttons for the options
choice_buttons = []
for i in range(4):
    button = tk.Button(root, text=f"Option {chr(97 + i)}", command=lambda i=i: check_answer(current_question, chr(97 + i)))
    choice_buttons.append(button)
    button.grid(row=i + 2, column=0, columnspan=2, padx=10, pady=5, ipadx=20, ipady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Set equal row and column weights for options buttons
for i in range(2):
    root.columnconfigure(i, weight=1)
for i in range(7):
    root.rowconfigure(i, weight=1)

# Start the quiz
next_question()

# Start the Tkinter main loop
root.mainloop()