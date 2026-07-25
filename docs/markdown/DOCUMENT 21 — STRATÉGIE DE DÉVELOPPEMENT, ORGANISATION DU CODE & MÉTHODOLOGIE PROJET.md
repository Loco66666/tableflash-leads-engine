# **DOCUMENT 21 --- STRATÉGIE DE DÉVELOPPEMENT, ORGANISATION DU CODE & MÉTHODOLOGIE PROJET**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification développement + organisation projet\
Module : Engineering Strategy & Software Development Lifecycle\
Produit : TableFlash Leads Engine\
Usage : Interne uniquement pour TableFlash**

# **21.1 --- Introduction**

Ce document définit la manière dont TFLE sera conçu, développé et
maintenu.

L\'objectif est d\'éviter les problèmes classiques des projets ambitieux
:

- code difficile à maintenir ;

- fonctionnalités ajoutées sans cohérence ;

- architecture qui bloque l\'évolution ;

- absence de documentation ;

- modifications risquées ;

- dette technique excessive.

La philosophie TFLE :

> Construire une plateforme professionnelle dès le départ, même si le
> premier utilisateur est uniquement TableFlash.

# **21.2 --- Principes de développement TFLE**

## **Principe 1 --- Modularité avant rapidité**

Chaque grande fonctionnalité doit être indépendante.

Exemple :

Mauvais :

Scraping + CRM + IA dans un seul fichier

Correct :

Scraping Service

CRM Service

AI Service

Scoring Service

# **Principe 2 --- Documentation avant complexité**

Chaque module doit expliquer :

- son rôle ;

- ses entrées ;

- ses sorties ;

- ses dépendances.

# **Principe 3 --- Code lisible**

Le code doit être compréhensible par :

- un développeur futur ;

- une IA de développement ;

- un collaborateur externe.

# **Principe 4 --- Sécurité par défaut**

Jamais :

- clés API dans le code ;

- accès ouverts ;

- données sensibles exposées.

# **Principe 5 --- Automatisation maximale**

Automatiser :

- tests ;

- déploiement ;

- validation ;

- documentation.

# **21.3 --- Architecture générale du projet**

TFLE suit une architecture monorepo.

Structure principale :

tableflash-leads-engine/

│

├── apps/

│

├── services/

│

├── packages/

│

├── infrastructure/

│

├── docs/

│

├── scripts/

│

└── tests/

# **21.4 --- Organisation complète des dossiers**

# **/apps**

Applications utilisateur.

apps/

├── web-dashboard/

└── admin-panel/

## **web-dashboard**

Interface principale TFLE.

Contient :

- CRM ;

- dashboards ;

- fiches restaurants ;

- IA.

Structure :

web-dashboard/

src/

├── components/

├── pages/

├── features/

├── hooks/

├── services/

├── stores/

├── types/

└── utils/

# **21.5 --- Organisation Frontend**

## **Components**

Composants réutilisables.

Exemple :

components/

├── Button

├── Modal

├── DataTable

├── ScoreCard

└── RestaurantCard

## **Features**

Organisation par domaine métier.

Exemple :

features/

├── restaurants/

├── crm/

├── scoring/

├── analytics/

└── ai/

Chaque feature possède :

feature/

├── components/

├── hooks/

├── api/

├── types/

└── utils/

# **21.6 --- Architecture Backend**

Structure :

services/

├── api/

├── scraping/

├── scoring/

├── ai/

├── analytics/

└── notifications/

# **API Service**

Responsabilité :

- routes HTTP ;

- authentification ;

- logique métier.

Structure :

api/

src/

├── controllers/

├── services/

├── repositories/

├── middleware/

├── validators/

└── models/

# **21.7 --- Service Scraping**

Structure :

scraping/

src/

├── crawlers/

├── extractors/

├── parsers/

├── validators/

├── queues/

└── workers/

Responsabilités :

- récupération données ;

- extraction ;

- nettoyage.

