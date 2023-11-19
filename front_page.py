import tkinter as tk
from PIL import Image, ImageTk
import importlib

def start_algorithm(root):
    root.destroy()
    second_algo = importlib.import_module("second_page")
    second_page_instance = second_algo.SecondPage(tk.Tk())
    second_page_instance.root.mainloop()

root = tk.Tk()
root.title("Algorithm Project")

# Load and display an image on the front page
image = Image.open(r"C:\Users\HP\OneDrive\Desktop\algo\Line inte\Tkinter\Back.jpeg")  # Replace with your image file
image = image.resize((700, 500), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=photo)
image_label.image = photo
image_label.pack()

# Add a title label
title_label = tk.Label(root, text="Welcome to Algorithm Project", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)

# Add a start button
start_button = tk.Button(root, text="Start", font=("Helvetica", 12, "bold"), command=lambda: start_algorithm(root))
start_button.pack(pady=2)

root.mainloop()