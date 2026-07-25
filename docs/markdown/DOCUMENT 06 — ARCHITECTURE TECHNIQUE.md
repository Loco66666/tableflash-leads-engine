# **DOCUMENT 06 --- ARCHITECTURE TECHNIQUE**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification technique\
Produit : TableFlash Leads Engine\
Type : Outil interne stratégique d\'acquisition commerciale**

# **06.1 --- Introduction**

Ce document définit l\'architecture technique de TFLE.

L\'objectif est de construire une plateforme :

- fiable ;

- maintenable ;

- évolutive ;

- sécurisée ;

- capable d\'automatiser des volumes importants d\'analyses.

La priorité n\'est pas de créer une infrastructure complexe dès le
départ, mais de construire une base professionnelle permettant
d\'évoluer progressivement.

# **06.2 --- Principes techniques fondamentaux**

Avant de choisir les technologies, TFLE doit respecter plusieurs
principes.

## **Principe 1 --- Modularité**

Chaque grande fonction doit être indépendante.

Exemple :

Scraping

≠

Analyse IA

≠

CRM

≠

Dashboard

Une évolution d\'un module ne doit pas casser les autres.

## **Principe 2 --- API First**

Tous les composants doivent communiquer via des interfaces clairement
définies.

Architecture :

Frontend

↓

API Backend

↓

Services métiers

↓

Base de données

## **Principe 3 --- Automatisation progressive**

Le système doit pouvoir fonctionner :

### **Version initiale**

Actions lancées manuellement.

↓

### **Version avancée**

Processus automatisés quotidiennement.

## **Principe 4 --- Données comme actif stratégique**

Les données collectées et analysées représentent une valeur importante.

Il faut donc prévoir :

- historique ;

- sauvegarde ;

- traçabilité ;

- qualité des données.

# **06.3 --- Architecture générale**

Architecture recommandée :

UTILISATEUR

\|

FRONTEND WEB

\|

API BACKEND

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\| \| \| \|

PostgreSQL Redis AI Engine Worker Queue

\| \|

\| \|

Data Layer Intelligence Layer

\|

Collection Services

\|

Sources publiques accessibles

# **06.4 --- Stack technique recommandée**

## **Frontend**

### **Technologie principale**

**React + Vite + TypeScript**

## **Pourquoi ?**

Avantages :

- rapide ;

- moderne ;

- grande communauté ;

- excellent pour dashboards ;

- compatible avec une architecture complexe.

## **Interface**

### **Framework UI**

Recommandation :

- Tailwind CSS

- composants réutilisables

- design system interne

## **Pages principales**

/dashboard

/restaurants

/restaurants/:id

/search

/scoring

/crm

/settings

# **06.5 --- Backend**

## **Technologie principale**

**Python + FastAPI**

## **Pourquoi Python ?**

Python est particulièrement adapté pour TFLE grâce à :

- scraping ;

- intelligence artificielle ;

- traitement de données ;

- automatisation.

## **Responsabilités Backend**

Le backend gère :

- authentification ;

- logique métier ;

- API ;

- traitement des données ;

- communication avec IA ;

- gestion utilisateurs.

## **Architecture backend**

backend/

├── api/

│

├── authentication/

│

├── restaurants/

│

├── scraping/

│

├── analysis/

│

├── scoring/

│

├── ai/

│

├── crm/

│

└── analytics/

# **06.6 --- Base de données**

## **Technologie**

**PostgreSQL**

## **Pourquoi PostgreSQL ?**

Adapté pour :

- données relationnelles ;

- historique ;

- recherches complexes ;

- statistiques ;

- montée en charge.

# **Structure principale**

## **Table restaurants**

Contient :

id

name

address

city

postal_code

category

website

phone

created_at

## **Table contacts**

id

restaurant_id

email

phone

source

verified_at

## **Table analyses**

id

restaurant_id

analysis_type

result

created_at

## **Table scores**

id

restaurant_id

score

reasons

created_at

## **Table CRM**

id

restaurant_id

status

assigned_user

notes

updated_at

# **06.7 --- Cache et tâches asynchrones**

## **Technologie**

**Redis**

## **Utilisation**

Redis servira pour :

- cache ;

- files d\'attente ;

- tâches temporaires.

Exemple :

Analyse de 10 000 sites :

Sans queue :

Application bloquée

Avec queue :

10 000 tâches

↓

Workers

↓

Résultats progressifs

# **06.8 --- Système de workers**

## **Technologie recommandée**

Celery ou Dramatiq.

## **Rôle**

Exécuter les tâches longues :

- scraping ;

- analyse de sites ;

- calcul de scores ;

- génération IA.

Exemple :

Utilisateur lance :

\"Analyser Bayonne\"

↓

Création de 500 tâches

↓

Workers exécutent

↓

Résultats disponibles

# **06.9 --- Architecture scraping**

## **Objectif**

Collecter des informations publiques utiles.

