# WebScrap

Un script Python simple pour récupérer et télécharger des pages web, avec gestion robuste des erreurs de compression gzip.

## Description

Ce projet utilise la bibliothèque `requests` pour télécharger le contenu d'une page web (ArcGIS) et le sauvegarder dans un fichier HTML local. Il inclut une logique de retry automatique en cas d'erreurs de décompression gzip.

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/<votre-username>/WebScrap.git
   cd WebScrap
   ```

2. Installez les dépendances :
   ```
   pip install requests
   ```

## Utilisation

Exécutez le script :
```
python scrap.py
```

Le script téléchargera la page web et la sauvegardera dans `webpage.html`.

## Dépendances

- Python 3.7+
- `requests` - pour les requêtes HTTP

## Fichiers

- `scrap.py` - Script principal
- `webpage.html` - Fichier généré (sauvegarde de la page web)

## Licence

MIT