# **21.8 --- Service IA**

Structure :

ai/

src/

├── agents/

├── prompts/

├── memory/

├── rag/

├── models/

└── evaluations/

Exemple :

agents/

├── discovery_agent

├── scoring_agent

├── sales_agent

└── crm_agent

# **21.9 --- Service Scoring**

Structure :

scoring/

src/

├── rules/

├── calculators/

├── models/

├── explanations/

└── tests/

# **21.10 --- Base de données**

Organisation :

database/

├── migrations/

├── seeds/

├── schemas/

└── backups/

Les migrations doivent être obligatoires.

Jamais modifier directement une base production.

# **21.11 --- Gestion Git**

TFLE utilise Git comme source de vérité.

# **Branches principales**

main

↓

Production

develop

↓

Staging

feature/\*

↓

Développement

# **21.12 --- Workflow Git**

Processus :

Nouvelle fonctionnalité

↓

Création branche

↓

Développement

↓

Tests

↓

Pull Request

↓

Review

↓

Merge

↓

Déploiement

Exemple :

git checkout develop

git checkout -b feature/lead-scoring-v2

# **21.13 --- Convention des commits**

Format :

TYPE: description

Types :

## **feat**

Nouvelle fonctionnalité.

Exemple :

feat: add restaurant scoring engine

## **fix**

Correction bug.

fix: repair email validator

## **docs**

Documentation.

docs: update API documentation

## **refactor**

Amélioration code.

refactor: simplify CRM pipeline

## **test**

Ajout tests.

test: add scoring tests

# **21.14 --- Pull Request Rules**

Une PR doit contenir :

## **Description**

Pourquoi cette modification ?

## **Impact**

Quels modules changent ?

## **Tests réalisés**

Comment vérifier ?

## **Risques**

Quels problèmes possibles ?

# **21.15 --- Méthodologie Agile TFLE**

Méthode :

## **Agile Scrum adaptée**

Sprint :

2 semaines

Chaque sprint possède :

- objectifs ;

- tâches ;

- validation ;

- rétrospective.

# **21.16 --- Organisation d\'un sprint**

## **Avant sprint**

Définition :

- fonctionnalités ;

- priorités ;

- estimation.

## **Pendant sprint**

Développement :

- tickets ;

- tests ;

- documentation.

## **Fin sprint**

Validation :

- démonstration ;

- correction ;

- décision suite.

# **21.17 --- Gestion des tickets**

Chaque fonctionnalité devient un ticket.

Format :

TFLE-001

Titre :

Créer système scoring restaurant

Description :

Objectif :

Calculer score prospect automatique.

Critères :

\- score 0-100

\- explication obligatoire

\- tests inclus

# **21.18 --- Priorités techniques**

# **P0 --- Obligatoire**

Bloquant pour fonctionnement.

Exemples :

- authentification ;

- base données ;

- scraping cœur ;

- CRM minimal.

# **P1 --- Important**

Améliore fortement produit.

Exemples :

- IA ;

- scoring avancé ;

- dashboards.

# **P2 --- Evolution**

Confort ou optimisation.

Exemples :

- automatisations avancées ;

- design amélioré ;

- optimisation performance.

# **21.19 --- Exemple roadmap tickets**

## **Sprint 1**

P0 :

Créer architecture projet

Configurer PostgreSQL

Créer authentification

## **Sprint 2**

P0 :

Créer restaurant database

Importer premiers prospects

Créer fiche restaurant

## **Sprint 3**

P0 :

Créer scraping engine

Créer extraction email

## **Sprint 4**

P1 :

Créer scoring engine

Créer dashboard qualification

# **21.20 --- Documentation développeur**

Chaque module possède :

README.md

Contenu :

- objectif ;

- installation ;

- utilisation ;

- architecture ;

- variables environnement.

Exemple :

\# Scraping Service

\## Objectif

Collecter données restaurants.

\## Installation

\## Configuration

\## API

