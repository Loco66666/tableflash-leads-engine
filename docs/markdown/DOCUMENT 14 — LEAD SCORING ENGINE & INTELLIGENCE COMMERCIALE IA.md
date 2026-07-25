# **DOCUMENT 14 --- LEAD SCORING ENGINE & INTELLIGENCE COMMERCIALE IA**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Spécification fonctionnelle + technique IA\
Module : Qualification commerciale intelligente\
Produit : TableFlash Leads Engine**

# **14.1 --- Introduction**

Le **Lead Scoring Engine TFLE** est le cerveau de qualification
commerciale.

Son objectif :

> Transformer une base de restaurants en une liste priorisée de
> prospects ayant le plus fort potentiel de devenir clients TableFlash.

Le système doit répondre à trois questions :

1.  **Ce restaurant a-t-il un besoin réel ?**

2.  **Est-il susceptible d\'utiliser TableFlash ?**

3.  **Quelle action commerciale est la plus pertinente ?**

# **14.2 --- Philosophie du scoring**

Le score TFLE ne doit jamais être un simple nombre.

Un score sans explication n\'a aucune valeur commerciale.

Chaque score doit répondre :

Pourquoi ce restaurant est intéressant ?

Pourquoi maintenant ?

Quelle action effectuer ?

# **14.3 --- Architecture globale**

DONNÉES RESTAURANT

↓

DATA PROCESSING ENGINE

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Digital Maturity Analyzer

Business Profile Analyzer

Opportunity Detector

Conversion Predictor

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

LEAD SCORING ENGINE

↓

IA COMMERCIALE

↓

CRM TABLEFLASH

# **14.4 --- Les quatre niveaux d\'intelligence**

Le système fonctionne avec quatre couches.

# **Niveau 1 --- Données factuelles**

Informations observables.

Exemples :

- restaurant indépendant ;

- présence site ;

- menu PDF ;

- absence QR ;

- nombre d\'avis ;

- localisation.

# **Niveau 2 --- Analyse digitale**

Le moteur comprend la maturité numérique.

Questions :

- Le restaurant utilise-t-il des outils modernes ?

- Est-il en retard digitalement ?

- TableFlash apporte-t-il une amélioration visible ?

# **Niveau 3 --- Qualification commerciale**

Le système estime :

- besoin ;

- urgence ;

- facilité de conversion.

# **Niveau 4 --- Intelligence prédictive**

L\'IA apprend :

- quels profils deviennent clients ;

- quels profils refusent ;

- quelles approches fonctionnent.

# **14.5 --- Score principal TFLE**

Le score final est compris entre :

0 → 100

Classification :

  ----------- ------------- -------------------
   **Score**   **Niveau**    **Signification**

    90-100      Excellent        Prospect
                                prioritaire

     75-89        Très      Contact recommandé
               intéressant  

     50-74        Moyen         À analyser

     0-49        Faible       Faible priorité
  ----------- ------------- -------------------

# **14.6 --- Architecture du calcul**

Score final :

Score TFLE =

Digital Opportunity

\+

Business Fit

\+

Commercial Probability

\+

Local Priority

\-

Negative Signals

# **14.7 --- Module 1 : Digital Opportunity Score**

## **Objectif**

Mesurer le potentiel d\'amélioration digitale.

Poids :

## **Absence de QR Code**

+20 points

Pourquoi :

Le QR menu est une fonctionnalité centrale TableFlash.

## **Menu papier uniquement**

+20 points

## **Menu PDF non interactif**

+15 points

## **Pas de commande digitale**

+15 points

## **Site ancien ou peu optimisé mobile**

+10 points

## **Présence digitale faible**

+10 points

Maximum :

90 points

# **Exemple**

Restaurant :

Site ancien

Menu PDF

Pas de QR

Pas de commande

Calcul :

10

\+

15

\+

20

\+

15

=60 points

# **14.8 --- Module 2 : Business Fit Score**

## **Objectif**

Déterminer si le restaurant correspond à la cible TableFlash.

# **Restaurant indépendant**

+20

# **Restaurant traditionnel**

+15

# **Clientèle sur place importante**

+15

# **Carte avec nombreux produits**

+10

# **Plusieurs tables / service salle**

+10

# **Restaurant saisonnier**

+5

# **Points négatifs**

Franchise très contrôlée :

-20

# **Exemple**

Brasserie indépendante :

20

\+

15

\+

15

\+

10

=60 points

# **14.9 --- Module 3 : Commercial Probability Score**

Objectif :

Estimer la probabilité de conversion.

Critères :

## **Restaurant similaire aux clients existants**

+25

## **Zone géographique prioritaire**

+20

## **Taille adaptée**

+15

## **Contact facilement accessible**

+10

## **Activité récente**

+10

# **14.10 --- Module 4 : Negative Signals**

Le système retire des points.

Exemples :

## **Restaurant fermé**

-100

## **Déjà équipé d\'une solution concurrente équivalente**

-30

## **Très forte présence digitale**

-20

Pourquoi :

Le besoin TableFlash peut être faible.

## **Informations non vérifiées**

-15

# **14.11 --- Exemple complet**

Restaurant :

Chez Martin

Bayonne

Brasserie indépendante

Données :

Pas de QR +20

