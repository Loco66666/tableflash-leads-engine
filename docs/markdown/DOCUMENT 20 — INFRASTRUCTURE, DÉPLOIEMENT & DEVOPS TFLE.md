# **DOCUMENT 20 --- INFRASTRUCTURE, DÉPLOIEMENT & DEVOPS TFLE**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Architecture technique + opérationnelle\
Module : Infrastructure, Cloud, CI/CD & Scalabilité\
Produit : TableFlash Leads Engine\
Usage : Interne uniquement pour TableFlash**

# **20.1 --- Introduction**

Le module **Infrastructure & DevOps** définit toute l\'architecture
nécessaire pour faire fonctionner TFLE de manière fiable.

Son rôle :

- héberger l\'application ;

- déployer les nouvelles versions ;

- exécuter les moteurs de scraping ;

- gérer les traitements IA ;

- surveiller les performances ;

- assurer la disponibilité du système.

La vision :

> Construire une infrastructure capable de fonctionner avec quelques
> centaines de restaurants analysés par semaine comme avec plusieurs
> centaines de milliers de prospects.

# **20.2 --- Objectifs infrastructure**

L\'infrastructure TFLE doit être :

## **Fiable**

Le système doit continuer à fonctionner sans intervention constante.

## **Évolutive**

Pouvoir augmenter les capacités :

- scraping ;

- IA ;

- stockage ;

- utilisateurs.

## **Sécurisée**

Respecter :

- accès contrôlés ;

- sauvegardes ;

- secrets protégés.

## **Maintenable**

Permettre :

- corrections rapides ;

- déploiements propres ;

- évolution progressive.

# **20.3 --- Architecture globale production**

UTILISATEURS

↓

FRONTEND

↓

API BACKEND

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

PostgreSQL

Redis Queue

Workers

Storage

AI Services

Scraping Engine

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

Monitoring

# **20.4 --- Environnements TFLE**

TFLE utilise trois environnements séparés.

# **ENVIRONNEMENT 1 --- Développement**

Objectif :

Créer et tester localement.

Utilisateurs :

Développeurs.

Exemple :

localhost

Base locale

Services simulés

# **ENVIRONNEMENT 2 --- Staging**

Objectif :

Tester avant production.

Utilisation :

- nouvelles fonctionnalités ;

- tests utilisateurs ;

- validation IA.

Architecture proche production.

# **ENVIRONNEMENT 3 --- Production**

Objectif :

Application réelle.

Contient :

- données prospects ;

- CRM ;

- IA ;

- scraping.

# **20.5 --- Architecture Frontend**

## **Technologie recommandée**

React + TypeScript

Responsabilités :

- interface TFLE ;

- dashboards ;

- CRM ;

- gestion utilisateurs.

Déploiement possible :

- Vercel ;

- Cloudflare Pages ;

- AWS Amplify.

Structure :

frontend/

├── components/

├── pages/

├── features/

├── hooks/

├── services/

└── permissions/

# **20.6 --- Architecture Backend**

Le backend est le centre logique.

Responsabilités :

- authentification ;

- API ;

- règles métier ;

- orchestration IA ;

- communication modules.

Technologies possibles :

## **Option A --- TypeScript**

Node.js

NestJS

Avantages :

- cohérent frontend/backend ;

- rapide développement.

## **Option B --- Python**

FastAPI

Avantages :

- excellent pour IA ;

- scraping ;

- data processing.

Architecture recommandée TFLE :

Frontend

↓

API Node/NestJS

↓

Services Python IA/Scraping

# **20.7 --- Architecture services**

TFLE est conçu en architecture modulaire.

TFLE PLATFORM

├── API Gateway

├── CRM Service

├── Scraping Service

├── AI Service

├── Scoring Service

├── Analytics Service

├── Notification Service

└── Auth Service

# **20.8 --- Service Scraping Engine**

Le scraping ne tourne pas directement dans l\'application.

Il utilise des workers.

Architecture :

API

↓

Queue

↓

Scraping Workers

↓

Database

Pourquoi ?

Parce que certaines tâches peuvent durer :

- quelques secondes ;

- plusieurs minutes ;

- plusieurs heures.

# **20.9 --- Système de files d\'attente (Queue)**

Technologie recommandée :

## **Redis + BullMQ**

ou

## **RabbitMQ**

Exemple :

Une tâche est créée :

{

\"type\":\"SCRAPE_CITY\",

\"location\":\"Bayonne\",

\"priority\":\"high\"

}

La queue distribue :

Worker 1

↓

Restaurants sites web

Worker 2

↓

Emails

Worker 3

↓

Validation

# **20.10 --- Workers TFLE**

Les workers sont des processus indépendants.

Types :

# **Scraping Worker**

Mission :

Collecter données.

# **Email Worker**

Mission :

Extraire et vérifier emails.

# **AI Worker**

Mission :

Analyser prospects.

# **Analytics Worker**

Mission :

Calculer statistiques.

# **Notification Worker**

Mission :

Envoyer alertes internes.

# **20.11 --- Gestion des tâches longues**

Certaines actions ne doivent jamais bloquer l\'utilisateur.

Mauvaise architecture :

Utilisateur

↓

Lance scraping 10 000 restaurants

↓

Application bloquée

Bonne architecture :

Utilisateur

↓

Création tâche

↓

Queue

↓

Worker

↓

Résultat disponible

# **20.12 --- Architecture Base de données**

Technologie :

PostgreSQL

Organisation :

Database TFLE

├── restaurants

├── contacts

├── crm

├── scoring

├── ai

├── analytics

└── security

# **20.13 --- Cache système**

