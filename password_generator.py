#importing necessory libraries
from tkinter import *
import random
import string

# Function to generate a random password
def generate_password():
    pw_length = int(entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    my_password = ''.join(random.choice(characters) for _ in range(pw_length))
    pw_entry.delete(0, END)
    pw_entry.insert(0, my_password)

# Function to copy the password to the clipboard
def copy_to_clipboard():
    root.clipboard_clear()  
    root.clipboard_append(pw_entry.get())
    root.update()

#screen
root = Tk()
root.title('Password Generator')
root.geometry("500x300")

#frame of screen
LF = LabelFrame(root, text="How many characters password you want")
LF.pack(pady=20)

# entry feild
entry = Entry(LF, font=("Helvetica", 24))
entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

#button to generat password
my_btn = Button(my_frame, text="Generate strong password", command=generate_password)
my_btn.pack()

#button to copy password in clipboard
clip_btn = Button(my_frame, text="Copy", command=copy_to_clipboard)
clip_btn.pack(padx=10) 

root.mainloop()
