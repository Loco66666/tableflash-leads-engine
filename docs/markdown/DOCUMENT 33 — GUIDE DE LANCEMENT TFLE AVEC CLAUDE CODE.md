# **DOCUMENT 33 --- GUIDE DE LANCEMENT TFLE AVEC CLAUDE CODE**

# **Installation locale, création repository, configuration environnement, premier sprint & commandes exactes**

**Version : 1.0\
Statut : Guide opérationnel développeur\
Module : Initialisation Projet & Environnement Local\
Produit : TableFlash Leads Engine (TFLE)\
Usage : Interne uniquement pour TableFlash**

# **33.1 --- Objectif du document**

Ce document explique comment démarrer concrètement le développement TFLE
depuis un PC Windows.

Objectif :

Passer de :

Documentation TFLE

à :

Projet Git fonctionnel

↓

Environnement local

↓

Premier commit

↓

Premier sprint développement

# **33.2 --- Environnement cible**

Configuration recommandée :

## **Système**

Windows 10 / Windows 11

## **Outils nécessaires**

  ------------ -------------------
   **Outil**     **Utilisation**

      Git         Gestion code

     GitHub        Repository

    VS Code          Éditeur

  Claude Code       Assistant
                  développement

    Node.js         Frontend

     Python          Backend

     Docker      Services locaux

   PostgreSQL     Base données
  ------------ -------------------

# **33.3 --- Vérification machine**

Avant installation :

Ouvrir PowerShell :

git \--version

Résultat attendu :

git version 2.x.x

Node :

node -v

Résultat :

v24.x.x

Python :

python \--version

Résultat :

Python 3.x

Docker :

docker \--version

Résultat :

Docker version xx

# **33.4 --- Création du repository GitHub**

Créer un repository :

Nom :

tableflash-leads-engine

Configuration :

Private Repository

Pourquoi :

TFLE contient :

- stratégie commerciale ;

- données prospects ;

- prompts IA ;

- logique interne.

Structure initiale :

tableflash-leads-engine/

README.md

.gitignore

docs/

frontend/

backend/

# **33.5 --- Clonage local**

Choisir emplacement :

Exemple :

cd C:\\Users\\courj\\Desktop

Cloner :

git clone https://github.com/Loco66666/tableflash-leads-engine.git

Entrer dans dossier :

cd tableflash-leads-engine

Vérifier :

git status

Résultat :

On branch main

nothing to commit

# **33.6 --- Installation Claude Code**

Installation globale :

npm install -g \@anthropic-ai/claude-code

Vérification :

claude \--version

Connexion :

claude

Suivre authentification.

# **33.7 --- Initialisation Claude Code TFLE**

Dans le dossier projet :

claude

Premier prompt obligatoire :

Tu es l\'assistant développeur principal du projet TFLE.

Lis tous les documents présents dans /docs.

Ne crée aucun code pour le moment.

Analyse :

\- architecture prévue ;

\- stack technique ;

\- modules ;

\- risques techniques.

Retourne uniquement un rapport d\'analyse.

Objectif :

Faire comprendre le projet avant génération code.

# **33.8 --- Organisation documentation**

Créer :

docs/

Puis :

docs/

00-VISION.md

01-PROBLEME.md

02-PERSONAS.md

\...

31-CAHIER-TECHNIQUE.md

32-PLAN-IMPLEMENTATION.md

Claude devra toujours consulter :

docs/

avant modification.

# **33.9 --- Initialisation Backend**

Créer environnement Python :

mkdir backend

cd backend

Créer environnement virtuel :

python -m venv venv

Activation :

.\\venv\\Scripts\\activate

Installer dépendances :

pip install fastapi uvicorn sqlalchemy psycopg2 alembic python-dotenv

Créer :

backend/

app/

main.py

requirements.txt

Exporter :

pip freeze \> requirements.txt

# **33.10 --- Premier backend TFLE**

Créer :

backend/app/main.py

Code initial :

from fastapi import FastAPI

app = FastAPI(

title=\"TFLE API\",

version=\"0.1\"

)

