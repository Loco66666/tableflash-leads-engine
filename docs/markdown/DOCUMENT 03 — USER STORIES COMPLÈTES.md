# **DOCUMENT 03 --- USER STORIES COMPLÈTES**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Document fonctionnel\
Produit : TableFlash Leads Engine\
Type : Outil interne d\'intelligence commerciale**

# **03.1 --- Introduction**

Les User Stories décrivent les actions que les utilisateurs doivent
pouvoir réaliser dans TFLE.

Elles servent de pont entre :

- la vision produit ;

- les fonctionnalités ;

- l\'expérience utilisateur ;

- le développement technique.

Format utilisé :

> **En tant que \[utilisateur\], je veux \[action\], afin de
> \[objectif\].**

Chaque User Story possède :

- un identifiant ;

- une priorité ;

- des critères d\'acceptation ;

- les règles métier associées.

# **03.2 --- Priorités**

  -------------- ----------------------------------
   **Priorité**          **Signification**

        P0       Obligatoire pour le fonctionnement
                               du MVP

        P1              Important pour la V1

        P2                Évolution future

        P3               Vision long terme
  -------------- ----------------------------------

# **MODULE 01 --- DISCOVERY ENGINE**

## **Objectif**

Permettre à TableFlash de découvrir automatiquement des restaurants
potentiellement intéressants.

# **US-001 --- Recherche de restaurants par zone géographique**

**Priorité : P0**

### **User Story**

> En tant que fondateur TableFlash, je veux rechercher des restaurants
> dans une zone précise afin d\'identifier mon marché potentiel.

### **Exemple**

Recherche :

Ville :

Bayonne

Catégorie :

Restaurant traditionnel

Rayon :

20 km

Résultat :

420 restaurants trouvés

### **Critères d\'acceptation**

✅ L\'utilisateur peut saisir une zone.

✅ Le système retourne une liste de restaurants.

✅ Chaque restaurant possède une fiche initiale.

# **US-002 --- Recherche par région**

**Priorité : P1**

### **User Story**

> En tant que fondateur, je veux analyser une région entière afin
> d\'étendre la prospection.

Exemple :

Nouvelle-Aquitaine

Restaurants détectés :

15 420

# **US-003 --- Détection des nouveaux restaurants**

**Priorité : P2**

### **User Story**

> En tant que TableFlash, je veux identifier les nouveaux établissements
> afin de contacter les restaurants dès leur lancement.

Le système pourra surveiller :

- nouvelles ouvertures ;

- changements d\'activité ;

- nouveaux sites.

# **MODULE 02 --- DATA COLLECTION**

## **Objectif**

Créer une fiche restaurant complète à partir d\'informations publiques.

# **US-004 --- Création automatique d\'une fiche restaurant**

**Priorité : P0**

### **User Story**

> En tant que système TFLE, je veux créer une fiche restaurant
> automatiquement afin de centraliser les informations.

Données initiales :

Nom

Adresse

Téléphone public

Site

Catégorie

Localisation

### **Critères d\'acceptation**

✅ Une fiche unique est créée.

✅ Les doublons sont détectés.

✅ La date de collecte est enregistrée.

# **US-005 --- Recherche des coordonnées publiques**

**Priorité : P0**

### **User Story**

> En tant que commercial, je veux disposer des coordonnées disponibles
> afin de pouvoir contacter le restaurant.

Informations recherchées :

- téléphone public ;

- email professionnel public ;

- formulaire de contact ;

- site internet.

# **US-006 --- Détection des réseaux sociaux**

**Priorité : P1**

### **User Story**

> En tant que commercial, je veux connaître les réseaux sociaux du
> restaurant afin de mieux comprendre son activité.

Détection :

- Facebook ;

- Instagram ;

- TikTok ;

- autres plateformes publiques.

# **MODULE 03 --- WEBSITE INTELLIGENCE**

## **Objectif**

Analyser automatiquement la présence numérique du restaurant.

# **US-007 --- Analyse automatique d\'un site web**

**Priorité : P0**

### **User Story**

> En tant que système TFLE, je veux analyser un site restaurant afin
> d\'identifier ses caractéristiques digitales.

Analyse :

- existence du site ;

- qualité mobile ;

- structure ;

- technologies utilisées.

# **US-008 --- Détection du menu numérique**

**Priorité : P0**

### **User Story**

> En tant que TableFlash, je veux détecter comment un restaurant
> présente son menu afin d\'identifier les opportunités.

Résultats possibles :

Menu :

✓ Interactif

✓ PDF

✓ Image

✓ Aucun menu trouvé

# **US-009 --- Détection QR Code**

**Priorité : P0**

### **User Story**

> En tant que TableFlash, je veux savoir si un restaurant utilise déjà
> un QR Code afin d\'évaluer son besoin.

Résultat :

QR Code détecté :

Oui / Non / Incertain

# **US-010 --- Détection des solutions concurrentes**

**Priorité : P1**

### **User Story**

> En tant que commercial, je veux savoir si un restaurant utilise déjà
> une solution similaire afin d\'adapter mon approche.

Détection :

- commande en ligne ;

- réservation ;

- menu digital ;

- solutions tierces.

# **MODULE 04 --- AI INTELLIGENCE ENGINE**

## **Objectif**

Transformer les données collectées en informations commerciales
exploitables.

# **US-011 --- Génération d\'un résumé IA**

**Priorité : P0**

### **User Story**

> En tant que commercial, je veux obtenir un résumé automatique du
> restaurant afin de comprendre rapidement son potentiel.

Exemple :

