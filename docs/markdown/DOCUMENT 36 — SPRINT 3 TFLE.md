# **DOCUMENT 36 --- SPRINT 3 TFLE**

# **Discovery Engine & Scraping Initial**

**Version : 1.0\
Statut : Plan d\'exécution développement Sprint 3\
Module : Data Acquisition Engine\
Produit : TableFlash Leads Engine (TFLE)\
Durée estimée : 15 jours ouvrés\
Objectif : Transformer TFLE d\'une base CRM manuelle en moteur
automatique de découverte restaurants**

# **36.1 --- Vision du Sprint 3**

Les deux premiers sprints ont construit :

Sprint 1

Infrastructure

↓

Sprint 2

Base restaurants + CRM

Le Sprint 3 apporte le premier avantage stratégique de TFLE :

> Trouver automatiquement des restaurants correspondant aux critères
> TableFlash.

Le nouveau workflow devient :

Sources publiques

↓

Collecteurs TFLE

↓

Extraction données

↓

Nettoyage

↓

Déduplication

↓

Qualification initiale

↓

Import base restaurants

↓

Création leads

# **36.2 --- Objectif business**

À la fin du Sprint 3, TableFlash doit pouvoir dire :

> \"TFLE peut trouver automatiquement des restaurants dans une zone
> donnée et préparer une liste de prospects exploitable.\"

# **36.3 --- Résultat attendu**

Version :

TFLE v0.3.0

Fonctionnalités :

✅ Architecture scraping\
✅ Gestion des sources\
✅ Collecteurs indépendants\
✅ Extraction restaurants\
✅ Normalisation données\
✅ Détection doublons\
✅ Import automatique\
✅ Historique provenance\
✅ Première génération de leads

# **36.4 --- Principes importants**

## **TFLE ne doit pas être un simple scraper**

Un scraper basique :

Site internet

↓

Extraction email

n\'est pas suffisant.

TFLE doit devenir un :

## **Lead Discovery Engine**

Avec :

Collecte

\+

Compréhension

\+

Qualification

\+

Traçabilité

# **36.5 --- Sources de données MVP**

Le Sprint 3 utilise uniquement des sources publiques.

## **Source 1 --- OpenStreetMap**

Priorité :

P0

Pourquoi :

- données ouvertes ;

- couverture géographique ;

- restaurants ;

- coordonnées.

Données récupérées :

Nom

Adresse

Téléphone

Site

Catégorie

Coordonnées GPS

## **Source 2 --- Sites restaurants**

Priorité :

P1

Objectif :

Enrichissement.

Recherche :

Site officiel

↓

Page contact

↓

Email professionnel public

## **Source 3 --- Annuaires publics**

Priorité :

P1

Exemples :

- annuaires professionnels ;

- pages publiques ;

- plateformes accessibles.

# **36.6 --- Architecture Discovery Engine**

Nouvelle architecture :

scraping/

├── collectors/

│

│ ├── osm/

│ │ ├── collector.py

│ │ └── parser.py

│

│ ├── website/

│ │ ├── crawler.py

│ │ └── extractor.py

│

│ └── directory/

├── cleaners/

│ ├── normalize.py

│ └── duplicate.py

├── pipelines/

│ └── import_pipeline.py

├── models/

│ └── scraped_restaurant.py

└── logs/

# **36.7 --- Nouveau modèle Database**

Création table :

## **scraped_restaurants**

Cette table est volontairement séparée.

Pourquoi ?

Ne jamais mélanger :

Données trouvées

≠

Données validées

Structure :

scraped_restaurants

id

name

address

city

postal_code

phone

email

website

category

latitude

longitude

source

source_url

scraping_date

quality_score

processed

created_at

# **36.8 --- Pipeline global**

## **Étape 1 --- Collecte**

Exemple :

Recherche :

restaurants Bayonne

Résultat brut :

{

\"name\":\"Restaurant X\",

\"address\":\"Bayonne\",

\"source\":\"OSM\"

}

## **Étape 2 --- Nettoyage**

Transformation :

Avant :

RESTAURANT CHEZ PAUL

Après :

Restaurant Chez Paul

## **Étape 3 --- Validation**

Vérifier :

- nom présent ;

- adresse valide ;

- restaurant réel.

## **Étape 4 --- Déduplication**

Comparer :

- nom ;

- adresse ;

- téléphone ;

- domaine.

## **Étape 5 --- Import**

Si valide :

scraped_restaurants

↓

restaurants

↓

lead

# **36.9 --- Ticket TFLE-200**

# **Création architecture Scraping Engine**

Priorité :

P0

Objectif :

Créer le framework des collecteurs.

Créer :

class Collector:

def collect():

pass

Chaque source devra respecter :

Collector

↓

Parser

↓

Cleaner

↓

Importer

# **Prompt Claude Code TFLE-200**

Tu travailles sur TFLE Sprint 3.

Crée uniquement l\'architecture Discovery Engine.

Objectifs :

\- architecture modulaire

\- collecteurs indépendants

\- aucune dépendance à une source spécifique

