import tkinter as tk 

def click_button():
    print("Clicked Button")

window=tk.Tk()

button=tk.Button(window,text="Click Me",command=click_button)
button.pack()

window.mainloop()