# **DOCUMENT 39 --- SPRINT 6 TFLE**

# **CRM Commercial Avancé, Automatisation Relances & Pipeline 30 jours gratuits**

**Version : 1.0\
Statut : Plan d\'exécution développement Sprint 6\
Module : Sales CRM & Conversion Engine\
Produit : TableFlash Leads Engine (TFLE)\
Durée estimée : 15 jours ouvrés\
Objectif : Transformer les prospects qualifiés en processus commercial
structuré jusqu\'à la conversion client TableFlash**

# **39.1 --- Vision du Sprint 6**

Les précédents sprints ont construit :

Sprint 1

Infrastructure

↓

Sprint 2

Restaurant Database + Lead Management

↓

Sprint 3

Discovery Engine

↓

Sprint 4

Enrichissement + Qualification

↓

Sprint 5

IA commerciale

TFLE sait maintenant :

- trouver des restaurants ;

- enrichir leurs données ;

- calculer leur potentiel ;

- préparer une approche commerciale.

Mais il manque l\'étape essentielle :

**transformer une opportunité en client.**

# **39.2 --- Nouveau workflow commercial TFLE**

Avant :

Restaurant intéressant

↓

Commercial contacte

↓

Suivi manuel

Après Sprint 6 :

Prospect identifié

↓

Création opportunité

↓

Premier contact

↓

Suivi automatique

↓

Relances intelligentes

↓

Proposition essai gratuit 30 jours

↓

Activation TableFlash

↓

Conversion client

# **39.3 --- Objectif business**

À la fin du Sprint 6, TableFlash doit disposer d\'un véritable système
commercial interne permettant :

- de ne plus perdre de prospects ;

- de savoir qui contacter chaque jour ;

- de suivre chaque échange ;

- de mesurer le taux de conversion ;

- de gérer les essais gratuits.

# **39.4 --- Résultat attendu**

Version :

TFLE v0.6.0

Fonctionnalités :

✅ CRM commercial complet\
✅ Pipeline Kanban\
✅ Gestion contacts\
✅ Historique interactions\
✅ Tâches commerciales\
✅ Relances automatiques\
✅ Gestion essais gratuits 30 jours\
✅ Suivi conversion client\
✅ Statistiques commerciales

# **39.5 --- Architecture Sprint 6**

Nouvelle architecture :

backend/app/

├── crm/

│

│ ├── contacts/

│ ├── deals/

│ ├── activities/

│ ├── tasks/

│

├── automation/

│

│ ├── reminders.py

│ ├── workflows.py

│

├── trials/

│

│ ├── trial_manager.py

│

└── analytics/

└── sales_metrics.py

# **39.6 --- Nouveau modèle commercial TFLE**

Avant :

Restaurant

↓

Lead

Après :

Restaurant

↓

Lead

↓

Opportunity

↓

Deal

↓

Trial

↓

Customer

# **39.7 --- Nouveau modèle Database CRM**

# **Table contacts**

Objectif :

Gérer les personnes liées au restaurant.

contacts

id

restaurant_id

first_name

last_name

role

email

phone

source

created_at

updated_at

Exemples :

Jean Dupont

Gérant

contact@restaurant.fr

# **Table opportunities**

Une opportunité commerciale.

opportunities

id

restaurant_id

contact_id

stage

priority

estimated_value

owner_id

created_at

updated_at

# **Pipeline :**

NEW

CONTACTED

QUALIFIED

DEMO

TRIAL

CUSTOMER

LOST

# **Table activities**

Historique complet.

activities

id

opportunity_id

type

description

created_by

created_at

Types :

CALL

EMAIL

MEETING

NOTE

DEMO

TRIAL_STARTED

# **Table tasks**

Actions à effectuer.

tasks

id

user_id

opportunity_id

title

due_date

status

priority

Exemple :

Appeler Restaurant Chez Paul

Demain 10h

Priorité haute

# **39.8 --- EPIC 01**

# **CRM Pipeline Commercial**

Priorité :

## **P0**

Objectif :

Créer une vue commerciale globale.

Nouvelle page :

/crm/pipeline

Vue Kanban :

Nouveaux prospects

↓

Contactés

↓

Démo

↓

Essai 30 jours

↓

Clients

Chaque carte :

Restaurant

↓

Score IA

↓

Dernière action

↓

Prochaine tâche

Composants :

PipelineBoard

DealCard

StageColumn

OpportunityDetail

# **Ticket TFLE-500**

Créer pipeline CRM.

Critères validation :

✅ Déplacement prospect entre étapes\
✅ Historique conservé\
✅ Filtres commerciaux fonctionnels

# **Prompt Claude Code TFLE-500**

Tu travailles sur TFLE Sprint 6.

Crée le module CRM Pipeline.

Contraintes :

\- architecture modulaire

\- aucune logique métier dans React

\- API séparée

\- historique obligatoire

Avant modification :

analyse les fichiers existants.

# **39.9 --- EPIC 02**

# **Gestion des contacts restaurants**

Priorité :

## **P0**

Objectif :

Ne plus gérer uniquement des entreprises mais des interlocuteurs.

Informations :

Nom

Fonction

Téléphone

Email

Restaurant associé

Règle métier :

Un restaurant peut avoir :

1 → plusieurs contacts

Exemple :

Gérant

Associé

Responsable salle

# **39.10 --- EPIC 03**

