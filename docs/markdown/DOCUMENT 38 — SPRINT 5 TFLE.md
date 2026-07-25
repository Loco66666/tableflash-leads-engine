# **DOCUMENT 38 --- SPRINT 5 TFLE**

# **Lead Scoring IA Avancé & Assistant Commercial IA**

**Version : 1.0\
Statut : Plan d\'exécution développement Sprint 5\
Module : Artificial Intelligence Sales Intelligence Layer\
Produit : TableFlash Leads Engine (TFLE)\
Durée estimée : 15 jours ouvrés\
Objectif : Transformer TFLE d\'un moteur de scoring classique en
assistant commercial intelligent**

# **38.1 --- Vision du Sprint 5**

Les précédents sprints ont construit :

Sprint 1

Infrastructure

↓

Sprint 2

Base restaurants + CRM

↓

Sprint 3

Discovery Engine

↓

Sprint 4

Enrichissement + scoring règles

Le Sprint 5 ajoute la première vraie couche IA.

Avant :

Restaurant

↓

Score automatique

↓

Priorité

Après :

Restaurant

↓

Analyse IA complète

↓

Compréhension commerciale

↓

Arguments personnalisés

↓

Message adapté

↓

Assistant commercial TableFlash

# **38.2 --- Objectif business**

À la fin du Sprint 5, TFLE doit être capable de répondre :

> \"Pourquoi contacter ce restaurant, quel argument utiliser, et comment
> l\'approcher ?\"

# **38.3 --- Résultat attendu**

Version :

TFLE v0.5.0

Fonctionnalités :

✅ Analyse IA restaurant\
✅ Résumé commercial automatique\
✅ Détection opportunités\
✅ Arguments personnalisés TableFlash\
✅ Génération messages commerciaux\
✅ Assistant IA interne\
✅ Historique analyses IA\
✅ Système de prompts versionnés

# **38.4 --- Principe IA TFLE**

L\'IA ne remplace pas le commercial.

Elle augmente ses capacités.

Architecture :

Données fiables

↓

Analyse IA

↓

Suggestions

↓

Validation humaine

↓

Action commerciale

# **38.5 --- Architecture IA Sprint 5**

Nouvelle architecture :

backend/app/ai/

├── client/

│ ├── llm_client.py

│

├── prompts/

│ ├── restaurant_analysis.txt

│ ├── sales_argument.txt

│ ├── outreach_message.txt

│

├── agents/

│ ├── analyst_agent.py

│ ├── sales_agent.py

│

├── memory/

│ └── context_manager.py

│

├── evaluation/

│ └── quality_checker.py

# **38.6 --- Architecture globale IA TFLE**

Restaurant Data

↓

Enrichment Data

↓

Lead Score Rules

↓

AI Analyst Agent

↓

Sales Assistant Agent

↓

Commercial TableFlash

# **38.7 --- Nouveaux modèles Database**

## **Table ai_analyses**

Stockage des analyses IA.

ai_analyses

id

restaurant_id

analysis_type

input_snapshot

output_result

model_used

prompt_version

created_at

Types d\'analyse :

restaurant_analysis

sales_strategy

message_generation

# **38.8 --- Table prompts_versions**

Objectif :

Ne jamais perdre l\'évolution des prompts.

prompts_versions

id

name

version

content

created_at

active

Exemple :

sales_argument_v1

sales_argument_v2

sales_argument_v3

# **38.9 --- EPIC 01**

# **Infrastructure LLM**

Priorité :

## **P0**

Objectif :

Créer une couche indépendante du fournisseur IA.

TFLE ne doit pas dépendre d\'un seul modèle.

Architecture :

class AIClient:

analyze()

generate()

summarize()

Compatible :

- OpenAI ;

- Anthropic ;

- modèles locaux futurs.

# **Ticket TFLE-400**

## **Création AI Client**

Priorité :

P0

Fichier :

backend/app/ai/client/llm_client.py

Interface :

class LLMClient:

def generate_response(

prompt,

context

):

pass

# **Prompt Claude Code TFLE-400**

Tu travailles sur TFLE Sprint 5.

Crée l\'infrastructure IA.

Contraintes :

\- architecture fournisseur indépendant

\- gestion erreurs

\- logs

\- coûts maîtrisés

\- aucune logique métier dans le client IA

Avant modification :

liste les fichiers concernés.

# **Critères validation**

✅ Client IA fonctionnel\
✅ Appels centralisés\
✅ Logs disponibles

# **38.10 --- EPIC 02**

# **Agent Analyste Restaurant**

Priorité :

## **P0**

Objectif :

Créer un agent capable d\'analyser un restaurant.

Entrées :

{

\"name\":\"Restaurant X\",

\"city\":\"Bayonne\",

\"website\":\"\...\",

\"score\":82,

\"signals\":\[

\"pas de commande en ligne\"

\]

}

Sortie :

{

\"summary\":

\"Restaurant indépendant avec potentiel digital\",

\"opportunities\":\[

\"absence commande QR\"

\],

\"priority\":

\"high\"

}

# **Prompt système Agent Analyste**

Tu es l\'analyste commercial TableFlash.

Ton rôle est d\'analyser un restaurant.

Tu dois :

\- utiliser uniquement les données fournies ;

\- séparer faits et hypothèses ;

\- identifier les opportunités ;

\- expliquer chaque recommandation.

Ne jamais inventer une information.