## **Technologies**

### **Navigation web**

Playwright

### **Parsing HTML**

BeautifulSoup

### **Extraction données**

- analyse HTML ;

- regex contrôlées ;

- règles métier.

## **Pipeline scraping**

URL trouvée

↓

Chargement page

↓

Extraction informations

↓

Nettoyage

↓

Validation

↓

Stockage PostgreSQL

# **06.10 --- Analyse intelligente des sites**

Le module Website Intelligence analysera :

## **Présence digitale**

Détection :

- site ;

- HTTPS ;

- CMS ;

- structure.

## **Menu**

Détection :

- page menu ;

- PDF ;

- images ;

- menu interactif.

## **Services**

Détection :

- réservation ;

- commande ;

- livraison.

## **Technologie possible**

Combinaison :

- règles classiques ;

- analyse DOM ;

- IA.

# **06.11 --- Intelligence artificielle**

## **Objectif**

Créer une couche d\'analyse commerciale.

## **Fonctions IA**

### **1. Résumé restaurant**

Entrées :

Données restaurant

\+

Analyse web

\+

Score

Sortie :

Résumé commercial.

### **2. Argumentaire**

Création :

- angle d\'approche ;

- points forts ;

- opportunités.

### **3. Classification**

Catégories :

Excellent prospect

Bon prospect

Moyen

Faible

# **Stratégie IA recommandée**

Architecture hybride :

Règles déterministes

\+

IA générative

\+

Historique conversion

Pourquoi ?

Une IA seule peut être imprécise.

Les règles métier apportent une stabilité.

# **06.12 --- API interne**

## **Architecture REST**

Exemples :

## **Restaurants**

GET /restaurants

GET /restaurants/{id}

POST /restaurants

## **Analyse**

POST /analysis/start

GET /analysis/{id}

## **Scoring**

GET /score/{restaurant_id}

## **CRM**

PATCH /crm/status

# **06.13 --- Authentification et sécurité**

Même interne, TFLE doit être sécurisé.

## **Authentification**

Recommandation :

- JWT ;

- sessions sécurisées.

## **Gestion des rôles**

Exemple :

ADMIN

↓

COMMERCIAL

↓

ANALYSTE

## **Protection**

Mesures :

- variables d\'environnement ;

- secrets hors code ;

- chiffrement ;

- logs ;

- sauvegardes.

# **06.14 --- Déploiement**

## **Environnement**

Trois environnements :

Développement

↓

Test

↓

Production

# **Développement local**

Exemple :

Windows / Linux

Docker

PostgreSQL local

Redis local

# **Production**

Possibilités :

## **Option simple MVP**

- VPS ;

- Docker ;

- PostgreSQL ;

- sauvegardes automatiques.

## **Option évolutive**

Cloud :

- AWS ;

- Google Cloud ;

- Azure.

# **06.15 --- Dockerisation**

Chaque service doit être isolé.

Exemple :

docker-compose

├── frontend

├── backend

├── postgres

├── redis

└── worker

Avantages :

- installation simplifiée ;

- environnement identique ;

- déploiement facilité.

# **06.16 --- Monitoring**

Le système doit surveiller :

## **Application**

- erreurs ;

- temps de réponse ;

- disponibilité.

## **Scraping**

- taux d\'échec ;

- sites inaccessibles ;

- blocages.

## **IA**

- coûts ;

- erreurs ;

- qualité.

# **06.17 --- Tests**

## **Tests backend**

- logique métier ;

- API ;

- base de données.

## **Tests frontend**

- composants ;

- navigation ;

- formulaires.

## **Tests fonctionnels**

Exemple :

Scénario :

Recherche Bayonne

↓

Restaurant trouvé

↓

Analyse réalisée

↓

Score généré

↓

Fiche CRM créée

# **06.18 --- Stratégie d\'évolution technique**

## **Phase MVP**

Architecture simple :

React

\+

FastAPI

\+

PostgreSQL

\+

Workers

## **Phase V1**

Ajout :

- recherche avancée ;

- automatisations ;

- analytics.

## **Phase V2**

Ajout :

- agents IA spécialisés ;

- prédiction conversion ;

- intelligence marché.

# **06.19 --- Décision finale d\'architecture**

Architecture retenue :

Frontend :

React + TypeScript + Tailwind

Backend :

FastAPI Python

Database :

PostgreSQL

Queue :

Redis + Worker

Scraping :

Playwright

IA :

LLM + règles métier

Déploiement :

Docker

# **Conclusion Document 06**

L\'architecture technique de TFLE est conçue pour répondre à un objectif
précis :

> Construire un moteur interne capable de transformer des données
> publiques sur les restaurants en intelligence commerciale exploitable
> pour accélérer la croissance de TableFlash.

Le choix technique privilégie :

- rapidité de développement ;

- flexibilité ;

- maîtrise des coûts ;

- évolutivité ;

- compatibilité avec l\'IA.
