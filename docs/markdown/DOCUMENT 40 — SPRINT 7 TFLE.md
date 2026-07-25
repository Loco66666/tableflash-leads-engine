# **DOCUMENT 40 --- SPRINT 7 TFLE**

# **Campaign Engine, Automatisation Prospection & Séquences Commerciales Multicanal**

**Version : 1.0\
Statut : Plan d\'exécution développement Sprint 7\
Module : Sales Automation & Campaign Intelligence Engine\
Produit : TableFlash Leads Engine (TFLE)\
Durée estimée : 20 jours ouvrés\
Objectif : Transformer le CRM TFLE en moteur d\'acquisition commerciale
automatisé capable de piloter des campagnes de prospection ciblées**

# **40.1 --- Vision du Sprint 7**

Les précédents sprints ont construit :

Sprint 1

Infrastructure

↓

Sprint 2

Restaurant Database + CRM initial

↓

Sprint 3

Discovery Engine

↓

Sprint 4

Enrichissement + Qualification

↓

Sprint 5

IA commerciale

↓

Sprint 6

CRM + Pipeline + Essais gratuits

TFLE sait maintenant :

✅ trouver des restaurants\
✅ analyser leur potentiel\
✅ créer des prospects\
✅ organiser le suivi commercial\
✅ suivre les essais TableFlash

Mais le commercial reste encore trop manuel.

Le Sprint 7 introduit :

**la machine commerciale automatisée.**

# **40.2 --- Nouveau workflow TFLE**

Avant :

Prospect identifié

↓

Commercial décide quoi faire

↓

Contact manuel

↓

Relances manuelles

Après Sprint 7 :

Segment restaurants

↓

Créer campagne

↓

Séquence commerciale automatique

↓

Messages personnalisés IA

↓

Actions commerciales

↓

Suivi performances

↓

Optimisation

# **40.3 --- Objectif business**

À la fin du Sprint 7, TableFlash doit pouvoir :

> Sélectionner une catégorie de restaurants, lancer une campagne adaptée
> et mesurer automatiquement les résultats.

Exemple :

Campagne :

Restaurants traditionnels Bayonne

Cible :

100 prospects

Séquence :

Email 1

↓

Relance J+3

↓

Appel J+7

↓

Proposition essai J+14

Résultat :

15 réponses

3 démos

1 client

# **40.4 --- Résultat attendu**

Version :

TFLE v0.7.0

Fonctionnalités :

✅ Création campagnes commerciales\
✅ Segmentation prospects\
✅ Séquences automatiques\
✅ Templates messages\
✅ Personnalisation IA\
✅ Suivi performances\
✅ A/B testing messages\
✅ Attribution conversion

# **40.5 --- Architecture Sprint 7**

Nouvelle architecture :

backend/app/

├── campaigns/

│

│ ├── models.py

│ ├── service.py

│ ├── router.py

│

├── sequences/

│

│ ├── engine.py

│ ├── steps.py

│

├── messaging/

│

│ ├── templates.py

│ ├── generator.py

│

├── analytics/

│

│ └── campaign_metrics.py

# **40.6 --- Concept Campaign Engine**

Une campagne est un ensemble organisé :

Campagne

↓

Audience

↓

Séquence

↓

Actions

↓

Résultats

Exemple :

Nom :

Bayonne Restaurants Traditionnels

Audience :

Restaurants indépendants

Rayon 30 km

Objectif :

Obtenir essais gratuits TableFlash

# **40.7 --- Nouveau modèle Database**

## **Table campaigns**

Stocke les campagnes.

campaigns

id

name

description

type

status

target_segment

created_by

created_at

updated_at

Types :

EMAIL

PHONE

MULTI_CHANNEL

LOCAL

Statuts :

DRAFT

ACTIVE

PAUSED

COMPLETED

ARCHIVED

# **40.8 --- Table campaign_targets**

Restaurants appartenant à une campagne.

campaign_targets

id

campaign_id

