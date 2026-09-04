from tkinter import filedialog
def getimage():
    filepath = filedialog.askopenfilename(initialdir="./drawings",title="Open Drawing",filetypes=[("Png Files","*.png")])
    return filepath