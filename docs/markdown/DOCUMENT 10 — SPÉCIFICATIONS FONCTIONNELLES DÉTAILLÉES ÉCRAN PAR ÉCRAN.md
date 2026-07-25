# **DOCUMENT 10 --- SPÉCIFICATIONS FONCTIONNELLES DÉTAILLÉES ÉCRAN PAR ÉCRAN**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification fonctionnelle détaillée\
Produit : TableFlash Leads Engine\
Type : Application interne de prospection intelligente restaurants**

# **10.1 --- Introduction**

Ce document transforme l\'architecture fonctionnelle TFLE en
spécifications directement exploitables par :

- UX/UI Designer ;

- développeur Frontend ;

- développeur Backend ;

- QA/Testeur ;

- Product Owner.

Chaque écran décrit :

- son objectif ;

- son rôle dans le parcours utilisateur ;

- sa structure ;

- ses composants ;

- les actions possibles ;

- les règles métier ;

- les états ;

- les critères d\'acceptation.

# **10.2 --- Structure globale de navigation**

## **Navigation principale**

TABLEFLASH LEADS ENGINE

├── Dashboard

│

├── Prospects

│

├── Recherche

│

├── Analyses

│

├── CRM

│

├── Intelligence IA

│

├── Statistiques

│

└── Administration

# **10.3 --- ÉCRAN AUTH-01 : Connexion**

## **Objectif**

Permettre uniquement aux membres autorisés de TableFlash d\'accéder à
TFLE.

# **Interface**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

TableFlash Leads Engine

Email

\[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]

Mot de passe

\[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\]

