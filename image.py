import tkinter as tk


window = tk.Tk()
window.title("Hello - Nadia Erica")
salam = tk.Label(text="Halo Dunia Tipu", fg="red", bg="white") 
logo = tk.PhotoImage(file="pokemon.gif") 
WLableImage = tk.Label(image=logo)
salam.pack()
WLableImage.pack()
window.mainloop()
