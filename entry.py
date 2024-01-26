import tkinter as tk
from tkinter import messagebox

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def createEntry(width: int, height: int) -> tuple:
    start = ()
    def onSubmit():
        nonlocal start
        startX = startXEntry.get()
        startY = startYEntry.get()
        
        # Validate entry
        if not isInt(startX) or not isInt(startY):
            messagebox.showerror("Error", "Please enter a valid interger value")
            return
        
        start = (int(startX), int(startY))
        window.destroy()
        
    
    window = tk.Tk()
    window.title("Coordinate Entry")
    
    # Get X values
    startXLabel = tk.Label(window, text="Starting X Coordinate:")
    startXLabel.grid(row=0, column=0, padx=10, pady=10)
    startXEntry = tk.Entry(window)
    startXEntry.grid(row=0, column=1, padx=10, pady=10)
    
    # Get Y values
    startYLabel = tk.Label(window, text="Starting Y Coordinate:")
    startYLabel.grid(row=1, column=0, padx=10, pady=10)
    startYEntry = tk.Entry(window)
    startYEntry.grid(row=1, column=1, padx=10, pady=10)
    
    submitBut = tk.Button(window, text="Submit", command=onSubmit)
    submitBut.grid(row=2, column=0, columnspan=2, pady=10)
    
    window.mainloop()
    
    return start
    
    
    
print(createEntry())