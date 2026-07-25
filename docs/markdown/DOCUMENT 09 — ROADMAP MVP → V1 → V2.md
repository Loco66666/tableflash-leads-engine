# **DOCUMENT 09 --- ROADMAP MVP → V1 → V2**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Plan stratégique de développement\
Produit : TableFlash Leads Engine\
Type : Outil interne d\'intelligence commerciale**

# **09.1 --- Introduction**

Ce document définit la trajectoire de développement de TFLE.

L\'objectif n\'est pas de construire immédiatement une plateforme
complexe, mais de construire progressivement un système qui apporte de
la valeur à chaque étape.

La stratégie retenue :

> Construire d\'abord un moteur de prospection efficace pour TableFlash,
> puis évoluer vers une véritable plateforme d\'intelligence
> commerciale.

# **09.2 --- Vision globale de l\'évolution**

TABLEFLASH LEADS ENGINE

PHASE MVP

\|

\|

Trouver les restaurants

Analyser leur potentiel

Prioriser les contacts

↓

VERSION 1

\|

\|

Automatiser la prospection

Structurer le CRM

Mesurer les conversions

↓

VERSION 2

\|

\|

Intelligence commerciale IA

Prédiction

Agents autonomes

Veille marché

# **09.3 --- Objectifs par phase**

  ----------- ----------------------------------
   **Phase**        **Objectif principal**

      MVP     Obtenir un système utilisable par
                          TableFlash

      V1        Industrialiser la prospection

      V2       Créer un avantage concurrentiel
                        grâce à l\'IA
  ----------- ----------------------------------

# **PHASE 1 --- MVP (Minimum Viable Product)**

## **Objectif**

Créer la première version réellement utilisée par TableFlash.

Le MVP doit répondre à une question :

> \"Quels restaurants dois-je contacter aujourd\'hui et pourquoi ?\"

# **Durée estimée**

## **6 à 10 semaines**

