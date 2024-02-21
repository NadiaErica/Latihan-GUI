import tkinter as tk

window = tk.Tk()
window.title("Hello - Nadia Erica")
salam = tk.Label(text="Halo Dunia Tipu", fg="red", bg="white") 
WButton = tk.Button( 

    text = "Klik Saya!", 

    width = 20, 

    height = 10, 

    bg = "red", 

    fg = "black" 

) 

WButton.pack()
window.mainloop()