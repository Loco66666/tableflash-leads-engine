# **DOCUMENT 11 --- SPÉCIFICATIONS API BACKEND**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification technique Backend\
Produit : TableFlash Leads Engine\
Architecture : API REST + Services métiers + Workers**

# **11.1 --- Introduction**

Ce document définit l\'ensemble des interfaces API utilisées par TFLE.

L\'API Backend est le cœur du système.

Elle assure :

- la communication Frontend ↔ Backend ;

- la gestion des utilisateurs ;

- la gestion des restaurants ;

- l\'analyse digitale ;

- le scoring ;

- l\'intelligence artificielle ;

- le CRM ;

- les statistiques.

# **11.2 --- Architecture API globale**

FRONTEND TFLE

\|

\|

API BACKEND

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\| \| \| \|

Auth Restaurants Analysis CRM

\| \| \|

Users Data AI Engine

\|

PostgreSQL

\|

Workers

# **11.3 --- Convention générale API**

## **URL principale**

Exemple :

https://api.tableflash-leads.com/v1

# **Format des réponses**

Toutes les réponses utilisent JSON.

## **Réponse succès standard**

{

\"success\": true,

\"data\": {},

\"message\": \"Operation completed\"

}

## **Réponse erreur standard**

{

\"success\": false,

\"error\": {

\"code\": \"RESOURCE_NOT_FOUND\",

\"message\": \"Restaurant introuvable\"

}

}

# **11.4 --- Authentification**

## **Méthode**

JWT Token.

Flux :

Utilisateur

↓

Connexion

↓

Validation

↓

Création JWT

↓

Accès API

# **Header obligatoire**

Authorization: Bearer TOKEN

# **11.5 --- Gestion utilisateurs**

# **POST /auth/login**

## **Objectif**

Connexion utilisateur.

## **Request**

{

\"email\": \"admin@tableflash.fr\",

\"password\": \"\*\*\*\*\*\*\*\*\"

}

## **Response**

{

\"success\": true,

\"data\": {

\"token\": \"jwt_token\",

\"user\": {

\"id\": \"123\",

\"name\": \"Admin\",

\"role\": \"ADMIN\"

}

}

}

# **POST /auth/logout**

Déconnexion.

# **GET /auth/me**

Retourne l\'utilisateur connecté.

Response :

{

\"id\":\"123\",

\"name\":\"Julien\",

\"role\":\"ADMIN\"

}

# **11.6 --- Permissions**

## **Rôles**

# **ADMIN**

Accès complet :

- utilisateurs ;

- scoring ;

- paramètres ;

- données.

# **COMMERCIAL**

Accès :

- prospects ;

- CRM ;

- analyses.

# **ANALYST**

Accès :

- recherche ;

- collecte ;

- validation données.

# **Matrice permissions**

  --------------- ----------- ---------------- -------------
    **Action**     **Admin**   **Commercial**   **Analyst**

       Voir           ✅             ✅             ✅
    restaurants                                

     Modifier         ✅             ✅             ✅
    restaurant                                 

     Modifier         ✅             ❌             ❌
      scoring                                  

      Gestion         ✅             ❌             ❌
   utilisateurs                                

        CRM           ✅             ✅           Lecture
  --------------- ----------- ---------------- -------------

# **11.7 --- API RESTAURANTS**

Module central TFLE.

# **GET /restaurants**

## **Objectif**

Liste des prospects.

## **Query Parameters**

Exemple :

?page=1

&limit=50

&city=Bayonne

&score_min=80

&status=CONTACTED

## **Response**

{

\"success\":true,

\"data\":\[

{

\"id\":\"abc123\",

\"name\":\"Chez Marcel\",

\"city\":\"Bayonne\",

\"score\":91,

\"status\":\"TO_CONTACT\"

}

\]

}

# **GET /restaurants/{id}**

## **Objectif**

Voir une fiche complète.

Response :

{

\"id\":\"123\",

\"name\":\"Chez Marcel\",

\"address\":\"Bayonne\",

\"website\":\"https://site.fr\",

\"score\":91,

\"crm_status\":\"CONTACTED\"

}

# **POST /restaurants**

## **Objectif**

Créer manuellement un restaurant.

Request :

{

\"name\":\"Chez Pierre\",

\"city\":\"Anglet\",

\"website\":\"https://site.fr\"

}

# **PATCH /restaurants/{id}**

Modification.

Exemple :

{

\"phone\":\"0559000000\"

}

# **DELETE /restaurants/{id}**

Suppression logique.

Le restaurant passe :

ACTIVE

↓

ARCHIVED

# **11.8 --- API RECHERCHE / DISCOVERY ENGINE**

# **POST /discovery/search**

## **Objectif**

Lancer une recherche restaurants.

Request :

{

\"city\":\"Bayonne\",

\"radius\":30,

\"category\":\[

\"restaurant_traditional\"

\]

}

Response :

{

\"job_id\":\"98765\",

\"status\":\"RUNNING\"

}

# **GET /discovery/jobs/{id}**

Suivi.

Response :

{

\"status\":\"RUNNING\",

\"found\":250,

\"processed\":120

}

# **11.9 --- API ANALYSE DIGITALE**

# **POST /analysis/website/{restaurant_id}**

## **Objectif**

Analyser un site.

Response :

{

\"job_id\":\"555\",

\"status\":\"QUEUED\"

}

# **GET /analysis/{restaurant_id}**

Retour analyse.

Response :

{

\"website\":true,

\"mobile\":true,

\"menu_type\":\"PDF\",

\"qr_detected\":false,

\"ordering\":false

}