# **Historique commercial**

Priorité :

## **P0**

Chaque action doit être enregistrée.

Exemple :

Timeline :

25/07

Restaurant ajouté

26/07

Email envoyé

28/07

Appel effectué

30/07

Démo proposée

Interface :

ActivityTimeline

# **39.11 --- EPIC 04**

# **Gestion des tâches commerciales**

Priorité :

## **P0**

Objectif :

Créer une routine commerciale quotidienne.

Page :

/tasks

Affichage :

Aujourd\'hui :

□ Appeler 5 restaurants

□ Relancer 3 prospects

□ Préparer une démo

Priorités :

LOW

MEDIUM

HIGH

URGENT

# **39.12 --- EPIC 05**

# **Automation Engine**

Priorité :

## **P1**

Objectif :

Automatiser les rappels.

Exemple :

Restaurant :

Email envoyé

↓

Après 3 jours :

Créer tâche :

Relancer restaurant

Architecture :

Event

↓

Rule Engine

↓

Action

Exemple :

EVENT:

EMAIL_SENT

RULE:

3 jours sans réponse

ACTION:

Créer rappel

# **39.13 --- Table workflows**

automation_rules

id

name

trigger

condition

action

active

Exemple :

{

\"name\":

\"Relance email\",

\"trigger\":

\"EMAIL_SENT\",

\"condition\":

\"3_DAYS\",

\"action\":

\"CREATE_TASK\"

}

# **39.14 --- EPIC 06**

# **Séquence commerciale TableFlash**

Priorité :

## **P0**

Créer un workflow officiel.

## **Séquence standard**

### **Jour 0**

Premier contact.

↓

### **Jour 3**

Première relance.

↓

### **Jour 7**

Deuxième relance.

↓

### **Jour 14**

Proposition démonstration.

↓

### **Jour 21**

Proposition essai gratuit.

↓

### **Jour 30**

Bilan.

# **39.15 --- EPIC 07**

# **Gestion Essai Gratuit 30 jours**

Priorité :

## **P0**

Objectif :

Suivre les restaurants en test.

Nouvelle table :

trials

id

restaurant_id

start_date

end_date

status

converted

created_at

Statuts :

ACTIVE

ENDING_SOON

EXPIRED

CONVERTED

# **Workflow :**

Prospect intéressé

↓

Essai créé

↓

30 jours

↓

Suivi utilisation

↓

Conversion

# **39.16 --- Dashboard Trial**

Page :

/trials

Affichage :

  ---------------- ----------- --------- ------------
   **Restaurant**   **Début**   **Fin**   **Statut**

     Chez Paul        01/08      31/08      Actif
  ---------------- ----------- --------- ------------

Alertes :

Essai expire dans 7 jours

# **39.17 --- EPIC 08**

# **Conversion client TableFlash**

Priorité :

## **P1**

Quand essai terminé :

Actions :

Convertir client

↓

Créer client TableFlash

↓

Archiver opportunité gagnée

Statut :

CUSTOMER

# **39.18 --- Sales Analytics**

Priorité :

## **P1**

Nouveaux KPI :

## **Acquisition**

Restaurants trouvés

↓

Prospects créés

↓

Contacts réalisés

## **Conversion**

Prospects → Clients

## **Commercial**

Temps moyen conversion

Nombre relances

Taux réponse

# **Dashboard :**

/sales/dashboard

# **39.19 --- API Sprint 6**

## **Pipeline**

GET /crm/opportunities

## **Déplacement étape**

PATCH /crm/opportunities/{id}/stage

## **Ajouter activité**

POST /crm/activity

## **Créer tâche**

POST /crm/tasks

## **Démarrer essai**

POST /trials/start

## **Conversion client**

POST /trials/{id}/convert

# **39.20 --- Tests Sprint 6**

## **CRM**

Tester :

- création opportunité ;

- changement étape ;

- historique.

## **Automation**

Tester :

- création automatique tâches ;

- délais ;

- désactivation règles.

## **Trial**

Tester :

- démarrage essai ;

- expiration ;

- conversion.

# **39.21 --- Planning Sprint 6**

## **Jour 1-3**

Base CRM + modèles DB.

## **Jour 4-6**

Pipeline Kanban.

## **Jour 7-8**

Contacts + historique.

## **Jour 9-10**

Tasks + workflows.

## **Jour 11-12**

Essais gratuits 30 jours.

## **Jour 13**

Dashboard commercial.

## **Jour 14-15**

Tests + optimisation.

# **39.22 --- Definition of Done Sprint 6**

Le sprint est terminé lorsque :

## **CRM**

✅ Pipeline complet\
✅ Historique commercial\
✅ Contacts gérés

## **Automatisation**

✅ Relances générées automatiquement\
✅ Tâches créées

## **TableFlash**

✅ Essai gratuit 30 jours suivi\
✅ Conversion client mesurable

# **39.23 --- Résultat opérationnel après Sprint 6**

Avant :

TFLE trouve les bons restaurants

Après :

TFLE trouve

↓

analyse

↓

priorise

↓

organise le commercial

↓

suit les relances

↓

transforme les essais en clients

# **39.24 --- Évolution stratégique**

À ce stade TFLE devient :

## **Une machine d\'acquisition interne TableFlash**

Capable de gérer :

Recherche

↓

Qualification

↓

Approche

↓

Suivi

↓

Conversion