# **21.21 --- Documentation API**

Toutes les routes doivent être documentées.

Format :

OpenAPI / Swagger.

Exemple :

GET /restaurants/{id}

Réponse :

{

\"id\":123,

\"name\":\"Chez Martin\"

}

# **21.22 --- Tests automatisés**

Objectif :

Éviter les régressions.

# **Tests unitaires**

Tester :

- fonctions ;

- calculs ;

- règles scoring.

Exemple :

Score restaurant sans QR

Résultat attendu :

+20 points

# **Tests intégration**

Tester :

- API ;

- base ;

- services.

# **Tests End-to-End**

Tester :

Parcours utilisateur complet.

Exemple :

Créer prospect

↓

Qualifier

↓

Ajouter CRM

↓

Créer tâche

# **21.23 --- Qualité du code**

Règles :

## **TypeScript strict**

Obligatoire.

## **Lint automatique**

Outils :

- ESLint ;

- Prettier.

## **Code review**

Toute modification importante est relue.

## **Pas de dette cachée**

Les problèmes connus sont documentés.

# **21.24 --- Gestion des variables environnement**

Structure :

.env.example

Exemple :

DATABASE_URL=

OPENAI_API_KEY=

REDIS_URL=

JWT_SECRET=

Jamais :

.env

dans Git.

# **21.25 --- Stratégie de déploiement**

Déploiement automatique :

Push Git

↓

Tests

↓

Build

↓

Deploy staging

↓

Validation

↓

Production

# **21.26 --- Documentation architecture**

Dossier :

docs/

├── architecture/

├── api/

├── database/

├── security/

├── ai/

└── decisions/

Chaque décision importante possède un ADR.

Exemple :

ADR-001

Pourquoi PostgreSQL ?

# **21.27 --- Architecture ADR**

Format :

Decision

Context

Options étudiées

Choix final

Conséquences

# **21.28 --- Gestion dette technique**

Table :

TECH-DEBT

Exemple :

  -------------- -------------- ------------
   **Problème**   **Priorité**   **Statut**

    Optimiser          P2          Prévu
     scraper                    

   Refactor CRM        P1         En cours
  -------------- -------------- ------------

# **21.29 --- Collaboration avec IA développeur**

TFLE est pensé pour être développé avec assistance IA.

Règles :

L\'IA doit toujours :

- lire architecture existante ;

- comprendre contexte ;

- proposer avant modifier ;

- éviter suppression massive.

Chaque modification IA doit fournir :

Fichiers modifiés

Pourquoi

Impact

Tests

# **21.30 --- Environnement développeur recommandé**

Minimum :

Windows / Linux / Mac

Node.js LTS

Python 3.12+

Docker

Git

VS Code

# **21.31 --- MVP développement**

Objectifs :

Créer une base propre :

✅ Monorepo.

✅ Frontend.

✅ Backend.

✅ PostgreSQL.

✅ Auth.

✅ Architecture modules.

✅ CI/CD simple.

# **21.32 --- V1 développement**

Ajouts :

- workers ;

- IA ;

- RAG ;

- analytics ;

- automatisations.

# **21.33 --- V2 développement**

Vision :

Architecture entreprise :

- microservices ;

- Kubernetes ;

- autoscaling ;

- agents IA autonomes.

# **21.34 --- Architecture finale TFLE**

TFLE PLATFORM

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Frontend

Backend API

Services métiers

Workers

IA Agents

Database

Infrastructure

Documentation

Tests

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\|

Production fiable

# **Conclusion Document 21**

La stratégie de développement TFLE repose sur une idée centrale :

> Construire une base suffisamment professionnelle pour permettre une
> croissance rapide sans devoir reconstruire le projet.

L\'objectif n\'est pas seulement de créer un scraper ou un CRM interne.

L\'objectif est de créer une véritable plateforme intelligente de
prospection restaurant, capable d\'évoluer avec TableFlash pendant
plusieurs années.
