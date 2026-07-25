# **DOCUMENT 16 --- INTELLIGENCE ARTIFICIELLE TFLE & ARCHITECTURE DES AGENTS IA**

# **TableFlash Leads Engine (TFLE)**

**Version : 1.0\
Statut : Architecture IA fonctionnelle + technique\
Module : Artificial Intelligence & Autonomous Sales Intelligence\
Produit : TableFlash Leads Engine**

# **16.1 --- Introduction**

L\'intelligence artificielle représente la couche d\'intelligence
stratégique de TFLE.

L\'objectif n\'est pas simplement d\'ajouter un chatbot.

L\'objectif est de construire progressivement une **équipe commerciale
IA interne** capable d\'assister TableFlash dans :

- la recherche de restaurants ;

- l\'analyse des opportunités ;

- la qualification ;

- la préparation des contacts ;

- le suivi commercial ;

- l\'amélioration continue.

# **16.2 --- Vision IA TFLE**

La vision finale :

> Transformer TFLE d\'un outil de prospection automatisé en un véritable
> collaborateur commercial augmenté.

Évolution prévue :

Niveau 1

IA Assistante

↓

Niveau 2

IA Analyste commerciale

↓

Niveau 3

Agents spécialisés

↓

Niveau 4

Équipe commerciale IA autonome

# **16.3 --- Principes fondateurs IA**

## **Principe 1 --- L\'IA ne remplace pas la décision humaine**

L\'IA recommande.

L\'humain valide.

## **Principe 2 --- Toute information doit être traçable**

L\'IA doit savoir :

- d\'où vient l\'information ;

- quand elle a été collectée ;

- son niveau de confiance.

## **Principe 3 --- Pas d\'hallucination commerciale**

L\'IA ne doit jamais inventer :

❌ un problème inexistant.

❌ un équipement absent.

❌ une information privée.

Elle doit formuler :

Information détectée :

Le restaurant utilise un menu PDF.

Hypothèse :

Une carte interactive pourrait améliorer

l\'expérience client.

Confiance :

87 %

# **16.4 --- Architecture globale IA**

DONNÉES TFLE

↓

AI ORCHESTRATOR

↓

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Agent Discovery

Agent Analyste

Agent Scoring

Agent Commercial

Agent CRM

Agent Data Quality

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

↓

Base Mémoire IA

↓

Utilisateur TFLE

# **16.5 --- AI Orchestrator**

Le chef d\'orchestre des agents.

Son rôle :

- distribuer les tâches ;

- sélectionner l\'agent adapté ;

- gérer les priorités ;

- contrôler les réponses.

Exemple :

Nouvelle fiche restaurant :

Restaurant trouvé

↓

Orchestrateur

↓

Agent Analyste

↓

Agent Scoring

↓

Agent Commercial

↓

CRM

# **16.6 --- Les agents IA TFLE**

# **AGENT 1 --- Discovery Intelligence Agent**

## **Mission**

Aider à trouver les meilleurs prospects.

Responsabilités :

- analyser les zones géographiques ;

- recommander des recherches ;

- identifier des opportunités.

Entrée :

{

\"zone\":\"Pays Basque\",

\"objectif\":\"trouver restaurants indépendants\"

}

Sortie :

{

\"recommendation\":

\"Prioriser Bayonne centre\",

\"reason\":

\"Forte densité restaurants traditionnels\"

}

# **AGENT 2 --- Restaurant Analyst Agent**

## **Mission**

Comprendre chaque restaurant.

Analyse :

- site web ;

- menu ;

- réseaux publics ;

- maturité digitale ;

- positionnement.

Exemple :

Entrée :

Restaurant Martin

Sortie :

Restaurant traditionnel indépendant.

Présence digitale faible.

Opportunité élevée pour QR menu.

# **AGENT 3 --- Lead Scoring Agent**

## **Mission**

Calculer et expliquer la priorité.

Fonctions :

- appliquer règles ;

- analyser contexte ;

- expliquer score.

Sortie :

Score :

91/100

Priorité :

Contact immédiat

# **AGENT 4 --- Sales Assistant Agent**

## **Mission**

Préparer l\'approche commerciale.

Il génère :

- email ;

- script téléphone ;

- message réseaux sociaux ;

- argumentaire.

Exemple :

Entrée :

Restaurant traditionnel

Pas de QR

Menu papier

Sortie :

Angle commercial :

Moderniser l\'expérience client

sans changer les habitudes.

# **AGENT 5 --- CRM Assistant Agent**

## **Mission**

Aider au suivi.

Fonctions :

- proposer relances ;

- analyser historique ;

- détecter blocages.

Exemple :

Prospect sans réponse depuis 7 jours.

Action recommandée :

Relance courte email.

# **AGENT 6 --- Data Quality Agent**

## **Mission**

Garantir la qualité des données.

Détecte :

- doublons ;

- erreurs ;

- informations obsolètes.

Exemple :

Deux fiches semblent correspondre

au même restaurant.

Confiance fusion :

94%.

# **16.7 --- Architecture mémoire IA**

La mémoire est essentielle.

TFLE utilise plusieurs niveaux.

# **Mémoire courte durée**

Contexte d\'une tâche.

Exemple :

Analyse d\'un restaurant.

Stockage :

Quelques minutes/heures.

# **Mémoire métier**

Connaissances TableFlash.

Exemple :

- positionnement produit ;

- tarifs ;

- objections fréquentes ;

- arguments commerciaux.

# **Mémoire historique**

Apprentissage commercial.

Exemple :

Restaurant similaire

↓

Contact effectué

↓

Client converti

# **Mémoire utilisateur**

Préférences internes.

Exemple :

- style de message ;

- méthode commerciale ;

