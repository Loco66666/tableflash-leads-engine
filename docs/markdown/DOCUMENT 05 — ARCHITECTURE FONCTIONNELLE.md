# **DOCUMENT 05 --- ARCHITECTURE FONCTIONNELLE**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Document architecture produit\
Produit : TableFlash Leads Engine\
Type : Outil interne stratégique d\'acquisition commerciale**

# **05.1 --- Introduction**

L\'architecture fonctionnelle définit **comment TFLE est organisé au
niveau métier**.

Ce document ne décrit pas encore les technologies utilisées (cela
viendra dans le Document 06 --- Architecture technique), mais explique :

- les grands modules du système ;

- leurs responsabilités ;

- les flux d\'informations ;

- les interactions entre composants ;

- la logique globale de fonctionnement.

L\'objectif est de construire un système :

- modulaire ;

- évolutif ;

- maintenable ;

- capable de grandir avec TableFlash.

# **05.2 --- Vision globale de l\'architecture**

TFLE fonctionne comme une chaîne d\'intelligence commerciale.

Le flux principal :

MARCHÉ RESTAURATION

↓

01 --- DISCOVERY ENGINE

↓

02 --- DATA COLLECTION

↓

03 --- DATA ENRICHMENT

↓

04 --- WEBSITE ANALYSIS

↓

05 --- AI INTELLIGENCE

↓

06 --- LEAD SCORING

↓

07 --- CRM COMMERCIAL

↓

08 --- DASHBOARD & INSIGHTS

↓

CLIENT TABLEFLASH

# **05.3 --- Les grands modules TFLE**

L\'application est composée de 9 domaines fonctionnels.

TableFlash Leads Engine

├── Discovery Engine

├── Data Collector

├── Data Enrichment

├── Website Intelligence

├── AI Engine

├── Lead Scoring

├── CRM

├── Analytics

└── Administration

# **MODULE 01 --- DISCOVERY ENGINE**

## **Rôle**

Trouver les restaurants correspondant aux critères TableFlash.

## **Responsabilités**

Le Discovery Engine doit :

- rechercher des restaurants ;

- gérer les zones géographiques ;

- identifier les établissements potentiels ;

- éviter les doublons.

## **Entrées**

Exemples :

Ville :

Bayonne

Catégorie :

Restaurant traditionnel

Rayon :

30 km

## **Sorties**

Création d\'une liste brute :

Restaurant A

Restaurant B

Restaurant C

Ces données passent ensuite au module Data Collector.

# **MODULE 02 --- DATA COLLECTOR**

## **Rôle**

Transformer une découverte brute en fiche restaurant.

## **Entrées**

Exemple :

Nom :

Chez Pierre

Adresse :

Bayonne

Source :

Découverte automatique

## **Traitement**

Le système cherche :

- site web ;

- téléphone public ;

- informations générales ;

- catégories.

## **Sortie**

Création :

Restaurant Profile

ID :

TFLE-000001

Nom :

Chez Pierre

Statut :

Nouveau

# **MODULE 03 --- DATA ENRICHMENT**

## **Rôle**

Compléter la fiche avec davantage d\'informations.

## **Informations recherchées**

### **Contact**

- email professionnel public ;

- téléphone ;

- formulaire.

### **Présence numérique**

- Facebook ;

- Instagram ;

- autres réseaux publics.

### **Informations commerciales**

- type de restaurant ;

- gamme ;

- taille estimée ;

- activité.

## **Sortie**

Une fiche enrichie :

Restaurant

\+

Contacts

\+

Présence digitale

\+

Informations commerciales

# **MODULE 04 --- WEBSITE INTELLIGENCE**

## **Rôle**

Analyser automatiquement la présence numérique.

## **Fonctionnement**

Le système visite le site du restaurant.

Il analyse :

Site web

↓

Structure

↓

Technologies

↓

Menu

↓

Services

↓

Expérience utilisateur

## **Données produites**

Exemple :

{

site:true,

menu:\"PDF\",

qr_code:false,

reservation:true,

ordering:false,

mobile:true

}

## **Objectif**

Identifier les opportunités TableFlash.

# **MODULE 05 --- AI INTELLIGENCE ENGINE**

## **Rôle**

Transformer les données en compréhension commerciale.

## **Entrées**

Le moteur reçoit :

- fiche restaurant ;

- analyse web ;

- informations digitales ;

- historique.

## **Traitement**

L\'IA produit :

### **Résumé**

Exemple :

> Restaurant indépendant avec menu PDF uniquement. Potentiel intéressant
> pour moderniser l\'accès à la carte.

### **Opportunités**

Exemple :

Opportunité :

Élevée

### **Arguments commerciaux**

Exemple :

Mettre en avant :

\- suppression des impressions papier ;

\- facilité de modification ;

\- expérience client.

# **MODULE 06 --- LEAD SCORING ENGINE**

## **Rôle**

Classer automatiquement les restaurants.