(selon disponibilité et niveau d\'automatisation souhaité)

# **Fonctionnalités MVP obligatoires**

# **MODULE 1 --- Authentification**

## **Fonctionnalités**

- connexion utilisateur ;

- gestion des rôles simples.

## **Rôles initiaux**

ADMIN

COMMERCIAL

## **Critères de validation**

✅ Un utilisateur peut se connecter.

✅ Les droits sont respectés.

# **MODULE 2 --- Base restaurants**

## **Fonctionnalités**

Création d\'une fiche restaurant.

Informations :

- nom ;

- adresse ;

- ville ;

- téléphone ;

- site ;

- catégorie.

## **Critères**

✅ Chaque restaurant possède un identifiant unique.

✅ Les doublons sont détectables.

# **MODULE 3 --- Import / Collecte initiale**

## **Objectif**

Alimenter rapidement la base.

Sources possibles :

- imports structurés ;

- collecte automatisée ;

- ajout manuel.

Version MVP :

Priorité à la fiabilité avant le volume.

Critères :

✅ Plusieurs centaines de restaurants peuvent être intégrés.

# **MODULE 4 --- Analyse digitale simple**

## **Fonctionnalités**

Analyser :

- présence site web ;

- présence menu ;

- type menu ;

- QR détecté ou non.

Exemple :

Restaurant X

Site :

Oui

Menu :

PDF

QR :

Non détecté

Critères :

✅ L\'analyse produit des informations exploitables.

# **MODULE 5 --- Lead Scoring**

## **Objectif**

Classer les prospects.

Version MVP :

Score basé sur règles fixes.

Exemple :

Pas de QR :

+20

Menu PDF :

+15

Restaurant indépendant :

+20

Site ancien :

+10

Résultat :

Score :

87/100

Priorité élevée

Critères :

✅ Chaque restaurant possède un score.

✅ Le score est explicable.

# **MODULE 6 --- IA commerciale simple**

## **Fonctionnalités**

Générer :

- résumé du restaurant ;

- opportunité ;

- argument commercial.

Exemple :

Opportunité :

Bonne

Pourquoi :

Restaurant indépendant.

Carte PDF uniquement.

Absence de QR.

Approche :

Proposer une modernisation

de la carte digitale.

Critères :

✅ L\'IA explique ses recommandations.

# **MODULE 7 --- CRM minimal**

## **Pipeline :**

Nouveau

↓

À contacter

↓

Contacté

↓

Essai gratuit

↓

Client

Fonctions :

- changer statut ;

- ajouter note ;

- historique.

Critères :

✅ Un prospect peut être suivi jusqu\'à conversion.

# **MODULE 8 --- Dashboard MVP**

Afficher :

Restaurants analysés

Prospects prioritaires

Contacts réalisés

Essais

Clients

# **MVP --- Résultat attendu**

À la fin du MVP :

TableFlash doit pouvoir :

1.  Trouver des restaurants.

2.  Voir leur potentiel.

3.  Choisir lesquels contacter.

4.  Suivre les échanges.

5.  Mesurer les résultats.

# **PHASE 2 --- VERSION 1**

## **Objectif**

Passer d\'un outil utile à un véritable moteur commercial.

# **Durée estimée**

## **3 à 6 mois après MVP**

# **Fonctionnalités V1**

# **1 --- Automatisation complète de collecte**

## **Ajout :**

- tâches planifiées ;

- nouvelles recherches automatiques ;

- surveillance zones.

Exemple :

Chaque lundi :

Nouvelle analyse :

Pays Basque

↓

Restaurants détectés

↓

Prospects ajoutés

# **2 --- Analyse web avancée**

Amélioration :

- qualité site ;

- technologie utilisée ;

- expérience mobile ;

- réservation ;

- commande.

# **3 --- Scoring intelligent**

Passage :

Règles fixes

↓

Scoring adaptatif

Le système apprend selon :

- essais gratuits ;

- conversions ;

- profils clients.

# **4 --- CRM complet**

Ajout :

- tâches ;

- rappels ;

- calendrier ;

- historique complet ;

- segmentation.

Pipeline avancé :

Découvert

↓

Qualifié

↓

Contacté

↓

Rendez-vous

↓

Démo

↓

Essai 30 jours

↓

Client

↓

Ambassadeur

# **5 --- Génération automatique des messages**

IA capable de proposer :

- email ;

- message Facebook ;

- script téléphone.

Exemple :

Restaurant :

Brasserie X

Situation :

Menu PDF

Message conseillé :

Bonjour,

nous avons remarqué que votre carte\...

# **6 --- Analytics avancés**

Mesurer :

- taux de réponse ;

- taux conversion ;

- meilleure zone ;

- meilleur profil client.

Exemple :

Restaurants avec menu PDF :

Conversion :

18%

Restaurants sans site :

Conversion :

4%

# **PHASE 3 --- VERSION 2**

## **Objectif**

Créer un avantage technologique majeur.

# **Vision**

TFLE devient :

> Un assistant commercial IA spécialisé dans la restauration.

# **Fonctionnalités V2**

# **1 --- Agents IA spécialisés**

Architecture :

TFLE AI MANAGER

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Agent Recherche

Agent Analyse

Agent Commercial

Agent Veille

Agent Data Quality

## **Agent Recherche**

Mission :

Trouver de nouveaux restaurants.

## **Agent Analyse**

Mission :

Comprendre leur situation digitale.

## **Agent Commercial**

Mission :

Préparer les meilleures approches.

# **2 --- Prédiction de conversion**

Le système pourra répondre :

> \"Quels restaurants ont le plus de chances de devenir clients ?\"

Exemple :

Restaurant A

Probabilité estimée :

82%

Raisons :

\- Profil similaire aux clients existants

\- Besoin digital élevé

\- Zone favorable

# **3 --- Veille permanente du marché**

Le système surveille :

- nouvelles ouvertures ;

- changements de site ;

- nouveaux services ;

- évolution digitale.

Exemple :

Restaurant X

Ancien état :

Menu papier

Nouveau :

Site refait

Opportunité détectée

# **4 --- Assistant commercial conversationnel**

Un chat interne :

Question :

> \"Trouve-moi 20 restaurants similaires à mes meilleurs clients.\"

Réponse :

20 prospects trouvés.

Score moyen :

88/100.

Arguments préparés.

# **5 --- Base de connaissance TableFlash**

Création d\'un cerveau interne :

Données :

- objections clients ;

- réponses efficaces ;

- arguments gagnants ;

- historiques commerciaux.

# **09.4 --- Ordre de développement recommandé**

L\'ordre doit être strict :

1

Base restaurants

↓

2

Collecte données

↓

3

Analyse digitale

↓

4

Scoring

↓

5

IA

↓

6

CRM

↓

7

Automatisation

↓

8

Prédiction

# **09.5 --- Fonctionnalités volontairement repoussées**

Certaines idées sont intéressantes mais non prioritaires.

## **Envoi automatique massif d\'emails**

Pourquoi repoussé :

- nécessite une stratégie commerciale mature ;

- risque de mauvaise qualification ;

- conformité à gérer.

## **Marketplace**

Hors objectif.

## **Vente externe du logiciel**

Non prévu.

TFLE reste un outil interne TableFlash.

## **Système trop complexe d\'agents IA**

Attendre d\'avoir assez de données.

# **09.6 --- Indicateurs de réussite**

## **MVP**

Objectifs :

- 1 000+ restaurants analysés ;

- premiers prospects qualifiés ;

- premiers essais TableFlash obtenus.

## **V1**

Objectifs :

- prospection régulière ;

- suivi commercial complet ;

- amélioration du taux de conversion.

## **V2**

Objectifs :

- prédiction fiable ;

- automatisation avancée ;

- avantage concurrentiel.

# **09.7 --- Stratégie finale**

La construction de TFLE doit suivre cette philosophie :

Ne pas construire un gros outil.

Construire un outil qui devient indispensable.

Chaque version doit apporter une amélioration mesurable :

### **MVP**

\"Je trouve mes prospects.\"

### **V1**

\"Je transforme mieux mes prospects.\"

### **V2**

\"Le système m\'aide à savoir qui deviendra client.\"

# **Conclusion Document 09**

TableFlash Leads Engine est conçu comme un actif stratégique interne.

La progression logique est :

**Recherche → Qualification → Conversion → Intelligence**

Le projet commence comme un outil de prospection spécialisé
restauration, mais son architecture permet d\'évoluer vers un véritable
moteur d\'intelligence commerciale basé sur la donnée et l\'IA.

# **FIN DU DOSSIER FONDATEUR TFLE --- DOCUMENTS 00 À 09**

## **Prochaines étapes recommandées pour poursuivre le PRD complet :**

**Document 10 --- Spécifications fonctionnelles détaillées écran par
écran\**
→ Description encore plus précise de chaque page, bouton, action, règle
et comportement.

**Document 11 --- Spécifications API Backend\**
→ Toutes les routes, paramètres, réponses et règles métier.

**Document 12 --- Plan de développement technique Sprint par Sprint\**
→ Découpage concret pour commencer le codage.
