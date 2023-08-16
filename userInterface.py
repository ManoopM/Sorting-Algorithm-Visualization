UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# drop-down to select algorithm
l1 = Label(UI_frame, text='Algorithm', bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# drop-down to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# button for generating array
b1 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b1.grid(row=2, column=0, padx=5, pady=5)

# sort button
b2 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b2.grid(row=2, column=1, padx=5, pady=5)

# exit button
b3 = Button(UI_frame, text="Stop", command=stop, bg=LIGHT_GRAY)
b3.grid(row=2, column=2, padx=5, pady=5)


# canvas to draw our array
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)