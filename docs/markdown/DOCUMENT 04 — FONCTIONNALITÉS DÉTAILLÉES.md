# **DOCUMENT 04 --- FONCTIONNALITÉS DÉTAILLÉES**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification fonctionnelle\
Produit : TableFlash Leads Engine\
Type : Outil interne stratégique d\'acquisition commerciale**

# **04.1 --- Introduction**

Ce document décrit précisément les fonctionnalités de TFLE.

Contrairement au document 03 qui décrit **ce que les utilisateurs
veulent faire**, ce document décrit :

- ce que le système doit permettre ;

- comment chaque fonctionnalité fonctionne ;

- les écrans concernés ;

- les règles métier ;

- les critères d\'acceptation.

Ce document servira de référence lors :

- de la conception UX/UI ;

- du développement ;

- des tests ;

- des évolutions futures.

# **04.2 --- Architecture fonctionnelle globale**

TFLE est organisé autour de 7 grands domaines :

TABLEFLASH LEADS ENGINE

Dashboard

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\| \| \| \|

Discovery Intelligence CRM Administration

\| \| \|

Collecte Analyse IA Pipeline

\|

Sources publiques

# **MODULE 01 --- DASHBOARD CENTRAL**

## **Objectif**

Donner une vision immédiate de l\'activité commerciale.

# **ÉCRAN 01 --- Tableau de bord principal**

## **Description**

Premier écran affiché après connexion.

Il doit répondre à :

> \"Quelle est la situation actuelle de ma prospection ?\"

## **Informations affichées**

### **Bloc 1 --- Vue globale**

Exemple :

Restaurants analysés

12 540

Prospects qualifiés

1 850

Score moyen

72/100

Essais TableFlash

46

### **Bloc 2 --- Actions prioritaires**

Liste automatique :

🔥 15 prospects prioritaires à contacter aujourd\'hui

1\. Chez Marcel

Score : 94

2\. La Brasserie du Port

Score : 91

### **Bloc 3 --- Évolution**

Graphiques :

- nouveaux restaurants détectés ;

- prospects qualifiés ;

- conversions ;

- zones performantes.

## **Règles métier**

- Les statistiques doivent être calculées automatiquement.

- Les données doivent être mises à jour régulièrement.

- Les prospects prioritaires sont ceux dépassant un seuil configurable.

## **Critères d\'acceptation**

✅ Le dashboard charge en moins de quelques secondes.

✅ Les données affichées correspondent à la base réelle.

✅ L\'utilisateur peut accéder directement aux prospects prioritaires.

# **MODULE 02 --- DISCOVERY ENGINE**

# **ÉCRAN 02 --- Recherche de restaurants**

## **Objectif**

Permettre de lancer une recherche de prospects.

## **Interface**

Champs :

### **Zone géographique**

- Ville

- Département

- Région

- Rayon kilométrique

### **Type de restaurant**

Filtres :

- Restaurant traditionnel

- Brasserie

- Pizzeria

- Burger

- Cuisine spécialisée

### **Options avancées**

- Avec site internet uniquement

- Sans QR détecté

- Sans commande en ligne

- Score minimum

## **Exemple**

Recherche :

Ville :

Bayonne

Rayon :

30 km

Type :

Restaurant traditionnel

QR :

Non détecté

Résultat :

248 restaurants trouvés

42 prospects prioritaires

## **Règles métier**

- Une recherche doit être enregistrée.

- Les résultats doivent être historisés.

- Les doublons doivent être évités.

## **Critères d\'acceptation**

✅ Une recherche peut être sauvegardée.

✅ Les restaurants déjà connus ne sont pas recréés.

✅ Les filtres fonctionnent indépendamment.

# **MODULE 03 --- FICHE RESTAURANT**

# **ÉCRAN 03 --- Profil prospect complet**

## **Objectif**

Centraliser toutes les informations concernant un restaurant.

# **Section 1 --- Informations générales**

Afficher :

Nom

Adresse

Téléphone

Site web

Catégorie

Localisation

# **Section 2 --- Présence digitale**

Afficher :

Site :

Oui

Mobile :

Optimisé

Menu :

PDF

QR Code :

Non détecté

Commande :

Non disponible

# **Section 3 --- Score IA**

Afficher :

Score TableFlash

91/100

Pourquoi :

\+ Restaurant indépendant

\+ Menu PDF

\+ Pas de QR Code

\+ Forte présence locale

# **Section 4 --- Analyse IA**

Afficher :

Résumé :

> Restaurant indépendant avec une présence digitale limitée. Le menu PDF
> représente une opportunité importante pour proposer une expérience
> plus moderne avec TableFlash.

# **Section 5 --- CRM**

Afficher :

Statut :

À contacter

Historique :

25/07

Restaurant ajouté

26/07

Analyse terminée

# **Règles métier**

- Une fiche restaurant possède un identifiant unique.

- Toutes les modifications doivent être historisées.

- Les analyses doivent conserver leur date.

# **Critères d\'acceptation**

✅ Toutes les informations sont accessibles depuis une seule page.

