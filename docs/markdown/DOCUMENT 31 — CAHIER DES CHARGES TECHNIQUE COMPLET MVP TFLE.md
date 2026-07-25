# **DOCUMENT 31 --- CAHIER DES CHARGES TECHNIQUE COMPLET MVP TFLE**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification technique exploitable développeur\
Module : Engineering Blueprint, Architecture & Development Execution\
Produit : TableFlash Leads Engine\
Usage : Interne uniquement pour TableFlash**

# **31.1 --- Objectif du document**

Ce document transforme toute la documentation stratégique TFLE
(Documents 00 à 30) en un cahier des charges technique permettant à un
développeur de construire le MVP.

Il définit :

- l\'architecture logicielle ;

- la stack technique ;

- l\'organisation du code ;

- les modules backend ;

- les composants frontend ;

- la base de données ;

- les API ;

- les services IA ;

- les workflows ;

- les tâches Git ;

- le planning de développement.

# **31.2 --- Objectif technique MVP**

Construire une application interne capable de :

Collecter des restaurants

↓

Stocker les données

↓

Nettoyer les informations

↓

Attribuer un score commercial

↓

Générer une analyse IA

↓

Créer une opportunité CRM

↓

Suivre la conversion TableFlash

# **31.3 --- Principes techniques fondamentaux**

## **Principe 1 --- Architecture modulaire**

Chaque fonctionnalité doit être indépendante.

Exemple :

Scraping Engine

≠

CRM

≠

IA

≠

Dashboard

## **Principe 2 --- Évolutivité**

Le MVP doit pouvoir évoluer vers :

- agents IA ;

- automatisation complète ;

- multi-utilisateurs ;

- volumes importants.

## **Principe 3 --- Simplicité opérationnelle**

Le système doit être maintenable par une petite équipe.

# **31.4 --- Stack technique finale recommandée**

## **Architecture générale**

TFLE

Frontend React

↓

Backend API

↓

PostgreSQL Database

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Scraping Workers

AI Services

Queue System

Storage

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **31.5 --- Frontend**

## **Technologies**

### **Framework**

React

### **Langage**

TypeScript

### **Styling**

Tailwind CSS

### **Routing**

React Router

### **State management**

MVP :

React Query + Context

### **UI Components**

Bibliothèque recommandée :

shadcn/ui

# **31.6 --- Backend**

## **Choix recommandé**

Python + FastAPI

Pourquoi :

- excellent pour IA ;

- excellent traitement données ;

- rapide ;

- documentation automatique API.

Architecture :

backend/

├── app/

│ ├── api/

│ ├── core/

│ ├── models/

│ ├── services/

│ ├── workers/

│ ├── ai/

│ └── scraping/

# **31.7 --- Base de données**

Choix :

PostgreSQL

ORM :

SQLAlchemy

Migration :

Alembic

# **31.8 --- Architecture dossiers complète**

Projet :

TFLE/

├── frontend/

│

├── backend/

│

├── workers/

│

├── ai/

│

├── scraping/

│

├── database/

│

├── docs/

│

├── tests/

│

└── docker/

# **31.9 --- Structure Frontend**

frontend/src/

├── app/

├── components/

├── pages/

├── features/

├── hooks/

├── services/

├── types/

├── utils/

└── styles/

# **31.10 --- Pages frontend MVP**

# **Dashboard**

Route :

/dashboard

Fonctions :

- KPI ;

- activité ;

- conversion.

# **Restaurants**

Route :

/restaurants

Fonctions :

- liste ;

- recherche ;

- filtres.

# **Restaurant détail**

Route :

/restaurants/:id

Affiche :

- informations ;

- score ;

- analyse IA ;

- historique.

# **Pipeline CRM**

Route :

/pipeline

Vue Kanban :

Nouveau

↓

Contacté

↓

Démo

↓

Essai

↓

Client

# **Tâches**

Route :

/tasks

