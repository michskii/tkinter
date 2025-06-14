import tkinter as tk
window=tk.Tk()
window.title("welcome to Tkinter")
window.geometry("400x500")

label1=tk.Label(window,text="Enter your name")
label1.pack(pady=10)
entry=tk.Entry(window)
entry.pack(pady=5)
display=tk.Label(window,text="",fg="blue")
display.pack(pady=10)
def hello():
    name=entry.get()
    display.config(text=f"heloo {name}, welcome to tkinter window!!")
button=tk.Button(window,text="submit", command=hello)
button.pack(pady=5)

window.mainloop()