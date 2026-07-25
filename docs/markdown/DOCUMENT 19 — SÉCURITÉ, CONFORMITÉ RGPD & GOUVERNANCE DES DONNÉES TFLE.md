# **DOCUMENT 19 --- SÉCURITÉ, CONFORMITÉ RGPD & GOUVERNANCE DES DONNÉES TFLE**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification sécurité + conformité + gouvernance\
Module : Security, Privacy & Data Governance\
Produit : TableFlash Leads Engine\
Usage : Interne uniquement pour TableFlash**

# **19.1 --- Introduction**

Le module **Sécurité, Conformité RGPD & Gouvernance des Données**
définit les règles permettant à TFLE d\'être utilisé comme un outil
professionnel de prospection tout en protégeant :

- les données collectées ;

- les informations commerciales ;

- les accès utilisateurs ;

- l\'historique des actions ;

- les droits des personnes concernées.

L\'objectif :

> Construire un outil puissant de prospection tout en appliquant une
> approche responsable de gestion des données.

# **19.2 --- Principes fondateurs sécurité TFLE**

TFLE repose sur 7 principes.

# **Principe 1 --- Minimisation des données**

TFLE ne collecte que les informations nécessaires.

Exemples utiles :

✅ Nom établissement\
✅ Adresse professionnelle\
✅ Téléphone professionnel\
✅ Email professionnel public\
✅ Site internet\
✅ Informations commerciales utiles

Informations inutiles :

❌ Données personnelles privées\
❌ Informations sans rapport avec la prospection\
❌ Données sensibles

# **Principe 2 --- Traçabilité complète**

Chaque donnée importante doit avoir une origine.

Exemple :

{

\"email\":\"contact@restaurant.fr\",

\"source\":

\"https://restaurant.fr/contact\",

\"collected_at\":

\"2026-07-25\",

\"confidence\":

95

}

# **Principe 3 --- Contrôle humain**

L\'automatisation aide la prospection.

Elle ne doit pas supprimer le contrôle humain.

Exemples :

Validation obligatoire avant :

- campagne importante ;

- suppression massive ;

- changement règles scoring.

# **Principe 4 --- Sécurité par conception**

La sécurité est intégrée dès la conception.

Pas ajoutée après.

# **Principe 5 --- Séparation des responsabilités**

Les modules sont séparés :

Scraping

↓

Data Processing

↓

CRM

↓

IA

↓

Analytics

# **Principe 6 --- Droit à l\'opposition**

Si un établissement demande :

\"Ne plus me contacter\"

TFLE doit pouvoir :

- enregistrer la demande ;

- bloquer les futures actions ;

- conserver une preuve interne.

# **Principe 7 --- Audit permanent**

Toute action importante est enregistrée.

# **19.3 --- Architecture sécurité globale**

UTILISATEUR

↓

AUTHENTIFICATION

↓

API SECURITY LAYER

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

CRM

DATABASE

SCRAPING

IA

ANALYTICS

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

AUDIT LOG SYSTEM

# **19.4 --- Gestion des utilisateurs**

TFLE est un outil interne.

Les comptes sont limités aux personnes autorisées.

# **Rôles utilisateurs**

# **ADMINISTRATEUR**

Accès complet.

Peut :

- gérer utilisateurs ;

- modifier règles ;

- voir toutes les données ;

- configurer IA.

# **COMMERCIAL**

Accès :

- prospects assignés ;

- CRM ;

- tâches ;

- historique commercial.

# **ANALYSTE**

Accès :

- scraping ;

- qualité données ;

- statistiques.

# **LECTURE SEULE**

Accès :

- dashboards ;

- rapports.

# **19.5 --- Authentification**

Architecture recommandée :

## **MVP**

Authentification classique :

- email ;

- mot de passe sécurisé ;

- sessions sécurisées.

## **V1**

Ajout :

- MFA ;

- connexion Google Workspace ;

- gestion organisation.

# **19.6 --- Gestion des permissions**

Principe :

Utilisateur

↓

Rôle

↓

Permissions

↓

Actions autorisées

Exemple :

Commercial :

Autorisé :

Voir prospect

Créer tâche

Ajouter note

Interdit :

Modifier scoring global

Supprimer base prospects

# **19.7 --- Sécurité base de données**

Base recommandée :

PostgreSQL.

Protection :

## **Chiffrement au repos**

Les données stockées sont protégées.

## **Chiffrement en transit**

Toutes les communications utilisent :

HTTPS / TLS

## **Sauvegardes**

Politique :

Sauvegarde quotidienne

\+

Restauration testée régulièrement

# **19.8 --- Protection des emails collectés**

Les emails professionnels collectés doivent être protégés.

Stockage :

Email

\+

Source

\+

Date collecte

\+

Validation

\+

Historique

Exemple :

{

\"email\":\"contact@restaurant.fr\",

\"source_type\":\"website\",

\"verified\":true,

\"do_not_contact\":false

}

# **19.9 --- Gouvernance des données**

Chaque donnée possède un cycle de vie.

Cycle :

Collecte

↓

Validation

↓

Utilisation

↓

Historique

↓

Archivage

↓

Suppression

# **19.10 --- Classification des données**

TFLE classe les données.

# **Niveau 1 --- Public professionnel**

Exemples :

- nom restaurant ;

- adresse établissement ;

- site internet.

# **Niveau 2 --- Commercial**

Exemples :

- historique contact ;

- notes commerciales ;

- échanges.

# **Niveau 3 --- Interne stratégique**

Exemples :

- scoring ;

- prédictions IA ;

- analyses conversion.

# **19.11 --- Conservation des données**

Politique configurable.

Exemple :

## **Prospect non qualifié**

