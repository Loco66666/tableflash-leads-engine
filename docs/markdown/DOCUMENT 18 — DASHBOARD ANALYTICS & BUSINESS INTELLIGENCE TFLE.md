# **DOCUMENT 18 --- DASHBOARD ANALYTICS & BUSINESS INTELLIGENCE TFLE**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification fonctionnelle + technique BI\
Module : Analytics, Reporting & Strategic Intelligence\
Produit : TableFlash Leads Engine\
Usage : Interne uniquement pour TableFlash**

# **18.1 --- Introduction**

Le module **Dashboard Analytics & Business Intelligence TFLE**
représente la couche de pilotage stratégique.

Son objectif :

> Transformer toutes les données générées par TFLE en décisions
> commerciales mesurables.

TFLE produit énormément d\'informations :

- restaurants découverts ;

- données collectées ;

- scores générés ;

- contacts réalisés ;

- réponses obtenues ;

- essais gratuits ;

- conversions clients.

Le dashboard doit permettre de répondre quotidiennement :

- Est-ce que notre prospection fonctionne ?

- Où sont les meilleurs prospects ?

- Quels restaurants convertissent ?

- Quels arguments fonctionnent ?

- Quel est le coût d\'acquisition ?

- Où devons-nous concentrer nos efforts ?

# **18.2 --- Vision Business Intelligence TFLE**

Le dashboard n\'est pas uniquement un outil statistique.

Il devient un véritable **centre de décision commercial**.

Évolution :

Niveau 1

Reporting simple

↓

Niveau 2

Analyse commerciale

↓

Niveau 3

Prédiction IA

↓

Niveau 4

Pilotage automatique

# **18.3 --- Architecture globale Analytics**

DONNÉES TFLE

↓

DATA COLLECTION LAYER

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Scraping Data

CRM Data

Scoring Data

AI Data

Customer Data

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

ANALYTICS ENGINE

↓

DATA WAREHOUSE

↓

DASHBOARD TFLE

# **18.4 --- Sources de données analytiques**

Le système récupère :

# **Source 1 --- Discovery Engine**

Données :

- recherches effectuées ;

- zones explorées ;

- restaurants trouvés ;

- sources utilisées.

# **Source 2 --- Data Enrichment**

Données :

- emails trouvés ;

- qualité données ;

- taux validation.

# **Source 3 --- Scoring Engine**

Données :

- scores prospects ;

- catégories ;

- raisons qualification.

# **Source 4 --- CRM**

Données :

- contacts ;

- réponses ;

- essais ;

- clients.

# **Source 5 --- IA**

Données :

- analyses générées ;

- recommandations ;

- précision.

# **18.5 --- Architecture des dashboards**

TFLE possède plusieurs dashboards spécialisés.

Dashboard principal

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1\. Acquisition

2\. Qualification

3\. Commercial

4\. Conversion

5\. IA

6\. Zones géographiques

7\. Performance système

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **DOCUMENT 18.1 --- DASHBOARD EXECUTIVE**

## **Objectif**

Vue globale dirigeant.

## **KPI principaux**

Carte 1 :

# **Prospects totaux**

Exemple :

12 540 restaurants analysés

Carte 2 :

# **Prospects qualifiés**

1 850 prospects haute priorité

Carte 3 :

# **Essais gratuits actifs**

24 restaurants

Carte 4 :

# **Clients TableFlash**

18 restaurants

Carte 5 :

# **Taux conversion**

8,4 %

# **Vue graphique**

Tunnel commercial :

Restaurants trouvés

↓

Restaurants analysés

↓

Prospects qualifiés

↓

Contactés

↓

Démo

↓

Essai gratuit

↓

Clients

# **18.6 --- Dashboard Acquisition**

## **Objectif**

Analyser la capacité de TFLE à trouver des prospects.

## **KPI**

### **Restaurants découverts**

Période :

- jour ;

- semaine ;

- mois.

### **Sources performantes**

Exemple :

OpenStreetMap

4 500 restaurants

Qualité moyenne : 82%

### **Zones explorées**

Carte :

Bayonne

Anglet

Biarritz

Pau

Bordeaux

# **Graphiques**

## **Evolution découverte**

Janvier

████

Février

████████

Mars

████████████

## **Répartition sources**

OSM

45%

Sites web

30%

Annuaires

25%

# **18.7 --- Dashboard Data Quality**

## **Objectif**

Mesurer la qualité des informations collectées.

# **KPI**

## **Emails trouvés**

Exemple :

8 500

## **Emails validés**

7 900

## **Taux validation**

92,9 %

## **Données complètes**

65 %

# **Score moyen qualité**

84 / 100

# **Alertes**

Exemple :

⚠ 300 prospects nécessitent une nouvelle analyse

# **18.8 --- Dashboard Lead Scoring**

## **Objectif**

Comprendre la qualité commerciale des prospects.

# **KPI**

## **Distribution scores**

90-100

250 prospects

75-89

600 prospects

50-74

900 prospects

# **Analyse opportunité**

Catégories :

🔥 Priorité haute

⭐ Intéressant

🟡 Moyen

⚪ Faible

# **Questions métier**

Le dashboard doit répondre :

\"Combien de restaurants ont un fort besoin TableFlash ?\"

# **Exemple :**

Restaurants sans QR détecté :

4 500

Restaurants sans commande digitale :

3 200

# **18.9 --- Dashboard Commercial CRM**

## **Objectif**

Suivre l\'activité commerciale.

# **KPI commerciaux**

## **Contacts effectués**

850

## **Réponses obtenues**

170

## **Taux réponse**

20 %

