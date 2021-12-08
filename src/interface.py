import tkinter as tk

root = tk.Tk()
percent = tk.IntVar()

def main():
    root.wm_title("Control de batería")
    root.resizable(False, False)

    intro_message = tk.Label(root, text="Seleccione tope de carga")
    intro_message.grid(row=0, columnspan=2)

    choice_30 = tk.Radiobutton(root, text="30", variable=percent, value=30)
    choice_30.grid(row=1, column=0)

    choice_60 = tk.Radiobutton(root, text="60", variable=percent, value=60)
    choice_60.grid(row=2, column=0)

    choice_85 = tk.Radiobutton(root, text="85", variable=percent, value=85)
    choice_85.grid(row=3, column=0)

    choice_full = tk.Radiobutton(root, text="100", variable=percent, value=100)
    choice_full.grid(row=4, column=0)

    accept_button = tk.Button(root, text="Aceptar", command=accept_and_save)
    accept_button.grid(row=5, column=0)

    cancell_button = tk.Button(root, text="Cancelar", command=cancel)
    cancell_button.grid(row=5, column=1)

    tk.mainloop()

def accept_and_save():
    print(percent.get())
    exit()

def cancel():
    exit()

if __name__ == "__main__":
    main()