# **Paramètres**

Route :

/settings

# **31.11 --- Composants frontend principaux**

## **RestaurantCard**

Affichage :

- nom ;

- ville ;

- score.

## **LeadScoreBadge**

Affiche :

Score 92/100

## **PipelineColumn**

Colonne CRM.

## **AIAnalysisPanel**

Affiche :

- résumé IA ;

- recommandation.

## **TaskItem**

Gestion actions commerciales.

# **31.12 --- Backend Modules**

Architecture :

backend/app/

├── restaurants/

├── leads/

├── scoring/

├── crm/

├── ai/

├── scraping/

├── analytics/

└── users/

# **31.13 --- Module Restaurants**

Responsabilité :

Gestion établissements.

Fonctions :

- création ;

- modification ;

- recherche ;

- suppression.

Service :

RestaurantService

# **31.14 --- Module Scraping Engine**

Responsabilité :

Collecte données publiques.

Architecture :

scraping/

├── collectors/

├── parsers/

├── cleaners/

├── validators/

└── exporters/

Pipeline :

Source

↓

Collector

↓

Parser

↓

Cleaner

↓

Database

# **31.15 --- Module Lead Scoring**

Responsabilité :

Notation prospects.

Service :

LeadScoringService

Entrée :

{

\"restaurant_type\":\"traditional\",

\"website\":false,

\"reviews\":350

}

Sortie :

{

\"score\":87,

\"priority\":\"high\"

}

# **31.16 --- Module IA**

Responsabilité :

Assistant commercial.

Architecture :

ai/

├── prompts/

├── agents/

├── models/

├── memory/

└── evaluation/

# **31.17 --- Prompt système IA principal**

Nom :

TFLE_SALES_ANALYST_V1

Prompt :

Tu es l\'assistant commercial interne de TableFlash.

Ton objectif est d\'analyser des restaurants

et d\'aider l\'équipe commerciale à identifier

les meilleures opportunités.

Tu dois :

\- analyser le potentiel digital ;

\- identifier les problèmes possibles ;

\- proposer un angle commercial ;

\- générer un message personnalisé.

Tu ne dois jamais inventer des informations.

Tu dois distinguer les faits des hypothèses.

# **31.18 --- Module CRM**

Tables :

- leads ;

- interactions ;

- tasks.

Services :

CRMService

PipelineService

TaskService

# **31.19 --- API Backend MVP**

Base URL :

/api/v1

# **Restaurants**

## **GET**

/restaurants

Liste restaurants.

## **POST**

/restaurants

Créer restaurant.

## **GET**

/restaurants/{id}

Détail.

# **Scoring**

POST :

/scoring/analyze/{restaurant_id}

Réponse :

{

\"score\":91,

\"reasons\":\[

\"Pas de commande digitale\",

\"Fort potentiel touristique\"

\]

}

# **IA**

POST :

/ai/analyze/{restaurant_id}

Réponse :

{

\"summary\":\"\",

\"argument\":\"\",

\"email\":\"\"

}

# **CRM**

GET :

/leads

PATCH :

/leads/{id}/status

POST :

/tasks

# **Dashboard**

GET :

/analytics/dashboard

Réponse :

{

\"restaurants\":5000,

\"qualified\":600,

\"trials\":12

}

# **31.20 --- Schéma PostgreSQL MVP**

# **Table restaurants**

CREATE TABLE restaurants (

id UUID PRIMARY KEY,

name TEXT NOT NULL,

address TEXT,

city TEXT,

phone TEXT,

email TEXT,

website TEXT,

source TEXT,

created_at TIMESTAMP

);

# **Table leads**

CREATE TABLE leads (

id UUID PRIMARY KEY,

restaurant_id UUID,

score INTEGER,

status TEXT,

priority TEXT,

created_at TIMESTAMP

);

# **Table interactions**

CREATE TABLE interactions (

id UUID PRIMARY KEY,

lead_id UUID,

type TEXT,

content TEXT,

created_at TIMESTAMP

);

