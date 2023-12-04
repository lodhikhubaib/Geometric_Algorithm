import tkinter as tk
from PIL import Image, ImageTk
import importlib
from tkinter import Tk, Canvas, Button, BOTTOM, StringVar, OptionMenu, Label
from tkinter import Canvas, messagebox

def start_algorithm(root):
    root.destroy()
    second_algo = importlib.import_module("second_page")
    second_page_instance = second_algo.SecondPage(tk.Tk())
    second_page_instance.root.mainloop()

root = tk.Tk()
root.title("Algorithm Project")

# Set the background color to white
root.configure(background="white")


# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the new width and height for the image (100% of the screen width and height)
image_width = int(0.7 * screen_width)
image_height = int(0.7 * screen_height)

# Load and display an image on the front page
image = Image.open(r"C:\Users\HP\OneDrive\Desktop\algo\Line inte\Tkinter\AlgoProject\Back.jpeg")  # Replace with your image file
image = image.resize((image_width, image_height), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=photo)
image_label.image = photo
image_label.pack()

# Add a title label
title_label = tk.Label(root, text="Welcome to Algorithm Project", font=("Helvetica", 20, "bold"), background="white")
title_label.pack(pady=20)

# Add a start button
start_button = tk.Button(root, text="Start", font=("Helvetica", 12, "bold"), command=lambda: start_algorithm(root))
start_button.pack(pady=10)

def on_close():
        # Prompt the user with a Yes/No messagebox
        user_response = messagebox.askyesno("Confirmation", "Do you want to close the application?")
        if user_response:
            print("Tkinter application closed.")
            root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()