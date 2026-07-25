# **DOCUMENT 34 --- SPRINT 1 TFLE COMPLET**

# **Tickets détaillés, prompts Claude Code par tâche, critères de validation & commandes exactes**

**Version : 1.0\
Statut : Guide d\'exécution premier sprint\
Module : Development Execution\
Produit : TableFlash Leads Engine (TFLE)\
Durée estimée : 7 jours\
Objectif : Obtenir un premier prototype TFLE fonctionnel localement**

# **34.1 --- Objectif du Sprint 1**

Le Sprint 1 ne cherche pas à construire les fonctionnalités
commerciales.

Il doit construire le socle technique.

À la fin du sprint, TFLE doit posséder :

Repository Git propre

↓

Frontend React fonctionnel

↓

Backend FastAPI fonctionnel

↓

Base PostgreSQL connectée

↓

Architecture modulaire

↓

Authentification initiale

↓

Dashboard vide prêt à évoluer

# **34.2 --- Résultat attendu fin Sprint 1**

Version :

TFLE v0.1.0

Capable de :

✅ démarrer localement\
✅ communiquer frontend/backend\
✅ utiliser PostgreSQL\
✅ gérer un utilisateur interne\
✅ afficher une interface TableFlash\
✅ respecter l\'architecture prévue

# **34.3 --- Organisation Sprint 1**

Durée :

7 jours

Découpage :

  ---------- ------------------
   **Jour**     **Objectif**

    Jour 1     Initialisation
                   projet

    Jour 2    Backend FastAPI

    Jour 3     Frontend React

    Jour 4    PostgreSQL + ORM

    Jour 5    Authentification

    Jour 6       Dashboard

    Jour 7   Tests + nettoyage
  ---------- ------------------

# **JOUR 1 --- INITIALISATION PROJET**

## **Objectif**

Créer une base professionnelle.

# **Ticket TFLE-001**

## **Création repository Git**

Priorité :

P0

## **Actions**

Créer :

tableflash-leads-engine

Structure :

tableflash-leads-engine/

├── frontend/

├── backend/

├── database/

├── docs/

├── tests/

└── README.md

## **Commandes**

cd C:\\Users\\courj\\Desktop

git clone https://github.com/Loco66666/tableflash-leads-engine.git

cd tableflash-leads-engine

Créer dossiers :

mkdir frontend

mkdir backend

mkdir database

mkdir docs

mkdir tests

Premier commit :

git add .

git commit -m \"chore: initialize TFLE structure\"

git push

# **Prompt Claude Code TFLE-001**

Tu es l\'architecte du projet TFLE.

Nous démarrons le Sprint 1.

Analyse uniquement la structure actuelle du repository.

Ne crée aucun code.

Retourne :

1\. Les dossiers présents

2\. Les problèmes éventuels

3\. Les recommandations avant développement

# **Critères validation**

✅ Repository créé\
✅ Structure présente\
✅ Premier push Git effectué

# **JOUR 2 --- INITIALISATION BACKEND FASTAPI**

## **Objectif**

Créer l\'API principale TFLE.

# **Ticket TFLE-010**

## **Création backend Python**

Priorité :

P0

Structure :

backend/

├── app/

│ ├── main.py

│ ├── config/

│ ├── api/

│ ├── models/

│ ├── services/

│ └── database/

├── requirements.txt

└── venv/

# **Commandes**

Entrer backend :

cd backend

Créer environnement :

python -m venv venv

Activation :

.\\venv\\Scripts\\activate

Installation :

pip install fastapi uvicorn python-dotenv

Créer requirements :

pip freeze \> requirements.txt

# **Premier fichier API**

Créer :

backend/app/main.py

Contenu :

from fastapi import FastAPI

app = FastAPI(

title=\"TFLE API\",

version=\"0.1.0\"

)

