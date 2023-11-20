from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
import math
import matplotlib.path as mpltPath
import matplotlib.pyplot as plt
import timeit
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class GUI:
    def __init__(self):
        self.lines = []

        self.root = tk.Tk()
        self.root.title("Line Intersection Checker")

        self.canvas = tk.Canvas(self.root, width=800, height=500, bg="white")
        self.canvas.pack(side=tk.RIGHT, pady=0)

        self.context = self.canvas

        self.status_label = tk.Label(self.root, text="Status: ")
        self.status_label.pack()

        self.intersection_method = tk.StringVar()
        self.intersection_method.set("bruteForce")

        self.intersection_method_menu = tk.OptionMenu(self.root, self.intersection_method, "bruteForce", "cramer", "ccw", "sweepLine","placeholder")
        self.intersection_method_menu.pack()

        self.add_points_button = tk.Button(self.root, text="Add Points to Line", command=self.add_points_to_line)
        self.add_points_button.pack()

        self.check_intersections_button = tk.Button(self.root, text="Check Intersections", command=self.check_intersections)
        self.check_intersections_button.pack()

        self.clear_canvas_button = tk.Button(self.root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_canvas_button.pack()

        self.root.mainloop()

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
        def do_intersect(p1, q1, p2, q2):
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

if __name__ == "__main__":
    line_intersection_gui = GUI()
    line_intersection_gui.root.mainloop()