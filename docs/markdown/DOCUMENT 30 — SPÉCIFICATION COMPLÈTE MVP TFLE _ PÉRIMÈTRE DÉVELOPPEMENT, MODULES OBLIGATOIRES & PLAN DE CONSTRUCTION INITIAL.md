# **DOCUMENT 30 --- SPÉCIFICATION COMPLÈTE MVP TFLE : PÉRIMÈTRE DÉVELOPPEMENT, MODULES OBLIGATOIRES & PLAN DE CONSTRUCTION INITIAL**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Document de cadrage développement MVP\
Module : Product Delivery, Engineering Scope & Initial Build Plan\
Produit : TableFlash Leads Engine\
Usage : Interne uniquement pour TableFlash**

# **30.1 --- Introduction**

Après les documents stratégiques précédents, TFLE entre dans une
nouvelle phase :

**Passer de la vision à la construction réelle.**

L\'objectif du MVP n\'est pas de créer immédiatement une plateforme IA
autonome complète.

L\'objectif est de construire une première version opérationnelle
capable de répondre à une question essentielle :

> Est-ce que TFLE permet réellement à TableFlash de trouver plus
> rapidement des restaurants pertinents et de convertir davantage de
> prospects ?

Le MVP doit donc privilégier :

- la simplicité ;

- la rapidité d\'exécution ;

- la validation terrain ;

- la mesure des résultats.

# **30.2 --- Objectif principal du MVP**

Créer une machine interne capable de :

id=\"mvpflow\"

Collecter restaurants

↓

Stocker informations

↓

Qualifier automatiquement

↓

Prioriser prospects

↓

Préparer contact

↓

Suivre conversion

# **30.3 --- Ce que le MVP doit prouver**

Le MVP doit répondre à 5 questions.

## **Question 1**

Peut-on trouver suffisamment de restaurants pertinents automatiquement ?

## **Question 2**

Le scoring permet-il d\'identifier les meilleurs prospects ?

## **Question 3**

L\'IA améliore-t-elle la préparation commerciale ?

## **Question 4**

Le CRM permet-il un meilleur suivi ?

## **Question 5**

TFLE augmente-t-il les conversions TableFlash ?

# **30.4 --- Philosophie MVP**

Le MVP ne doit PAS construire :

❌ Une plateforme SaaS publique\
❌ Un CRM complet concurrent de Salesforce\
❌ Une IA totalement autonome\
❌ Un scraper mondial complexe\
❌ Une usine marketing automatisée

Le MVP doit construire :

✅ Un outil interne puissant\
✅ Une base prospects intelligente\
✅ Un assistant commercial IA\
✅ Un pipeline simple\
✅ Une boucle d\'apprentissage

# **30.5 --- Architecture MVP globale**

Architecture recommandée :

TFLE MVP

↓

Frontend Application

↓

Backend API

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

PostgreSQL Database

Scraping Workers

AI Services

CRM Engine

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

TableFlash Commercial

# **30.6 --- Stack technique recommandée MVP**

## **Frontend**

Objectif :

Interface rapide et maintenable.

Technologies :

- React ;

- TypeScript ;

- Tailwind CSS ;

- composants UI modernes.

## **Backend**

Objectif :

Centraliser logique métier.

Technologies possibles :

- Node.js ;

- NestJS ;

- Python FastAPI.

Recommandation :

Python pour la partie IA/data.

Node possible pour cohérence frontend.

## **Base de données**

Choix :

PostgreSQL.

Pourquoi :

- robuste ;

- relationnel ;

- adapté CRM ;

- compatible IA.

## **Recherche**

MVP :

PostgreSQL Full Text Search.

Evolution :

Vector Database.

# **30.7 --- Modules obligatoires MVP**

Le MVP comporte 7 modules.

# **MODULE 1 --- Lead Database**

## **Objectif**

Stocker les restaurants.

Fonctions :

- création restaurant ;

- modification ;

- recherche ;

