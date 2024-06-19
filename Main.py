import tkinter as tk
from tkinter import scrolledtext, messagebox
from nmap_scan import run_nmap
from ssh_brute_force import run_brute_force
from ddos_attack import run_ddos

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Security Tool")
        self.geometry("500x400")
        
        tk.Button(self, text="Nmap Scan", command=lambda: run_nmap(self.log_widget)).pack(pady=10)
        tk.Button(self, text="SSH Brute Force", command=lambda: run_brute_force(self.log_widget)).pack(pady=10)
        tk.Button(self, text="DDoS Attack", command=lambda: run_ddos(self.log_widget)).pack(pady=10)
        
        self.log_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=10)
        self.log_widget.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