\[ Se connecter \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **Composants**

## **Champ Email**

Type :

- email.

Validation :

- format obligatoire ;

- impossible vide.

## **Champ Mot de passe**

Validation :

- minimum selon politique sécurité.

## **Bouton \"Se connecter\"**

Action :

1.  Vérification identifiants.

2.  Création session.

3.  Redirection Dashboard.

# **États**

## **Chargement**

Bouton :

Connexion\...

## **Erreur**

Message :

Identifiants incorrects.

Veuillez réessayer.

## **Succès**

Redirection :

/dashboard

# **Critères d\'acceptation**

✅ Un utilisateur valide accède à l\'application.

✅ Un utilisateur inconnu est bloqué.

✅ Une session sécurisée est créée.

# **ÉCRAN DASH-01 : Dashboard principal**

# **Objectif**

Être le centre de décision quotidien.

Question utilisateur :

> \"Sur quoi dois-je agir aujourd\'hui ?\"

# **Structure écran**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Bonjour 👋

Résumé activité

\[Restaurants analysés\]

\[Prospects prioritaires\]

\[Relances du jour\]

\[Essais actifs\]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

🔥 Priorités commerciales

Restaurant

Score

Action recommandée

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Dernières activités

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **Bloc 1 --- KPI Cards**

## **Carte Restaurants analysés**

Affiche :

- nombre total ;

- évolution période précédente.

Exemple :

12 540

+340 cette semaine

## **Carte Prospects prioritaires**

Calcul :

Restaurants avec :

score \>= seuil priorité

## **Carte Relances**

Nombre :

tâches prévues aujourd\'hui

## **Carte Essais actifs**

Nombre :

restaurants en période essai TableFlash

# **Bloc 2 --- Liste \"Priorités commerciales\"**

Chaque ligne :

Restaurant

Ville

Score

Opportunité

Action

Exemple :

Chez Marcel

Bayonne

94/100

Très forte

Appeler aujourd\'hui

# **Actions disponibles**

Cliquer sur restaurant :

→ ouverture fiche restaurant.

Bouton :

Voir tous les prospects

→ /prospects

# **Règles métier**

Les prospects affichés sont triés :

1.  Score décroissant.

2.  Dernière activité.

3.  Priorité commerciale.

# **Critères d\'acceptation**

✅ Le dashboard affiche une vision immédiate.

✅ Les prospects prioritaires sont accessibles en un clic.

# **ÉCRAN SEARCH-01 : Recherche restaurants**

# **Objectif**

Permettre de lancer une campagne de découverte.

# **Structure**

Nouvelle recherche

Zone géographique

Ville :

\[\_\_\_\_\_\_\_\_\]

Rayon :

\[\_\_\_\_\_\_\_\_\]

Catégorie :

☐ Traditionnel

☐ Brasserie

☐ Burger

☐ Pizzeria

Options :

☐ Sans QR détecté

☐ Sans commande digitale

☐ Menu PDF

\[Lancer recherche\]

# **Composants**

## **Sélecteur géographique**

Options :

- ville ;

- département ;

- région.

## **Catégories**

Multi-sélection.

## **Filtres opportunité**

Exemples :

Restaurants sans QR

Restaurants sans réservation

Restaurants sans menu digital

# **Action \"Lancer recherche\"**

Processus :

Validation paramètres

↓

Création recherche

↓

Lancement collecte

↓

Affichage progression

# **État progression**

Recherche en cours

Restaurants trouvés :

350

Analysés :

120

Temps estimé :

15 min

# **Critères d\'acceptation**

✅ Une recherche peut être sauvegardée.

✅ L\'utilisateur voit la progression.

✅ Les doublons sont évités.

# **ÉCRAN PROS-01 : Liste des prospects**

# **Objectif**

Explorer l\'ensemble du portefeuille.

# **Vue principale**

Tableau :

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nom

Ville

Score

Statut

Dernière action

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Chez Paul

Bayonne

91

À contacter

Jamais

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **Colonnes obligatoires**

- Nom.

- Ville.

- Score.

- Statut.

- Dernière action.

# **Filtres**

## **Score**

Tous

90+

70+

50+

## **Statut CRM**

Nouveau

Contacté

Démo

Essai

Client

## **Opportunités**

Sans QR

Menu PDF

Sans commande

# **Actions ligne**

Menu :

Voir fiche

Modifier statut

Ajouter note

Créer tâche

# **Critères d\'acceptation**

✅ Recherche instantanée.

✅ Filtres combinables.

✅ Pagination fonctionnelle.

# **ÉCRAN REST-01 : Fiche restaurant**

# **Objectif**

Être la source complète de décision.

# **En-tête**

Chez Martin

Bayonne

Score :

92/100

🔥 Prospect prioritaire

\[Modifier statut\]

\[Créer tâche\]

# **SECTION 1 --- Informations générales**

Affiche :

- nom ;

- adresse ;

- téléphone ;

- site ;

- catégorie.

Actions :

Modifier manuellement.

# **SECTION 2 --- Analyse digitale**

Carte :

Présence digitale

Site :

Oui

Menu :

PDF

QR :

Non détecté

Commande :

Non disponible

# **SECTION 3 --- Score**

Affiche :

92/100

Détail :

+20 Restaurant indépendant

+15 Menu PDF

+15 Pas de QR

# **SECTION 4 --- Intelligence IA**

Affiche :

## **Résumé**

Exemple :

> Restaurant avec une présence digitale limitée, fort potentiel de
> modernisation.

## **Arguments commerciaux**

Mettre en avant :

\- suppression menu papier

\- modification facile de carte

\- expérience client

# **SECTION 5 --- CRM**

Affiche :

Statut :

À contacter

Dernière action :

Aucune

Prochaine action :

Créer relance

# **SECTION 6 --- Timeline**

Historique :

25/07

Restaurant découvert

26/07

Analyse terminée

27/07

Contact effectué

# **Critères d\'acceptation**

✅ Toutes les informations importantes sont visibles.

✅ L\'utilisateur peut passer de l\'analyse à l\'action.

# **ÉCRAN CRM-01 : Pipeline commercial**

# **Objectif**

Suivre les prospects jusqu\'au client.

# **Vue Kanban**

Colonnes :

Nouveaux

À contacter

Contactés

Démo

Essai 30 jours

Clients

# **Carte prospect**

Contient :

Nom

Ville

Score

Dernière action

# **Actions**

Drag & drop :

Exemple :

Contacté

↓

Démo

Lors du déplacement :

Fenêtre confirmation :

Changer le statut ?

\[Annuler\]

\[Confirmer\]

# **Règles**

Chaque changement crée :

- historique ;

- date ;

- utilisateur.

# **Critères**

✅ Aucun changement n\'est perdu.

✅ Historique complet disponible.

# **ÉCRAN AI-01 : Intelligence artificielle**

# **Objectif**

Centraliser les analyses IA.

# **Sections**

## **Dernières analyses**

Liste :

Restaurant

Score IA

Résumé

Date

## **Suggestions commerciales**

Exemple :

Les restaurants avec menu PDF

semblent avoir un meilleur potentiel.

## **Générateur d\'approche**

Entrée :

Restaurant sélectionné

Sortie :

Email personnalisé

Script téléphone

Message court

# **Règles**

L\'IA doit :

- expliquer ses recommandations ;

- conserver les historiques ;

- indiquer le niveau de confiance.

# **ÉCRAN STAT-01 : Statistiques**

# **Objectif**

Mesurer la performance commerciale.

# **Graphiques**

## **Acquisition**

Restaurants trouvés / mois

## **Conversion**

Contact

↓

Démo

↓

Essai

↓

Client

## **Performance zones**

Ville

Nombre prospects

Conversion

# **Critères**

✅ Les statistiques correspondent aux données CRM.

# **ÉCRAN ADMIN-01 : Administration**

# **Objectif**

Contrôler le système.

# **Sections**

## **Utilisateurs**

Gestion :

- création ;

- suppression ;

- rôles.

## **Scoring**

Modifier :

- règles ;

- pondérations ;

- seuils.

## **Sources**

Gestion :

- sources utilisées ;

- fréquence collecte.

## **IA**

Paramètres :

- modèles ;

- limites ;

- coûts.

# **10.4 --- Règles globales UX**

## **Règle 1**

Toute information importante doit avoir une source.

## **Règle 2**

Toute recommandation IA doit être expliquée.

## **Règle 3**

Tout prospect doit avoir un statut.

## **Règle 4**

Tout prospect prioritaire doit proposer une action suivante.

# **10.5 --- États globaux de l\'application**

## **Chargement**

Toujours afficher :

- skeleton ;

- progression.

## **Erreur**

Toujours afficher :

- cause simple ;

- action possible.

## **Vide**

Toujours afficher :

- explication ;

- bouton d\'action.

# **10.6 --- Résumé fonctionnel**

TFLE doit permettre ce parcours complet :

Recherche restaurant

↓

Création fiche

↓

Analyse digitale

↓

Score IA

↓

Recommandation

↓

Action commerciale

↓

Conversion TableFlash

# **Conclusion Document 10**

Ce document transforme TFLE d\'une vision produit en une spécification
exploitable par une équipe de développement.

Chaque écran possède :

- un objectif ;

- des composants ;

- des règles métier ;

- des comportements attendus.
