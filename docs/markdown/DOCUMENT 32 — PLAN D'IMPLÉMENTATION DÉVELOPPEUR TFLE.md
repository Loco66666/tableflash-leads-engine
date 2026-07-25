# **DOCUMENT 32 --- PLAN D\'IMPLÉMENTATION DÉVELOPPEUR TFLE**

# **Tickets Git, Backlog Détaillé, Architecture Fichiers Réelle & Prompts IA Développement**

**Version : 1.0\
Statut : Plan d\'exécution technique\
Module : Engineering Execution, AI-Assisted Development & Project
Management\
Produit : TableFlash Leads Engine (TFLE)\
Usage : Interne uniquement pour TableFlash**

# **32.1 --- Objectif du document**

Ce document transforme le cahier des charges technique du Document 31 en
un plan directement exploitable par :

- un développeur humain ;

- Claude Code ;

- Cursor ;

- GitHub Copilot ;

- autres assistants IA de développement.

L\'objectif est de supprimer l\'ambiguïté :

> Chaque tâche doit pouvoir devenir un ticket Git réalisable.

# **32.2 --- Méthode de développement TFLE**

TFLE sera construit selon une approche :

Architecture d\'abord

↓

Modules indépendants

↓

Petites fonctionnalités

↓

Tests

↓

Validation

↓

Déploiement

# **32.3 --- Organisation Git recommandée**

Repository :

tableflash-leads-engine

Branches :

main

│

├── develop

│

├── feature/\*

│

├── bugfix/\*

│

└── hotfix/\*

# **32.4 --- Convention des commits**

Format :

type(scope): description

Types :

feat nouvelle fonctionnalité

fix correction bug

refactor amélioration code

test ajout tests

docs documentation

chore maintenance

security sécurité

Exemples :

feat(scraping): add restaurant collector

feat(scoring): implement lead score engine

fix(crm): correct pipeline status update

# **32.5 --- Architecture finale des fichiers**

Structure complète :

tableflash-leads-engine/

│

├── frontend/

│

├── backend/

│

├── workers/

│

├── database/

│

├── docker/

│

├── ai/

│

├── scraping/

│

├── tests/

│

├── docs/

│

├── .env.example

├── docker-compose.yml

├── README.md

└── package.json

# **32.6 --- Frontend Architecture**

frontend/

src/

├── app/

│

│ ├── router.tsx

│ ├── providers.tsx

│

├── components/

│

│ ├── ui/

│ ├── layout/

│ └── common/

│

├── features/

│

│ ├── restaurants/

│ ├── leads/

│ ├── scoring/

│ ├── crm/

│ ├── dashboard/

│ └── ai/

│

├── pages/

│

├── hooks/

│

├── services/

│

├── types/

│

└── utils/

# **32.7 --- Backend Architecture**

backend/

app/

├── main.py

├── config/

│ ├── settings.py

│

├── database/

│ ├── connection.py

│ ├── migrations/

│

├── models/

│ ├── restaurant.py

│ ├── lead.py

│ ├── task.py

│

├── schemas/

│ ├── restaurant.py

│

├── api/

│ ├── routes/

│

├── services/

│ ├── restaurant_service.py

│ ├── scoring_service.py

│ ├── crm_service.py

│

├── ai/

│ ├── client.py

│ ├── prompts/

│

├── scraping/

│ ├── collectors/

│

└── workers/

# **32.8 --- Découpage développement MVP**

Le MVP est divisé en :

- 12 épics ;

- 60+ tickets ;

- 8 semaines.

# **EPIC 01 --- Initialisation Projet**

Priorité :

## **P0**

Objectif :

Créer la base technique.

## **Ticket TFLE-001**

### **Initialiser repository Git**

Tâches :

- créer repo ;

- README ;

- .gitignore ;

- conventions.

Critères validation :

✅ Repository propre\
✅ Premier commit effectué

## **Ticket TFLE-002**

### **Configuration Docker**

Créer :

docker-compose.yml

Services :

- PostgreSQL ;

- backend ;

- frontend.

Validation :

docker compose up