## **Fonctionnement**

Le score est calculé selon plusieurs facteurs.

Exemple :

Restaurant indépendant

+20

Menu PDF

+10

Pas de QR Code

+15

Site ancien

+10

Bonne réputation locale

+10

Résultat :

Score :

85/100

Catégorie :

Prospect prioritaire

# **MODULE 07 --- CRM COMMERCIAL**

## **Rôle**

Transformer les prospects en clients.

## **Le CRM reçoit :**

Restaurant

\+

Analyse

\+

Score

\+

Recommandation IA

## **Gestion du cycle commercial**

Nouveau

↓

Qualifié

↓

Contacté

↓

Démo

↓

Essai gratuit

↓

Client

## **Informations conservées**

- appels ;

- emails ;

- notes ;

- rendez-vous ;

- décisions.

# **MODULE 08 --- ANALYTICS ENGINE**

## **Rôle**

Mesurer et améliorer la stratégie commerciale.

## **Analyse :**

### **Acquisition**

- restaurants trouvés ;

- zones couvertes.

### **Qualification**

- scores moyens ;

- profils intéressants.

### **Conversion**

- contacts ;

- essais ;

- clients.

## **Exemple**

Zone :

Pays Basque

Restaurants analysés :

2 500

Prospects intéressants :

420

Contacts :

80

Essais :

20

Clients :

7

# **MODULE 09 --- ADMINISTRATION**

## **Rôle**

Gérer le fonctionnement interne.

## **Responsabilités**

- utilisateurs ;

- permissions ;

- paramètres ;

- règles métier ;

- surveillance.

# **05.4 --- Flux de données complet**

Voici le parcours d\'un restaurant dans TFLE :

## **Étape 1 --- Découverte**

Le système trouve :

Restaurant Le Sud

Bayonne

Site détecté

↓

## **Étape 2 --- Création fiche**

Création :

Restaurant ID :

TFLE-00125

↓

## **Étape 3 --- Enrichissement**

Ajout :

Téléphone

Email public

Réseaux sociaux

↓

## **Étape 4 --- Analyse digitale**

Résultat :

Menu :

PDF

QR :

Non

Commande :

Non

↓

## **Étape 5 --- Intelligence IA**

Analyse :

Très bon candidat TableFlash

↓

## **Étape 6 --- Score**

Résultat :

91/100

↓

## **Étape 7 --- CRM**

Statut :

À contacter

↓

## **Étape 8 --- Action humaine**

Le commercial contacte le restaurant.

# **05.5 --- Architecture logique des informations**

Chaque restaurant possède une entité centrale.

RESTAURANT

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\| \| \|

Informations Analyse Commercial

générales digitale CRM

\|

Intelligence IA

\|

Score

# **05.6 --- Principes d\'échange entre modules**

## **Principe 1 --- Un module = une responsabilité**

Exemple :

Le scraper collecte.

Il ne décide pas si un prospect est intéressant.

La décision appartient au moteur IA/scoring.

## **Principe 2 --- Les données sources sont conservées**

Une information collectée ne doit jamais être écrasée sans historique.

Exemple :

Avant :

Menu PDF

Après :

Menu interactif

Les deux états doivent rester consultables.

## **Principe 3 --- Les analyses sont indépendantes**

Une nouvelle IA ou une nouvelle règle de scoring doit pouvoir être
ajoutée sans reconstruire toute l\'application.

# **05.7 --- Gestion des erreurs fonctionnelles**

Exemples :

## **Site inaccessible**

Résultat :

Analyse impossible

Nouvelle tentative dans 7 jours

## **Information manquante**

Exemple :

Pas d\'email.

Résultat :

Email non trouvé

Fiche conservée

## **Restaurant doublon**

Résultat :

Restaurant déjà existant

Fusion proposée

# **05.8 --- Vision d\'évolution**

L\'architecture doit permettre l\'ajout futur de :

## **Agents IA spécialisés**

Exemple :

Agent Recherche

Agent Analyse Web

Agent Commercial

Agent Veille Marché

## **Automatisation avancée**

Exemple :

Chaque matin :

Nouveaux restaurants détectés

↓

Analysés

↓

Classés

↓

Présentés dans Dashboard

# **05.9 --- Résumé architectural**

TFLE repose sur une chaîne simple :

COLLECTER

↓

COMPRENDRE

↓

QUALIFIER

↓

PRIORISER

↓

CONVERTIR

Chaque module possède une mission claire.

La force du système ne vient pas d\'un seul composant, mais de
l\'enchaînement :

**Données publiques → Analyse → Intelligence → Action commerciale**

# **Conclusion Document 05**

L\'architecture fonctionnelle de TFLE est conçue pour devenir le système
nerveux commercial de TableFlash.

Elle permet :

- une acquisition structurée ;

- une meilleure connaissance du marché ;

- une prospection plus intelligente ;

- une évolution progressive vers une plateforme d\'intelligence
  commerciale avancée.
