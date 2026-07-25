# **DOCUMENT 13 --- SPÉCIFICATIONS SCRAPING ENGINE**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification technique détaillée\
Module : Discovery & Data Collection Engine\
Produit : TableFlash Leads Engine\
Usage : Interne uniquement pour TableFlash**

# **13.1 --- Introduction**

Le **Scraping Engine TFLE** est le moteur chargé de découvrir,
collecter, nettoyer et enrichir automatiquement des informations
publiques concernant les restaurants.

Son objectif n\'est pas de collecter \"le plus de données possible\".

Son objectif est :

> Trouver les restaurants ayant le plus fort potentiel commercial pour
> TableFlash.

Le moteur doit transformer :

Sources publiques

↓

Données brutes

↓

Données nettoyées

↓

Restaurants qualifiés

↓

Prospects exploitables

# **13.2 --- Objectifs fonctionnels**

Le Scraping Engine doit permettre :

## **Découverte**

Trouver de nouveaux restaurants.

Exemples :

- restaurants indépendants ;

- brasseries ;

- pizzerias ;

- burgers ;

- restaurants traditionnels.

## **Extraction**

Récupérer :

- nom ;

- adresse ;

- téléphone ;

- site web ;

- email professionnel public ;

- réseaux sociaux publics ;

- catégorie ;

- horaires.

## **Analyse commerciale**

Détecter :

- présence ou absence de menu digital ;

- présence QR code ;

- présence commande en ligne ;

- qualité site web ;

- maturité numérique.

## **Enrichissement**

Compléter automatiquement :

- coordonnées ;

- informations manquantes ;

- catégorie ;

- potentiel commercial.

# **13.3 --- Architecture globale**

DISCOVERY ENGINE

\|

Source Management Layer

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Crawler Google Maps

Crawler OpenStreetMap

Crawler Annuaires publics

Crawler Sites restaurants

Crawler Réseaux publics

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\|

Extraction Engine

\|

Cleaning Engine

\|

Deduplication Engine

\|

Enrichment Engine

\|

Qualification Engine

\|

PostgreSQL TFLE

# **13.4 --- Principe architectural**

Le moteur est composé de modules indépendants.

Chaque source possède son propre connecteur.

Exemple :

sources/

├── osm_connector.py

├── directory_connector.py

├── website_connector.py

└── social_connector.py

Avantage :

Si une source change :

→ on modifie uniquement son connecteur.

# **13.5 --- Sources de données**

## **Priorité P0 --- MVP**

# **Source 1 --- OpenStreetMap**

## **Objectif**

Découverte géographique.

Données récupérées :

- nom ;

- adresse ;

- position GPS ;

- catégorie ;

- téléphone parfois disponible.

Exemple :

Nom :

Le Petit Bistrot

Ville :

Bayonne

Type :

Restaurant

Avantages :

✅ données ouvertes\
✅ couverture importante\
✅ stable

# **Source 2 --- Sites web restaurants**

Objectif :

Analyser la maturité digitale.

Informations :

- présence site ;

- email public ;

- menu ;

- réservation ;

- technologie utilisée.

Analyse :

https://restaurant.fr

↓

Crawler

↓

HTML

↓

Extraction

# **Source 3 --- Annuaires professionnels publics**

Objectif :

Compléter les informations.

Données :

- téléphone ;

- adresse ;

- catégorie.

# **Source 4 --- Pages publiques professionnelles**

Objectif :

Détecter :

- présence sociale ;

- activité.

# **13.6 --- Sources futures V2**

## **Veille ouverture restaurants**

Détecter :

- nouveaux établissements ;

- changements.

## **Sources partenaires**

Possibilité future :

- intégrations API ;

- bases commerciales autorisées.

# **13.7 --- Architecture des Crawlers**

Chaque crawler respecte une interface commune.

## **Interface Collector**

Exemple conceptuel :

class Collector:

def search(area):

pass

def extract(url):

pass

def normalize(data):

pass

Chaque source retourne un format commun :

{

\"name\":\"Restaurant X\",

\"address\":\"Bayonne\",

\"phone\":\"0559000000\",

\"website\":\"https://site.fr\",

\"source\":\"osm\"

}

# **13.8 --- Pipeline complet de collecte**

## **Étape 1 --- Recherche**

Entrée :

Ville :

Bayonne

Rayon :

30 km

Résultat :

500 établissements trouvés

# **Étape 2 --- Extraction**

Transformation :

HTML

↓

Informations structurées

# **Étape 3 --- Nettoyage**

Correction :

Avant :

Chez Paul!!!

Après :

Chez Paul

# **Étape 4 --- Déduplication**

Objectif :

Éviter :

Chez Paul

Chez-Paul

Chez Paul Restaurant

# **Étape 5 --- Enrichissement**

Ajout :

Email trouvé

Site analysé

Score initial

# **Étape 6 --- Qualification**

Création :

Lead TFLE

# **13.9 --- Extraction des données**

## **Données restaurant principales**