fonctionne.

## **Ticket TFLE-003**

### **Configuration environnements**

Créer :

.env.example

Variables :

DATABASE_URL

SECRET_KEY

AI_API_KEY

ENVIRONMENT

# **EPIC 02 --- Base Backend**

Priorité :

## **P0**

## **Ticket TFLE-010**

Créer application FastAPI.

Structure :

app/main.py

Validation :

Endpoint :

GET /health

Réponse :

{

\"status\":\"ok\"

}

## **Ticket TFLE-011**

Connexion PostgreSQL.

Créer :

- connection ;

- session ;

- migrations.

## **Ticket TFLE-012**

Installer ORM.

Créer modèles SQLAlchemy.

# **EPIC 03 --- Base Restaurant**

Priorité :

## **P0**

## **Ticket TFLE-020**

Créer modèle Restaurant.

Champs :

id

name

address

city

phone

email

website

source

created_at

## **Ticket TFLE-021**

API CRUD Restaurants.

Routes :

GET /restaurants

POST /restaurants

GET /restaurants/{id}

PUT /restaurants/{id}

DELETE /restaurants/{id}

## **Ticket TFLE-022**

Interface liste restaurants.

Composants :

RestaurantTable

RestaurantCard

SearchBar

# **EPIC 04 --- Discovery Engine**

Priorité :

## **P0**

Objectif :

Importer des restaurants.

Architecture :

scraping/

collector

↓

parser

↓

cleaner

↓

database

## **Ticket TFLE-030**

Créer système collector.

Interface :

class Collector:

def collect():

pass

## **Ticket TFLE-031**

Créer parser restaurant.

Extraction :

- nom ;

- adresse ;

- téléphone ;

- email.

## **Ticket TFLE-032**

Créer nettoyage données.

Fonctions :

- normalisation téléphone ;

- suppression doublons.

# **EPIC 05 --- Lead Scoring Engine**

Priorité :

## **P0**

## **Ticket TFLE-040**

Créer moteur scoring.

Entrées :

restaurant data

Sortie :

score 0-100

Code :

calculate_score()

## **Ticket TFLE-041**

Créer règles scoring.

Exemple :

absence site +15

indépendant +20

zone stratégique +15

## **Ticket TFLE-042**

Afficher score frontend.

Composant :

LeadScoreBadge

# **EPIC 06 --- AI Sales Assistant**

Priorité :

## **P1**

## **Ticket TFLE-050**

Créer client IA.

Fichier :

ai/client.py

## **Ticket TFLE-051**

Créer prompt système.

Fichier :

ai/prompts/sales_analysis.txt

Prompt :

Tu es un assistant commercial TableFlash.

Analyse ce restaurant.

Donne :

1\. Opportunité

2\. Arguments

3\. Message personnalisé

Ne jamais inventer.

## **Ticket TFLE-052**

API analyse IA.

Route :

POST /ai/analyze/{restaurant_id}

# **EPIC 07 --- CRM Pipeline**

Priorité :

## **P0**

## **Ticket TFLE-060**

Créer statuts :

NEW

QUALIFIED

CONTACTED

DEMO

TRIAL

CUSTOMER

LOST

## **Ticket TFLE-061**

Créer pipeline Kanban.

Composants :

PipelineBoard

PipelineColumn

LeadCard

## **Ticket TFLE-062**

Créer historique interactions.

Types :

email

call

note

meeting

# **EPIC 08 --- Gestion Essai 30 jours**

Priorité :

## **P1**

## **Ticket TFLE-070**

Créer statut trial.

Champs :

trial_start

trial_end

trial_status

## **Ticket TFLE-071**

Créer rappels.

Exemples :

J+7

J+15

J+25

J+30

# **EPIC 09 --- Dashboard Analytics**

Priorité :

## **P1**

## **Ticket TFLE-080**

Créer KPI.

Afficher :

restaurants analysés

prospects qualifiés

contacts

essais

clients

## **Ticket TFLE-081**

Créer graphiques.

Librairie :

Recharts.

# **EPIC 10 --- Tests**

Priorité :

