# Gestionnaire de Tournois d'Échecs avec Openclassrooms :

Ce projet est un gestionnaire de tournois d'échecs développé en Python. Il permet de créer et gérer des joueurs, des tournois, et de suivre les résultats des matchs.

## Fonctionnalités :

- Création et gestion de joueurs
- Création et gestion de tournois
- Ajout de joueurs aux tournois
- Lancement et suivi des tournois
- Génération de rapports sur les joueurs et les tournois

## Installation :

1. Clonez ce dépôt :
git clone https://github.com/eva64290/Projet_P4.git

2. Accédez au répertoire du projet :
cd Projet_P4

3. Créez un environnement virtuel :
python3 -m venv env

4. Activez l'environnement virtuel :
- Sur Windows :
  ```
  env\Scripts\activate
  ```
- Sur macOS et Linux :
  ```
  source env/bin/activate
  ```

5. Installez les dépendances :
pip install -r requirements.txt (pip3 sur Mac)


## Utilisation :

Pour lancer le programme, exécutez :
python3 main.py


Suivez les instructions à l'écran pour naviguer dans le menu et utiliser les différentes fonctionnalités.

## Structure du Projet :

- `main.py` : Point d'entrée du programme
- `controllers/` : Contient les contrôleurs pour les joueurs et les tournois
- `models/` : Contient les modèles de données (joueur, tournoi, round, match)
- `views/` : Contient la vue pour l'interface utilisateur
- `data/` : Dossier où sont stockées les données (fichiers JSON)

## Contribution :

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Contact :

Contactez moi sur githubeva64290@hotmail.com

### Générer un nouveau fichier flake8-html :

pip install flake8 (ou pip3 install flake8 pour Mac) si jamais vous ne l'avez pas déjà installé 
puis 
pip install flake8-html (ou pip3 install flake8-html pour Mac)
Une fois installé, vous pouvez générer un rapport HTML des violations flake8 en suivant ces étapes :

    Ouvrez un terminal et naviguez vers le répertoire de votre projet Python.
    Exécutez la commande flake8 avec les options suivantes :
    flake8 --format=html --htmldir=rapport-flake8 votre_code.py ou suivant les modifications et mises à jour faire flake8 --format=html --htmldir=rapport-flake8
    Cela créer un dossier flake8_report (sur Visual Studio Code) et générer un rapport html du nom index.html.
    Si des erreurs de type E501 trop longue, est émise lorsqu’une ligne dépasse 80 caractères.
    Pour palier à ce genre d'erreurs, il suffit de créer un fichier .flake8 et le sauvegarder à la racine du projet.
    Dans ce fichier y écrire : 
    [flake8]
max-line-length = 120 par exemple afin que la longueur soit plus considérée comme une erreur.

Bonne lecture !
