import tkinter as tk

count = 0

def increment():
    global add
    
    label.config(text=str(count))

root = tk.Tk()
root.title("Click Counter")

label = tk.Label(root, text="0", font=("Arial", 18))
label.pack(pady=10)

#textbox 1
tk.Label(root, text="Enter a number:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry_f1 = tk.Entry(root, width=12)
entry_f1.grid(row=0, column=1, padx=8, pady=8, sticky="w")

#textbox 2

tk.Label(root, text="Enter another number:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
entry_f2 = tk.Entry(root, width=12)
entry_f2.grid(row=1, column=1, padx=8, pady=8, sticky="w")

tk.Button(root, text="Addition", command=add).pack(pady=6)
tk.Button(root, text="Subtraction", command=minus).pack(pady=6)
tk.Button(root, text="Multiplication", command=multiply).pack(pady=6)
tk.Button(root, text="Division", command=divide).pack(pady=6)

root.mainloop()
