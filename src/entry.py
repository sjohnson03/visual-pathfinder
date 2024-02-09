import tkinter as tk
from tkinter import messagebox

def isInt(value):
    if not value:
        return False
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
        endX = endXEntry.get()
        endY = endYEntry.get()
        
        if endX == startX and endY == startY:
            messagebox.showerror("Error", "Start coordinate must be different to end coordinate")
            return
        # Validate entry
        if not isInt(startX) or not isInt(startY) or not isInt(endX) or not isInt(endY):
            messagebox.showerror("Error", "Please enter a valid interger value!")
            return
        startX, startY = abs(int(startX)), abs(int(startY))
        endX, endY = abs(int(endX)), abs(int(endY))
        if startX >= width or startY >= height or endX >= width or endY >= height:
            messagebox.showerror("Index out of bounds", f"Please enter coordinates between ({width}, {height})")
            return
            
        start = ((int(startX), int(startY)), (int(endY), int(endX)))
        window.destroy()
    
    window = tk.Tk()
    window.title("Coordinate Entry")
    
    # Get starting X values
    startXLabel = tk.Label(window, text="Starting X Coordinate:")
    startXLabel.grid(row=0, column=0, padx=5, pady=10)
    startXEntry = tk.Entry(window)
    startXEntry.grid(row=0, column=1, padx=10, pady=10)
    
    # Get starting Y values
    startYLabel = tk.Label(window, text="Starting Y Coordinate:")
    startYLabel.grid(row=0, column=2, padx=5, pady=10)
    startYEntry = tk.Entry(window)
    startYEntry.grid(row=0, column=3, padx=10, pady=10)
    
    # Get ending X values
    endXLabel = tk.Label(window, text="Ending X Coordinate:")
    endXLabel.grid(row=1, column=0, padx=5, pady=10)
    endXEntry = tk.Entry(window)
    endXEntry.grid(row=1, column=1, padx=10, pady=10)
    
    # Get ending Y values
    endYLabel = tk.Label(window, text="Ending Y Coordinate:")
    endYLabel.grid(row=1, column=2, padx=5, pady=10)
    endYEntry = tk.Entry(window)
    endYEntry.grid(row=1, column=3, padx=10, pady=10)
    
    submitBut = tk.Button(window, text="Submit", command=onSubmit)
    submitBut.grid(row=2, column=0, columnspan=4, pady=10)  # Placed below, spanning all columns
    
    window.mainloop()
    
    return start

if __name__ == "__main__":
    createEntry(400,400)
    