Utilisation :

Redis

Stockage temporaire :

- sessions ;

- résultats fréquents ;

- files tâches ;

- limites API.

Exemple :

Dashboard demandé 100 fois :

Première fois :

Calcul PostgreSQL

Après :

Cache Redis

# **20.14 --- Stockage fichiers**

TFLE peut stocker :

- exports ;

- rapports ;

- documents IA ;

- captures analyse.

Solutions :

- AWS S3 ;

- Cloudflare R2 ;

- Supabase Storage.

Architecture :

Application

↓

Storage Service

↓

Bucket sécurisé

# **20.15 --- Déploiement CI/CD**

Objectif :

Automatiser les mises en production.

Pipeline :

Développeur

↓

Git Push

↓

Tests automatiques

↓

Build

↓

Déploiement staging

↓

Validation

↓

Production

# **20.16 --- Git Workflow**

Organisation recommandée :

main

↓

production

develop

↓

staging

feature/\*

↓

nouvelles fonctionnalités

Exemple :

feature/new-scoring-engine

↓

Pull Request

↓

Review

↓

Merge

# **20.17 --- Tests automatisés**

Avant déploiement :

## **Tests frontend**

Vérifier :

- composants ;

- navigation ;

- formulaires.

## **Tests backend**

Vérifier :

- API ;

- règles métier.

## **Tests scraping**

Vérifier :

- extraction ;

- nettoyage.

## **Tests IA**

Vérifier :

- formats ;

- garde-fous.

# **20.18 --- Conteneurisation Docker**

Recommandé pour services backend.

Architecture :

docker-compose.yml

services:

api

postgres

redis

worker

ai-service

Avantages :

- environnement identique ;

- déploiement simplifié ;

- isolation services.

# **20.19 --- Monitoring système**

TFLE doit surveiller :

## **Application**

- erreurs ;

- temps réponse ;

- disponibilité.

## **Infrastructure**

- CPU ;

- RAM ;

- stockage ;

- réseau.

## **Workers**

- tâches réussies ;

- tâches échouées ;

- temps traitement.

# **Outils possibles :**

- Sentry ;

- Grafana ;

- Prometheus ;

- Datadog.

# **20.20 --- Monitoring métier**

Important :

Surveiller aussi les performances commerciales.

Exemples :

Nombre restaurants analysés

Nombre emails trouvés

Nombre prospects qualifiés

Nombre conversions

# **20.21 --- Gestion des erreurs**

Chaque service doit gérer ses erreurs.

Exemple scraping :

Erreur site inaccessible

↓

Retry automatique

↓

Nouvelle tentative

↓

Échec enregistré

# **20.22 --- Système Retry**

Pour tâches temporaires :

Exemple :

Tentative 1 :

Échec.

↓

Attente 5 minutes.

↓

Tentative 2.

↓

Tentative 3.

Après :

FAILED

\+

raison erreur

# **20.23 --- Scalabilité**

## **Phase MVP**

Architecture simple :

1 serveur

\+

PostgreSQL

\+

Workers limités

## **Phase V1**

Séparation :

Frontend

Backend

Workers

Database

## **Phase V2**

Architecture cloud complète :

Cluster

Workers multiples

Auto scaling

Data warehouse

# **20.24 --- Gestion des coûts infrastructure**

Le système doit suivre :

- coût serveur ;

- coût IA ;

- stockage ;

- APIs externes.

Dashboard :

Coût mensuel TFLE

€

Répartition :

IA : 60%

Serveurs : 25%

API : 15%

# **20.25 --- Sauvegardes**

Politique :

Base :

Backup quotidien

Fichiers :

Backup hebdomadaire

Configuration :

Versionnée Git

# **20.26 --- Disaster Recovery**

En cas de problème :

Processus :

Incident

↓

Isolation

↓

Restauration backup

↓

Validation

↓

Retour production

Objectifs :

## **RPO**

Perte maximale données acceptable.

Exemple :

24 heures.

## **RTO**

Temps restauration.

Exemple :

4 heures.

# **20.27 --- Sécurité DevOps**

Protection :

Secrets :

Variables environnement

Secret Manager

Accès serveur :

- clés SSH ;

- MFA ;

- permissions limitées.

Logs :

- centralisés ;

- protégés.

# **20.28 --- Architecture recommandée finale**

USERS

↓

VERCEL / FRONTEND

↓

API BACKEND

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

PostgreSQL

Redis

Workers

AI Services

Scrapers

Storage

Analytics

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

Monitoring + Logs

# **20.29 --- MVP Infrastructure**

Obligatoire :

✅ Frontend déployé.

✅ Backend API.

✅ PostgreSQL.

✅ Worker scraping.

✅ Queue Redis.

✅ CI/CD simple.

✅ Monitoring erreurs.

# **20.30 --- Version 1**

Ajouts :

- Docker complet ;

- staging automatique ;

- monitoring avancé ;

- scaling workers.

# **20.31 --- Version 2**

Vision :

Infrastructure autonome.

L\'IA peut :

- prévoir charge serveur ;

- optimiser coûts ;

- détecter anomalies ;

- proposer améliorations.

# **Conclusion Document 20**

L\'infrastructure TFLE doit être pensée comme une véritable plateforme
SaaS interne.

La règle fondamentale :

> Séparer l\'interface utilisateur, les traitements lourds,
> l\'intelligence artificielle et les données afin de pouvoir évoluer
> sans reconstruire le système.

Avec cette architecture, TFLE peut commencer comme un outil interne
simple pour TableFlash et évoluer vers une plateforme commerciale de
prospection intelligente capable de traiter des milliers de restaurants