\@app.get(\"/health\")

def health_check():

return {

\"status\": \"ok\",

\"application\": \"TFLE\"

}

Démarrage :

uvicorn app.main:app \--reload

Test :

http://localhost:8000/health

# **Prompt Claude Code TFLE-010**

Implémente la fondation backend TFLE.

Contraintes :

\- Python FastAPI

\- architecture modulaire

\- aucune logique métier pour le moment

Crée uniquement :

\- structure app/

\- endpoint health

\- configuration minimale

Avant toute modification :

explique les fichiers concernés.

# **Critères validation**

✅ API démarre\
✅ Endpoint health répond\
✅ requirements.txt présent

Commit :

git add .

git commit -m \"feat(api): initialize FastAPI backend\"

git push

# **JOUR 3 --- INITIALISATION FRONTEND**

## **Objectif**

Créer l\'interface TFLE.

# **Ticket TFLE-020**

## **Création React TypeScript**

Priorité :

P0

Depuis racine :

npm create vite@latest frontend

Choisir :

React

TypeScript

Installation :

cd frontend

npm install

Démarrage :

npm run dev

Résultat :

localhost:5173

# **Structure souhaitée**

src/

├── components/

├── pages/

├── services/

├── hooks/

├── types/

└── utils/

# **Installer dépendances**

npm install react-router-dom

# **Prompt Claude Code TFLE-020**

Configure le frontend TFLE.

Objectifs :

\- React TypeScript

\- architecture par features

\- préparation dashboard

Ne crée pas encore de logique métier.

Crée uniquement :

\- structure dossiers

\- routing

\- layout principal

# **Critères validation**

✅ Frontend démarre\
✅ Routing configuré\
✅ Structure propre

Commit :

git add .

git commit -m \"feat(frontend): initialize React application\"

git push

# **JOUR 4 --- BASE DE DONNÉES POSTGRESQL**

## **Objectif**

Connecter TFLE à PostgreSQL.

# **Ticket TFLE-030**

## **Docker PostgreSQL**

Créer :

docker-compose.yml

Contenu :

services:

postgres:

image: postgres:latest

environment:

POSTGRES_DB: tfle

POSTGRES_USER: tfle

POSTGRES_PASSWORD: tfle_password

ports:

\- \"5432:5432\"

Lancer :

docker compose up -d

Vérifier :

docker ps

# **Backend ORM**

Installer :

pip install sqlalchemy psycopg2-binary alembic

Initialiser :

alembic init migrations

# **Prompt Claude Code TFLE-030**

Configure la couche database TFLE.

Objectifs :

\- PostgreSQL

\- SQLAlchemy

\- Alembic

Ne crée aucune table métier.

Crée seulement :

\- connexion DB

\- configuration

\- migrations

# **Critères validation**

✅ PostgreSQL tourne\
✅ Backend communique avec DB\
✅ Migration prête

Commit :

git add .

git commit -m \"feat(database): setup PostgreSQL layer\"

git push

# **JOUR 5 --- AUTHENTIFICATION**

## **Objectif**

Créer accès interne TFLE.

# **Ticket TFLE-040**

Créer :

Table :

users

Champs :

id

email

password_hash

role

created_at

Rôles :

ADMIN

COMMERCIAL

ANALYST

Fonctions :

- login ;

- session ;

- protection routes.

Installer :

pip install python-jose passlib bcrypt

# **Prompt Claude Code TFLE-040**

Ajoute une authentification interne TFLE.

Contraintes :

\- sécurité prioritaire

\- mots de passe hashés

\- JWT

\- architecture propre

Avant modification :

liste les fichiers impactés.

# **Critères validation**

✅ Création utilisateur\
✅ Connexion fonctionnelle\
✅ Route protégée

Commit :

git commit -am \"feat(auth): add internal authentication\"

git push

# **JOUR 6 --- DASHBOARD INITIAL**

## **Objectif**

Créer la première interface TFLE.

# **Ticket TFLE-050**

Route :

/dashboard

Afficher :

Cartes :

Restaurants trouvés

Prospects qualifiés

Essais actifs

Clients

Valeurs :

0

pour le moment.

Composants :

KpiCard

DashboardLayout

Sidebar

# **Prompt Claude Code TFLE-050**

Crée le dashboard initial TFLE.

Objectif :

Une interface professionnelle interne TableFlash.

Contraintes :

\- design simple

\- mobile compatible

\- composants réutilisables

Ne crée aucune donnée fictive commerciale.

Utilise uniquement des valeurs vides.

# **Critères validation**

✅ Dashboard accessible\
✅ Design cohérent\
✅ Aucun faux prospect affiché

Commit :

git add .

git commit -m \"feat(dashboard): create initial dashboard\"

git push

# **JOUR 7 --- TESTS ET FINALISATION**

## **Objectif**

Préparer Sprint 2.

# **Ticket TFLE-060**

## **Nettoyage code**

Vérifier :

- imports inutiles ;

- erreurs console ;

- fichiers inutilisés.

# **Ticket TFLE-061**

## **Documentation**

Mettre à jour :

README.md

Inclure :

Installation :

git clone

docker compose up

npm install

uvicorn

# **Ticket TFLE-062**

## **Tests**

Backend :

pytest

Frontend :

npm test

# **Prompt Claude Code Review finale**

Effectue une revue complète du Sprint 1 TFLE.

Analyse :

\- architecture

\- sécurité

\- qualité code

\- dette technique

\- préparation Sprint 2

Classe les problèmes :

P0 critique

P1 important

P2 amélioration

# **34.4 --- Definition of Done Sprint 1**

Le Sprint est terminé uniquement si :

## **Git**

✅ Repository propre\
✅ Historique clair\
✅ Commits organisés

## **Backend**

✅ FastAPI actif\
✅ Structure modulaire\
✅ PostgreSQL connecté

## **Frontend**

✅ React actif\
✅ Routing actif\
✅ Dashboard disponible

## **Sécurité**

✅ Variables environnement\
✅ Authentification initiale

## **Documentation**

✅ README complet\
✅ Architecture documentée

# **34.5 --- État attendu fin Sprint 1**

Arborescence :

tableflash-leads-engine

├── backend

│ └── FastAPI

│

├── frontend

│ └── React

│

├── database

│ └── PostgreSQL

│

├── docs

│ └── TFLE documentation

│

└── docker-compose.yml

# **34.6 --- Préparation Sprint 2**

Sprint suivant :

# **DOCUMENT 35 --- Sprint 2 TFLE : Module Restaurant Database & Lead Management**

Objectif :

Construire le premier vrai module métier :

Restaurant Discovery

↓

Restaurant Database

↓

Recherche

↓

Filtres

↓

Premiers Leads

Ce sera la première étape où TFLE commencera réellement à devenir un
outil commercial utilisable par TableFlash.
