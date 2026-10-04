"""
1) Add the file name and activity details.
   a) Mention the file name as `my-profile-card.py`.
   b) Mention the activity name as "My Profile Card".
   c) Mention the lesson topic and grade range.

2) Import Tkinter and create the main window.
   a) Import everything from the `tkinter` module.
   b) Create the main window using `Tk()`.
   c) Set the window title.
   d) Set the window size using `geometry()`.

3) Add the title label.
   a) Create a `Label` for the heading "My Profile Card".
   b) Add text colour, background colour, and width.
   c) Place it at the top using `grid()`.
   d) Use `columnspan` to make it stretch across two columns.

4) Add name and hobby input fields.
   a) Create a label for "Name".
   b) Create an `Entry` box for typing the name.
   c) Create a label for "Hobby".
   d) Create an `Entry` box for typing the hobby.
   e) Place all labels and entries using `grid()`.

5) Create the About Me section.
   a) Add a `Frame` to group the About Me content.
   b) Use border and relief to make the frame visible.
   c) Add an About Me label inside the frame.
   d) Add a `Text` box for writing a short description.
   e) Use `pack()` to place widgets inside the frame.

6) Add the submit button.
   a) Create a button with the text "Show My Card".
   b) Style it with background colour, text colour, and width.
   c) Place it using `grid()` across two columns.

7) Run the Tkinter window.
   a) Use `window.mainloop()` to keep the window open.
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("My Photo Album")
window.geometry("800x600")

title_label = Label(window, text="My Photo Album", fg="white", bg="purple", width=40)
title_label.pack(pady=10)

image_file = Image.open("unnamed.webp")
image_file = image_file.resize((300, 200))
photo = ImageTk.PhotoImage(image_file)

pic = Label(window, image=photo)
pic.pack(pady=10)

def show_message():
    top = Toplevel()
    top.title("Photo Details")
    top.geometry("600x500")
    info = Label(top, text="Location: My Garden")
    info.pack(pady=10)
    place = Label(top, text="Taken on: 20th June, 2022")
    place.pack()
    top.mainloop()

details_button = Button(window, text="See Details", bg="green", fg="black", command=show_message)
details_button.pack(pady=5)

window.mainloop()