# **11.10 --- API SCORING**

# **POST /scoring/run/{restaurant_id}**

Calcul du score.

Response :

{

\"score\":92,

\"category\":\"HIGH\",

\"reasons\":\[

\"Pas de QR Code\",

\"Menu PDF\",

\"Restaurant indépendant\"

\]

}

# **GET /scoring/rules**

Retour règles actuelles.

# **POST /scoring/rules**

Création règle.

Request :

{

\"name\":\"Menu PDF\",

\"condition\":{

\"menu_type\":\"PDF\"

},

\"points\":15

}

# **11.11 --- API INTELLIGENCE IA**

# **POST /ai/analyze/{restaurant_id}**

## **Objectif**

Créer une analyse commerciale.

Response :

{

\"status\":\"PROCESSING\",

\"job_id\":\"444\"

}

# **GET /ai/result/{restaurant_id}**

Response :

{

\"summary\":

\"Restaurant avec potentiel élevé\",

\"opportunity\":

\"HIGH\",

\"arguments\":\[

\"Moderniser la carte\",

\"Améliorer expérience client\"

\]

}

# **POST /ai/generate-message**

## **Objectif**

Créer un message commercial.

Request :

{

\"restaurant_id\":\"123\",

\"type\":\"email\"

}

Response :

{

\"message\":

\"Bonjour, nous avons remarqué\...\"

}

# **11.12 --- API CRM**

# **GET /crm/pipeline**

Retour Kanban.

Response :

{

\"new\":120,

\"contacted\":40,

\"trial\":8,

\"customer\":5

}

# **PATCH /crm/{restaurant_id}/status**

Modification statut.

Request :

{

\"status\":\"DEMO\"

}

Actions automatiques :

Création :

- historique ;

- timestamp ;

- utilisateur.

# **POST /crm/activity**

Créer activité.

Request :

{

\"restaurant_id\":\"123\",

\"type\":\"CALL\",

\"note\":\"Intéressé par essai gratuit\"

}

# **GET /crm/history/{restaurant_id}**

Historique complet.

# **11.13 --- API TÂCHES**

# **GET /tasks**

Liste tâches.

Filtres :

?status=pending

&date=today

# **POST /tasks**

Création.

Request :

{

\"restaurant_id\":\"123\",

\"title\":\"Relancer restaurant\",

\"due_date\":\"2026-08-01\"

}

# **PATCH /tasks/{id}**

Modification.

# **11.14 --- API STATISTIQUES**

# **GET /analytics/dashboard**

Retour données principales.

Response :

{

\"restaurants_total\":12540,

\"qualified\":1850,

\"trials\":46,

\"customers\":12

}

# **GET /analytics/conversion**

Retour tunnel commercial.

Response :

{

\"contacted\":200,

\"demo\":50,

\"trial\":20,

\"customers\":8

}

# **GET /analytics/zones**

Performance géographique.

Response :

\[

{

\"city\":\"Bayonne\",

\"prospects\":450,

\"conversion\":12

}

\]

# **11.15 --- API ADMINISTRATION**

# **GET /admin/users**

Liste utilisateurs.

# **POST /admin/users**

Créer utilisateur.

# **PATCH /admin/users/{id}**

Modifier rôle.

# **GET /admin/logs**

Voir historique système.

Response :

{

\"user\":\"Admin\",

\"action\":\"UPDATE_SCORE\",

\"date\":\"2026-07-25\"

}

# **11.16 --- Gestion des tâches longues**

Certaines opérations ne doivent jamais bloquer l\'API.

Exemples :

- scraping ;

- analyse milliers de sites ;

- génération IA.

Architecture :

API

↓

Création Job

↓

Worker

↓

Traitement

↓

Résultat disponible

Table jobs :

{

\"id\":\"123\",

\"type\":\"WEBSITE_ANALYSIS\",

\"status\":\"RUNNING\",

\"progress\":65

}

# **11.17 --- Webhooks futurs**

Préparation intégrations :

Exemple :

Restaurant devient client

↓

Webhook

↓

CRM externe

# **11.18 --- Sécurité API**

Mesures obligatoires :

## **Rate limiting**

Protection :

- scraping abusif ;

- attaques API.

## **Validation données**

Toutes les entrées doivent être validées.

## **Logs**

Chaque action importante est enregistrée.

## **Secrets**

Jamais dans le code.

Utilisation :

.env

Secret Manager

# **11.19 --- Versioning API**

Toutes les routes possèdent une version.

Exemple :

/api/v1/restaurants

Future :

/api/v2/restaurants

# **11.20 --- Tests API**

Chaque endpoint doit posséder :

## **Test succès**

Exemple :

Création restaurant.

## **Test erreur**

Exemple :

Email invalide.

## **Test permission**

Exemple :

Commercial tente modifier scoring.

# **11.21 --- Architecture finale Backend**

FRONTEND

\|

REST API

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Auth

Restaurants

Discovery

Analysis

Scoring

AI

CRM

Analytics

Admin

\|

PostgreSQL

\|

Worker Queue

\|

Scraping + IA

# **Conclusion Document 11**

L\'API Backend TFLE est conçue comme une plateforme modulaire.

Elle permet :

- une séparation claire des responsabilités ;

- une évolution progressive ;

- l\'intégration future d\'agents IA ;

- une automatisation complète de la prospection.

Le principe directeur :

> Le Frontend demande.\
> Le Backend décide.\
> Les Workers exécutent.\
> La base conserve la connaissance.
