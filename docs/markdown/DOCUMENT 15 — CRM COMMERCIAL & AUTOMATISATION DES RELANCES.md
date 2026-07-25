# **DOCUMENT 15 --- CRM COMMERCIAL & AUTOMATISATION DES RELANCES**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification fonctionnelle + technique CRM\
Module : Sales Pipeline & Customer Conversion Engine\
Produit : TableFlash Leads Engine**

# **15.1 --- Introduction**

Le module CRM de TFLE représente la couche de transformation
commerciale.

Le Scraping Engine trouve des restaurants.

Le Lead Scoring Engine identifie les opportunités.

Le CRM transforme ces opportunités en clients TableFlash.

La mission du CRM :

> Organiser chaque interaction commerciale afin qu\'aucun prospect
> intéressant ne soit oublié.

# **15.2 --- Philosophie CRM TFLE**

Le CRM n\'est pas conçu comme un simple carnet de contacts.

Il doit fonctionner comme un assistant commercial.

Il doit répondre :

- Qui contacter aujourd\'hui ?

- Quel prospect est bloqué ?

- Quelle action effectuer ?

- Pourquoi ce restaurant est prioritaire ?

- Où en sommes-nous dans la conversion ?

# **15.3 --- Architecture globale CRM**

PROSPECTS

↓

CRM PIPELINE

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Contacts

Activités

Tâches

Relances

Notes

Historique

Essais gratuits

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

CLIENT TABLEFLASH

# **15.4 --- Cycle de vie complet d\'un prospect**

Le parcours commercial TFLE :

Découvert

↓

Qualifié

↓

À contacter

↓

Contacté

↓

Réponse obtenue

↓

Démo proposée

↓

Essai gratuit 30 jours

↓

Client

↓

Ambassadeur

# **15.5 --- Statuts CRM**

## **STATUT 1 --- Découvert**

Restaurant trouvé automatiquement.

Données disponibles :

- nom ;

- adresse ;

- site ;

- score initial.

Aucune action commerciale réalisée.

## **STATUT 2 --- Qualifié**

Le prospect répond aux critères :

- score suffisant ;

- informations validées ;

- potentiel confirmé.

## **STATUT 3 --- À contacter**

Le prospect est prêt pour une action.

Informations nécessaires :

- email ;

- téléphone ;

- canal recommandé.

## **STATUT 4 --- Contacté**

Une première approche a été effectuée.

Exemples :

- email envoyé ;

- appel effectué ;

- message envoyé.

## **STATUT 5 --- Réponse obtenue**

Le restaurant a répondu.

Sous-statuts :

Intéressé

À rappeler

Pas maintenant

Refus

## **STATUT 6 --- Démo**

Le restaurant souhaite découvrir TableFlash.

Actions :

- planification démonstration ;

- présentation produit.

## **STATUT 7 --- Essai gratuit**

Le restaurant utilise TableFlash pendant 30 jours.

Suivi :

- activation ;

- utilisation ;

- retours.

## **STATUT 8 --- Client**

Conversion réussie.

Informations transférées :

- abonnement ;

- date début ;

- formule choisie.

# **15.6 --- Vue Pipeline Kanban**

Interface principale :

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Découverts

\[Restaurant A\]

Qualifiés

\[Restaurant B\]

À contacter

\[Restaurant C\]

Contactés

\[Restaurant D\]

Démo

\[Restaurant E\]

Essai 30 jours

\[Restaurant F\]

Clients

\[Restaurant G\]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **Actions possibles**

Sur une carte :

Ouvrir fiche

Changer statut

Créer tâche

Ajouter note

Voir historique

# **15.7 --- Fiche CRM Restaurant**

La fiche CRM reprend la fiche restaurant mais ajoute la dimension
commerciale.

# **En-tête**

Chez Martin

Bayonne

Score TFLE :

92/100

Statut :

Essai gratuit

Prochaine action :

Appeler vendredi

# **Section Informations commerciales**

Contact principal :

Jean Martin

Téléphone :

05 xx xx xx xx

Email :

contact@restaurant.fr

Dernier échange :

25/07/2026

# **Section Historique**

Timeline :

25/07

Email envoyé

27/07

Réponse positive

30/07

Démo réalisée

01/08

Début essai gratuit

# **Section Actions**

Boutons :

\+ Ajouter note

\+ Créer tâche

\+ Envoyer message

\+ Modifier statut

# **15.8 --- Gestion des contacts**

Un restaurant peut avoir plusieurs contacts.

Exemple :

Restaurant

\|

├── Gérant

├── Responsable salle

└── Associé

Table :

contacts

Champs :

id

restaurant_id

first_name

last_name

role

email

phone

preferred_contact_method

# **15.9 --- Gestion des activités commerciales**

Chaque interaction est enregistrée.

Types :

EMAIL

CALL

SMS

MEETING

DEMO

NOTE

Exemple :