- historique.

Données principales :

Restaurant

Nom

Adresse

Ville

Téléphone

Email

Site web

Source

Date découverte

Critère validation :

✅ Un restaurant peut être ajouté, recherché et modifié.

# **MODULE 2 --- Discovery Engine**

## **Objectif**

Trouver automatiquement des restaurants.

Sources MVP :

Priorité :

1.  Sources publiques autorisées.

2.  Sites professionnels.

3.  Annuaires accessibles.

Fonctions :

- collecte ;

- extraction ;

- normalisation.

Pipeline :

Source

↓

Crawler

↓

Extraction

↓

Nettoyage

↓

Base TFLE

Critère validation :

✅ TFLE peut importer plusieurs centaines/milliers de restaurants.

# **MODULE 3 --- Data Cleaning Engine**

## **Objectif**

Nettoyer les données.

Fonctions :

- suppression doublons ;

- format adresse ;

- validation email ;

- normalisation téléphone.

Exemple :

Avant :

Restaurant Dupont

06 xx xx xx xx

Après :

Restaurant Dupont

Téléphone valide

Adresse normalisée

Critère validation :

✅ Les doublons sont détectés automatiquement.

# **MODULE 4 --- Lead Scoring Engine**

## **Objectif**

Classer les prospects.

Score :

0 → 100

Version MVP :

Score basé sur règles.

Critères :

  ---------------------- ------------
       **Critère**        **Points**

  Restaurant indépendant     +20

     Absence commande        +20
         digitale        

       Site ancien           +15

     Beaucoup d\'avis        +15

     Zone stratégique        +15

    Type restauration        +15
          adapté         
  ---------------------- ------------

Exemple :

{

\"restaurant\":\"Chez Pierre\",

\"score\":88

}

Critère validation :

✅ Les meilleurs prospects apparaissent en priorité.

# **MODULE 5 --- AI Sales Assistant**

## **Objectif**

Aider la prospection.

Fonctions :

- résumé restaurant ;

- analyse opportunité ;

- génération message.

Entrée :

Restaurant

Données disponibles

Score

Sortie :

Pourquoi contacter ce restaurant

Quel argument utiliser

Message proposé

Critère validation :

✅ Chaque prospect possède une recommandation commerciale IA.

# **MODULE 6 --- CRM Commercial MVP**

## **Objectif**

Suivre les prospects.

Pipeline :

Nouveau

↓

Analysé

↓

Contacté

↓

Réponse

↓

Démo

↓

Essai

↓

Client

Fonctions :

- changement statut ;

- notes ;

- tâches ;

- historique.

Critère validation :

✅ Aucun prospect intéressant ne se perd.

# **MODULE 7 --- Dashboard MVP**

## **Objectif**

Piloter l\'activité.

Indicateurs :

## **Leads**

- restaurants trouvés ;

- qualifiés ;

- contactés.

## **Commercial**

- réponses ;

- démos ;

- essais.

## **Conversion**

- clients gagnés.

Exemple :

Cette semaine :

Restaurants analysés : 850

Prospects qualifiés : 120

Contacts : 40

Essais : 5

Clients : 2

# **30.8 --- Fonctionnalités exclues MVP**

Pour éviter la dispersion :

## **Pas de :**

❌ Agents IA autonomes complexes\
❌ Prédiction conversion avancée\
❌ Multi-utilisateurs complet\
❌ Internationalisation\
❌ Marketplace données\
❌ Automatisation email massive\
❌ Machine learning personnalisé

Ces éléments appartiennent aux versions futures.

# **30.9 --- Base de données MVP minimale**

Tables principales :

## **restaurants**

id

name

address

city

phone

email

website

source

created_at

## **leads**

id

restaurant_id

score

status

priority

## **interactions**

id

lead_id

type

note

date

## **ai_analysis**

id

restaurant_id

analysis

recommendation

created_at

## **tasks**

id

lead_id

title

status

due_date

