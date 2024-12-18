# API MongoDB et Neo4j

## API réalisée par Mathis GUILLOU, Mathis BOSSARD et Alexis LOPEZ, étudiants à l'ESEO Angers 

## Installation 

Pré-requis: Avoir une base de données MongoDB et Neo4J en local sur votre machine. Avoir la base de données de test MOVIES sur MongoDB et Neo4J.

1) Cloner le repository dans un répertoire local
2) Ouvrir un terminal dans le dossier puis pour installer l'environnement virtuel taper :
   ` python -m venv env-arangodb-fastapi `
3) Accéder à l'environnement : `.\env-arangodb-fastapi\Scripts\Activate.ps1`
4) Installer toutes les dépendances : `pip install -r requirements.txt`
5) Dans le fichier .env, modifiez les URI et les identifiants en fonction de ceux utilisés sur votre environnement local.
6) Lancer l'API : `python -m uvicorn main:app --reload`
7) Accédez au swagger et testez les routes: http://127.0.0.1:8000/docs