Menu PDF +15

Pas commande +15

Indépendant +20

Traditionnel +15

Zone prioritaire +20

Total :

105

Plafonné :

100/100

Résultat :

Score TFLE : 100

Priorité :

CRITIQUE

Action :

Contacter sous 48h

# **14.12 --- Explication obligatoire du score**

Chaque score génère un résumé.

Exemple :

Score : 92/100

Pourquoi ?

✓ Restaurant indépendant

✓ Menu uniquement PDF

✓ Aucun QR détecté

✓ Zone stratégique TableFlash

Opportunité :

Très forte

Action recommandée :

Proposer un essai gratuit 30 jours.

# **14.13 --- Intelligence IA commerciale**

Le scoring classique devient ensuite un moteur IA.

# **Objectifs IA**

L\'IA doit :

- comprendre le contexte ;

- générer des arguments ;

- prévoir les objections ;

- proposer une approche.

# **14.14 --- Analyse IA restaurant**

Entrées :

{

\"name\":\"Chez Marcel\",

\"city\":\"Bayonne\",

\"score\":92,

\"website\":\"true\",

\"menu\":\"pdf\"

}

Sortie :

{

\"opportunity\":\"HIGH\",

\"summary\":

\"Restaurant traditionnel avec faible digitalisation.\",

\"recommended_action\":

\"Proposer modernisation carte digitale.\",

\"confidence\":0.87

}

# **14.15 --- Générateur d\'approche commerciale**

L\'IA produit :

## **Email**

Exemple :

Bonjour,

Nous accompagnons les restaurants

qui souhaitent simplifier l\'accès

à leur carte grâce au QR code.

Nous proposons actuellement un essai

gratuit de 30 jours\...

## **Script téléphone**

Bonjour,

je me permets de vous appeler car\...

## **Message court**

Pour réseaux sociaux.

# **14.16 --- Analyse des objections**

L\'IA doit préparer :

Objection :

\"Nous avons déjà une carte papier.\"

Réponse :

\"TableFlash ne remplace pas votre carte papier,\
il ajoute une solution simple\...\"

\-\--

Objection :

\"C\'est trop compliqué.\"

Réponse :

\"Le système est conçu pour fonctionner

sans changer vos habitudes.\"

# **14.17 --- Modèle prédictif V2**

À terme TFLE apprend grâce aux résultats.

Données d\'apprentissage :

Prospect trouvé

↓

Score

↓

Contact

↓

Réponse

↓

Essai

↓

Client

Le modèle apprend :

Quels facteurs augmentent :

- réponse ;

- rendez-vous ;

- conversion.

# **14.18 --- Machine Learning futur**

Variables possibles :

## **Features restaurant**

- catégorie ;

- ville ;

- taille ;

- avis ;

- ancienneté.

## **Features digitales**

- site ;

- menu ;

- QR ;

- réservation.

## **Features commerciales**

- date contact ;

- méthode ;

- argument utilisé.

Sortie :

Probabilité conversion :

78%

# **14.19 --- Base de données nécessaire**

Tables :

## **lead_scores**

id

restaurant_id

score

category

calculation_details

created_at

## **scoring_rules**

id

name

condition

points

active

## **ai_insights**

id

restaurant_id

summary

arguments

confidence

created_at

## **conversion_history**

restaurant_id

initial_score

final_status

converted

# **14.20 --- Interface utilisateur**

Dans la fiche restaurant :

## **Carte Score**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Score TFLE

92/100

🔥 Très forte opportunité

Pourquoi :

✓ Pas de QR

✓ Menu PDF

✓ Restaurant indépendant

Action :

Contacter cette semaine

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

# **14.21 --- Paramétrage Admin**

L\'administrateur peut modifier :

- poids des critères ;

- seuils ;

- règles ;

- catégories.

Exemple :

Changer :

Pas de QR

+20

vers :

+25

# **14.22 --- Protection contre les erreurs IA**

Règles obligatoires :

L\'IA ne doit jamais :

❌ inventer une information.

❌ affirmer un besoin certain.

❌ générer une conclusion sans source.

Elle doit utiliser :

Information trouvée

↓

Hypothèse

↓

Niveau confiance

# **14.23 --- MVP Lead Scoring**

Version obligatoire :

✅ Score automatique.

✅ Règles configurables.

✅ Explication du score.

✅ Catégorie priorité.

✅ Suggestions IA simples.

# **14.24 --- Version 1**

Ajouts :

- apprentissage conversion ;

- scoring adaptatif ;

- segmentation automatique ;

- meilleurs arguments.

# **14.25 --- Version 2**

Vision :

Un commercial IA spécialisé restauration.

Capable de dire :

> \"Voici les 20 restaurants qui ont 80% de chances d\'accepter
> TableFlash cette semaine, avec l\'approche recommandée pour chacun.\"

# **Conclusion Document 14**

Le Lead Scoring Engine est l\'élément qui transforme TFLE d\'un simple
scraper en véritable outil stratégique.

La différence fondamentale :

Un scraper dit :

> \"Voici 10 000 restaurants.\"

TFLE doit dire :

> \"Voici les 50 restaurants qui méritent votre temps aujourd\'hui,
> voici pourquoi, et voici comment les convertir.\"