# **30.10 --- Ordre de développement recommandé**

## **Sprint 1 --- Fondation**

Durée :

1-2 semaines.

Objectifs :

- initialisation projet ;

- base PostgreSQL ;

- authentification simple ;

- structure frontend/backend.

Validation :

Application accessible.

# **Sprint 2 --- Base restaurants**

Durée :

1-2 semaines.

Créer :

- CRUD restaurants ;

- recherche ;

- filtres.

Validation :

Gestion complète prospects.

# **Sprint 3 --- Discovery Engine**

Durée :

2-4 semaines.

Créer :

- import sources ;

- extraction ;

- nettoyage.

Validation :

Premiers milliers restaurants.

# **Sprint 4 --- Scoring**

Durée :

1-2 semaines.

Créer :

- règles score ;

- classement ;

- filtres.

Validation :

Top prospects identifiables.

# **Sprint 5 --- IA Assistant**

Durée :

2 semaines.

Créer :

- prompts ;

- génération analyses ;

- messages.

Validation :

Assistant commercial fonctionnel.

# **Sprint 6 --- CRM**

Durée :

2 semaines.

Créer :

- pipeline ;

- tâches ;

- historique.

Validation :

Suivi commercial complet.

# **Sprint 7 --- Dashboard**

Durée :

1-2 semaines.

Créer :

- KPI ;

- statistiques ;

- rapports.

Validation :

Pilotage activité.

# **30.11 --- Backlog MVP initial**

## **P0 --- Obligatoire**

### **Lead Database**

- Créer restaurant

- Modifier restaurant

- Rechercher restaurant

### **Scoring**

- Calcul automatique score

- Trier par potentiel

### **CRM**

- Pipeline commercial

- Notes

- Historique

### **IA**

- Analyse restaurant

- Génération argument

# **P1 --- Important**

- Import CSV

- Filtres avancés

- Tags restaurants

- Export données

- Templates messages

# **P2 --- Plus tard**

- Automatisation relances

- Agents IA spécialisés

- Prédictions

- Analytics avancés

# **30.12 --- Critères réussite MVP**

Le MVP est considéré réussi si :

## **Critère 1**

TFLE possède :

\>10 000 restaurants

analysés.

## **Critère 2**

Le scoring identifie des prospects pertinents.

## **Critère 3**

Le commercial gagne du temps.

## **Critère 4**

Les messages IA sont réellement utilisés.

## **Critère 5**

Des restaurants TableFlash sont convertis grâce au système.

# **30.13 --- Métriques MVP**

## **Acquisition**

- restaurants collectés/semaine ;

- prospects qualifiés.

## **Qualité**

- \% emails valides ;

- \% prospects pertinents.

## **Commercial**

- taux réponse ;

- taux démo ;

- taux essai.

## **Business**

- clients acquis ;

- revenu généré.

# **30.14 --- Passage MVP → V1**

Conditions :

Le passage V1 est validé si :

TFLE génère régulièrement des opportunités commerciales.

Alors ajout :

- agents IA ;

- automatisations ;

- mémoire ;

- prédictions.

# **30.15 --- Architecture cible après MVP**

TFLE V1

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Discovery Engine

Data Intelligence

AI Agents

CRM Automation

Analytics

Knowledge Base

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

TableFlash Growth

# **30.16 --- Vision finale**

Le MVP TFLE n\'est pas la destination.

C\'est la fondation.

La stratégie :

Petit outil interne

↓

Machine commerciale efficace

↓

Plateforme IA stratégique

# **Conclusion Document 30**

Le MVP TFLE doit rester concentré sur une mission :

> Trouver les bons restaurants, les qualifier rapidement et aider
> TableFlash à convertir davantage de clients.

La priorité absolue n\'est pas la sophistication technique.

La priorité est :

**Créer une première machine commerciale qui fonctionne réellement sur
le terrain.**

# **Fin de la phase Documentation stratégique TFLE --- Documents 00 à 30**
