# **DOCUMENT 17 --- SYSTÈME DE COLLECTE EMAIL, ENRICHISSEMENT DONNÉES & QUALIFICATION PROSPECTS**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification fonctionnelle + technique\
Module : Data Acquisition & Prospect Intelligence\
Produit : TableFlash Leads Engine\
Usage : Interne uniquement pour TableFlash**

# **17.1 --- Introduction**

Le module **Email Collection & Data Enrichment Engine** est responsable
de transformer une simple découverte de restaurants en prospects
commerciaux exploitables.

Le Scraping Engine trouve des restaurants.

Ce module répond à une question plus importante :

> \"Avons-nous suffisamment d\'informations fiables pour contacter ce
> restaurant avec une approche pertinente ?\"

# **17.2 --- Objectifs du module**

Le système doit permettre :

## **Collecter**

Récupérer les informations professionnelles publiques :

- email professionnel ;

- téléphone ;

- site internet ;

- réseaux professionnels publics ;

- formulaire de contact ;

- adresse établissement.

## **Nettoyer**

Supprimer :

- doublons ;

- erreurs ;

- emails invalides ;

- informations obsolètes.

## **Qualifier**

Déterminer :

- qualité des données ;

- facilité de contact ;

- intérêt commercial.

## **Enrichir**

Ajouter :

- informations digitales ;

- profil restaurant ;

- opportunités TableFlash.

# **17.3 --- Architecture globale**

RESTAURANT

↓

DATA COLLECTION ENGINE

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Email Extractor

Website Analyzer

Contact Discovery

Data Cleaner

Validation Engine

Enrichment AI

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

QUALITY SCORING ENGINE

↓

CRM TABLEFLASH

# **17.4 --- Principe fondamental**

Le système ne cherche pas uniquement des emails.

Un email seul n\'est pas un prospect.

Un prospect TFLE doit être :

Restaurant identifié

\+

Informations fiables

\+

Besoin potentiel

\+

Possibilité de contact

# **17.5 --- Sources de collecte**

## **Priorité P0 --- MVP**

# **Source 1 --- Site officiel du restaurant**

Source principale.

Pages analysées :

/contact

/mentions-legales

/reservation

/footer

/about

Données possibles :

- email ;

- téléphone ;

- nom du responsable si public ;

- adresse ;

- réseaux sociaux.

# **Source 2 --- Informations publiques établissement**

Données :

- adresse ;

- téléphone ;

- catégorie ;

- horaires.

# **Source 3 --- Réseaux professionnels publics**

Objectif :

Identifier :

- présence sociale ;

- activité récente ;

- moyen de contact privilégié.

# **17.6 --- Architecture Email Extractor**

Module :

email_extractor/

Fonctions :

extract_emails()

validate_email()

classify_email()

remove_invalid()

# **17.7 --- Extraction email**

Le système analyse :

HTML :

\<a href=\"mailto:contact@restaurant.fr\"\>

Texte :

Nous contacter :

contact@restaurant.fr

Documents publics :

- PDF menu ;

- mentions légales.

# **17.8 --- Classification des emails**

Tous les emails n\'ont pas la même valeur.

# **Niveau A --- Excellent**

Exemples :

direction@restaurant.fr

contact@restaurant.fr

bonjour@restaurant.fr

Score :

+20

# **Niveau B --- Correct**

Exemples :

reservation@restaurant.fr

info@restaurant.fr

Score :

+15

# **Niveau C --- Faible**

Exemples :

gmail professionnel

hotmail professionnel

Score :

+5

# **Niveau D --- Rejet**

Exemples :

noreply@

support@

newsletter@

Score :

0

# **17.9 --- Validation email**

Avant stockage :

Le système vérifie :

## **Format**

Exemple :

Valide :

contact@restaurant.fr

Invalide :

contact@

## **Domaine**

Analyse :

restaurant.fr

## **Existence technique**

Possibilité future :

Vérification MX.

Résultat :

{

\"email\":\"contact@restaurant.fr\",

\"valid\":true,

\"confidence\":95

}

# **17.10 --- Stockage des emails**

Table :

restaurant_contacts

Structure :

id

restaurant_id

type

value

source_url

confidence

verified_at

Exemple :

{

\"type\":\"email\",

\"value\":\"contact@restaurant.fr\",

\"source\":

\"https://restaurant.fr/contact\",

\"confidence\":95

}

# **17.11 --- Enrichissement des données**

Après collecte :

L\'IA complète le profil.

Exemple :

Données initiales :

Nom :

Chez Martin

Ville :

Bayonne

Site :

Oui

Enrichissement :

Type :

Brasserie traditionnelle

Positionnement :

Cuisine locale

Opportunité :

Élevée

# **17.12 --- Restaurant Profile Intelligence**

Création d\'un profil complet.

Exemple :

{

\"name\":\"Chez Martin\",

\"type\":\"brasserie\",

\"independent\":true,

\"digital_level\":\"low\",

\"tableflash_fit\":\"high\"

}

# **17.13 --- Data Quality Score**

