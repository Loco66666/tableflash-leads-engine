# **DOCUMENT 37 --- SPRINT 4 TFLE**

# **Enrichissement Données, Email Discovery & Qualification Automatique**

**Version : 1.0\
Statut : Plan d\'exécution développement Sprint 4\
Module : Data Intelligence & Lead Qualification Engine\
Produit : TableFlash Leads Engine (TFLE)\
Durée estimée : 15 jours ouvrés\
Objectif : Transformer des restaurants trouvés en prospects commerciaux
exploitables**

# **37.1 --- Vision du Sprint 4**

Les précédents sprints ont construit :

Sprint 1

Infrastructure

↓

Sprint 2

Base restaurants + CRM

↓

Sprint 3

Discovery Engine + collecte automatique

Le Sprint 4 apporte la première couche d\'intelligence commerciale.

Avant :

Restaurant trouvé

Après :

Restaurant trouvé

↓

Données enrichies

↓

Contact professionnel identifié

↓

Potentiel TableFlash évalué

↓

Priorité commerciale calculée

↓

Prospect prêt pour démarchage

# **37.2 --- Objectif business**

À la fin du Sprint 4, TFLE doit répondre automatiquement à :

> \"Quels restaurants contacter en premier et pourquoi ?\"

# **37.3 --- Résultat attendu**

Version :

TFLE v0.4.0

Fonctionnalités :

✅ Enrichissement automatique restaurants\
✅ Recherche email professionnel public\
✅ Validation qualité email\
✅ Analyse présence digitale\
✅ Qualification commerciale\
✅ Score opportunité initial\
✅ Priorisation prospects\
✅ Suggestions d\'actions commerciales

# **37.4 --- Principe fondamental**

TFLE ne doit pas simplement collecter des emails.

Le but n\'est pas :

Restaurant → Email

Mais :

Restaurant

\+

Informations commerciales

\+

Signaux d\'opportunité

\+

Priorité

# **37.5 --- Architecture Sprint 4**

Nouvelle architecture :

backend/

├── enrichment/

│

│ ├── email_finder.py

│ ├── website_analyzer.py

│ ├── social_analyzer.py

│

├── qualification/

│

│ ├── scoring.py

│ ├── rules.py

│

├── intelligence/

│

│ └── recommendations.py

# **37.6 --- Nouveau pipeline TFLE**

Workflow complet :

Restaurant Discovery

↓

Enrichment Engine

↓

Data Validation

↓

Qualification Engine

↓

Lead Scoring

↓

CRM Pipeline

# **37.7 --- Nouveau modèle Database**

Création table :

# **restaurant_enrichment**

Cette table conserve les informations enrichies séparément.

Pourquoi ?

Séparation :

Données collectées

≠

Analyse commerciale

Structure :

restaurant_enrichment

id

restaurant_id

email_found

email_source

email_quality

website_status

website_quality

social_presence

digital_score

enriched_at

# **37.8 --- Table Lead Intelligence**

Nouvelle table :

lead_intelligence

id

restaurant_id

commercial_score

priority

reason

recommended_action

created_at

Exemple :

{

\"commercial_score\":87,

\"priority\":\"HIGH\",

\"reason\":\[

\"Pas de commande en ligne\",

\"Site ancien\",

\"Restaurant indépendant\"

\],

\"recommended_action\":

\"Proposer essai TableFlash\"

}

# **37.9 --- EPIC 01**

# **Email Discovery Engine**

Priorité :

## **P0**

## **Objectif**

Identifier les emails professionnels publics.

Sources possibles :

Site officiel

↓

Page contact

↓

Mentions légales

↓

Adresse professionnelle publique

## **Important**

TFLE doit rechercher :

✅ email professionnel public

Éviter :

❌ données personnelles privées\
❌ emails non liés à l\'activité\
❌ bases illégales

# **Ticket TFLE-300**

## **Création Email Finder**

Priorité :

P0

Créer :

backend/app/enrichment/email_finder.py

Fonction :

find_business_email(

restaurant_url

)

Entrée :

{

\"website\":

\"https://restaurant.fr\"

}

Sortie :

{

\"email\":

\"contact@restaurant.fr\",

\"source\":

\"website\",

\"confidence\":

95

}

# **Prompt Claude Code TFLE-300**

Tu travailles sur TFLE Sprint 4.

Crée le module Email Discovery.

Contraintes :

\- uniquement données professionnelles publiques

\- conserver la source

\- retourner un niveau de confiance

\- gérer les erreurs

Ne crée aucune automatisation de campagne email.

# **Critères validation**

✅ Email trouvé si disponible\
✅ Source conservée\
✅ Pas d\'invention

# **37.10 --- EPIC 02**

# **Validation Email**

Priorité :

## **P0**

Problème :

Un email trouvé peut être :

- invalide ;

- ancien ;

- faux.

Créer :

email_validator.py

Vérifications :

## **Format**

Exemple :

contact@restaurant.fr

## **Domaine**