✅ L\'utilisateur comprend immédiatement l\'opportunité.

# **MODULE 04 --- ANALYSE DIGITALE**

# **ÉCRAN 04 --- Rapport d\'analyse web**

## **Objectif**

Présenter l\'état numérique du restaurant.

## **Analyse du site**

Le système vérifie :

### **Structure**

- présence d\'un site ;

- pages principales ;

- technologies utilisées.

### **Expérience utilisateur**

- adaptation mobile ;

- vitesse ;

- navigation.

### **Menu**

Détection :

Menu interactif

Menu PDF

Menu image

Pas de menu

### **Services**

Détection :

Réservation

Commande

Livraison

Click & Collect

## **Règles métier**

- Une analyse possède une date d\'expiration.

- Une nouvelle analyse peut remplacer l\'ancienne.

- L\'historique est conservé.

# **MODULE 05 --- INTELLIGENCE ARTIFICIELLE**

# **ÉCRAN 05 --- Analyse IA commerciale**

## **Objectif**

Transformer les données en recommandations.

## **Fonction 1 --- Résumé automatique**

Entrées :

- données restaurant ;

- analyse site ;

- score.

Sortie :

Résumé commercial.

## **Fonction 2 --- Arguments personnalisés**

Exemple :

Approche recommandée :

Mettre en avant la suppression

des menus papier et la facilité

de modification de la carte.

## **Fonction 3 --- Détection opportunité**

Catégories :

Très forte opportunité

Bonne opportunité

Moyenne

Faible

# **Règles métier**

- L\'IA ne modifie jamais les données sources.

- Les suggestions restent des recommandations.

- Les décisions finales restent humaines.

# **MODULE 06 --- LEAD SCORING**

# **ÉCRAN 06 --- Configuration du scoring**

## **Objectif**

Permettre d\'adapter la qualification.

## **Exemple de règles**

Pas de QR Code

+15 points

Menu PDF

+10 points

Restaurant indépendant

+20 points

Site ancien

+10 points

## **Catégories**

0-40

Faible

40-70

Moyen

70-100

Prioritaire

# **Règles métier**

- Le score doit être recalculable.

- Chaque changement doit être enregistré.

- L\'ancien score doit rester consultable.

# **MODULE 07 --- CRM COMMERCIAL**

# **ÉCRAN 07 --- Pipeline commercial**

## **Objectif**

Suivre la transformation des prospects.

Pipeline :

Découvert

↓

Qualifié

↓

À contacter

↓

Contacté

↓

Démo

↓

Essai 30 jours

↓

Client

## **Actions disponibles**

L\'utilisateur peut :

- changer statut ;

- ajouter commentaire ;

- créer une tâche ;

- programmer une relance.

# **ÉCRAN 08 --- Historique commercial**

Afficher :

Date

Action

Utilisateur

Commentaire

Exemple :

26/07

Appel réalisé

Intérêt confirmé

Relance prévue lundi

# **MODULE 08 --- RECHERCHE ET FILTRES**

# **ÉCRAN 09 --- Recherche avancée**

Filtres :

## **Géographie**

- Ville

- Département

- Région

## **Opportunité**

- Score minimum

- Sans QR

- Sans menu digital

- Site existant

## **Commercial**

- Statut

- Dernière action

- Responsable

# **MODULE 09 --- EXPORT**

# **ÉCRAN 10 --- Export données**

## **Objectif**

Permettre l\'utilisation externe des données.

Formats :

- CSV

- Excel

Champs exportables :

- Nom

- Adresse

- Téléphone

- Email public

- Score

- Statut

- Résumé IA

# **MODULE 10 --- ADMINISTRATION**

# **ÉCRAN 11 --- Paramètres système**

Gestion :

- utilisateurs ;

- rôles ;

- règles scoring ;

- fréquence analyses ;

- intégrations.

# **04.3 --- Fonctionnalités MVP obligatoires**

Pour une première version opérationnelle :

  -------------------- --------------
   **Fonctionnalité**   **Priorité**

       Recherche             P0
      restaurants      

    Création fiches          P0

      Analyse site           P0

        Score IA             P0

       Résumé IA             P0

       CRM simple            P0

       Export CSV            P0
  -------------------- --------------

# **04.4 --- Fonctionnalités V1**

Après validation du MVP :

  ---------------------
   **Fonctionnalité**

    Carte interactive

     Automatisation
       quotidienne

        Relances

  Statistiques avancées

   Historique complet

        Recherche
      intelligente

  Détection changements
  ---------------------

# **04.5 --- Règle de conception générale**

Chaque écran TFLE doit respecter cette logique :

Information brute

↓

Analyse

↓

Compréhension

↓

Décision

↓

Action commerciale

Un écran qui affiche uniquement des données n\'apporte pas assez de
valeur.

# **Conclusion Document 04**

TableFlash Leads Engine doit être conçu comme un **système d\'aide à la
décision commerciale**, pas comme une simple base de données.

La valeur principale vient de la transformation :

> Données publiques → Intelligence commerciale → Action commerciale →
> Client TableFlash.