Chaque prospect possède une note qualité.

Score :

0 → 100

Composition :

Qualité données

\+

Complétude

\+

Fiabilité sources

\+

Actualité

# **17.14 --- Calcul Data Quality Score**

## **Nom valide**

+15

## **Adresse complète**

+20

## **Téléphone valide**

+15

## **Email professionnel**

+25

## **Site officiel**

+15

## **Source vérifiée**

+10

Maximum :

100

# **Exemple**

Restaurant :

Nom ✅

Adresse ✅

Téléphone ✅

Email ✅

Site ✅

Score :

100/100

# **17.15 --- Qualification commerciale automatique**

Le système combine :

Data Quality Score

\+

Lead Score

\+

Digital Opportunity

Résultat :

{

\"priority\":\"HIGH\",

\"contact_ready\":true,

\"recommended_action\":

\"Email personnalisé\"

}

# **17.16 --- Classification prospects**

# **Prospect Premium**

Conditions :

Score TFLE \>85

\+

Email valide

\+

Restaurant indépendant

Action :

Contact rapide.

# **Prospect Standard**

Conditions :

Score 60-85

Action :

Analyse complémentaire.

# **Prospect Faible**

Conditions :

Score \<60

Action :

Archivage ou surveillance.

# **17.17 --- Détection des doublons contacts**

Problème :

Un restaurant peut avoir :

contact@

info@

reservation@

Le système regroupe :

Restaurant

\|

Contacts multiples

Priorité :

direction@

contact@

bonjour@

# **17.18 --- Historique des données**

Chaque modification est conservée.

Table :

data_history

Exemple :

{

\"field\":\"email\",

\"old\":

\"info@ancien.fr\",

\"new\":

\"contact@nouveau.fr\",

\"date\":

\"2026-07-25\"

}

# **17.19 --- Préparation prospection**

Le système prépare les campagnes.

Mais il ne lance pas automatiquement sans validation.

Création :

Prospect List

Exemple :

Campagne :

Restaurants Bayonne

Score \>80

Pas de QR détecté

Email validé

Résultat :

150 prospects prêts

# **17.20 --- Personnalisation IA des messages**

L\'IA utilise :

- données restaurant ;

- analyse digitale ;

- scoring.

Exemple :

Données :

Restaurant traditionnel

Menu PDF

Pas de commande

Message généré :

Bonjour,

Nous avons remarqué que votre restaurant

propose une carte en ligne PDF.

TableFlash permet de transformer simplement

votre carte en expérience digitale avec QR code\...

# **17.21 --- Sécurité et conformité**

Principes :

## **Minimisation**

Collecter uniquement :

- données nécessaires à la prospection professionnelle.

## **Traçabilité**

Chaque donnée garde :

- source ;

- date ;

- méthode.

## **Suppression**

Possibilité :

- suppression prospect ;

- exclusion future.

## **Respect opposition**

Si un établissement demande :

\"Ne plus être contacté\"

Le système bloque :

DO_NOT_CONTACT = TRUE

# **17.22 --- Gestion du consentement et conformité commerciale**

TFLE doit intégrer :

- identification claire de TableFlash ;

- possibilité de demander l\'arrêt des communications ;

- conservation des preuves de traitement ;

- distinction entre données professionnelles publiques et données
  personnelles.

# **17.23 --- Tables PostgreSQL**

## **contacts**

id

restaurant_id

contact_type

value

source

confidence

verified

## **enrichment_data**

id

restaurant_id

field

value

source

confidence

## **data_quality_scores**

id

restaurant_id

score

details

created_at

## **exclusion_list**

id

restaurant_id

reason

created_at

# **17.24 --- MVP**

Fonctionnalités obligatoires :

✅ Extraction email depuis sites.

✅ Validation format.

✅ Nettoyage.

✅ Déduplication.

✅ Score qualité.

✅ Enrichissement simple.

✅ Préparation liste prospects.

# **17.25 --- Version 1**

Ajouts :

- validation avancée ;

- enrichissement IA ;

- historique complet ;

- segmentation automatique.

# **17.26 --- Version 2**

Vision avancée :

Un moteur capable de dire :

> \"Ces 500 restaurants sont les meilleurs prospects TableFlash cette
> semaine, leurs emails sont vérifiés, leur besoin est identifié et un
> argument personnalisé est prêt.\"

# **17.27 --- Architecture finale**

SOURCES PUBLIQUES

↓

COLLECTE DONNÉES

↓

EXTRACTION EMAIL

↓

VALIDATION

↓

ENRICHISSEMENT IA

↓

QUALITY SCORE

↓

CRM TABLEFLASH

# **Conclusion Document 17**

Le système de collecte email TFLE ne doit pas être vu comme un simple
récupérateur d\'adresses.

Sa valeur vient de la combinaison :

**Données fiables + compréhension commerciale + qualification
intelligente.**

La finalité :

> Donner à TableFlash une base de prospects qualifiés, compréhensibles
> et exploitables, plutôt qu\'une simple liste de restaurants.