Conservation limitée.

## **Prospect contacté**

Conservation historique commercial.

## **Client**

Conservation longue durée nécessaire au suivi commercial.

## **Prospect opposé**

Conservation minimale :

Objectif :

empêcher une nouvelle sollicitation.

# **19.12 --- Gestion suppression données**

Fonction :

Supprimer prospect

Processus :

1.  Vérification demande.

2.  Suppression données non nécessaires.

3.  Conservation éventuelle preuve opposition.

4.  Journalisation action.

# **19.13 --- Liste d\'exclusion**

Table essentielle :

do_not_contact

Structure :

id

restaurant_id

reason

created_at

source_request

Exemple :

{

\"restaurant_id\":5421,

\"reason\":

\"Demande de retrait\",

\"created_at\":

\"2026-07-25\"

}

# **19.14 --- Audit Log System**

Chaque événement important est enregistré.

Exemples :

Connexion utilisateur

Modification prospect

Export données

Suppression fiche

Modification scoring

Action IA

Table :

audit_logs

Structure :

id

user_id

action

entity

entity_id

timestamp

metadata

Exemple :

{

\"user\":\"admin\",

\"action\":

\"UPDATE_SCORE\",

\"restaurant_id\":

1234

}

# **19.15 --- Sécurité API**

Toutes les API doivent appliquer :

# **Authentification**

Chaque requête nécessite une identité valide.

# **Autorisation**

Vérification rôle utilisateur.

# **Validation entrées**

Protection contre :

- injections ;

- données incorrectes ;

- appels abusifs.

# **Rate Limiting**

Protection contre :

- abus ;

- erreurs scripts ;

- attaques.

# **19.16 --- Sécurité Scraping Engine**

Le scraper doit intégrer :

## **Respect des règles techniques**

Gestion :

- fréquence requêtes ;

- erreurs ;

- limitations serveur.

## **Identification source**

Chaque donnée garde :

URL source

Date collecte

Méthode extraction

## **Pas de collecte excessive**

Le système évite :

- duplication inutile ;

- surcharge sources.

# **19.17 --- Sécurité Intelligence Artificielle**

L\'IA représente un risque particulier.

# **Risque 1**

Hallucination.

Solution :

- sources ;

- confiance ;

- validation.

# **Risque 2**

Fuite informations internes.

Solution :

- isolation contexte ;

- contrôle accès ;

- filtrage données.

# **Risque 3**

Actions automatiques incorrectes.

Solution :

Validation humaine.

# **19.18 --- Gouvernance des prompts IA**

Les prompts système sont considérés comme des éléments stratégiques.

Gestion :

- versioning ;

- historique ;

- validation modification.

Table :

ai_prompt_versions

Structure :

id

agent

version

content

created_by

created_at

# **19.19 --- Protection secrets techniques**

Les éléments sensibles :

- clés API ;

- tokens ;

- mots de passe ;

- accès services.

Ne doivent jamais être stockés :

❌ dans le code source\
❌ dans GitHub public\
❌ dans les fichiers frontend

Utilisation :

Variables environnement

Secret Manager

Vault

# **19.20 --- Sauvegarde et récupération**

Politique recommandée :

## **Base principale**

Sauvegarde quotidienne.

## **Fichiers importants**

Sauvegarde :

- documents IA ;

- prompts ;

- configurations.

## **Test restauration**

Régulièrement.

Une sauvegarde non testée n\'est pas une vraie sauvegarde.

# **19.21 --- Monitoring sécurité**

Dashboard sécurité :

KPI :

Tentatives connexion

Actions sensibles

Erreurs API

Exports réalisés

Suppressions

Alertes sécurité

# **19.22 --- Gestion incidents**

Procédure :

## **Étape 1**

Détection.

## **Étape 2**

Blocage.

## **Étape 3**

Analyse.

## **Étape 4**

Correction.

## **Étape 5**

Documentation.

# **19.23 --- Architecture technique recommandée**

## **Frontend**

React + TypeScript

Gestion permissions UI

## **Backend**

API sécurisée

Validation

Authentification

## **Base**

PostgreSQL

Row Level Security

## **Infrastructure**

HTTPS

Secrets Manager

Logs centralisés

# **19.24 --- Modèle données sécurité**

## **users**

id

email

role

status

created_at

## **permissions**

id

role

action

allowed

## **audit_logs**

id

user_id

event

timestamp

metadata

## **data_requests**

id

restaurant_id

type

status

created_at

# **19.25 --- MVP Sécurité**

Obligatoire :

✅ Authentification.

✅ Gestion rôles.

✅ Logs actions.

✅ Sauvegardes.

✅ Liste exclusion.

✅ Traçabilité sources.

# **19.26 --- Version 1**

Ajouts :

- MFA ;

- monitoring avancé ;

- politique automatique conservation ;

- audits réguliers.

# **19.27 --- Version 2**

Vision :

Un système auto-surveillé.

L\'IA sécurité peut :

- détecter anomalies ;

- recommander corrections ;

- surveiller conformité.

# **19.28 --- Architecture finale sécurité**

TFLE

\|

SECURITY GOVERNANCE

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Identity Management

Data Protection

Compliance Engine

Audit System

AI Security

Backup System

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\|

Données protégées

# **Conclusion Document 19**

La puissance de TFLE repose sur sa capacité à exploiter intelligemment
des données professionnelles.

Mais une plateforme de prospection sérieuse doit être construite avec
une règle fondamentale :

> La donnée est un actif stratégique qui doit être utilisée avec
> méthode, transparence et contrôle.

La sécurité et la conformité ne sont pas un frein au projet.

Elles permettent de construire un outil durable, professionnel et
exploitable à long terme.