- zones prioritaires.

# **16.8 --- Architecture RAG TFLE**

RAG :

**Retrieval Augmented Generation**

Principe :

L\'IA consulte une base documentaire avant de répondre.

Architecture :

Documents TFLE

↓

Vector Database

↓

Recherche contexte

↓

LLM

↓

Réponse IA

# **16.9 --- Documents utilisés par le RAG**

Sources internes :

## **Produit TableFlash**

- fonctionnalités ;

- avantages ;

- FAQ.

## **Commercial**

- scripts ;

- emails ;

- objections.

## **Restaurants**

- analyses précédentes ;

- historiques.

## **Stratégie**

- marchés prioritaires ;

- résultats campagnes.

# **16.10 --- Base vectorielle**

Technologies possibles :

## **MVP**

PostgreSQL + pgvector.

## **V1**

Solutions dédiées :

- Qdrant ;

- Weaviate ;

- Pinecone.

Structure :

Document

↓

Chunks

↓

Embeddings

↓

Recherche sémantique

# **16.11 --- Choix des modèles IA**

Architecture hybride.

# **Modèle rapide**

Utilisation :

- classification ;

- extraction ;

- tâches simples.

# **Modèle puissant**

Utilisation :

- stratégie ;

- génération commerciale ;

- analyse complexe.

# **Modèle spécialisé futur**

Possibilité :

- modèle fine-tuné restauration ;

- modèle interne TableFlash.

# **16.12 --- Gestion des prompts système**

Chaque agent possède son propre prompt.

Exemple :

## **Sales Assistant Agent**

Tu es un assistant commercial spécialisé

dans la vente de TableFlash aux restaurants.

Objectifs :

\- comprendre le besoin du restaurant ;

\- proposer un argument pertinent ;

\- rester naturel.

Contraintes :

\- ne jamais inventer ;

\- utiliser uniquement les données disponibles.

# **16.13 --- Prompt Engineering Framework**

Chaque prompt contient :

ROLE

OBJECTIF

CONTEXTE

DONNÉES DISPONIBLES

RÈGLES

FORMAT DE SORTIE

CRITÈRES QUALITÉ

# **16.14 --- Exemple workflow IA complet**

Nouveau restaurant détecté :

## **Étape 1**

Discovery Agent :

Restaurant trouvé.

## **Étape 2**

Analyst Agent :

Analyse site.

Menu PDF détecté.

Pas de QR.

## **Étape 3**

Scoring Agent :

Score :

88/100.

## **Étape 4**

Sales Agent :

Prépare email personnalisé.

## **Étape 5**

CRM Agent :

Crée tâche de contact.

# **16.15 --- Système de confiance IA**

Chaque réponse possède :

{

\"confidence\":0.91,

\"sources\":\[

\"website_analysis\",

\"restaurant_database\"

\]

}

Niveaux :

  --------------- -------------------
   **Confiance**      **Action**

       \>90%        Automatisation
                       possible

      70-90%      Validation humaine

       \<70%            Analyse
                    supplémentaire
  --------------- -------------------

# **16.16 --- Garde-fous IA**

Obligatoires :

## **Validation humaine**

Avant :

- envoi massif ;

- changement CRM important.

## **Limites actions**

L\'IA ne peut pas :

- supprimer prospects ;

- envoyer campagnes sans validation ;

- modifier règles scoring seule.

## **Audit logs**

Chaque décision IA est enregistrée.

# **16.17 --- Monitoring IA**

Dashboard :

Nombre analyses IA

Temps moyen réponse

Coût IA

Erreurs

Taux validation humaine

Précision prédictions

# **16.18 --- Base de données IA**

## **ai_agents**

id

name

version

prompt_version

status

## **ai_tasks**

id

agent_id

input

output

status

created_at

## **ai_memory**

id

type

content

embedding

metadata

## **ai_feedback**

id

task_id

human_rating

correction

# **16.19 --- Apprentissage continu**

Chaque action commerciale devient une donnée.

Exemple :

Score 90

↓

Contact

↓

Refus

Le système apprend :

Ce profil était surestimé.

Autre exemple :

Score 75

↓

Client

Le système apprend :

Ce profil est sous-évalué.

# **16.20 --- MVP IA**

Version minimale :

✅ Analyse restaurant automatique.

✅ Résumé IA.

✅ Explication score.

✅ Génération message commercial.

✅ Suggestions relances.

# **16.21 --- V1 IA**

Ajouts :

- mémoire RAG ;

- agents spécialisés ;

- analyse objections ;

- apprentissage conversion.

# **16.22 --- V2 IA : Équipe commerciale autonome**

Vision finale :

DIRECTEUR IA

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Agent Recherche

Agent Analyse

Agent Commercial

Agent CRM

Agent Data

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\|

Commercial humain

Le système pourrait dire chaque matin :

> \"Voici les 25 restaurants les plus intéressants aujourd\'hui.\
> J\'ai préparé les arguments, les messages et les prochaines actions.\"

# **16.23 --- Résumé architecture finale**

TFLE AI PLATFORM

AI ORCHESTRATOR

\|

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Discovery Agent

Analyst Agent

Scoring Agent

Sales Agent

CRM Agent

Quality Agent

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\|

RAG + Mémoire

\|

PostgreSQL + Vector DB

# **Conclusion Document 16**

L\'IA TFLE n\'est pas conçue comme une simple fonctionnalité.

Elle devient progressivement une infrastructure intelligente capable de
:

- trouver ;

- comprendre ;

- prioriser ;

- conseiller ;

- apprendre.

L\'objectif final :

> Construire un véritable assistant commercial IA spécialisé dans
> l\'acquisition de restaurants pour TableFlash.
