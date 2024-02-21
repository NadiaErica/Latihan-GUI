import tkinter as tk

master = tk.Tk()
master.title("Hello - Nadia Erica")

def luas_Ppanjang():
    panjang = int(entry_panjang.get())
    lebar = int(entry_lebar.get())
    luas = panjang * lebar
    label_hasil.config(text=f"Luas persegi panjang: {luas}")

label_panjang = tk.Label(master, text="Masukkan panjang:")
label_panjang.pack()

entry_panjang = tk.Entry(master)
entry_panjang.pack()

label_lebar = tk.Label(master, text="Masukkan lebar:")
label_lebar.pack()

entry_lebar = tk.Entry(master)
entry_lebar.pack()

button_hitung = tk.Button(master, text="Hitung Luas", command=luas_Ppanjang)
button_hitung.pack()

label_hasil = tk.Label(master, text="")
label_hasil.pack()
master.mainloop()



