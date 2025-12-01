import tkinter as tk
janela = tk.Tk()
janela.title("Testando Tk")
janela.geometry("300x200")
tk.Label(janela, text="Se você está vendo isso, o Tk funciona").pack()
janela.mainloop()