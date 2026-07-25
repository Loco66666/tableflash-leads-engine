# **DOCUMENT 35 --- SPRINT 2 TFLE**

# **Module Restaurant Database & Lead Management**

**Version : 1.0\
Statut : Plan d\'exécution développement Sprint 2\
Module : Core Data Platform & Lead Management\
Produit : TableFlash Leads Engine (TFLE)\
Durée estimée : 10 jours ouvrés\
Objectif : Créer le premier véritable module métier TFLE**

# **35.1 --- Objectif du Sprint 2**

Le Sprint 1 a construit les fondations :

Repository

↓

Frontend

↓

Backend

↓

Database

↓

Authentification

Le Sprint 2 donne une première utilité commerciale au produit.

À la fin de ce sprint, TFLE doit permettre :

Découvrir un restaurant

↓

Créer sa fiche

↓

Stocker ses informations

↓

Rechercher

↓

Filtrer

↓

Créer un prospect

↓

Suivre son statut

# **35.2 --- Résultat attendu**

Version :

TFLE v0.2.0

Fonctionnalités disponibles :

✅ Base restaurants\
✅ Création manuelle restaurant\
✅ Import initial CSV\
✅ Recherche intelligente\
✅ Filtres commerciaux\
✅ Fiche restaurant complète\
✅ Conversion restaurant → lead\
✅ Première gestion pipeline

# **35.3 --- Périmètre Sprint 2**

## **Inclus**

  -------------------- --------------
   **Fonctionnalité**   **Priorité**

   Modèle Restaurant         P0

    CRUD Restaurant          P0

    Interface liste          P0

       Recherche             P0

        Filtres              P1

       Import CSV            P1

     Création Lead           P0

  Statuts commerciaux        P0

       Historique            P1
     modifications     
  -------------------- --------------

## **Hors périmètre**

❌ Scraping automatique avancé\
❌ IA scoring\
❌ Emails automatiques\
❌ Agents IA commerciaux

Ces modules arriveront après.

# **35.4 --- Architecture Sprint 2**

Nouvelle architecture :

TFLE

Frontend

↓

Restaurant Module

Backend

↓

Restaurant Service

Database

↓

restaurants table

↓

leads table

# **35.5 --- Nouveau module Backend**

Création :

backend/app/

├── restaurants/

│

│ ├── router.py

│ ├── service.py

│ ├── models.py

│ ├── schemas.py

│ └── repository.py

│

├── leads/

│

│ ├── router.py

│ ├── service.py

│ └── schemas.py

# **35.6 --- Modèle Database Restaurant**

## **Table restaurants**

Structure complète MVP :

restaurants

id

name

description

category

address

city

postal_code

country

phone

email

website

instagram

facebook

source

source_url

status

created_at

updated_at

# **Explication des champs**

## **Informations identité**

name

category

description

Permet :

- identifier ;

- classifier ;

- préparer analyse future.

## **Localisation**

address

city

postal_code

country

Permet :

- recherche géographique ;

- campagnes locales.

## **Contacts**

phone

email

website

Permet :

- qualification ;

- prospection.

## **Source**

source

source_url

Important pour :

- traçabilité ;

- conformité ;

- analyse qualité données.

# **35.7 --- Migration PostgreSQL**

Créer migration :

alembic revision \--autogenerate -m \"create restaurants table\"

Appliquer :

alembic upgrade head

# **35.8 --- Ticket TFLE-100**

# **Création modèle Restaurant**

Priorité :

P0

## **Objectif**

Créer le modèle SQLAlchemy.

Fichier :

backend/app/restaurants/models.py

Structure :

class Restaurant(Base):

\_\_tablename\_\_ = \"restaurants\"

id = Column(UUID, primary_key=True)

name = Column(String)

city = Column(String)

email = Column(String)

website = Column(String)

created_at = Column(DateTime)

## **Critères validation**

✅ Table créée\
✅ Migration fonctionnelle\
✅ Connexion DB OK

# **Prompt Claude Code TFLE-100**

Tu travailles sur TFLE Sprint 2.

Implémente uniquement le modèle Restaurant.

Respecte :

\- architecture Document 31

\- séparation model/schema/service

\- SQLAlchemy

\- migrations Alembic

Avant modification :

1\. Liste les fichiers impactés

2\. Explique le choix technique

3\. Attends validation

# **35.9 --- Ticket TFLE-110**

# **API CRUD Restaurants**

Priorité :

P0

Créer routes :

## **GET liste**

GET /api/v1/restaurants

Réponse :

\[

{

\"id\":\"123\",

\"name\":\"Restaurant Exemple\",

\"city\":\"Bayonne\"

}

\]

## **GET détail**

GET /restaurants/{id}

## **POST création**

POST /restaurants

Exemple :

{

\"name\":\"Chez Pierre\",

\"city\":\"Bayonne\",

\"email\":\"contact@restaurant.fr\"

}

## **PUT modification**

PUT /restaurants/{id}

## **DELETE**

DELETE /restaurants/{id}

# **Critères validation**

✅ Toutes les routes fonctionnent\
✅ Validation Pydantic active\
✅ Erreurs gérées

# **Prompt Claude Code TFLE-110**

Crée le module API Restaurant TFLE.