# **Ticket TFLE-410**

Créer :

agents/analyst_agent.py

Fonction :

analyze_restaurant(

restaurant_data

)

# **Critères validation**

✅ Analyse cohérente\
✅ Raisons explicites\
✅ Pas d\'hallucination

# **38.11 --- EPIC 03**

# **Générateur d\'arguments commerciaux**

Priorité :

## **P0**

Objectif :

Transformer l\'analyse en arguments de vente.

Exemple :

Données :

Restaurant traditionnel

Pas de commande digitale

Site ancien

IA :

Argument 1 :

\"Vos clients peuvent commander directement depuis leur table grâce à un
QR code.\"

Argument 2 :

\"Vous réduisez la dépendance aux plateformes externes.\"

# **Table arguments_generated**

arguments_generated

id

restaurant_id

arguments

created_at

# **Ticket TFLE-420**

Créer :

agents/sales_agent.py

# **Critères validation**

✅ Arguments personnalisés\
✅ Adaptés au restaurant\
✅ Pas de texte générique

# **38.12 --- EPIC 04**

# **Génération messages commerciaux**

Priorité :

## **P1**

Objectif :

Créer des premiers messages personnalisés.

Formats :

## **Email**

Bonjour,

J\'ai découvert votre restaurant\...

## **Message LinkedIn**

Bonjour,

je travaille avec TableFlash\...

## **Appel téléphonique**

Script :

Bonjour, je me permets de vous appeler\...

# **Important**

TFLE génère une proposition.

Le commercial valide avant envoi.

# **Ticket TFLE-430**

API :

POST /ai/generate-message

Entrée :

{

\"restaurant_id\":123,

\"type\":\"email\"

}

Sortie :

{

\"message\":\"\...\"

}

# **38.13 --- EPIC 05**

# **Assistant Commercial IA**

Priorité :

## **P1**

Objectif :

Créer un chat interne.

Page :

/ai-assistant

Questions possibles :

Pourquoi contacter ce restaurant ?

Quel argument utiliser ?

Prépare-moi un appel.

Quels prospects contacter aujourd\'hui ?

# **Architecture :**

Commercial

↓

Assistant IA

↓

TFLE Database

↓

Réponse contextualisée

# **38.14 --- Mémoire IA TFLE**

MVP :

Mémoire courte.

Stockage :

Conversation

↓

Restaurant concerné

↓

Historique

Table :

ai_conversations

id

user_id

restaurant_id

messages

created_at

# **38.15 --- RAG initial TFLE**

Objectif :

Permettre à l\'IA de connaître :

- TableFlash ;

- fonctionnalités ;

- arguments ;

- objections.

Base documentaire :

ai/knowledge/

tableflash_features.md

sales_arguments.md

faq.md

objections.md

Workflow :

Question commerciale

↓

Recherche documentation

↓

IA répond avec contexte

# **38.16 --- EPIC 06**

# **Evaluation qualité IA**

Priorité :

## **P0**

Problème :

Une IA peut produire de mauvaises réponses.

Créer :

evaluation/

quality_checker.py

Vérifications :

## **Exactitude**

La réponse utilise uniquement les données disponibles.

## **Commercial**

Le message correspond à TableFlash.

## **Style**

Pas :

- agressif ;

- mensonger ;

- trop robotique.

# **Score IA :**

0-100

# **38.17 --- Interface IA**

Nouvelle section :

/ai

Pages :

AI Dashboard

Restaurant Analysis

Message Generator

Assistant Chat

Composants :

AIChat

AnalysisCard

ArgumentCard

PromptBadge

# **38.18 --- API Sprint 5**

## **Analyse restaurant**

POST /ai/analyze/{restaurant_id}

## **Génération arguments**

POST /ai/arguments/{restaurant_id}

## **Génération message**

POST /ai/message

## **Assistant**

POST /ai/chat

# **38.19 --- Tests Sprint 5**

## **Tests IA**

Cas :

Restaurant sans site.

Restaurant avec site moderne.

Restaurant déjà équipé.

## **Tests sécurité**

Vérifier :

- aucune donnée sensible envoyée inutilement ;

- clés API protégées ;

- logs propres.

## **Tests qualité**

Vérifier :

- réponses cohérentes ;

- pas d\'invention.

# **38.20 --- Planning Sprint 5**

## **Jour 1-3**

Infrastructure IA.

## **Jour 4-6**

Agent Analyste.

## **Jour 7-9**

Arguments commerciaux.

## **Jour 10-11**

Génération messages.

## **Jour 12-13**

Assistant IA.

## **Jour 14-15**

Tests + optimisation.

# **38.21 --- Definition of Done Sprint 5**

Le sprint est terminé lorsque :

## **IA**

✅ Analyse restaurant disponible\
✅ Arguments personnalisés générés\
✅ Messages préparés

## **Commercial**

✅ Un commercial TableFlash peut demander conseil à TFLE

## **Sécurité**

✅ Validation humaine obligatoire avant contact

# **38.22 --- Résultat opérationnel après Sprint 5**

Avant :

TFLE dit :

\"Ce restaurant a un score de 85.\"

Après :

TFLE dit :

\"Ce restaurant est prioritaire car :

\- indépendant ;

\- peu digitalisé ;

\- zone stratégique.

Arguments recommandés :

1\. Augmenter les commandes directes.

2\. Simplifier l\'expérience client.

Message conseillé :

Bonjour\...

\"