\@app.get(\"/health\")

def health():

return {

\"status\": \"ok\",

\"project\": \"TFLE\"

}

Lancer :

uvicorn app.main:app \--reload

Tester :

Navigateur :

http://localhost:8000/health

Résultat :

{

\"status\":\"ok\",

\"project\":\"TFLE\"

}

# **33.11 --- Initialisation Frontend**

Retour racine :

cd ..

Créer React :

npm create vite@latest frontend

Choisir :

React

Puis :

TypeScript

Installer :

cd frontend

npm install

Tester :

npm run dev

Résultat :

localhost:5173

# **33.12 --- Installation Tailwind**

Dans frontend :

npm install tailwindcss \@tailwindcss/vite

Configurer selon version Vite.

Objectif :

Créer design system TFLE.

# **33.13 --- Configuration Docker**

À la racine :

Créer :

docker-compose.yml

Premier objectif :

Lancer PostgreSQL.

Structure :

services:

postgres:

image: postgres

environment:

POSTGRES_DB: tfle

POSTGRES_USER: tfle

POSTGRES_PASSWORD: password

ports:

\- \"5432:5432\"

Démarrage :

docker compose up -d

Vérifier :

docker ps

# **33.14 --- Variables environnement**

Créer :

.env

Exemple :

DATABASE_URL=postgresql://tfle:password@localhost:5432/tfle

AI_API_KEY=

SECRET_KEY=

Créer également :

.env.example

Sans secrets.

# **33.15 --- Premier Sprint TFLE**

## **Sprint 01 --- Fondation**

Durée :

7 jours.

Objectif :

Obtenir :

TFLE v0.1

Frontend

\+

Backend

\+

Database

\+

Git propre

# **Jour 1 --- Repository**

Tâches :

- GitHub créé ;

- clone local ;

- documentation installée.

Commit :

git add .

git commit -m \"chore: initialize TFLE project\"

git push

# **Jour 2 --- Backend**

Créer :

- FastAPI ;

- structure dossiers ;

- endpoint health.

Commit :

feat(api): initialize backend

# **Jour 3 --- Frontend**

Créer :

- React ;

- routing ;

- layout.

Commit :

feat(frontend): initialize application

# **Jour 4 --- Database**

Créer :

- PostgreSQL ;

- SQLAlchemy ;

- première migration.

Commit :

feat(database): setup postgres

# **Jour 5 --- Authentification simple**

Créer :

- utilisateur ;

- connexion ;

- protection routes.

Commit :

feat(auth): add authentication

# **Jour 6 --- Dashboard vide**

Créer :

Page :

/dashboard

Avec :

- cartes KPI ;

- layout.

Commit :

feat(dashboard): create base dashboard

# **Jour 7 --- Nettoyage**

Faire :

- tests ;

- documentation ;

- review.

Commit :

docs: update sprint 1 documentation

# **33.16 --- Premier prompt Claude Code développement**

Après installation :

Nous commençons le Sprint 1 TFLE.

Tu dois agir comme développeur senior.

Avant chaque modification :

1\. Explique le changement.

2\. Liste les fichiers concernés.

3\. Indique les risques.

4\. Attends validation.

Respecte strictement :

\- architecture Document 31 ;

\- tickets Document 32 ;

\- aucune modification inutile.

# **33.17 --- Règles d\'utilisation Claude Code**

Claude ne doit jamais :

❌ Supprimer un dossier complet\
❌ Réécrire toute l\'application\
❌ Modifier plusieurs modules sans raison\
❌ Installer une dépendance sans justification

Claude doit :

✅ Lire documentation\
✅ Proposer plan\
✅ Modifier progressivement\
✅ Tester après chaque étape

# **33.18 --- Workflow quotidien recommandé**

Chaque session :

## **Étape 1**

Lire état Git :

git status

## **Étape 2**

Demander analyse :

Analyse l\'état actuel du projet TFLE.

Dis-moi la prochaine tâche prioritaire.

## **Étape 3**

Développement.

## **Étape 4**

Tests.

## **Étape 5**

Commit.

# **33.19 --- Structure finale après Sprint 1**

Résultat attendu :

tableflash-leads-engine/

├── backend/

│ └── app/

│ └── main.py

├── frontend/

│ └── src/

├── docs/

├── docker-compose.yml

├── .env.example

└── README.md

# **33.20 --- Critères réussite Sprint 1**

Le sprint est validé si :

✅ Repository propre\
✅ Claude Code opérationnel\
✅ Frontend lancé\
✅ Backend lancé\
✅ PostgreSQL actif\
✅ Documentation intégrée\
✅ Premier déploiement local possible

# **33.21 --- Après Sprint 1**

Sprint 2 :

# **Base Restaurant Management**

Objectifs :

Créer :

- modèle Restaurant ;

- CRUD ;

- recherche ;

- interface liste.

# **Conclusion Document 33**

TFLE peut maintenant passer de la documentation à la construction
réelle.

La méthode recommandée :

Documentation

↓

Claude comprend le projet

↓

Architecture

↓

Petits tickets

↓

Code contrôlé

↓

Tests

↓

Evolution

Le point essentiel :

**Ne pas demander à Claude de \"créer TFLE\".**

Il faut lui faire construire :

- un ticket ;

- un module ;

- une fonctionnalité ;

- une validation à la fois.
