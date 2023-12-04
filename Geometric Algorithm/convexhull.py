import tkinter as tk
import math
import matplotlib.path as mpltPath
import matplotlib.pyplot as plt
import timeit
import importlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Canvas, Button, BOTTOM, StringVar, OptionMenu, Label
from tkinter import Canvas, messagebox
from tkinterhtml import HtmlFrame
import webbrowser

photo_images = []
points = []

def on_close():
    user_response = messagebox.askyesno("Confirmation", "Do you want to close the application?")
    if user_response:
        print("Tkinter application closed.")
        window.withdraw()
        end_program()

def end_program():
    if hasattr(bar_graph, "canvas"):
        bar_graph.canvas.get_tk_widget().destroy()
    # Load the last page HTML content
    load_last_page()

def load_last_page():
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

    with open("last_page.html", "w") as f:
        f.write(last_page_content)

    # Open the HTML file in the default web browser
    webbrowser.open("last_page.html")

    # Close the Tkinter window
    window.destroy()

    
    #window.update()
    
    #window.withdraw()

    # Create a new Tkinter window
    #last_page_window = tk.Toplevel()
    #last_page_window.title("Last Page")

    # Create an HTML frame (WebView) in the new window
    #last_page_html_frame = HtmlFrame(last_page_window)
    #last_page_html_frame.pack(expand=True, fill="both")

    # Set the HTML content for the last page
    #last_page_html_frame.set_content(last_page_content)


def remove_edges():
    my_canvas.delete('all')
    draw_vertices()


def execute_time():
#    print("Executing time complexity")
    execution_times = []
    
    if len(points) < 3:
        errorbox.set("More than two vertices are needed \nto calculate convex hull")
        return
    
    for i in range(5):
        if i == 0:
            algo.set('Brute Force')
        elif i == 1:
            algo.set('Jarvis March')
        elif i == 2:
            algo.set('Graham Scan')
        elif i == 3:
            algo.set('Quick Elimination')
        elif i == 4:
            algo.set('Monotone Andrew')
        
        execution_time = timeit.timeit(execute, number=10) 
        average_time_per_run = execution_time / 10
        execution_times.append(execution_time)
#    print(execution_times)
    
    bar_graph(execution_times)
#....................................................
    
def bar_graph(execution_times):
    algorithm = ['BF','JM','GS','QE','MA']
    fig, ax = plt.subplots()
    ax.bar(algorithm, execution_times, color='blue')
    ax.set_xlabel('Algorithms')
    ax.set_ylabel('Seconds')
    ax.set_title('Execution Times of Algorithms')
    fig.set_size_inches(4.7, 4)
    
    if hasattr(bar_graph, "canvas"):
        # Destroy the existing canvas if it exists
        bar_graph.canvas.get_tk_widget().destroy()
        plt.close('all')
    
    bar_graph.canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    #conects matplotlib with tkinter graph_frame
    bar_graph.canvas.draw()
    bar_graph.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
    # in python attributes of functions can also exist which are basically ariables made inside functions.acts just like classes when calling
    
#............................................................

def show_cordinates(event):
    x, y = int(event.x/5), int(event.y/5)
    cordinates_entry.delete(0,tk.END)
    cordinates_entry.insert(0,f'({x}, {y})')
#..................................

def display_cordinates(event):
    x.set(int(event.x/5))
    y.set(int(event.y/5))
#    print(x.get(),y.get())
    Add_point()
#...................................

def clear_points():
    points.clear()
    my_canvas.delete('all')

#...................................

def draw_vertices():
    for x, y in points:
        if x >= 5 and x <= 695 and y >=5 and y <= 495:
            my_canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", outline="black")

#...................................

def Rem_point():
    x_value = x.get()
    y_value = y.get()
    flag = True
    if x_value:
        try:
            x_number = float(x_value)
            x.set("")
        except ValueError:
            flag = False
            x.set("Only numbers allowed")
    else:
        flag = False
        x.set("Enter cordinates first")
    if y_value:
        try:
            y_number = float(y_value)
            y.set("")
        except ValueError:
            flag = False
            y.set("Only numbers allowed")
    else:
        flag = False
        y.set("Enter cordinates first")
    
    if flag == True:
        p = [x_number*5,y_number*5]
        if p in points:
            points.remove(p)
        remove_edges()
        
#..................
def Add_point():
    errorbox.set('')
    x_value = x.get()
    y_value = y.get()
    flag = True
    if x_value:
        try:
            x_number = float(x_value)
            x.set("")
        except ValueError:
            flag = False
            x.set("Only numbers allowed")
    else:
        flag = False
        x.set("Enter cordinates first")
    if y_value:
        try:
            y_number = float(y_value)
            y.set("")
        except ValueError:
            flag = False
            y.set("Only numbers allowed")
    else:
        flag = False
        y.set("Enter cordinates first")
    
    if flag == True:
        x_number *= 5
        y_number *= 5
        if x_number >= 5 and x_number <= 695 and y_number >=5 and y_number <= 495:
            if [x_number,y_number] not in points:
                points.append([x_number,y_number])
                draw_vertices()
            else:
                errorbox.set("Duplicate cordinate")
    
        else:
            errorbox.set("X-cordinate has range(1,139)\nand Y-cordinate has range(1,99)")
    
        
