from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import random
from colors import *
from Algorithms.bubbleSort import bubble_sort
from Algorithms.mergeSort import merge_sort
from Algorithms.insertionSort import insertion_sort
from Algorithms.shellSort import shell_sort
from Algorithms.selectionSort import selection_sort
from Algorithms.quickSortIter import quick_sort

# basic window
window = Tk()
window.title("Sorting Algorithm Visualizer")
window.maxsize(1920, 1080)
window.config(bg=WHITE)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort', 'Shell Sort']

speed_name = StringVar()
speed_list = ['Slow', 'Medium', 'Fast']

data = []


def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 1900
    canvas_height = 850
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 2
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.0001


def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)

    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)

    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data) - 1, drawData, timeTick)

    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, timeTick)

    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)

    elif algo_menu.get() == 'Shell Sort':
        shell_sort(data, drawData, timeTick)


def stop():
    global window
    window.quit()


# *********************************************************************************************************************
# USER INTERFACE #

style = ttk.Style()

# style for UI
style.configure("BW.TLabel", background="white", font=('lato', 10))

UI_frame = Frame(window, width=1900, height=1000, style="BW.TLabel")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# drop-down to select algorithm
l1 = Label(UI_frame, text='Algorithm', style="BW.TLabel")
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# drop-down to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", style="BW.TLabel")
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# *********************************************************************************************************************
# BUTTONS


style.configure('W.TButton',
                font=('lato', 10),
                background='white')

# button for generating array
b1 = Button(UI_frame, text="Generate Array", style='W.TButton', command=generate)
b1.grid(row=2, column=0, padx=15, pady=15)

# sort button
b2 = Button(UI_frame, text="Sort", style='W.TButton', command=sort)
b2.grid(row=2, column=1, padx=5, pady=5)

# exit button
b3 = Button(UI_frame, text="Stop", style='W.TButton', command=stop)
b3.grid(row=2, column=2, padx=5, pady=5)

# canvas to draw our array
canvas = Canvas(window, width=1900, height=1000)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()
