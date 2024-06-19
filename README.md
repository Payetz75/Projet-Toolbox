Toolbox Pentest

Ce projet est une toolbox qui est accessible depuis une interface graphique, il suffit de lancer "main.py" pour l’exécuter et accéder a l'ensemble des fonctionnalités sans avoir a lancer chaque script individuellement.

Pré-Requis :

Pour utiliser cette toolbox de sécurité, un utilisateur doit:

1. Avoir un système d'exploitation compatible (Windows, macOS ou Linux).
2. Avoir Python 3.11.6 et Pip installés.
3. Installer Nmap.
4. Installer les bibliothèques Python nécessaires via Pip.
5. Disposer d'un accès Internet et éventuellement de permissions administratives.

En respectant ces prérequis, l'utilisateur pourra exécuter la toolbox sans soucis sur sa machine.

Bibliothèques a installer et leurs fonctionnalités :

TKINTER
* Module principal (tk): Créer la fenêtre principale, les boutons, et gérer les événements GUI.
* ScrolledText: Ajouter une zone de texte défilante pour afficher les logs des activités.
* SimpleDialog: Demander à l'utilisateur des entrées comme l'adresse IP, le nom d'utilisateur, etc.
* MessageBox: Afficher des messages d'information ou d'erreur.
* FileDialog: Ouvrir une boîte de dialogue pour enregistrer les fichiers PDF.

NMAP
* nmap.PortScanner: Scanner les ports d'un hôte cible et récupérer les informations sur les services et leurs versions.

REQUESTS
* requests.get(): Envoyer des requêtes HTTP pour récupérer des informations sur les CVE à partir de bases de données publiques.

PARAMIKO
* paramiko.SSHClient: Configurer et gérer les connexions SSH pour tenter des connexions avec différents mots de passe.

REPORTLABS
* canvas.Canvas: Créer et dessiner des éléments dans un document PDF, comme les titres, les rapports de scan, et les conseils de sécurité.
 

Scripts et leurs fonctions :

main.py
* Gère l'interface utilisateur principale avec des boutons pour lancer différents types d'attaques ou de scans.

nmap_scan.py
* Effectue des scans Nmap, recherche des CVE associées et génère des rapports PDF avec des conseils de protection.

ddos_attack.py
* Lance des attaques DDoS simulées et génère des rapports PDF avec des conseils de protection contre les attaques DDoS.

ssh_brute_force.py
* Effectue des attaques par force brute SSH et génère des rapports PDF avec des conseils de sécurité pour SSH.


