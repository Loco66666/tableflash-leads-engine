# **DOCUMENT 07 --- MODÈLE DE DONNÉES (DATABASE DESIGN)**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification base de données\
Produit : TableFlash Leads Engine\
SGBD cible : PostgreSQL\
Type : Outil interne d\'intelligence commerciale**

# **07.1 --- Introduction**

Le modèle de données définit la structure permettant à TFLE de stocker,
organiser et exploiter les informations liées aux restaurants.

L\'objectif est de créer une base capable de gérer :

- des milliers de restaurants ;

- plusieurs sources de données ;

- des analyses répétées ;

- des scores historiques ;

- un suivi commercial complet ;

- des recommandations IA ;

- des statistiques de conversion.

# **07.2 --- Principes de conception**

## **Principe 1 --- Une donnée = une source identifiable**

Chaque information doit conserver :

- son origine ;

- sa date ;

- sa fiabilité.

Exemple :

Email

Source :

Site officiel

Date :

25/07/2026

Confiance :

Élevée

## **Principe 2 --- Historisation obligatoire**

Les données changent.

TFLE doit pouvoir répondre :

> \"Quelle était la situation de ce restaurant il y a 6 mois ?\"

Exemple :

Avant :

Menu PDF

Après :

Menu interactif

Les deux informations doivent être conservées.

## **Principe 3 --- Séparation des responsabilités**

Les informations sont séparées :

Restaurant

↓

Données générales

Analyse digitale

↓

Compréhension

CRM

↓

Action commerciale

# **07.3 --- Vue globale des entités**

Architecture principale :

USERS

\|

\|

RESTAURANTS

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\| \| \| \|

CONTACTS ANALYSES SCORES CRM

\|

AI INSIGHTS

\|

ACTIVITIES

# **07.4 --- TABLE : restaurants**

## **Rôle**

Table centrale de TFLE.

Elle représente chaque établissement découvert.

## **Structure**

restaurants

  ------------- ------------ -----------------
    **Champ**     **Type**    **Description**

       id           UUID        Identifiant
                                  unique

      name        VARCHAR     Nom restaurant

      slug        VARCHAR       URL interne

    category      VARCHAR          Type
                               établissement

   description      TEXT        Description

     address        TEXT     Adresse complète

      city        VARCHAR          Ville

   postal_code    VARCHAR       Code postal

   department     VARCHAR       Département

     region       VARCHAR         Région

    latitude      DECIMAL      Position GPS

    longitude     DECIMAL      Position GPS

     website        TEXT       Site internet

      phone       VARCHAR        Téléphone

     status         ENUM        Statut TFLE

   created_at    TIMESTAMP       Création

   updated_at    TIMESTAMP     Modification
  ------------- ------------ -----------------

## **Statuts possibles**

DISCOVERED

ANALYZING

QUALIFIED

CONTACTED

CUSTOMER

ARCHIVED

# **07.5 --- TABLE : restaurant_sources**

## **Rôle**

Tracer l\'origine des données.

Exemple :

Un restaurant peut être trouvé via :

- Google ;

- annuaire public ;

- site officiel ;

- import manuel.

Structure :

  --------------- ------------
     **Champ**      **Type**

        id            UUID

   restaurant_id      UUID

    source_type     VARCHAR

    source_url        TEXT

   collected_at    TIMESTAMP

    confidence      INTEGER
  --------------- ------------

Exemple :

{

\"source\":\"website\",

\"confidence\":95

}

# **07.6 --- TABLE : contacts**

## **Rôle**

Stocker les moyens de contact publics.

Structure :

  --------------- ------------
     **Champ**      **Type**

        id            UUID

   restaurant_id      UUID

       type           ENUM

       value          TEXT

      source          TEXT

     verified       BOOLEAN

    created_at     TIMESTAMP
  --------------- ------------

Types :

EMAIL

PHONE

CONTACT_FORM

SOCIAL

Exemple :

Email

contact@restaurant.fr

Source :

Site officiel

Validé :

Oui

# **07.7 --- TABLE : social_profiles**

## **Rôle**

Stocker la présence sociale.

Structure :

  --------------- ------------
     **Champ**      **Type**

        id            UUID

   restaurant_id      UUID

     platform       VARCHAR

        url           TEXT

     followers      INTEGER

   last_checked    TIMESTAMP
  --------------- ------------

Plateformes :

Instagram

Facebook

TikTok

LinkedIn

# **07.8 --- TABLE : website_analysis**

## **Rôle**

Stocker les analyses digitales.

Structure :

  -------------------- ------------
       **Champ**         **Type**

           id              UUID

     restaurant_id         UUID

     website_exists      BOOLEAN

    mobile_optimized     BOOLEAN

          cms            VARCHAR

       menu_type           ENUM

      qr_detected        BOOLEAN

   booking_available     BOOLEAN

   ordering_available    BOOLEAN

      analyzed_at       TIMESTAMP
  -------------------- ------------

Valeurs menu :

INTERACTIVE

PDF

IMAGE

NONE

UNKNOWN

# **07.9 --- TABLE : scraping_jobs**

## **Rôle**

Gérer les tâches de collecte.

Structure :

  --------------- ------------
     **Champ**      **Type**

        id            UUID

       type         VARCHAR

      status          ENUM

    started_at     TIMESTAMP

   completed_at    TIMESTAMP

   error_message      TEXT
  --------------- ------------

Statuts :

PENDING

RUNNING

SUCCESS

FAILED

# **07.10 --- TABLE : AI_ANALYSIS**

## **Rôle**

Conserver les analyses générées par IA.