Vérifier :

restaurant.fr

existe.

## **Qualité**

Score :

0-100

Exemple :

contact@site.fr

95/100

gmail personnel

40/100

# **37.11 --- EPIC 03**

# **Website Intelligence**

Priorité :

## **P1**

Objectif :

Analyser le site restaurant.

Signaux recherchés :

## **Présence commande en ligne**

Détection :

Commander

Réserver

Menu

Click & Collect

## **Technologie**

Identifier :

- site moderne ;

- site ancien ;

- absence site.

## **Score digital**

Exemple :

Site absent

+30 opportunité

Site ancien

+20

Site moderne

+5

# **Ticket TFLE-320**

Créer :

website_analyzer.py

Sortie :

{

\"has_website\":true,

\"online_order\":false,

\"digital_score\":80

}

# **37.12 --- EPIC 04**

# **Social Presence Analyzer**

Priorité :

## **P1**

Analyser :

- Instagram ;

- Facebook ;

- autres liens publics.

Objectif :

Comprendre maturité digitale.

Signaux :

Facebook actif

\+

Instagram actif

\+

Photos récentes

Résultat :

{

\"social_score\":75

}

# **37.13 --- EPIC 05**

# **Lead Qualification Engine**

Priorité :

## **P0**

C\'est le cœur du Sprint.

Objectif :

Répondre :

> Ce restaurant est-il intéressant pour TableFlash ?

# **37.14 --- Modèle de scoring initial**

Score :

0 → 100

## **Critères**

### **Type restaurant**

Restaurant traditionnel

+20

### **Indépendant**

Indépendant

+20

### **Zone stratégique**

Exemple :

Bayonne / Anglet / Biarritz :

+15

### **Absence commande digitale**

+20

### **Email professionnel trouvé**

+15

### **Site absent**

+10

# **Exemple**

Restaurant :

Chez Paul

Bayonne

Pas de commande

Email trouvé

Indépendant

Score :

85/100

Priorité :

HAUTE

# **Ticket TFLE-340**

Créer :

qualification/scoring.py

Fonction :

calculate_lead_score(

restaurant

)

Retour :

{

\"score\":85,

\"priority\":\"HIGH\"

}

# **Prompt Claude Code TFLE-340**

Crée le Lead Qualification Engine TFLE.

Contraintes :

\- règles explicables

\- score transparent

\- aucun modèle IA pour le moment

\- chaque point doit avoir une justification

Le commercial doit comprendre pourquoi un prospect est prioritaire.

# **37.15 --- EPIC 06**

# **Interface Qualification**

Priorité :

## **P1**

Nouvelle page :

/qualification

Affichage :

Table :

  ---------------- ----------- -------------- --------------
   **Restaurant**   **Score**   **Priorité**   **Raisons**

     Chez Paul         85          Haute          Pas de
                                                 commande
  ---------------- ----------- -------------- --------------

Composants :

LeadScoreBadge

OpportunityCard

ReasonList

# **37.16 --- EPIC 07**

# **Actions commerciales recommandées**

Priorité :

## **P1**

TFLE propose :

Selon score :

## **Score 80-100**

Contacter rapidement

Proposer essai 30 jours

## **Score 50-80**

Analyser davantage

## **Score \<50**

Priorité faible

# **37.17 --- API Sprint 4**

Nouvelles routes :

## **Enrichissement**

POST /restaurants/{id}/enrich

## **Score**

GET /restaurants/{id}/score

## **Qualification**

GET /leads/prioritized

# **37.18 --- Tests Sprint 4**

## **Tests Email**

Tester :

- email valide ;

- email absent ;

- erreur site.

## **Tests scoring**

Cas :

Restaurant A :

Score élevé

Restaurant B :

Score faible

## **Tests pipeline**

Vérifier :

Restaurant

↓

Enrichissement

↓

Score

↓

Lead

# **37.19 --- Planning Sprint 4**

## **Jour 1-3**

Email Discovery Engine

## **Jour 4-5**

Validation emails

## **Jour 6-8**

Analyse sites

## **Jour 9-10**

Qualification Engine

## **Jour 11-12**

Interface scoring

## **Jour 13**

API intégration

## **Jour 14-15**

Tests + optimisation

# **37.20 --- Definition of Done Sprint 4**

Le sprint est terminé lorsque :

## **Données**

✅ Restaurant enrichi\
✅ Email professionnel identifié si disponible\
✅ Sources conservées

## **Intelligence**

✅ Score calculé\
✅ Raisons affichées\
✅ Priorités générées

## **Commercial**

✅ Les meilleurs restaurants ressortent automatiquement

# **37.21 --- Résultat opérationnel après Sprint 4**

Avant :

TFLE trouve des restaurants

Après :

TFLE comprend quels restaurants valent la peine d\'être contactés

Workflow :

10 000 restaurants trouvés

↓

Enrichissement

↓

Score automatique

↓

500 prospects prioritaires

↓

Commercial TableFlash contacte les meilleurs