Contraintes :

\- FastAPI Router

\- Service layer obligatoire

\- Validation Pydantic

\- Gestion erreurs HTTP propre

Ne mélange pas logique API et base de données.

# **35.10 --- Ticket TFLE-120**

# **Interface Restaurant Management**

Priorité :

P0

Créer pages :

/restaurants

Liste.

/restaurants/new

Création.

/restaurants/:id

Détail.

# **Composants**

Créer :

RestaurantTable

RestaurantForm

RestaurantCard

RestaurantDetail

# **Affichage liste**

Colonnes :

  -----------
   **Champ**

      Nom

     Ville

     Email

    Source

    Statut
  -----------

# **Critères validation**

✅ Navigation fonctionnelle\
✅ Création restaurant depuis interface\
✅ Modification possible

# **Prompt Claude Code TFLE-120**

Crée le module frontend Restaurant.

Objectif :

Une interface professionnelle interne TableFlash.

Contraintes :

\- React TypeScript

\- composants réutilisables

\- aucune donnée fictive

\- appels API uniquement

Ne crée pas encore de scoring.

# **35.11 --- Ticket TFLE-130**

# **Recherche Restaurants**

Priorité :

P0

Objectif :

Trouver rapidement un restaurant.

Recherche sur :

- nom ;

- ville ;

- email ;

- catégorie.

API :

GET /restaurants?search=bayonne

Exemple :

Recherche :

pizza bayonne

Résultat :

10 restaurants

# **Index PostgreSQL**

Créer :

CREATE INDEX idx_restaurant_name

ON restaurants(name);

# **Critères validation**

✅ Recherche instantanée\
✅ Résultats pertinents

# **35.12 --- Ticket TFLE-140**

# **Système de filtres**

Priorité :

P1

Filtres :

## **Localisation**

Ville

Département

Région

## **Type restaurant**

Brasserie

Burger

Pizza

Kebab

Gastronomique

## **Statut**

Nouveau

Contacté

Client

# **Interface**

Créer :

FilterSidebar

# **35.13 --- Ticket TFLE-150**

# **Import CSV Restaurants**

Priorité :

P1

Objectif :

Importer rapidement une liste.

Format accepté :

CSV

Colonnes :

name,address,city,email,phone

Workflow :

Upload fichier

↓

Validation

↓

Prévisualisation

↓

Import

↓

Confirmation

# **Protection**

Avant import :

Détecter doublons.

# **35.14 --- Module Lead Management**

Le restaurant devient un prospect.

Relation :

Restaurant

1

↓

1

Lead

# **Table leads**

leads

id

restaurant_id

status

priority

assigned_to

created_at

updated_at

# **Statuts MVP**

NEW

QUALIFIED

CONTACTED

DEMO

TRIAL

CUSTOMER

LOST

# **35.15 --- Ticket TFLE-160**

# **Création automatique Lead**

Priorité :

P0

Action :

Bouton :

Créer prospect

Workflow :

Restaurant :

Restaurant trouvé

↓

Bouton

↓

Lead créé :

NEW

# **Critères validation**

✅ Un restaurant peut devenir prospect\
✅ Statut initial correct\
✅ Historique conservé

# **35.16 --- Ticket TFLE-170**

# **Pipeline commercial initial**

Priorité :

P0

Créer page :

/pipeline

Vue :

Kanban.

Colonnes :

Nouveau

Contacté

Démo

Essai

Client

Composants :

LeadCard

PipelineColumn

PipelineBoard

# **35.17 --- Historique des actions**

Priorité :

P1

Table :

lead_events

Champs :

id

lead_id

action

description

created_at

Exemple :

25/07

Email envoyé

Premier contact TableFlash

# **35.18 --- Tests Sprint 2**

## **Backend**

Tester :

- création restaurant ;

- modification ;

- suppression ;

- recherche ;

- création lead.

## **Frontend**

Tester :

- formulaire ;

- tableau ;

- filtres.

## **Base**

Tester :

- migrations ;

- contraintes.

# **35.19 --- Planning Sprint 2**

## **Jour 1**

Modèle Restaurant

## **Jour 2**

Migration DB

## **Jour 3**

API CRUD

## **Jour 4**

Frontend liste restaurants

## **Jour 5**

Formulaire création/modification

## **Jour 6**

Recherche

## **Jour 7**

Filtres

## **Jour 8**

Import CSV

## **Jour 9**

Lead Management

## **Jour 10**

Tests + correction

# **35.20 --- Definition of Done Sprint 2**

Sprint terminé lorsque :

## **Base données**

✅ Table restaurants\
✅ Table leads\
✅ Relations fonctionnelles

## **Backend**

✅ CRUD complet\
✅ Recherche\
✅ API documentée

## **Frontend**

✅ Liste restaurants\
✅ Création\
✅ Modification\
✅ Pipeline

## **Commercial**

✅ Premier prospect suivi dans TFLE

# **35.21 --- Résultat business après Sprint 2**

À partir de ce moment, TableFlash possède :

Une vraie base commerciale interne.

Le workflow devient :

Restaurant trouvé manuellement

↓

Ajout TFLE

↓

Qualification humaine

↓

Création prospect

↓

Suivi commercial