# **Table ai_analysis**

CREATE TABLE ai_analysis (

id UUID PRIMARY KEY,

restaurant_id UUID,

summary TEXT,

recommendation TEXT,

created_at TIMESTAMP

);

# **Table tasks**

CREATE TABLE tasks (

id UUID PRIMARY KEY,

lead_id UUID,

title TEXT,

status TEXT,

due_date DATE

);

# **31.21 --- Sécurité MVP**

Obligatoire :

- authentification ;

- rôles utilisateurs ;

- HTTPS ;

- variables environnement ;

- logs.

Variables :

.env

DATABASE_URL=

AI_API_KEY=

SECRET_KEY=

# **31.22 --- Git Workflow**

Branches :

main

↓

develop

↓

feature/\*

Exemple :

feature/scoring-engine

Commit :

Format :

feat:

fix:

docs:

refactor:

Exemple :

feat: add restaurant scoring system

# **31.23 --- CI/CD MVP**

Pipeline :

Push GitHub

↓

Tests

↓

Build

↓

Deploy

Tests automatiques :

- backend ;

- frontend ;

- API.

# **31.24 --- Tests MVP**

## **Backend**

Tests :

- création restaurant ;

- scoring ;

- CRM.

## **Frontend**

Tests :

- navigation ;

- formulaires ;

- affichage données.

## **IA**

Tests :

- qualité réponses ;

- absence hallucination.

# **31.25 --- Planning développement jour par jour**

## **Semaine 1**

### **Jour 1**

- création repository ;

- configuration Docker ;

- PostgreSQL.

### **Jour 2**

- architecture backend ;

- connexion DB.

### **Jour 3**

- structure frontend ;

- routing.

### **Jour 4**

- authentification.

### **Jour 5**

- premier dashboard.

# **Semaine 2**

### **Jour 6-7**

Module restaurants.

### **Jour 8-9**

Recherche + filtres.

### **Jour 10**

Tests.

# **Semaine 3**

Scraping Engine.

Jour 11-13 :

- collectors ;

- parsing ;

- import.

Jour 14-15 :

- nettoyage données.

# **Semaine 4**

Scoring.

Jour 16-18 :

- règles scoring ;

- interface score.

Jour 19-20 :

- tests.

# **Semaine 5**

IA.

Jour 21-25 :

- prompts ;

- API IA ;

- analyses.

# **Semaine 6**

CRM.

Jour 26-30 :

- pipeline ;

- tâches ;

- historique.

# **Semaine 7**

Dashboard final.

Jour 31-35 :

- KPI ;

- graphiques ;

- optimisation.

# **Semaine 8**

Validation MVP.

Jour 36-40 :

- tests complets ;

- corrections ;

- déploiement.

# **31.26 --- Définition MVP terminé**

Le MVP est validé lorsque :

✅ Application fonctionnelle\
✅ Restaurants importés automatiquement\
✅ Score automatique disponible\
✅ Analyse IA générée\
✅ Pipeline CRM opérationnel\
✅ Dashboard actif\
✅ Premier cycle commercial réalisé

# **31.27 --- Évolution après MVP**

V1 :

Ajout :

- automatisation emails ;

- agents IA ;

- mémoire ;

- enrichissement avancé.

V2 :

Ajout :

- équipe IA autonome ;

- prédiction ;

- multi-marchés.

# **Conclusion Document 31**

Le MVP TFLE doit être construit comme une véritable application
professionnelle interne.

L\'ordre de construction recommandé :

Données

↓

Organisation

↓

Qualification

↓

Intelligence

↓

Commercial

↓

Automatisation

La priorité absolue :

Créer rapidement une première version utilisée réellement par
TableFlash.

La technologie doit servir un objectif unique :

> Transformer la recherche de restaurants en une machine d\'acquisition
> commerciale mesurable et scalable.
