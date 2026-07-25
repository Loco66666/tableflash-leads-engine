# **DOCUMENT 08 --- UX/UI COMPLÈTE**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification UX/UI\
Produit : TableFlash Leads Engine\
Type : Application interne d\'intelligence commerciale**

# **08.1 --- Introduction**

L\'objectif de l\'expérience utilisateur de TFLE est simple :

> Transformer une grande quantité de données commerciales en décisions
> rapides et évidentes.

TFLE ne doit pas ressembler à un simple tableau de données.

L\'utilisateur ne doit pas avoir l\'impression de \"chercher dans une
base\".

Il doit ressentir :

> \"L\'application m\'indique où concentrer mes efforts aujourd\'hui.\"

# **08.2 --- Principes UX fondamentaux**

## **Principe 1 --- Action avant information**

Une donnée seule n\'a pas de valeur.

Mauvais exemple :

Restaurant :

Chez Martin

Score :

87

Bon exemple :

Restaurant :

Chez Martin

Score :

87/100

Pourquoi :

✓ Menu PDF uniquement

✓ Aucun QR détecté

✓ Restaurant indépendant

Action recommandée :

Contacter cette semaine

# **Principe 2 --- La priorité doit être visible immédiatement**

Les informations importantes doivent apparaître en premier.

Ordre :

1\. Opportunité

2\. Pourquoi ?

3\. Action suivante

4\. Informations détaillées

# **Principe 3 --- Réduire la charge cognitive**

Un commercial doit pouvoir comprendre un prospect en moins de 30
secondes.

# **Principe 4 --- L\'IA doit rester transparente**

L\'utilisateur doit toujours savoir :

- d\'où vient l\'information ;

- pourquoi une recommandation existe ;

- quel niveau de confiance possède l\'analyse.

# **08.3 --- Architecture générale des écrans**

Navigation principale :

TABLEFLASH LEADS ENGINE

├── Dashboard

│

├── Prospects

│

├── Recherche

│

├── Analyses

│

├── Pipeline CRM

│

├── Intelligence IA

│

├── Statistiques

│

└── Administration

# **08.4 --- Structure globale de l\'application**

## **Layout principal**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Logo TableFlash Leads Engine

Sidebar Zone principale

Dashboard Contenu

Prospects

Recherche

CRM

Analytics

Paramètres

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **08.5 --- ÉCRAN 01 : Dashboard principal**

## **Objectif**

Donner une vision immédiate de l\'activité commerciale.

## **Structure**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Bonjour Julien 👋

Aujourd\'hui

\[ 320 \] Restaurants analysés

\[ 45 \] Prospects prioritaires

\[ 12 \] Relances prévues

\[ 6 \] Essais actifs

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

🔥 Opportunités prioritaires

Restaurant A

Score 94

Action :

Appeler aujourd\'hui

Restaurant B

Score 91

Action :

Envoyer proposition

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **Composants UI**

## **KPI Cards**

Chaque carte affiche :

- valeur ;

- évolution ;

- tendance.

Exemple :

Prospects qualifiés

1 250

+12% cette semaine

## **Liste priorité**

Composant essentiel.

Chaque ligne :

Nom restaurant

Ville

Score

Opportunité

Action

# **États possibles**

## **Chargement**

Afficher :

Skeleton loading.

## **Aucun prospect**

Message :

Aucun prospect prioritaire actuellement.

Lancer une nouvelle recherche.

## **Erreur**

Message :

Impossible de charger les données.

Réessayer.

# **08.6 --- ÉCRAN 02 : Recherche restaurants**

## **Objectif**

Permettre de lancer une campagne de découverte.

# **Structure**

Nouvelle recherche

Zone

\[ Bayonne \]

Rayon

\[ 30 km \]

Catégorie

\[ Restaurant \]

Options avancées

☐ Sans QR détecté

☐ Menu PDF

☐ Site ancien

\[BOUTON ANALYSER\]

# **Résultat**

Après lancement :

Analyse en cours\...

Restaurants trouvés :

248

Analyses terminées :

87

# **Composants**

## **Recherche géographique**

Possibilités :

- ville ;

- département ;

- région ;

- carte.

## **Filtres intelligents**

Exemples :

Afficher uniquement :

Score \> 80

Pas de QR

Pas de commande digitale

# **08.7 --- ÉCRAN 03 : Liste prospects**

## **Objectif**

Permettre une vue globale du marché.

# **Tableau principal**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Restaurant \| Ville \| Score \| Opportunité \| Statut

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Chez Paul \| Bayonne \| 92 \| Haute \| À contacter

La Table \| Anglet \| 75 \| Moyenne \| Contacté

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **Colonnes importantes**

Obligatoires :

- Nom ;

- Ville ;

- Score ;

- Statut ;

- Dernière action.

Colonnes secondaires :

- Site ;

- Email ;

- Téléphone ;

- Réseaux sociaux.

# **Filtres**

## **Commercial**

Statut :

Nouveau

Contacté

Démo

Essai

Client

## **Opportunité**

Score :

90+

70+

50+

## **Digital**

Sans QR

Menu PDF

Pas de site

# **08.8 --- ÉCRAN 04 : Fiche restaurant détaillée**