Table :

restaurants

Champs :

id

name

address

city

postal_code

country

latitude

longitude

phone

website

category

source

created_at

# **Données commerciales**

Table :

lead_profiles

Champs :

digital_score

opportunity_level

qr_detected

menu_type

ordering_available

# **13.10 --- Extraction email**

## **Objectif**

Trouver uniquement les emails publics professionnels.

Sources :

Pages :

Contact

Mentions légales

Footer

Page réservation

Recherche patterns :

contact@

info@

reservation@

bonjour@

Nettoyage :

Supprimer :

noreply@

support@

tracking@

# **13.11 --- Gestion conformité données**

TFLE doit respecter :

- RGPD ;

- règles de prospection commerciale ;

- minimisation des données.

Principes :

## **Collecter uniquement nécessaire**

Exemple :

Utile :

email professionnel public

Inutile :

données personnelles privées

## **Traçabilité**

Chaque donnée possède :

source_url

date_collecte

méthode_collecte

Exemple :

{

\"email\":\"contact@restaurant.fr\",

\"source\":

\"https://restaurant.fr/contact\",

\"collected_at\":

\"2026-07-25\"

}

# **13.12 --- Déduplication**

Module essentiel.

## **Problème**

Un restaurant peut apparaître :

Google

OSM

Site

Annuaire

## **Algorithme**

Comparaison :

### **Nom**

Distance Levenshtein.

### **Adresse**

Normalisation :

Avant :

12 rue Victor Hugo

Après :

12 rue victor hugo

### **Téléphone**

Suppression :

+33

espaces

points

Score similarité :

Nom 40%

Adresse 40%

Téléphone 20%

Si score :

\>90%

fusion automatique

Entre :

70-90%

validation humaine

# **13.13 --- Enrichissement IA**

Après collecte :

L\'IA analyse :

- type restaurant ;

- potentiel ;

- argument commercial.

Exemple :

Entrée :

Restaurant traditionnel

Menu PDF

120 avis

Pas de commande

Sortie :

Potentiel :

Très élevé

Pourquoi :

Digitalisation faible

Clientèle locale

Carte facilement adaptable

# **13.14 --- Système de Jobs**

Les gros traitements utilisent une file.

Architecture :

API

↓

Job Queue

↓

Worker

↓

Résultat

Exemples jobs :

SCRAPE_CITY

ANALYZE_WEBSITE

EXTRACT_EMAIL

CALCULATE_SCORE

Table :

jobs

Champs :

id

type

status

progress

started_at

finished_at

error

# **13.15 --- Gestion erreurs**

Chaque crawler doit gérer :

## **Site inaccessible**

Action :

retry 3 fois

## **Timeout**

Action :

abandon propre

## **Blocage**

Action :

pause source

## **Données invalides**

Action :

mettre en quarantaine

# **13.16 --- Optimisation performances**

## **Cache**

Éviter :

Analyser 10 fois le même site

Stockage :

website_last_checked

## **Limitation vitesse**

Respecter :

- serveurs ;

- robots.txt lorsque applicable ;

- fréquence raisonnable.

## **Traitement parallèle**

Exemple :

100 restaurants

↓

10 workers

↓

traitement simultané

# **13.17 --- Monitoring**

Dashboard technique :

Afficher :

Sources actives

Restaurants/jour

Erreurs

Temps moyen analyse

Coût IA

# **13.18 --- Sécurité**

Protection :

## **Secrets API**

Jamais dans le code.

## **Logs**

Conserver :

Qui

Quand

Quelle source

Quelle action

## **Isolation workers**

Un crawler défaillant ne doit pas arrêter TFLE.

# **13.19 --- MVP Scraping Engine**

Fonctionnalités obligatoires :

## **P0**

✅ Recherche restaurants par zone.

✅ Import données.

✅ Nettoyage.

✅ Déduplication.

✅ Analyse site simple.

✅ Extraction email public professionnel.

✅ Stockage PostgreSQL.

# **13.20 --- V1 Scraping Engine**

Ajouts :

- collecte automatique programmée ;

- plus de sources ;

- meilleure déduplication ;

- enrichissement IA ;

- surveillance changements.

# **13.21 --- V2 Scraping Engine**

Vision avancée :

Agent IA Discovery

Capable de :

- choisir les meilleures zones ;

- trouver de nouveaux restaurants ;

- expliquer pourquoi ils sont intéressants ;

- prioriser automatiquement.

# **13.22 --- Résumé architecture finale**

TFLE DISCOVERY ENGINE

Sources publiques

↓

Collectors

↓

Extraction

↓

Nettoyage

↓

Déduplication

↓

Enrichissement IA

↓

Scoring

↓

CRM TableFlash

# **Conclusion Document 13**

Le Scraping Engine est le moteur d\'acquisition de TFLE.

Sa mission n\'est pas seulement de collecter des restaurants.

Sa véritable valeur est :

> Transformer Internet en une source permanente de prospects qualifiés
> pour TableFlash.
