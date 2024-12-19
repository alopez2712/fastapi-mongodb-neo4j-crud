# API MongoDB et Neo4j

## API réalisée par Mathis GUILLOU, Mathis BOSSARD et Alexis LOPEZ, étudiants à l'ESEO Angers 

Notre application FastAPI permet d'interagir avec des bases de données MongoDB et Neo4j. Elle offre des endpoints pour interroger les films, gérer les évaluations des utilisateurs et comparer les données entre les deux bases de données.

## Table des Matières

1. [Fonctionnalités](#fonctionnalités)
2. [Structure du Projet](#structure-du-projet)
3. [Prérequis](#prérequis)
4. [Configuration](#configuration)
5. [Installation](#installation)
6. [Préparation des Bases de Données](#préparation-des-bases-de-données)
7. [Lancement](#lancement)
8. [API Endpoints](#api-endpoints)
9. [Structure des Données](#structure-des-données)


## Fonctionnalités

L'API propose les fonctionnalités suivantes :

### MongoDB (Endpoint `/mongodb`)
- Lister les films (limité à 10)
- Rechercher des films par titre ou acteur
- Mettre à jour les informations d'un film

### Neo4j (Endpoint `/neo4j`)
- Lister les utilisateurs ayant évalué un film spécifique
- Obtenir les statistiques d'évaluation d'un utilisateur

### Commun (Endpoint `/common`)
- Comparer les films présents dans les deux bases de données

## Structure du Projet

```
├── main.py              # Point d'entrée de l'application
├── models.py            # Modèles Pydantic
├── routes_movies.py     # Routes pour MongoDB
├── routes_neo4j.py      # Routes pour Neo4j
├── routes_common.py     # Routes communes
├── requirements.txt     # Dépendances du projet
└── .env                 # Configuration des variables d'environnement
```

## Prérequis

- Python 3.8 ou supérieur
- MongoDB
- Neo4j
- Base de données "Movies" de Neo4j
- Les dépendances suivantes (spécifiées dans requirements.txt) :
  - fastapi==0.115.6
  - uvicorn==0.32.1
  - pymongo==4.10.1
  - neo4j==5.27.0
  - python-dotenv==1.0.1
  - pydantic==2.10.3
  - dnspython==2.7.0

## Configuration

Modifier le fichier `.env` à la racine du projet avec les variables suivantes :

```
ATLAS_URI=votre_uri_mongodb
DB_NAME=nom_de_votre_base_mongodb
NEO4J_URI=votre_uri_neo4j
NEO4J_USER=votre_utilisateur_neo4j
NEO4J_PASSWORD=votre_mot_de_passe_neo4j
```

## Installation

1) Cloner le repository dans un répertoire local
2) Ouvrir un terminal dans le dossier puis pour installer l'environnement virtuel taper :
   ` python -m venv env-arangodb-fastapi `
3) Accéder à l'environnement : `.\env-arangodb-fastapi\Scripts\Activate.ps1`
4) Installer toutes les dépendances : `pip install -r requirements.txt`


## Préparation des Bases de Données

### Neo4j
1. Installez Neo4j Desktop si ce n'est pas déjà fait
2. Créez une nouvelle base de données ou utilisez une existante
3. Dans Neo4j Browser, accédez à la section "Movies" dans les guides de démarrage rapide
4. Exécutez le script de création de la base de données Movies fourni par Neo4j
5. Vérifiez que les données sont bien importées avec la requête :
```cypher
MATCH (m:Movie) RETURN m LIMIT 10
```

### MongoDB
1. Importez le jeu de données dans votre base MongoDB :
   -  MongoDB Atlas :
     - Accédez à votre cluster
     - Cliquez sur "..." puis "Load Sample Dataset"
   -MongoDB en local :
     - Téléchargez le jeu de données 
     -  mongoimport pour importer les données

## Lancement

Lancer l'API : 
```bash
`python -m uvicorn main:app --reload`
```

L'API sera accessible à l'adresse : http://127.0.0.1:8000
La documentation OpenAPI sera disponible à : http://127.0.0.1:8000/docs

## API Endpoints

### MongoDB Endpoints (`/mongodb`)

#### GET `/`
- Description : Liste les 10 premiers films
- Réponse : Liste des films avec leurs détails

#### GET `/search`
- Description : Recherche des films par nom ou acteur
- Paramètres de requête : 
  - `movie_name` (optionnel) : Titre du film
  - `actor_name` (optionnel) : Nom de l'acteur
- Réponse : Liste des films correspondants aux critères

#### PUT `/update/{movie_name}`
- Description : Met à jour les informations d'un film
- Paramètres : 
  - `movie_name` : Titre du film à mettre à jour
- Corps de la requête : Objet `UpdateMovieModel` avec les champs à mettre à jour

### Neo4j Endpoints (`/neo4j`)

#### GET `/users_rated`
- Description : Liste les utilisateurs ayant évalué un film spécifique
- Paramètres de requête :
  - `movie_name` : Titre du film
- Réponse : Liste des utilisateurs et leurs évaluations

#### GET `/user_ratings`
- Description : Obtient les statistiques d'évaluation d'un utilisateur
- Paramètres de requête :
  - `user_name` : Nom de l'utilisateur
- Réponse : Statistiques d'évaluation de l'utilisateur

### Common Endpoints (`/common`)

#### GET `/common_movies`
- Description : Compte le nombre de films communs entre MongoDB et Neo4j
- Réponse : Nombre de films communs

## Structure des Données

### MongoDB Movie Schema
Le schéma des films dans MongoDB comprend les champs suivants (tous optionnels sauf indiqué) :
- plot
- genres (array)
- runtime
- cast (array)
- poster
- title
- fullplot
- languages (array)
- released
- directors (array)
- rated
- awards (object)
- year
- imdb (object)
- countries (array)
- type
- tomatoes (object)
- num_mflix_comments
