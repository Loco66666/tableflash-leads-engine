# **DOCUMENT 12 --- PLAN DE DÉVELOPPEMENT TECHNIQUE SPRINT PAR SPRINT**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Plan d\'exécution développement\
Produit : TableFlash Leads Engine\
Méthode : Développement agile par sprints**

# **12.1 --- Introduction**

Ce document transforme le PRD TFLE en plan de construction concret.

Objectif :

> Passer d\'une documentation produit complète à une application
> fonctionnelle utilisée quotidiennement par TableFlash.

Le développement est organisé en sprints progressifs.

Chaque sprint doit produire :

- une fonctionnalité utilisable ;

- des tests ;

- une validation métier ;

- une base solide pour la suite.

# **12.2 --- Stratégie générale de développement**

## **Approche retenue**

Construction par couches :

Fondations techniques

↓

Gestion données

↓

Collecte restaurants

↓

Analyse intelligente

↓

Qualification

↓

CRM

↓

Automatisation

↓

IA avancée

# **12.3 --- Stack technique finale**

## **Frontend**

React

\+

TypeScript

\+

Vite

\+

Tailwind CSS

\+

React Query

\+

React Router

## **Backend**

Python

\+

FastAPI

\+

SQLAlchemy

\+

Pydantic

## **Base de données**

PostgreSQL

## **Tâches asynchrones**

Redis

\+

Celery / Dramatiq

## **Scraping**

Playwright

\+

BeautifulSoup

## **Infrastructure**

Docker

\+

Docker Compose

\+

CI/CD

# **12.4 --- Organisation du projet**

Structure recommandée :

tableflash-leads-engine/

│

├── frontend/

│

│ ├── src/

│ │

│ ├── components/

│ ├── pages/

│ ├── hooks/

│ ├── services/

│ └── styles/

│

│

├── backend/

│

│ ├── app/

│ │

│ ├── api/

│ ├── models/

│ ├── schemas/

│ ├── services/

│ ├── workers/

│ └── core/

│

│

├── database/

│

│ ├── migrations/

│

│

├── docker/

│

├── tests/

│

└── docs/

# **12.5 --- Sprint 0 : Préparation projet**

## **Durée**

1 semaine

# **Objectif**

Créer une base professionnelle.

# **Tickets**

## **TFLE-001 --- Initialisation repository**

Priorité :

P0

Tâches :

- création Git ;

- branches ;

- règles commit ;

- README.

Critères :

✅ Projet clonable.

✅ Documentation installation disponible.

# **TFLE-002 --- Configuration Docker**

P0

Créer :

frontend

backend

postgres

redis

Critères :

✅ Tous les services démarrent.

# **TFLE-003 --- Environnement développement**

P0

Configurer :

- variables environnement ;

- fichiers .env ;

- scripts lancement.

# **Résultat Sprint 0**

Une base prête pour développer.

# **SPRINT 1 --- Authentification + Base application**

## **Durée**

2 semaines

# **Objectif**

Créer le squelette TFLE.

# **Backend**

## **TFLE-010 --- API FastAPI initiale**

P0

Créer :

/api/v1

## **TFLE-011 --- Système utilisateur**

P0

Fonctions :

- inscription interne ;

- connexion ;

- JWT.

## **TFLE-012 --- Modèle User PostgreSQL**

Créer table :

users

# **Frontend**

## **TFLE-013 --- Layout application**

P0

Créer :

- sidebar ;

- navigation ;

- pages vides.

## **TFLE-014 --- Page connexion**

P0

Critères Sprint 1 :

✅ Connexion fonctionnelle.

✅ Dashboard accessible.

# **SPRINT 2 --- Gestion restaurants**

## **Durée**

2 semaines

# **Objectif**

Créer le cœur de données.

# **Backend**

## **TFLE-020 --- Modèle Restaurant**

P0

Créer :

restaurants

## **TFLE-021 --- API restaurants**

P0

Routes :

GET /restaurants

GET /restaurants/:id

POST /restaurants

PATCH /restaurants/:id

# **Frontend**

## **TFLE-022 --- Liste prospects**

P0

Créer :

- tableau ;

- recherche ;

- filtres.

## **TFLE-023 --- Fiche restaurant**

P0

Créer :

- informations générales ;

- historique.

# **Validation**

✅ Création restaurant.

✅ Modification.

✅ Recherche.

# **SPRINT 3 --- Discovery Engine**

## **Durée**

3 semaines

# **Objectif**

Trouver automatiquement des restaurants.

# **Backend**

## **TFLE-030 --- Système de recherche**

P0

Créer :

Discovery Service

## **TFLE-031 --- Gestion jobs**

P0

Créer :

scraping_jobs

## **TFLE-032 --- Premier collecteur**

P0

Fonctions :

- récupération restaurants ;

- nettoyage ;

- stockage.

# **Frontend**

## **TFLE-033 --- Interface recherche**

P0

Permettre :

- ville ;

- catégorie ;

- rayon.

## **TFLE-034 --- Progression recherche**

P1

Afficher :

350 trouvés

120 analysés

# **Validation**

✅ Une recherche crée des prospects.

# **SPRINT 4 --- Analyse digitale**

## **Durée**

3 semaines

# **Objectif**

Comprendre la présence numérique.

# **Backend**

## **TFLE-040 --- Website Analyzer**

P0

Détecter :

- site ;