#................................................................
def draw_convex_hull(convex_hull):
#    print(convex_hull)
    for i in range(len(convex_hull)-1):
        x1,y1 = convex_hull[i]
        x2,y2 = convex_hull[i+1]
        my_canvas.create_line(x1,y1,x2,y2,fill = 'pink')


#................................................................
def execute():
    if len(points) < 3:
        errorbox.set("More than two vertices are needed \nto calculate convex hull")
        return
    unique_points = []
    for point in points:
        if point not in unique_points:
            unique_points.append(point)
    points1 = [[int(point[0]),int(point[1])] for point in unique_points]
    execute_algorithms(points1)

#..................
def execute_algorithms(points):
    selected_algorithm = algo.get()
    convex_hull = []
    remove_edges()
    if selected_algorithm == "Brute Force":
        convex_hull = brute_force(points,convex_hull)   
    elif selected_algorithm == "Jarvis March":
        convex_hull = jarvis_march(points,convex_hull)
    elif selected_algorithm == "Graham Scan":
        convex_hull = graham_scan(points,convex_hull)
    elif selected_algorithm == "Quick Elimination":
        convex_hull = quick_elimination(points,convex_hull)
    elif selected_algorithm == "Monotone Andrew":
        convex_hull = monotone_andrew(points,convex_hull)
    else:
        algo.set("Select an algorithm first!")
    if selected_algorithm == "Brute Force":
        draw_edges(convex_hull)
    else:
        draw_vertices()    
        draw_convex_hull(convex_hull)
        convex_hull = []
        draw_convex_hull(convex_hull)
#..................
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # counterclockwise or clockwise

#..............................................................
def distance(a,b,c):
    y1 = a[1] - b[1]
    y2 = a[1] - c[1]
    x1 = a[0] - b[0]
    x2 = a[0] - c[0]
    x,y = y1 * y1 + x1 * x1 , y2 * y2 + x2 * x2
    return x-y
    
#..................
def draw_edges(convex_hull):
#    print(convex_hull)
    for i in range(len(convex_hull)):
        p1,p2 = convex_hull[i]
        x1,y1 = p1
        x2,y2 = p2
        my_canvas.create_line(x1,y1,x2,y2,fill = 'pink')
   # x1,y1 = convex_hull[-1]
   # x2,y2 = convex_hull[0]
   # my_canvas.create_line(x1,y1,x2,y2,fill = 'pink')

#..................................
def brute_force(points, hull):

    for i in range(len(points)):
        for j in range(len(points)):
            ccw_flag = False
            cw_flag = False
            for k in range(len(points)):
                t = orientation(points[i],points[j], points[k])
                if t == 1:
                    ccw_flag = True
                if t == 2:
                    cw_flag = True
            is_convex = ccw_flag ^ cw_flag
#            print(ccw_flag,cw_flag,is_convex,points[i][0]/5,points[j][0]/5)
            if is_convex and [points[i],points[j]] not in hull:
                hull.append([points[i],points[j]])              

    return hull
    
#...................
def jarvis_march(points,convex_hull):
#    print("Jarvis March")
    start_point = min(points,key = lambda x : x[0])
    convex_hull.append(start_point)
      # Initialize next_point to None
    collinear = []
    while True:
        next_point = points[0]
        for i in range(1,len(points)):
            if points[i] == convex_hull[-1]:
                continue
            val = orientation(next_point,convex_hull[-1], points[i])
            if val == 2:
                next_point = points[i]
                collinear = []
                
            elif val == 0:
                if distance(convex_hull[-1],next_point,points[i]) < 0:
                    collinear.append(points[i])
                    next_point = points[i]
                else:
                    collinear.append(points[i])                    
        
        convex_hull.extend(collinear)
                                     
        if next_point == start_point:
            break
        convex_hull.append(next_point)
    convex_hull.append(convex_hull[0])
    return convex_hull
#...................
def graham_scan(points,convex_hull):
    
#    print("Graham scan")
    p0 = min(points,key = lambda x : x[1])
    s_points = sorted(points, key = lambda p : (math.atan2(p[1] - p0[1], p[0] - p0[0]), (p[0] - p0[0])**2 + (p[1] - p0[1])**2))
    polar_angle = [math.atan2(point[1] - p0[1], point[0] - p0[0]) for point in s_points]
    
    for i in range(len(polar_angle) - 2,-1,-1):
        if polar_angle[i] == polar_angle[i + 1]:
            del s_points[i]
    convex_hull.append(s_points[0])
    convex_hull.append(s_points[1])
    convex_hull.append(s_points[2])

    for i in range(3,len(s_points)):
        while len(convex_hull) >= 2 and orientation(convex_hull[-1],convex_hull[-2],s_points[i]) != 1:
            convex_hull.pop()
        convex_hull.append(s_points[i])
    convex_hull.append(p0)
    return convex_hull 
    
    