Structure :

  ------------------- ------------
       **Champ**        **Type**

          id              UUID

     restaurant_id        UUID

      model_used        VARCHAR

        summary           TEXT

   opportunity_level      ENUM

    recommendations      JSONB

      created_at       TIMESTAMP
  ------------------- ------------

Exemple :

{

\"argument\":

\"Mettre en avant le remplacement du menu papier\"

}

# **07.11 --- TABLE : lead_scores**

## **Rôle**

Stocker les scores commerciaux.

Structure :

  --------------- ------------
     **Champ**      **Type**

        id            UUID

   restaurant_id      UUID

       score        INTEGER

     category         ENUM

      reasons        JSONB

    created_at     TIMESTAMP
  --------------- ------------

Catégories :

LOW

MEDIUM

HIGH

PRIORITY

Exemple :

{

\"no_qr_code\":15,

\"pdf_menu\":10,

\"independent\":20

}

# **07.12 --- TABLE : scoring_rules**

## **Rôle**

Permettre de modifier les règles.

Structure :

  ----------- ----------
   **Champ**   **Type**

      id         UUID

     name      VARCHAR

   condition    JSONB

    points     INTEGER

    active     BOOLEAN
  ----------- ----------

Exemple :

{

\"condition\":

\"qr_code=false\",

\"points\":

15

}

# **07.13 --- TABLE : CRM_PIPELINE**

## **Rôle**

Gestion commerciale.

Structure :

  --------------- ------------
     **Champ**      **Type**

        id            UUID

   restaurant_id      UUID

   assigned_user      UUID

      status          ENUM

     priority       INTEGER

    created_at     TIMESTAMP

    updated_at     TIMESTAMP
  --------------- ------------

Statuts :

NEW

TO_CONTACT

CONTACTED

DEMO

TRIAL

CUSTOMER

LOST

# **07.14 --- TABLE : activities**

## **Rôle**

Historique des actions commerciales.

Structure :

  --------------- ------------
     **Champ**      **Type**

        id            UUID

   restaurant_id      UUID

      user_id         UUID

       type           ENUM

       note           TEXT

    created_at     TIMESTAMP
  --------------- ------------

Types :

CALL

EMAIL

MEETING

NOTE

STATUS_CHANGE

Exemple :

26/07

Appel effectué

Intérêt confirmé

Essai 30 jours proposé

# **07.15 --- TABLE : users**

## **Rôle**

Utilisateurs internes.

Structure :

  ------------ ------------
   **Champ**     **Type**

       id          UUID

      name       VARCHAR

     email       VARCHAR

      role         ENUM

   created_at   TIMESTAMP
  ------------ ------------

Rôles :

ADMIN

COMMERCIAL

ANALYST

# **07.16 --- TABLE : tasks**

## **Rôle**

Gestion des actions futures.

Structure :

  --------------- ----------
     **Champ**     **Type**

        id           UUID

   restaurant_id     UUID

   assigned_user     UUID

       title       VARCHAR

     due_date        DATE

      status         ENUM
  --------------- ----------

Exemple :

Relancer restaurant

Date :

02/08/2026

# **07.17 --- TABLE : audit_logs**

## **Rôle**

Traçabilité complète.

Structure :

  ------------ ------------
   **Champ**     **Type**

       id          UUID

    user_id        UUID

     action      VARCHAR

     entity      VARCHAR

   entity_id       UUID

   created_at   TIMESTAMP
  ------------ ------------

Exemple :

Utilisateur Julien

Modification score

Restaurant X

26/07

# **07.18 --- Relations principales**

Schéma :

restaurants

\|

\|

+\-\-\-- contacts

\|

+\-\-\-- website_analysis

\|

+\-\-\-- ai_analysis

\|

+\-\-\-- lead_scores

\|

+\-\-\-- crm_pipeline

\|

+\-\-\-- activities

\|

+\-\-\-- tasks

# **07.19 --- Index recommandés**

Pour les performances :

## **Restaurants**

INDEX city

INDEX postal_code

INDEX category

## **Scoring**

INDEX score

INDEX category

## **CRM**

INDEX status

INDEX assigned_user

# **07.20 --- Recherche avancée future**

Prévoir :

## **PostgreSQL Full Text Search**

Pour rechercher :

- noms ;

- descriptions ;

- notes.

## **Extension géographique**

Possibilité future :

**PostGIS**

Pour :

- cartes ;

- rayon ;

- zones commerciales.

# **07.21 --- Gestion des doublons**

Un restaurant peut apparaître plusieurs fois.

Le système doit comparer :

Critères :

- nom ;

- adresse ;

- téléphone ;

- coordonnées GPS ;

- site.

Exemple :

Restaurant trouvé

↓

Comparaison

↓

Probabilité doublon : 96%

↓

Fusion proposée

# **07.22 --- Règles de conservation**

Les données doivent conserver :

- date collecte ;

- source ;

- historique modification ;

- utilisateur responsable.

# **07.23 --- Préparation IA future**

La base doit être compatible avec :

- embeddings ;

- recherche vectorielle ;

- RAG interne.

Evolution possible :

PostgreSQL

\+

pgvector

\+

Base connaissance TableFlash

# **07.24 --- Résumé du modèle**

Le cœur du système :

RESTAURANT

↓

Données publiques

↓

Analyse digitale

↓

Intelligence IA

↓

Score commercial

↓

CRM

↓

Conversion

# **Conclusion Document 07**

Le modèle PostgreSQL de TFLE est conçu pour devenir une véritable base
de connaissance commerciale sur le marché restaurant.

Il permet :

- collecte structurée ;

- historique complet ;

- analyse évolutive ;

- intelligence artificielle ;

- suivi commercial.

La donnée n\'est pas seulement stockée : elle est transformée en
avantage stratégique pour TableFlash.