lead_id

status

added_at

Statuts :

PENDING

CONTACTED

RESPONDED

CONVERTED

FAILED

# **40.9 --- Table sequences**

Définit les scénarios.

sequences

id

campaign_id

name

active

created_at

Exemple :

Séquence Restaurant Traditionnel

# **40.10 --- Table sequence_steps**

Les étapes de la séquence.

sequence_steps

id

sequence_id

order_number

action_type

delay_days

template_id

Exemple :

Étape 1

EMAIL

Jour 0

Étape 2

RELANCE

Jour 3

Étape 3

APPEL

Jour 7

# **40.11 --- EPIC 01**

# **Campaign Management**

Priorité :

## **P0**

Objectif :

Créer et gérer des campagnes.

Nouvelle page :

/campaigns

Fonctions :

Créer :

Nom campagne

Objectif

Audience

Séquence

Afficher :

Campagne

Nombre prospects

Statut

Résultats

Composants :

CampaignList

CampaignCard

CampaignBuilder

CampaignStats

# **Ticket TFLE-600**

Créer module campagnes.

Critères validation :

✅ Création campagne\
✅ Modification\
✅ Activation / pause

# **Prompt Claude Code TFLE-600**

Tu travailles sur TFLE Sprint 7.

Implémente le Campaign Engine.

Contraintes :

\- architecture backend existante

\- séparation service/API/database

\- aucune automatisation réelle avant validation

Créer uniquement le socle campagne.

# **40.12 --- EPIC 02**

# **Segmentation intelligente des restaurants**

Priorité :

## **P0**

Objectif :

Choisir les bons prospects.

Filtres disponibles :

## **Localisation**

Ville

Département

Rayon GPS

## **Profil restaurant**

Brasserie

Burger

Pizza

Kebab

Gastronomique

## **Maturité digitale**

Sans site

Site ancien

Pas de commande en ligne

## **Score commercial**

80-100

60-80

\<60

# **Exemple segment :**

Restaurants indépendants

Bayonne + 20 km

Score \>80

Sans commande digitale

# **40.13 --- EPIC 03**

# **Sequence Engine**

Priorité :

## **P0**

Objectif :

Créer un moteur d\'exécution des étapes.

Architecture :

Sequence Engine

Lit étapes

↓

Vérifie dates

↓

Déclenche action

↓

Enregistre résultat

Exemple :

Prospect ajouté :

01/08

Aujourd\'hui :

04/08

Action :

Créer relance

# **Table execution_logs**

execution_logs

id

sequence_step_id

lead_id

status

executed_at

result

# **40.14 --- EPIC 04**

# **Templates commerciaux**

Priorité :

## **P0**

Objectif :

Créer une bibliothèque de messages.

Table :

message_templates

id

name

channel

content

variables

created_at

Variables dynamiques :

{{restaurant_name}}

{{city}}

{{owner_name}}

{{opportunity_reason}}

Exemple :

Bonjour {{owner_name}},

Nous avons remarqué que votre restaurant

à {{city}} ne propose pas encore de commande

directe par QR code\...

# **40.15 --- EPIC 05**

# **Personnalisation IA automatique**

Priorité :

## **P1**

L\'IA intervient ici.

Workflow :

Template général

↓

Données restaurant

↓

Analyse IA

↓

Message personnalisé

Exemple :

Avant :

Bonjour restaurant,

nous proposons une solution digitale.

Après :

Bonjour Jean,

J\'ai vu que votre établissement à Bayonne

fonctionne principalement sur place.

TableFlash permettrait à vos clients

de commander directement depuis leur table.

# **40.16 --- Agent IA Campaign Writer**

Nouvel agent :

campaign_writer_agent

Mission :

Créer :

- emails ;

- scripts appels ;

- messages personnalisés.

Prompt système :

Tu es l\'assistant commercial TableFlash.

Tu dois créer des messages professionnels,

courts et personnalisés.

Tu utilises uniquement les informations

