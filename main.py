import tkinter as tk
from tkinter import messagebox
from interfaceJeu.InterfaceJeu import InterfaceJeu
def main():
    fenetre = tk.Tk()
    app = InterfaceJeu(fenetre)
    fenetre.mainloop()
if __name__ == '__main__':
    main()