Ne scrape aucune donnée pour le moment.

Avant modification :

liste tous les fichiers créés.

# **Critères validation**

✅ Structure créée\
✅ Aucun scraper spécifique mélangé\
✅ Tests architecture

# **36.10 --- Ticket TFLE-210**

# **Collecteur OpenStreetMap**

Priorité :

P0

Objectif :

Trouver restaurants par zone.

Entrée :

{

\"city\":\"Bayonne\"

}

Sortie :

\[

{

\"name\":\"Restaurant Exemple\",

\"address\":\"\...\"

}

\]

Module :

scraping/collectors/osm/

# **Fonction :**

collect_restaurants(location)

# **Critères validation**

✅ Recherche fonctionnelle\
✅ Données enregistrées\
✅ Source conservée

# **Prompt Claude Code TFLE-210**

Implémente le collecteur OpenStreetMap TFLE.

Contraintes :

\- respecter architecture collector

\- gérer erreurs réseau

\- logger les opérations

\- ne pas créer de doublons

Ajoute des tests.

# **36.11 --- Ticket TFLE-220**

# **Parser et normalisation données**

Priorité :

P0

Objectif :

Transformer les données brutes.

Avant :

{

\"name\":\"CHEZ PAUL !!!\",

\"phone\":\"+33 6\...\"

}

Après :

{

\"name\":\"Chez Paul\",

\"phone\":\"+336\...\"

}

Normalisation :

## **Nom**

- espaces ;

- majuscules ;

- caractères.

## **Téléphone**

Format :

+336XXXXXXXX

## **Adresse**

Standardisation.

# **Critères validation**

✅ Données propres\
✅ Formats homogènes

# **36.12 --- Ticket TFLE-230**

# **Système de déduplication**

Priorité :

P0

Problème :

Le même restaurant peut apparaître :

Google

\+

OSM

\+

Site officiel

Créer :

duplicate_detector.py

Score similarité :

Exemple :

Nom 40%

Adresse 40%

Téléphone 20%

Si score \> seuil :

Fusion.

# **Critères validation**

✅ Doublons détectés\
✅ Aucun écrasement automatique dangereux

# **36.13 --- Ticket TFLE-240**

# **Interface Discovery**

Priorité :

P1

Nouvelle page :

/discovery

Fonctions :

Créer une recherche :

Ville :

Catégorie :

Rayon :

Exemple :

Bayonne

Restaurant traditionnel

20 km

Résultat :

Table :

  ---------------- ----------- ------------ -------------
   **Restaurant**   **Ville**   **Source**   **Qualité**

     Chez Paul       Bayonne       OSM           82
  ---------------- ----------- ------------ -------------

# **Composants :**

DiscoverySearch

DiscoveryResults

SourceBadge

QualityScore

# **36.14 --- Ticket TFLE-250**

# **Import automatique vers CRM**

Priorité :

P0

Workflow :

Restaurant découvert

↓

Validation

↓

Importer

↓

Restaurant TFLE

↓

Créer Lead

Bouton :

Convertir en prospect

# **36.15 --- Quality Score initial**

Avant IA avancée :

Score simple.

Formule :

Quality Score =

Nom valide

+20

Adresse valide

+20

Téléphone

+15

Site

+20

Email

+25

Score :

0-100

# **36.16 --- Gestion des logs scraping**

Important.

Chaque collecte doit garder :

date

source

durée

résultat

erreurs

nombre trouvés

Table :

scraping_jobs

id

source

status

started_at

finished_at

items_found

errors

# **36.17 --- Tests Sprint 3**

## **Tests collecteurs**

Tester :

- connexion source ;

- parsing ;

- erreurs.

## **Tests données**

Tester :

- doublons ;

- formats ;

- imports.

## **Tests sécurité**

Vérifier :

- limitation fréquence ;

- stockage sécurisé ;

- logs.

# **36.18 --- Planning Sprint 3**

## **Jour 1-2**

Architecture scraping.

## **Jour 3-5**

Collecteur OpenStreetMap.

## **Jour 6-7**

Nettoyage données.

## **Jour 8-9**

Déduplication.

## **Jour 10-11**

Interface Discovery.

## **Jour 12**

Import CRM.

## **Jour 13**

Logs.

## **Jour 14-15**

Tests + optimisation.

# **36.19 --- Definition of Done Sprint 3**

Le sprint est terminé lorsque :

## **Discovery Engine**

✅ Collecteur fonctionnel\
✅ Données récupérées automatiquement

## **Data Quality**

✅ Nettoyage automatique\
✅ Déduplication

## **CRM**

✅ Import restaurant\
✅ Création prospect

## **Interface**

✅ Recherche disponible\
✅ Résultats affichés

# **36.20 --- Résultat opérationnel**

Après Sprint 3, TableFlash possède :

Avant :

Trouver restaurants manuellement

↓

Ajouter dans CRM

Après :

Choisir une zone

↓

TFLE trouve les restaurants

↓

Nettoie les données

↓

Prépare les prospects

↓

Commercial contacte