## **Écran le plus important de TFLE**

C\'est l\'endroit où la décision commerciale est prise.

# **Header**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Chez Martin

Bayonne

Score TableFlash

92/100

🔥 Forte opportunité

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **Bloc 01 --- Informations générales**

Adresse

Téléphone

Site

Catégorie

Horaires

# **Bloc 02 --- Analyse digitale**

Carte :

Présence digitale

Site :

Oui

Mobile :

Bon

Menu :

PDF

QR :

Non détecté

Commande :

Non

# **Bloc 03 --- Intelligence IA**

Carte :

Analyse IA

Ce restaurant semble être

un bon candidat car :

✓ Carte non interactive

✓ Restaurant indépendant

✓ Présence locale forte

Argument conseillé :

\"Vous pourriez simplifier

l\'accès à votre carte\...\"

# **Bloc 04 --- CRM**

Statut :

À contacter

Dernière action :

Aucune

Prochaine action :

Créer une relance

# **08.9 --- ÉCRAN 05 : Pipeline CRM**

## **Objectif**

Visualiser la conversion.

# **Vue Kanban**

Nouveaux

\[Restaurant A\]

À contacter

\[Restaurant B\]

Contactés

\[Restaurant C\]

Essais

\[Restaurant D\]

Clients

\[Restaurant E\]

# **Actions**

Glisser-déposer :

Contacté

↓

Démo

# **08.10 --- ÉCRAN 06 : Intelligence IA**

## **Objectif**

Explorer les recommandations générées.

Sections :

Analyses récentes

Tendances marché

Arguments commerciaux

Profils convertisseurs

# **Exemple**

Cette semaine :

Les restaurants avec :

✓ Menu PDF

✓ Plus de 100 avis

✓ Pas de QR

convertissent 2,4x mieux.

# **08.11 --- ÉCRAN 07 : Statistiques**

## **Objectif**

Mesurer la performance.

## **Graphiques**

### **Acquisition**

Restaurants analysés / mois

### **Conversion**

Contact

↓

Démo

↓

Essai

↓

Client

### **Zones**

Carte :

Pays Basque

Potentiel élevé

# **08.12 --- ÉCRAN 08 : Administration**

## **Objectif**

Gestion système.

Sections :

Utilisateurs

Permissions

Scoring

Sources

Paramètres IA

Logs

# **08.13 --- Design System**

## **Philosophie visuelle**

TFLE doit inspirer :

- intelligence ;

- fiabilité ;

- efficacité ;

- simplicité.

# **Couleurs fonctionnelles**

## **Priorité haute**

Rouge / orange :

Action urgente

## **Opportunité positive**

Vert :

Bon prospect

## **Information neutre**

Bleu :

Donnée

## **Attention**

Orange :

À vérifier

# **08.14 --- Typographie**

Recommandation :

- Inter ;

- Geist ;

- Roboto.

Hiérarchie :

Titre page

Titre section

Texte normal

Informations secondaires

# **08.15 --- Composants réutilisables**

## **Prospect Card**

Utilisée partout.

Contient :

Nom

Ville

Score

Statut

Action

## **Score Badge**

Exemple :

92

Excellent

## **AI Insight Card**

Contient :

Pourquoi ?

Que faire ?

## **Timeline**

Historique :

25/07

Analyse réalisée

26/07

Appel effectué

# **08.16 --- Responsive Design**

Même si TFLE est principalement desktop :

Support :

## **Desktop**

Usage principal :

- analyse ;

- CRM ;

- statistiques.

## **Tablette**

Usage commercial terrain.

## **Mobile**

Fonctions essentielles :

- consultation fiche ;

- ajout note ;

- changement statut.

# **08.17 --- Parcours utilisateur complet**

## **Parcours Fondateur**

Connexion

↓

Dashboard

↓

Voir opportunités

↓

Ouvrir fiche

↓

Analyser potentiel

↓

Décider action

## **Parcours Commercial**

Connexion

↓

Liste prospects

↓

Choisir restaurant

↓

Lire résumé IA

↓

Contacter

↓

Ajouter résultat

## **Parcours Analyste**

Recherche zone

↓

Lancer collecte

↓

Vérifier données

↓

Valider prospects

# **08.18 --- Règles UX critiques**

## **Règle 1**

Jamais afficher un score sans explication.

## **Règle 2**

Chaque prospect doit avoir une prochaine action.

## **Règle 3**

Les informations importantes doivent être visibles sans ouvrir 5 pages.

## **Règle 4**

L\'utilisateur doit toujours savoir :

Où suis-je ?

Que regarde-je ?

Quelle est la prochaine étape ?

# **08.19 --- Vision UX future**

À terme, TFLE pourrait évoluer vers un véritable :

## **\"Sales Command Center IA\"**

Avec :

- assistant commercial intégré ;

- recommandations quotidiennes ;

- agents IA ;

- prédiction de conversion ;

- automatisations.

# **Conclusion Document 08**

L\'expérience utilisateur de TFLE repose sur une idée centrale :

> Ne pas montrer plus de données, mais aider TableFlash à prendre de
> meilleures décisions commerciales.

L\'interface doit transformer :

**Données → Compréhension → Priorité → Action**
