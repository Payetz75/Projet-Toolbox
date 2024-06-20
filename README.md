<!-- Utiliser des styles inline pour les titres -->
<h1 style="color:green;">I - Toolbox Pentest 🧑‍💻</h1>
<p>Ce projet est une toolbox de sécurité conçue pour évaluer la sécurité d'une entreprise à l'aide de plusieurs scripts d'attaque. Chaque test génère un rapport détaillé, incluant des recommandations de sécurité à suivre. Cette toolbox est accessible via une interface graphique conviviale. Pour l'exécuter, il suffit de lancer "main.py", permettant ainsi d'accéder à toutes les fonctionnalités sans avoir à exécuter chaque script individuellement.</p>

<h1 style="color:green;">II - Pré-Requis ✅:</h1>
<p>Pour utiliser cette toolbox de sécurité, un utilisateur doit:</p>
<ul>
    <li>Avoir un système d'exploitation compatible (Windows, macOS ou Linux).</li>
    <li>Avoir Python 3.11.6 et Pip installés.</li>
    <li>Installer Nmap.</li>
    <li>Installer les bibliothèques Python nécessaires via Pip.</li>
    <li>Disposer d'un accès Internet et éventuellement de permissions administratives.</li>
</ul>
<p>En respectant ces prérequis, l'utilisateur pourra exécuter la toolbox sans soucis sur sa machine.</p>

<h1 style="color:green;">III - Bibliothèques à installer et leurs fonctionnalités 🍉:</h1>
<p><strong>TKINTER</strong></p>
<ul>
    <li>Module principal (tk): Créer la fenêtre principale, les boutons, et gérer les événements GUI.</li>
    <li>ScrolledText: Ajouter une zone de texte défilante pour afficher les logs des activités.</li>
    <li>SimpleDialog: Demander à l'utilisateur des entrées comme l'adresse IP, le nom d'utilisateur, etc.</li>
    <li>MessageBox: Afficher des messages d'information ou d'erreur.</li>
    <li>FileDialog: Ouvrir une boîte de dialogue pour enregistrer les fichiers PDF.</li>
</ul>

<p><strong>NMAP</strong></p>
<ul>
    <li>nmap.PortScanner: Scanner les ports d'un hôte cible et récupérer les informations sur les services et leurs versions.</li>
</ul>

<p><strong>REQUESTS</strong></p>
<ul>
    <li>requests.get(): Envoyer des requêtes HTTP pour récupérer des informations sur les CVE à partir de bases de données publiques.</li>
</ul>

<p><strong>PARAMIKO</strong></p>
<ul>
    <li>paramiko.SSHClient: Configurer et gérer les connexions SSH pour tenter des connexions avec différents mots de passe.</li>
</ul>

<p><strong>REPORTLABS</strong></p>
<ul>
    <li>canvas.Canvas: Créer et dessiner des éléments dans un document PDF, comme les titres, les rapports de scan, et les conseils de sécurité.</li>
</ul>

<h1 style="color:green;">IV - Scripts et leurs fonctions 💻:</h1>
<p><strong>main.py</strong></p>
<ul>
    <li>Gère l'interface utilisateur principale avec des boutons pour lancer différents types d'attaques ou de scans.</li>
</ul>

<p><strong>nmap_scan.py</strong></p>
<ul>
    <li>Effectue des scans Nmap, recherche des CVE associées et génère des rapports PDF avec des conseils de protection.</li>
</ul>

<p><strong>ddos_attack.py</strong></p>
<ul>
    <li>Lance des attaques DDoS simulées et génère des rapports PDF avec des conseils de protection contre les attaques DDoS.</li>
</ul>

<p><strong>ssh_brute_force.py</strong></p>
<ul>
    <li>Effectue des attaques par force brute SSH et génère des rapports PDF avec des conseils de sécurité pour SSH.</li>
</ul>
