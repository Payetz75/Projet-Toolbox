import tkinter as tk
from tkinter import simpledialog, scrolledtext, filedialog, messagebox
import nmap
import requests
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
        
        # Split content into multiple lines
        text = content.split('\n')
        y = 690
        for line in text:
            c.drawString(100, y, line)
            y -= 20
            if y < 50:
                c.showPage()
                y = 750
        
        # Ajouter les conseils de protection contre les attaques Nmap
        conseils = [
            "Conseils pour se protéger contre les scans Nmap :",
            "1. Utiliser un firewall pour limiter l'accès au réseau.",
            "2. Mettre à jour régulièrement les services et logiciels pour corriger les vulnérabilités connues.",
            "3. Utiliser des mots de passe forts et un mécanisme d'authentification robuste.",
            "4. Surveiller régulièrement les logs pour détecter les activités suspectes.",
            "5. Limiter l'exposition des services et des ports inutiles."
        ]
        
        # Dessiner chaque conseil sur le PDF
        for conseil in conseils:
            c.drawString(100, y, conseil)
            y -= 20
            if y < 50:
                c.showPage()
                y = 750
        
        c.save()
        messagebox.showinfo("Rapport Créé", f"Le rapport a été enregistré sous {file_path}")

def scan_ports(target, log_widget):
    nm = nmap.PortScanner()
    log_widget.insert(tk.END, f"Scanning {target}...\n")
    nm.scan(target, arguments='-sV')
    
    open_ports = []
    
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                if nm[host][proto][port]['state'] == 'open':
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port]['version']
                    open_ports.append({
                        'port': port,
                        'service': service,
                        'version': version
                    })
                    log_widget.insert(tk.END, f"Found open port {port} with service {service} version {version}\n")
                    log_widget.see(tk.END)
    return open_ports

def search_cve(service, version, log_widget):
    query = f"{service} {version}"
    url = f"https://cve.circl.lu/api/search/{query}"
    log_widget.insert(tk.END, f"Searching CVEs for {service} {version}...\n")
    response = requests.get(url)
    
    if response.status_code == 200:
        cve_data = response.json()
        log_widget.insert(tk.END, f"Found {len(cve_data)} CVEs\n" if cve_data else "No CVEs found\n")
        log_widget.see(tk.END)
        return cve_data if cve_data else []
    return []

def run_nmap(log_widget):
    log_widget.delete('1.0', tk.END)
    target = simpledialog.askstring("Nmap Scan", "Enter the target IP address:")
    if target:
        open_ports = scan_ports(target, log_widget)
        report_content = ""
        for port_info in open_ports:
            cves = search_cve(port_info['service'], port_info['version'], log_widget)
            if cves:
                report_content += f"CVEs for {port_info['service']} {port_info['version']} on port {port_info['port']}:\n"
                for cve in cves:
                    report_content += f"- {cve['id']}: {cve['summary']}\n"
            else:
                report_content += f"No CVEs found for {port_info['service']} {port_info['version']} on port {port_info['port']}.\n"
        create_pdf_report("Nmap_Scan", report_content)
