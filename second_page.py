from PIL import Image, ImageTk
import tkinter as tk
import importlib
from Line_Intersection import GUI as LineIntersectionGUI

class SecondPage:
    def __init__(self, root, displayed=False):
        self.root = root
        self.root.title("Algorithm Project")
        root.configure(background="white")
        self.root.geometry(f"{1400}x{1400}")
        self.displayed = displayed  # Flag to indicate if the page has been displayed

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the new width and height for the image (100% of the screen width and height)
        image_width = int(1 * screen_width)
        image_height = int(1 * screen_height)

        # Load the background image and resize it
        background_image = Image.open(r"C:\Users\HP\OneDrive\Desktop\Geometric_Algorithms\Geometric_Algorithm\src\images\background.jpg")
        image = background_image.resize((image_width, image_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the resized background image
        self.image_label = tk.Label(root, image=photo)
        self.image_label.image = photo
        self.image_label.place(x=screen_width // 4 - image_width // 4, y=screen_height // 4 - image_height // 4)  # Center the image on the screen

        # Create buttons with appropriate spacing
        button_spacing = 80  # Adjust the spacing between buttons as needed

        # Button for Convex Hull
        Conex_Hull_button = tk.Button(root, text="Convex Hull", command=self.Convex_Hull, font=("Helvetica", 18, "bold"))
        Conex_Hull_button.place(x=screen_width // 4, y=screen_height // 4 + image_height // 4 + button_spacing, anchor="w")

        # Button for Line Intersection
        Line_Intersection_button = tk.Button(root, text="Line Intersection", command=self.Line_Intersection, font=("Helvetica", 18, "bold"))
        Line_Intersection_button.place(x=screen_width // 4, y=screen_height // 4 + image_height // 4 + 2 * button_spacing, anchor="w")

    def Convex_Hull(self):
        if not self.displayed:  # Check if the page has been displayed
            self.displayed = True  # Set the flag to True
            self.root.destroy()  # Destroy the current page
            start_algo = importlib.import_module("convexhull")
            start_gui = start_algo.window()
            start_gui.window.mainloop()

    def Line_Intersection(self):
        if not self.displayed:  # Check if the page has been displayed
            self.displayed = True  # Set the flag to True
            self.root.destroy()  # Destroy the current page
            line_intersection_gui = LineIntersectionGUI()
            line_intersection_gui.window.mainloop()
# Run the Tkinter main loop
if __name__ == "__main__":
    root = tk.Tk()
    second_page = SecondPage(root)
    root.mainloop()