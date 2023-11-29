from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
import math
import importlib
import matplotlib.path as mpltPath
import matplotlib.pyplot as plt
import timeit
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Canvas, Button, BOTTOM, StringVar, OptionMenu, Label
from tkinter import Canvas, messagebox
import webbrowser

class GUI:
    def __init__(self):
        self.lines = []
        self.root = tk.Tk()
        self.root.title("Line Intersection Checker")

        self.canvas = tk.Canvas(self.root, width=800, height=500, bg="white")
        self.canvas.pack(side=tk.RIGHT, pady=0)

        self.context = self.canvas

        self.intersection_method = tk.StringVar()
        self.intersection_method.set("bruteForce")

        self.clear_canvas_button = tk.Button(self.root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_canvas_button.pack(side=tk.BOTTOM)   
        
        self.compare_time_button = tk.Button(self.root, text="Compare Time", command=self.execute_time)
        self.compare_time_button.pack(side=tk.BOTTOM)

        self.check_intersections_button = tk.Button(self.root, text="Check Intersections", command=self.check_intersections)
        self.check_intersections_button.pack(side=tk.BOTTOM)

        self.add_points_button = tk.Button(self.root, text="Add Points to Line", command=self.add_points_to_line)
        self.add_points_button.pack(side=tk.BOTTOM)
                                
        self.intersection_method_menu = tk.OptionMenu(self.root, self.intersection_method, "bruteForce", "cramer", "ccw", "sweepLine","placeholder")
        self.intersection_method_menu.pack(side=tk.BOTTOM)
        
        self.status_label = tk.Label(self.root, text="Status: ")
        self.status_label.pack(side=tk.BOTTOM)
        
        # Graph Frame
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(side=tk.LEFT,pady=100) 
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
    # Prompt the user with a Yes/No messagebox
        user_response = messagebox.askyesno("Confirmation", "Do you want to close the application?")
        if user_response:
            print("Tkinter application closed.")
        # Hide the current window (assuming it's the 'window' variable from the previous code)
            self.root.withdraw()
        # Open a new application or perform other actions
            self.End_program()

    def End_program(self):
        # Hide the current window
        self.root.withdraw()
        
        # Create a new Tkinter window
        last_page_window = tk.Toplevel()
        last_page_window.title("Last Page")

        # Load the last page HTML content
        self.load_last_page(last_page_window)

    def load_last_page(self, root):
        last_page_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Algorithm Project</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: white;
                    text-align: center;
                }

                #main-frame {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    padding: 12px;
                }

                #developer-content {
                    margin: 12px;
                    padding: 12px;
                    border: 0px solid #ddd;
                    background-color: white;
                    text-align: center;
                    font-size: 20px;
                    font-weight: bold;
                }

                #canvas-container-wrapper {
                    display: flex;
                    justify-content: space-around;
                    width: 100%;
                }

                .canvas-container {
                    flex: 0 0 30%; /* Each canvas container takes 30% of the available space */
                    margin: 12px;
                    padding: 12px;
                    border: 1px solid #ddd;
                    background-color: white;
                    text-align: center;
                }

                canvas {
                    max-width: 100%;
                    height: auto;
                    border: 1px solid #ddd;
                }

                .details {
                    background-color: white;
                    color: black;
                    padding: 6px;
                    text-align: left;
                }
            </style>
        </head>
        <body>
            <div id="main-frame">
                <!-- Developer-specific content -->
                <div id="developer-content">
                    <p>Welcome, Developer!</p>
                    <p>Thank you for using our application.</p>
                    <p>Here is the Information Of the Developer!</p>
                </div>

                <!-- Canvas containers -->
                <div id="canvas-container-wrapper">
                    <div class="canvas-container">
                        <canvas id="aahail-canvas" width="300" height="400"></canvas>
                        <div class="details" id="aahail-details">
                            <p>Name: Aahil Ashiq Ali</p>
                            <p>Email: aahilashiqali@gmail.com</p>
                            <p>LinkedIn: Aahil Ashiq Ali</p>
                            <p>University: FAST NUCES, Karachi</p>
                        </div>
                    </div>

                    <div class="canvas-container">
                        <canvas id="khubaib-canvas" width="300" height="400"></canvas>
                        <div class="details" id="khubaib-details">
                            <p>Name: Muhammad Khubaib Khan Lodhi</p>
                            <p>Email: lodhikhubaib12@gmail.com</p>
                            <p>LinkedIn: Khubaib Lodhi</p>
                            <p>University: FAST NUCES, Karachi</p>
                        </div>
                    </div>

                    <div class="canvas-container">
                        <canvas id="khuzaima-canvas" width="300" height="400"></canvas>
                        <div class="details" id="khuzaima-details">
                            <p>Name: Khuzaima Ahsan</p>
                            <p>Email: khuzaimaahsan07@gmail.com</p>
                            <p>LinkedIn: KHUZAIMA AHSAN</p>
                            <p>University: FAST NUCES, Karachi</p>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                function loadAndDisplayImage(imagePath, canvasId) {
                    const canvas = document.getElementById(canvasId);
                    const ctx = canvas.getContext('2d');

                    const image = new Image();
                    image.onload = function () {
                        ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
                    };
                    image.src = imagePath;
                }

                // Replace these paths with the actual paths to your images
                const aahailImagePath = "aahail.png";
                const khubaibImagePath = "khubaib.png";
                const khuzaimaImagePath = "Khuzaima.png";

                loadAndDisplayImage(aahailImagePath, "aahail-canvas");
                loadAndDisplayImage(khubaibImagePath, "khubaib-canvas");
                loadAndDisplayImage(khuzaimaImagePath, "khuzaima-canvas");
            </script>
        </body>
        </html>
        """
        # Save the HTML content to a temporary file
        with open("Last_Page.html", "w") as f:
            f.write(last_page_content)

        # Open the HTML file in the default web browser
        webbrowser.open("Last_Page.html")

        # Destroy the Tkinter window
        self.root.destroy()
            
            
    def execute_time(self):
        execution_times = []
    
        if len(self.lines) < 2:
            self.status_label.config(text="Status: More than two vertices are needed to calculate convex hull")
            return

        default_algorithm = self.intersection_method.get()  # Save the current algorithm
        self.intersection_method.set

        for i in range(5):
            if i == 0:
                method = "bruteForce"
            elif i == 1:
                method = "cramer"
            elif i == 2:
                method = "ccw"
            elif i == 3:
                method = "sweepLine"
            elif i == 4:
                method = "placeholder"
                
            self.intersection_method.set(method)
            
            execution_time = timeit.timeit(self.check_intersections, number=10) 
            average_time_per_run = execution_time / 10
            execution_times.append(average_time_per_run)
    
        self.bar_graph(execution_times)
        
        self.intersection_method.set(default_algorithm)
    
    def bar_graph(self, execution_times):
        algorithm = ['BF', 'CR', 'CCW', 'SL', 'PH']
        self.fig, self.ax = plt.subplots()
        self.ax.bar(algorithm, execution_times, color='blue')
        self.ax.set_xlabel('Algorithms')
        self.ax.set_ylabel('Average Seconds')
        self.ax.set_title('Average Execution Times of Algorithms')
        self.fig.set_size_inches(4.7, 4)

        if hasattr(self, "bar_graph_canvas"):
        # Destroy the existing canvas if it exists
            self.bar_graph_canvas.get_tk_widget().destroy()

        self.bar_graph_canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.bar_graph_canvas.draw()
        self.bar_graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    
                
    def add_points_to_line(self):
        self.canvas.bind("<Button-1>", self.handle_point_click)

    def handle_point_click(self,event):
        x, y = event.x, event.y

        if not self.lines or len(self.lines[-1]) == 2:
            self.lines.append([{"x": x, "y": y}])
        else:
            self.lines[-1].append({"x": x, "y": y})

        self.draw_lines_on_canvas()

    def draw_lines_on_canvas(self):
        self.context.delete("all")

        for line in self.lines:
            if len(line) >= 2:  # Check if there are enough points to draw a line
                for point in line:
                    x, y = point["x"], point["y"]
                    self.context.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
                    self.context.create_text(x + 8, y - 8, text=f"({x}, {y})", font=('Arial', 8))

                self.context.create_line(*[(point["x"], point["y"]) for point in line], fill="black")

    def check_intersections(self):
        method = self.intersection_method.get()

        if method == 'bruteForce':
            self.check_intersections_brute_force()
        elif method == 'cramer':
            self.check_intersections_cramer()
        elif method == 'ccw':
            self.check_intersections_ccw()
        elif method == 'sweepLine':
            self.sweep_line_algorithm()
        elif method == 'placeholder':
            self.check_intersections_with_placeholder_algorithm()

    def placeholder_intersection_algorithm(self,p1, q1, p2, q2):
        def do_intersect(self,p1, q1, p2, q2):
            def orientation(p, q, r):
                val = (q["y"] - p["y"]) * (r["x"] - q["x"]) - (q["x"] - p["x"]) * (r["y"] - q["y"])
                if val == 0:
                    return 0  # Collinear
                return 1 if val > 0 else 2  # Clockwise or counterclockwise

            o1 = orientation(p1, q1, p2)
            o2 = orientation(p1, q1, q2)
            o3 = orientation(p2, q2, p1)
            o4 = orientation(p2, q2, q1)

            if o1 != o2 and o3 != o4:
                return True

            if o1 == 0 and self.on_segment(p1, p2, q1):
                return True
            if o2 == 0 and self.on_segment(p1, q2, q1):
                return True
            if o3 == 0 and self.on_segment(p2, p1, q2):
                return True
            if o4 == 0 and self.on_segment(p2, q1, q2):
                return True

            return False

        def on_segment(p, q, r):
            return q["x"] <= max(p["x"], r["x"]) and q["x"] >= min(p["x"], r["x"]) and q["y"] <= max(p["y"], r["y"]) and q["y"] >= min(p["y"], r["y"])

        result = do_intersect(self,p1, q1, p2, q2)
        return result

    def check_intersections_with_placeholder_algorithm(self):
        for i in range(len(self.lines) - 1):
            for j in range(i + 1, len(self.lines)):
                result = self.placeholder_intersection_algorithm(self.lines[i][0], self.lines[i][-1], self.lines[j][0], self.lines[j][-1])
            
                if result:
                    self.status_label.config(text="Status: Lines intersect!")
                    return

        self.status_label.config(text="Status: No intersections found")


    def check_intersections_brute_force(self):
        for i in range(len(self.lines) - 1):
            for j in range(i + 1, len(self.lines)):
                if self.do_intersect(self.lines[i][0], self.lines[i][-1], self.lines[j][0], self.lines[j][-1]):
                    self.status_label.config(text="Status: Lines intersect!")
                    return

        self.status_label.config(text="Status: No intersections found")

    def check_intersections_cramer(self):
        for i in range(len(self.lines) - 1):
            for j in range(i + 1, len(self.lines)):
                A, B, C, D = self.lines[i][0], self.lines[i][-1], self.lines[j][0], self.lines[j][-1]
                det = (B["x"] - A["x"]) * (D["y"] - C["y"]) - (D["x"] - C["x"]) * (B["y"] - A["y"])

                if det != 0:
                    alpha = ((D["y"] - C["y"]) * (D["x"] - A["x"]) + (C["x"] - D["x"]) * (D["y"] - A["y"])) / det
                    beta = ((A["y"] - B["y"]) * (D["x"] - A["x"]) + (B["x"] - A["x"]) * (D["y"] - A["y"])) / det

                    if 0 <= alpha <= 1 and 0 <= beta <= 1:
                        self.status_label.config(text="Status: Lines intersect!")
                        return

        self.status_label.config(text="Status: No intersections found")

    def check_intersections_ccw(self):
        for i in range(len(self.lines) - 1):
            for j in range(i + 1, len(self.lines)):
                A, B, C, D = self.lines[i][0], self.lines[i][-1], self.lines[j][0], self.lines[j][-1]
                ccw1 = self.ccw(A, B, C) * self.ccw(A, B, D)
                ccw2 = self.ccw(C, D, A) * self.ccw(C, D, B)

                if ccw1 <= 0 and ccw2 <= 0:
                    self.status_label.config(text="Status: Lines intersect!")
                    return

        self.status_label.config(text="Status: No intersections found")

    def sweep_line_algorithm(self):
        self.lines.sort(key=lambda line: line[0]["x"])

        for i in range(len(self.lines) - 1):
            for j in range(i + 1, len(self.lines)):
                if self.do_intersect_sweep(self.lines[i], self.lines[j]):
                    self.status_label.config(text="Status: Lines intersect!")
                    return

        self.status_label.config(text="Status: No intersections found")

    def do_intersect(self,p1, q1, p2, q2):
        def orientation(p, q, r):
            val = (q["y"] - p["y"]) * (r["x"] - q["x"]) - (q["x"] - p["x"]) * (r["y"] - q["y"])
            if val == 0:
                return 0  # Collinear
            return 1 if val > 0 else 2  # Clockwise or counterclockwise

        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and self.on_segment(p1, p2, q1):
            return True
        if o2 == 0 and self.on_segment(p1, q2, q1):
            return True
        if o3 == 0 and self.on_segment(p2, p1, q2):
            return True
        if o4 == 0 and self.on_segment(p2, q1, q2):
            return True

        return False

    def on_segment(self,p, q, r):
        return q["x"] <= max(p["x"], r["x"]) and q["x"] >= min(p["x"], r["x"]) and q["y"] <= max(p["y"], r["y"]) and q["y"] >= min(p["y"], r["y"])

    def ccw(self,a, b, c):
        return (c["y"] - a["y"]) * (b["x"] - a["x"]) - (b["y"] - a["y"]) * (c["x"] - a["x"])

    def do_intersect_sweep(self,line1, line2):
        p1, q1 = line1[0], line1[-1]
        p2, q2 = line2[0], line2[-1]

        def orientation(p, q, r):
            val = (q["y"] - p["y"]) * (r["x"] - q["x"]) - (q["x"] - p["x"]) * (r["y"] - q["y"])
            if val == 0:
                return 0  # Collinear
            return 1 if val > 0 else 2  # Clockwise or counterclockwise

        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and self.on_segment(p1, p2, q1):
            return True
        if o2 == 0 and self.on_segment(p1, q2, q1):
            return True
        if o3 == 0 and self.on_segment(p2, p1, q2):
            return True
        if o4 == 0 and self.on_segment(p2, q1, q2):
            return True

        return False

    def clear_canvas(self):
       # global lines
        self.lines = []
        self.context.delete("all")
        self.status_label.config(text="Status: Canvas cleared")
        
        if hasattr(self, "graph_frame"):
            self.graph_frame.destroy()

        # Recreate an empty time graph frame
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(side=tk.BOTTOM)

if __name__ == "__main__":
    line_intersection_gui = GUI()
    #line_intersection_gui.plot_time_complexity()
    line_intersection_gui.root.mainloop()