Restaurant indépendant.

Site existant mais menu uniquement PDF.

Aucun QR détecté.

Bonne présence locale.

Opportunité élevée pour TableFlash.

# **US-012 --- Génération des arguments commerciaux**

**Priorité : P1**

### **User Story**

> En tant que commercial, je veux obtenir un argument adapté afin de
> personnaliser mon approche.

Exemple :

Argument conseillé :

\"Votre carte semble être uniquement disponible

en PDF. TableFlash permettrait à vos clients

d\'accéder à une carte interactive depuis leur téléphone.\"

# **US-013 --- Explication IA du score**

**Priorité : P0**

### **User Story**

> En tant qu\'utilisateur, je veux comprendre pourquoi un restaurant
> possède un score afin de faire confiance au système.

Interdit :

Score : 87

Obligatoire :

Score : 87

Raisons :

\+ Menu PDF

\+ Pas de QR Code

\+ Restaurant indépendant

\+ Site ancien

# **MODULE 05 --- LEAD SCORING ENGINE**

## **Objectif**

Classer automatiquement les restaurants selon leur potentiel.

# **US-014 --- Calcul automatique du score**

**Priorité : P0**

### **User Story**

> En tant que TableFlash, je veux attribuer une note aux restaurants
> afin de prioriser les prospects.

Exemple :

0-40 :

Faible potentiel

40-70 :

Potentiel moyen

70-100 :

Prospect prioritaire

# **US-015 --- Modification des règles de scoring**

**Priorité : P2**

### **User Story**

> En tant que fondateur, je veux modifier les critères afin d\'améliorer
> la qualification.

Exemple :

Changer :

Absence QR Code

+15 points

en :

+20 points

# **MODULE 06 --- CRM INTERNE**

## **Objectif**

Transformer les prospects en clients.

# **US-016 --- Voir la fiche complète d\'un restaurant**

**Priorité : P0**

### **User Story**

> En tant que commercial, je veux consulter toutes les informations
> d\'un restaurant afin de préparer mon contact.

La fiche contient :

- informations générales ;

- analyse ;

- score ;

- historique ;

- notes.

# **US-017 --- Modifier le statut commercial**

**Priorité : P0**

### **User Story**

> En tant que commercial, je veux changer le statut d\'un prospect afin
> de suivre son évolution.

Pipeline :

Nouveau

↓

À contacter

↓

Contacté

↓

Démo

↓

Essai gratuit

↓

Client

# **US-018 --- Ajouter une note commerciale**

**Priorité : P0**

### **User Story**

> En tant que commercial, je veux noter mes échanges afin de conserver
> l\'historique.

Exemple :

25/07 :

Appelé le propriétaire.

Intéressé par un essai 30 jours.

Relancer lundi.

# **US-019 --- Programmer une relance**

**Priorité : P1**

### **User Story**

> En tant que commercial, je veux programmer une action future afin de
> ne pas oublier un prospect.

# **MODULE 07 --- DASHBOARD**

## **Objectif**

Piloter la stratégie commerciale.

# **US-020 --- Visualiser les KPIs**

**Priorité : P1**

### **User Story**

> En tant que fondateur, je veux voir les statistiques globales afin de
> mesurer la performance.

Indicateurs :

- restaurants analysés ;

- prospects prioritaires ;

- contacts réalisés ;

- essais ;

- conversions.

# **US-021 --- Voir les meilleures opportunités**

**Priorité : P0**

### **User Story**

> En tant que fondateur, je veux voir les meilleurs prospects actuels
> afin de savoir où concentrer mes efforts.

Exemple :

Top 20 prospects semaine

# **MODULE 08 --- ADMINISTRATION**

# **US-022 --- Gestion des utilisateurs**

**Priorité : P1**

### **User Story**

> En tant qu\'administrateur, je veux gérer les accès afin de sécuriser
> les données.

Rôles :

Admin

Commercial

Analyste

# **US-023 --- Gestion des paramètres**

**Priorité : P1**

### **User Story**

> En tant qu\'administrateur, je veux modifier les paramètres système
> afin d\'adapter TFLE.

Paramètres :

- fréquence d\'analyse ;

- règles ;

- intégrations.

# **MODULE 09 --- AUTOMATISATION FUTURE**

# **US-024 --- Analyse automatique planifiée**

**Priorité : P2**

### **User Story**

> En tant que système, je veux réanalyser régulièrement les restaurants
> afin de maintenir les informations à jour.

# **US-025 --- Détection d\'opportunités nouvelles**

**Priorité : P3**

### **User Story**

> En tant que TableFlash, je veux détecter automatiquement les
> changements importants afin d\'identifier de nouvelles opportunités.

Exemple :

Restaurant X

Avant :

Menu PDF

Maintenant :

Site refait mais aucune solution QR

Opportunité détectée

# **03.3 --- Synthèse MVP**

Pour la première version utilisable, TFLE doit absolument couvrir :

  ------------ -----------------------
   **Module**       **Fonction**

   Discovery     Trouver restaurants

   Collection       Créer fiches

    Analyse      Comprendre présence
                      digitale

       IA       Résumé + opportunité

    Scoring         Priorisation

      CRM         Suivi commercial

     Export      Utilisation terrain
  ------------ -----------------------

# **03.4 --- Règle fondamentale des User Stories**

Toute fonctionnalité future devra répondre à cette question :

> \"Est-ce que cette fonctionnalité aide TableFlash à trouver,
> comprendre ou convertir plus efficacement un restaurant ?\"

Si la réponse est non, elle n\'a pas sa place dans TFLE.