{

\"type\":\"CALL\",

\"restaurant\":\"Chez Martin\",

\"result\":\"Interested\",

\"note\":

\"Souhaite tester la solution\"

}

# **15.10 --- Système de tâches commerciales**

Objectif :

Ne jamais perdre une opportunité.

Exemples :

Appeler restaurant X

Date :

28/07

Envoyer proposition

Date :

30/07

Relancer après essai

Date :

15/08

Table :

tasks

Champs :

id

restaurant_id

assigned_user

title

description

priority

due_date

status

# **Priorités**

## **Haute**

Action urgente.

Exemple :

Restaurant score 95.

## **Normale**

Suivi classique.

## **Faible**

Prospect secondaire.

# **15.11 --- Automatisation des relances**

C\'est un élément stratégique du CRM.

# **Principe**

Le système surveille :

- statut ;

- dernière interaction ;

- score ;

- absence de réponse.

Puis il propose ou crée une action.

# **Exemple 1**

## **Email envoyé sans réponse**

Après :

J+3

Création :

Relancer restaurant

# **Exemple 2**

## **Démo réalisée**

Après :

J+2

Création :

Demander retour démo

# **Exemple 3**

## **Essai gratuit**

Jour 7 :

Vérifier activation

Jour 20 :

Préparer conversion

Jour 28 :

Proposer abonnement

# **15.12 --- Séquence Essai Gratuit 30 jours**

Fonction essentielle pour TableFlash.

# **Jour 0 --- Activation**

Actions :

- création compte restaurant ;

- envoi instructions ;

- suivi installation.

# **Jour 3**

Objectif :

Vérifier première utilisation.

Message :

Avez-vous réussi à créer votre première carte ?

# **Jour 7**

Objectif :

Mesurer engagement.

Données :

- nombre produits créés ;

- QR générés ;

- commandes test.

# **Jour 14**

Objectif :

Recueillir feedback.

# **Jour 21**

Objectif :

Préparer conversion.

Analyse :

Utilisation élevée

↓

Client probable

# **Jour 28**

Objectif :

Transformer en abonnement.

# **Jour 30**

Résultat :

## **Converti**

→ Client.

## **Non converti**

→ Relance longue durée.

# **15.13 --- Scoring commercial dynamique**

Le CRM enrichit le score initial.

Exemple :

Score initial :

92

Après interactions :

Réponse positive :

+10

Démo réalisée :

+15

Score commercial :

117

Plafonné :

100

# **15.14 --- Automatisation IA commerciale**

L\'IA peut assister le commercial.

## **Avant contact**

Générer :

- email personnalisé ;

- script téléphone ;

- objections probables.

## **Après échange**

Analyser :

Notes :

> \"Intéressé mais trouve le prix élevé.\"

IA :

Objection principale :

Prix

Réponse recommandée :

Mettre en avant le gain de temps

et l\'essai gratuit.

# **15.15 --- Gestion des relances intelligentes**

L\'IA choisit :

- moment ;

- canal ;

- message.

Exemple :

Restaurant très actif midi :

Recommandation :

Contacter après 15h

Restaurant répond souvent par Facebook :

Recommandation :

Privilégier Messenger

# **15.16 --- Tables PostgreSQL CRM**

## **crm_pipeline**

id

restaurant_id

status

priority

assigned_user

created_at

updated_at

## **activities**

id

restaurant_id

user_id

type

content

created_at

## **tasks**

id

restaurant_id

title

priority

due_date

status

## **trials**

id

restaurant_id

start_date

end_date

status

conversion_date

## **customer_conversion**

id

restaurant_id

converted_at

subscription_type

# **15.17 --- Dashboard CRM**

Indicateurs :

## **Pipeline**

Prospects actifs

Démo

Essais

Clients

## **Performance commerciale**

Contacts réalisés

Réponses

Conversions

## **Essais gratuits**

Essais actifs

Taux conversion

Abandons

# **15.18 --- Permissions CRM**

## **Administrateur**

Tout accès.

## **Commercial**

Peut :

- modifier prospects ;

- créer activités ;

- gérer tâches.

## **Analyste**

Lecture uniquement.

# **15.19 --- MVP CRM**

Fonctionnalités obligatoires :

✅ Pipeline Kanban.

✅ Changement statut.

✅ Notes.

✅ Historique.

✅ Tâches.

✅ Suivi essai 30 jours.

# **15.20 --- V1 CRM**

Ajouts :

- automatisations avancées ;

- séquences email ;

- modèles messages ;

- statistiques commerciales.

# **15.21 --- V2 CRM**

Vision :

Un CRM semi-autonome.

L\'IA :

- prépare les relances ;

- analyse les échanges ;

- recommande les actions ;

- prédit les conversions.

# **Conclusion Document 15**

Le CRM TFLE est la dernière étape de transformation :

Données

↓

Prospects

↓

Opportunités

↓

Clients TableFlash

Sa valeur principale :

> Faire en sorte que chaque restaurant intéressant reçoive la bonne
> action commerciale au bon moment.