## **Démonstrations**

45

## **Essais gratuits**

22

## **Clients**

12

# **Pipeline graphique**

Découverts

████████████████

Qualifiés

████████

Contactés

████

Démo

██

Clients

█

# **18.10 --- Dashboard Conversion**

## **Objectif**

Comprendre la transformation prospect → client.

# **Funnel principal**

10 000 restaurants trouvés

↓

2 000 qualifiés

↓

500 contactés

↓

100 réponses

↓

40 essais

↓

15 clients

# **KPI essentiels**

## **Taux qualification**

Formule :

Prospects qualifiés /

Restaurants trouvés

## **Taux réponse**

Réponses /

Contacts envoyés

## **Taux conversion essai**

Clients /

Essais gratuits

## **Taux conversion global**

Clients /

Prospects initiaux

# **18.11 --- Dashboard Essais gratuits 30 jours**

Spécifique TableFlash.

## **Vue actuelle**

Liste :

Restaurant

Début essai

Jour actuel

Utilisation

Probabilité conversion

Exemple :

Chez Martin

Jour 18/30

Utilisation élevée

Conversion probable : 87%

# **KPI**

## **Essais actifs**

## **Essais terminés**

## **Conversion**

## **Abandons**

# **Analyse comportement utilisateur**

Données possibles :

- nombre produits créés ;

- QR générés ;

- connexions ;

- commandes test.

# **18.12 --- Dashboard IA Intelligence**

## **Objectif**

Mesurer la valeur de l\'intelligence artificielle.

# **KPI**

## **Analyses IA générées**

15 000

## **Temps économisé**

Avant IA :

20 minutes / prospect

Après IA :

3 minutes / prospect

## **Suggestions validées**

86 %

## **Qualité prédiction**

78 %

# **18.13 --- Dashboard Zones géographiques**

## **Objectif**

Identifier les territoires les plus rentables.

Carte :

France

↓

Régions

↓

Villes

↓

Restaurants

# **KPI par zone**

Exemple :

  ----------- --------------- ----------------
   **Ville**   **Prospects**   **Conversion**

    Bayonne         450             12%

    Anglet          320             10%

   Biarritz         280             14%
  ----------- --------------- ----------------

# **Intelligence future**

L\'IA pourra recommander :

> \"Développer la prospection autour de Biarritz car le taux de
> conversion est supérieur de 40%.\"

# **18.14 --- Dashboard ROI Commercial**

## **Objectif**

Mesurer la rentabilité de TFLE.

# **KPI**

## **Temps commercial économisé**

Avant :

100 heures recherche

Après :

15 heures validation

## **Coût acquisition client**

Formule :

Coûts prospection /

Clients obtenus

## **Valeur client**

Exemple :

Abonnement moyen × durée moyenne

## **Ratio ROI**

Formule :

Valeur client /

Coût acquisition

# **18.15 --- Alertes intelligentes**

Le système surveille.

Exemple :

## **Alerte commerciale**

15 prospects score \>90

non contactés depuis 7 jours

## **Alerte qualité**

Baisse validation emails de 20%

## **Alerte conversion**

Les restaurants traditionnels convertissent

3 fois mieux que les franchises

# **18.16 --- Intelligence prédictive future**

V2 :

Le dashboard prédit :

## **Probabilité conversion**

Exemple :

Restaurant X

Probabilité client :

82%

## **Meilleur moment contact**

Exemple :

Contacter mardi après 15h

## **Meilleur argument**

Exemple :

Mettre en avant simplicité d\'installation

# **18.17 --- Architecture technique BI**

## **Base analytique**

Possibilité :

MVP :

PostgreSQL

V1 :

Data Warehouse dédié

## **Technologies possibles**

Frontend :

React Charts

Recharts

ECharts

Backend :

Analytics API

Traitement :

Workers statistiques

# **18.18 --- Modèle données Analytics**

## **analytics_events**

id

event_type

user_id

restaurant_id

timestamp

metadata

## **daily_metrics**

date

restaurants_found

qualified_leads

contacts

trials

customers

## **conversion_metrics**

period

source

conversion_rate

revenue

# **18.19 --- Permissions Dashboard**

## **Administrateur**

Accès complet.

## **Commercial**

Accès :

- CRM ;

- conversion ;

- prospects.

## **Analyste**

Accès :

- données ;

- qualité ;

- scraping.

# **18.20 --- MVP Dashboard**

Obligatoire :

✅ Dashboard principal.

✅ Nombre prospects.

✅ Scores.

✅ Pipeline CRM.

✅ Essais gratuits.

✅ Conversion.

# **18.21 --- Version 1**

Ajouts :

- cartes géographiques ;

- ROI ;

- analyses avancées ;

- exports.

# **18.22 --- Version 2**

Vision :

Dashboard autonome IA.

Chaque matin :

Résumé TFLE du jour :

+320 restaurants découverts

+45 prospects prioritaires

12 relances nécessaires

3 conversions probables

Zone recommandée :

Biarritz centre

# **18.23 --- Architecture finale**

DONNÉES TFLE

↓

ANALYTICS ENGINE

↓

BUSINESS INTELLIGENCE

↓

DASHBOARD IA

↓

DÉCISIONS TABLEFLASH

# **Conclusion Document 18**

Le Dashboard Analytics transforme TFLE en véritable centre de pilotage
commercial.

La différence entre un simple outil de prospection et une plateforme
stratégique :

Un outil affiche des chiffres.

TFLE doit expliquer :

> \"Voici ce qui fonctionne, pourquoi cela fonctionne, et quelle action
> maximise les chances de croissance.\"
