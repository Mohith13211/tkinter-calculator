import tkinter as tk 

root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.resizable(False, True)

entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="dark gray",
    bd=0,
    fg="white",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12)

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
buttons = ["7","8","9","/",
           "4","5","6","*",
           "1","2","3","-",
           "0",".","=","+",]
r = 1
c = 0
for b in buttons:
    cmd = calc if b == "=" else lambda x = b: press(x)
    tk.Button(
        root,
        text = b,
        command = cmd,
        font = ("Seoge UI",14),
        width=5,
        height= 2,
        bg = "Orange" if b in "+-*/=" else "dark gray",
        fg = "White",
        bd = 0
    ).grid(row = r, column = c, padx = 6, pady = 6)
    c+=1
    if c == 4:
        c = 0
        r += 1
tk.Button(root,
          text = "C",
          command=clear,
          font = ("Segoe UI",14),
          bg = "Red",
          fg = "White",
          bd = 0,
          width = 22,
          height = 2
          ).grid(row = r, column = c, columnspan = 4, pady = 10)
root.mainloop()