#...................
def quick_elimination(points, convex_hull):
#    print("Quick Elimination")
    p0x = min(points, key=lambda x: x[0])
    p1x = max(points, key=lambda x: x[0])
    p0y = min(points, key=lambda x: x[1])
    p1y = max(points, key=lambda x: x[1])
    square = [p0x, p1x, p0y, p1y]  
    s_points = []
    for i in square:
        if i not in s_points:
            s_points.append(i)
    i = 0
    while len(s_points) < 3:
        while points[i] in s_points:
            i+=1
        s_points.append(points[i])
            
    s_points.append(s_points[0])
    path = mpltPath.Path(s_points)
    unique = []
    for i in points:
        if path.contains_point(i) is False:
            unique.append(i)
    unique.extend(s_points)
    arr = []
    for i in unique:
        if i not in arr:
            arr.append(i)
#    print(arr)

    return graham_scan(arr,convex_hull)


#..................................................
def monotone_andrew(points,hull):
    n = len(points)
    if n < 3:
        return []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(0, n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    hull.append(hull[0])
    return hull

'''def on_close():
        # Prompt the user with a Yes/No messagebox
        user_response = messagebox.askyesno("Confirmation", "Do you want to close the application?")
        if user_response:
            print("Tkinter application closed.")
            window.destroy()'''
        
        
#..................
window = tk.Tk()
window.geometry("1500x750")
Title = tk.Label(window,text="Calculating Convex Hull",font=("arial",35,"bold")).place(x=500,y=50)

#..................................
#grid_container = tk.Frame(window)
#grid_container.grid()
#tk.total_columns = 4
#.................................

x = tk.StringVar()
y = tk.StringVar()
algo = tk.StringVar()
errorbox = tk.StringVar()
hover = tk.StringVar()
#.................................
# after 850 is all free space in region 100-520 time complexity
#.................................

cordinates_label = tk.Label(window,font=("arial",15,"bold"), text="Cordinates:")
cordinates_label.place(x=850,y=200)
cordinates_entry = tk.Entry(window,font=("arial",15,"bold"),textvar=hover, width=10, justify="center")
cordinates_entry.place(x=850,y=230)

add_points_label_x = tk.Label(window, text="X Coordinate:")
add_points_label_x.place(x=850, y=520)
add_points_entry_x = tk.Entry(window,textvar=x)
add_points_entry_x.place(x=950, y=520)

add_points_label_y = tk.Label(window, text="Y Coordinate:")
add_points_label_y.place(x=850, y=550)
add_points_entry_y = tk.Entry(window,textvar=y)
add_points_entry_y.place(x=950, y=550)

add_error_box_label = tk.Label(window,font=("arial",15,"bold"),text='Error Box:')
add_error_box_label.place(x=1225, y=600)

frame = tk.Frame(window,bg = 'white',height=80,width=200)
frame.place(x=1225,y=640)
errorbox.set("")
add_error_box = tk.Label(frame,width=180,bg="white",textvariable=errorbox)
add_error_box.place(relx=0.5, rely=0.5, anchor="center")

graph_frame = tk.Frame(window,bg = 'white',height=300,width=400)
graph_frame.place(x=1100,y=175)

#...............................................................................................................
my_frame = tk.Frame(window,bg = 'black',height=550,width=750)
my_frame.place(x=25,y=175)
my_canvas = tk.Canvas(my_frame,width=700,height=500,bg='white')
my_canvas.place(x=20,y=20)
print("X cord limit 1 - 139 and Y cord limit 1 - 99")

#.................................................................................
mouse_hover = my_canvas.bind("<Motion>", show_cordinates)
mouse_click = my_canvas.bind('<Button-1>',display_cordinates)
add_points = tk.Button(window,text="Add Point",font=("arial",15,"bold"),command = Add_point).place(x=1000,y=600)
rem_points = tk.Button(window,text="Remove Point",font=("arial",15,"bold"),command = Rem_point).place(x=850,y=600)

#.................................................................................
algorithms = ['Brute Force','Jarvis March','Graham Scan','Quick Elimination','Monotone Andrew']
dropdown = tk.OptionMenu(window,algo,*algorithms)
algo.set("Select Algorithm")
dropdown.config(width=20)
dropdown.place(x = 850, y = 675)

calculate = tk.Button(window,text="Calculate",font=("arial",15,"bold"),command = execute).place(x=1020,y=675)
time_complexity = tk.Button(window,text="Compare Time Complexity",font=("arial",15,"bold"),command = execute_time)
time_complexity.place(x=800,y=300)

#................................................................................................
clear = tk.Button(window,text="Clear",font=("arial",15,"bold"),command = clear_points).place(x=850,y=720)
window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()