fournies.

Tu ne dois jamais inventer.

# **40.17 --- EPIC 06**

# **Multi-channel Outreach**

Priorité :

## **P1**

Canaux :

EMAIL

PHONE

NOTE CRM

TASK

Architecture future :

EMAIL

↓

SMS

↓

LinkedIn

↓

Téléphone

Sprint 7 MVP :

Seulement orchestration.

Pas d\'envoi massif automatique.

# **40.18 --- EPIC 07**

# **A/B Testing commercial**

Priorité :

## **P2**

Objectif :

Optimiser les messages.

Exemple :

Version A :

Augmentez vos commandes directes

Version B :

Réduisez votre dépendance aux plateformes

Mesures :

Taux ouverture

Taux réponse

Conversion

# **40.19 --- Analytics Campagnes**

Priorité :

## **P0**

Nouvelle page :

/campaigns/:id/analytics

KPI :

## **Acquisition**

Prospects ciblés

Contacts réalisés

Réponses

## **Conversion**

Démos

Essais

Clients

## **Performance**

Taux réponse

Coût acquisition

Temps conversion

# **40.20 --- API Sprint 7**

## **Créer campagne**

POST /campaigns

## **Ajouter prospects**

POST /campaigns/{id}/targets

## **Lancer campagne**

POST /campaigns/{id}/activate

## **Générer message IA**

POST /campaigns/{id}/generate-message

## **Statistiques**

GET /campaigns/{id}/analytics

# **40.21 --- Tests Sprint 7**

## **Tests campagnes**

Vérifier :

- création ;

- activation ;

- arrêt.

## **Tests séquences**

Vérifier :

- ordre étapes ;

- délais ;

- logs.

## **Tests IA**

Vérifier :

- personnalisation ;

- absence invention.

## **Tests conversion**

Vérifier :

Prospect

↓

Campagne

↓

Contact

↓

Essai

↓

Client

# **40.22 --- Planning Sprint 7**

## **Jour 1-4**

Campaign Engine

## **Jour 5-7**

Segmentation

## **Jour 8-10**

Sequence Engine

## **Jour 11-12**

Templates commerciaux

## **Jour 13-15**

IA personnalisation

## **Jour 16-17**

Analytics

## **Jour 18-20**

Tests + optimisation

# **40.23 --- Definition of Done Sprint 7**

Le sprint est terminé lorsque :

## **Campagnes**

✅ Création campagnes\
✅ Segmentation prospects\
✅ Séquences configurables

## **Automatisation**

✅ Actions déclenchées automatiquement\
✅ Historique complet

## **IA**

✅ Messages personnalisés générés

## **Business**

✅ TableFlash peut lancer une campagne complète

# **40.24 --- Résultat opérationnel après Sprint 7**

Avant :

TFLE aide le commercial

Après :

TFLE pilote l\'acquisition commerciale

Workflow :

Choisir cible

↓

Créer campagne

↓

Sélection automatique prospects

↓

IA prépare messages

↓

Commercial valide

↓

Séquence démarre

↓

Résultats mesurés

↓

Optimisation

# **40.25 --- Positionnement TFLE après Sprint 7**

TFLE devient :

## **Une plateforme interne d\'acquisition commerciale TableFlash**

Capable de gérer :

Découverte

↓

Qualification

↓

Intelligence IA

↓

CRM

↓

Campagnes

↓

Conversion

# **40.26 --- Préparation Sprint 8**

## **DOCUMENT 41 --- Sprint 8 TFLE : Data Intelligence Platform, Analytics Avancés & Pilotage Stratégique**

Objectif :

Passer de :

Machine commerciale automatisée

à :

Système décisionnel complet

↓

Analyse marché restaurants

↓

Prévisions acquisition

↓

Optimisation ROI

↓

Pilotage stratégique TableFlash

Ce sprint transformera TFLE d\'un outil commercial en **véritable centre
de renseignement stratégique pour la croissance de TableFlash**.