## **P0**

## **Ticket TFLE-090**

Tests backend.

Tester :

- API ;

- scoring ;

- CRM.

## **Ticket TFLE-091**

Tests frontend.

Tester :

- pages ;

- formulaires.

## **Ticket TFLE-092**

Tests IA.

Vérifier :

- format réponse ;

- absence invention.

# **EPIC 11 --- Déploiement**

Priorité :

## **P1**

## **Ticket TFLE-100**

Créer environnement production.

## **Ticket TFLE-101**

Configurer CI/CD.

Pipeline :

Push

↓

Tests

↓

Build

↓

Deploy

# **EPIC 12 --- Documentation**

Priorité :

## **P1**

## **Ticket TFLE-110**

Créer documentation développeur.

Inclure :

- installation ;

- architecture ;

- API ;

- maintenance.

# **32.9 --- Prompts prêts pour Claude Code / Cursor**

# **Prompt 01 --- Architecte logiciel**

Tu es l\'architecte principal du projet TFLE.

Analyse l\'architecture existante.

Ne modifie aucun fichier sans validation.

Ton rôle :

\- identifier problèmes architecture ;

\- proposer améliorations ;

\- respecter la documentation TFLE.

Avant toute modification :

explique :

1\. problème

2\. solution

3\. fichiers concernés

4\. risques

# **Prompt 02 --- Développeur Backend**

Tu es développeur backend senior Python FastAPI.

Travaille uniquement sur le module demandé.

Respecte :

\- architecture existante ;

\- typage ;

\- tests ;

\- sécurité.

Avant modification :

liste les fichiers impactés.

Après modification :

fournis :

\- résumé ;

\- tests effectués ;

\- risques.

# **Prompt 03 --- Développeur Frontend**

Tu es développeur React TypeScript senior.

Respecte :

\- composants réutilisables ;

\- Tailwind ;

\- UX simple ;

\- aucune régression.

Ne crée pas de nouvelle librairie sans justification.

# **Prompt 04 --- IA Engineer**

Tu es responsable IA TFLE.

Ton objectif :

Créer une intelligence commerciale fiable.

Règles :

\- ne jamais inventer des informations ;

\- distinguer faits/hypothèses ;

\- optimiser coûts ;

\- versionner les prompts.

# **Prompt 05 --- Code Review**

Effectue une revue complète.

Analyse :

\- bugs potentiels ;

\- sécurité ;

\- performances ;

\- dette technique.

Classe :

P0 critique

P1 important

P2 amélioration

# **32.10 --- Workflow quotidien développeur**

Chaque journée :

## **Matin**

Lire :

- tickets ouverts ;

- erreurs ;

- priorités.

## **Développement**

Cycle :

Ticket

↓

Code

↓

Test

↓

Commit

↓

Review

## **Fin journée**

Documenter :

- terminé ;

- bloquants ;

- prochaine tâche.

# **32.11 --- Règle absolue IA Coding**

Les assistants IA ne doivent jamais :

❌ réécrire tout le projet\
❌ supprimer des fichiers importants\
❌ modifier architecture sans validation\
❌ ajouter dépendances inutiles

Ils doivent :

✅ proposer\
✅ expliquer\
✅ modifier petit à petit\
✅ tester

# **32.12 --- Definition of Done (DoD)**

Un ticket est terminé uniquement si :

✅ Code écrit\
✅ Tests passés\
✅ Documentation mise à jour\
✅ Commit effectué\
✅ Fonction validée

# **32.13 --- Première version livrable MVP**

Objectif :

Créer :

TFLE MVP v0.1

Avec :

✅ Base restaurants\
✅ Scraping initial\
✅ Scoring\
✅ CRM simple\
✅ Assistant IA\
✅ Dashboard

# **Conclusion Document 32**

TFLE est maintenant transformé en plan d\'exécution concret.

La documentation complète devient :

Vision

↓

Stratégie

↓

Architecture

↓

Spécifications

↓

Tickets Git

↓

Code

La prochaine étape logique n\'est plus de réfléchir au produit.

C\'est de commencer la construction.