- menu ;

- QR ;

- réservation.

## **TFLE-041 --- Stockage analyse**

P0

Créer :

website_analysis

# **Frontend**

## **TFLE-042 --- Vue analyse digitale**

P0

Afficher :

- résultats ;

- opportunités.

# **Validation**

✅ Un restaurant possède une analyse.

# **SPRINT 5 --- Lead Scoring**

## **Durée**

2 semaines

# **Objectif**

Classer automatiquement les prospects.

# **Backend**

## **TFLE-050 --- Moteur scoring**

P0

Créer règles :

Pas QR

+15

Menu PDF

+10

## **TFLE-051 --- Historique score**

P0

Créer :

lead_scores

# **Frontend**

## **TFLE-052 --- Affichage score**

P0

Ajouter :

- badge ;

- explication.

# **Validation**

✅ Score calculé automatiquement.

✅ Raisons visibles.

# **SPRINT 6 --- Intelligence IA**

## **Durée**

3 semaines

# **Objectif**

Ajouter la couche intelligence commerciale.

# **Backend**

## **TFLE-060 --- Service IA**

P0

Fonctions :

- résumé ;

- opportunité ;

- arguments.

## **TFLE-061 --- Historisation IA**

P0

Créer :

ai_analysis

# **Frontend**

## **TFLE-062 --- Carte IA**

P0

Afficher :

- résumé ;

- recommandations.

# **Validation**

✅ Chaque prospect prioritaire possède une analyse IA.

# **SPRINT 7 --- CRM commercial**

## **Durée**

3 semaines

# **Objectif**

Transformer les prospects en clients.

# **Backend**

Créer :

crm_pipeline

activities

tasks

# **API**

Routes :

PATCH /crm/status

POST /activities

POST /tasks

# **Frontend**

Créer :

- Kanban CRM ;

- timeline ;

- tâches.

# **Validation**

✅ Suivi complet d\'un prospect.

# **SPRINT 8 --- Dashboard + Analytics**

## **Durée**

2 semaines

# **Objectif**

Mesurer l\'activité.

Fonctions :

- KPI ;

- conversion ;

- zones performantes.

# **Validation**

Dashboard réel utilisable.

# **SPRINT 9 --- Automatisation**

## **Durée**

3 à 4 semaines

# **Objectif**

Réduire les actions manuelles.

Ajout :

- recherches planifiées ;

- analyses automatiques ;

- alertes.

Exemple :

Chaque matin :

Nouvelle recherche

↓

Analyse

↓

Score

↓

Liste prioritaire

# **SPRINT 10 --- Optimisation production**

## **Durée**

2 semaines

# **Objectif**

Préparer usage quotidien.

Tâches :

## **Performance**

- cache ;

- optimisation requêtes.

## **Sécurité**

- audit ;

- permissions.

## **Qualité**

- tests ;

- logs.

# **12.6 --- Priorités globales**

## **P0 --- Obligatoire MVP**

Authentification

Restaurants

Recherche

Analyse

Scoring

IA simple

CRM basique

Dashboard

## **P1 --- Important V1**

Automatisation

Analytics avancés

Messages IA

Historique complet

## **P2 --- Vision future**

Agents IA

Prédiction conversion

Veille marché

Assistant commercial

# **12.7 --- Stratégie Git**

Organisation branches :

main

↓

develop

↓

feature/\*

Exemple :

feature/discovery-engine

feature/scoring

feature/crm

# **Convention commit**

Format :

feat: add restaurant scoring engine

fix: correct CRM status update

docs: update API specification

# **12.8 --- Stratégie tests**

Chaque fonctionnalité doit avoir :

## **Tests unitaires**

Exemple :

Calcul score.

## **Tests API**

Exemple :

Création restaurant.

## **Tests utilisateur**

Exemple :

Parcours complet :

Recherche

↓

Restaurant trouvé

↓

Score

↓

CRM

# **12.9 --- Mise en production**

## **Environnement**

Trois niveaux :

LOCAL

↓

STAGING

↓

PRODUCTION

# **Déploiement production**

Conteneurs :

Frontend

Backend

Database

Workers

Redis

# **Sauvegardes**

Obligatoires :

- base quotidienne ;

- stockage sécurisé ;

- restauration testée.

# **12.10 --- Critères de réussite MVP**

TFLE MVP est considéré terminé lorsque :

✅ TableFlash peut importer/trouver des restaurants.

✅ Les restaurants sont analysés automatiquement.

✅ Chaque restaurant reçoit un score.

✅ L\'IA produit une recommandation.

✅ Les prospects peuvent être suivis dans un CRM.

✅ Les statistiques commerciales sont visibles.

# **12.11 --- Vision finale développement**

La construction suit cette logique :

Sprint 0-2

Fondations

↓

Sprint 3-5

Collecte + Qualification

↓

Sprint 6-8

Intelligence + Vente

↓

Sprint 9-10

Automatisation + Production

# **Conclusion Document 12**

Le plan de développement TFLE est conçu pour éviter le piège classique
des projets ambitieux :

> Construire beaucoup de fonctionnalités avant d\'avoir une vraie
> utilité.

La stratégie retenue :

1.  Construire un outil simple mais immédiatement utile à TableFlash.

2.  Collecter des données réelles.

3.  Améliorer progressivement l\'intelligence.

4.  Transformer TFLE en avantage commercial durable.
