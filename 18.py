import tkinter as tk

window= tk.Tk()

label=tk.Label(window,text="Heyo World!")
button=tk.Button(window,text="Click Me")

label.pack()
button.pack()

window.mainloop()
