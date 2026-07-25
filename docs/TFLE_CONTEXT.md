# TFLE_CONTEXT.md
# TableFlash Leads Engine
# Contexte stratégique principal pour IA de développement

Version : 1.0
Statut : Document fondateur
Projet parent : TableFlash
Audience : Codex / Claude Code / Développeurs / Architectes


# 1. IDENTITÉ DU PROJET

TFLE signifie :

TableFlash Leads Engine.

TFLE est une plateforme interne de prospection commerciale développée exclusivement pour accélérer l'acquisition de restaurants pour TableFlash.

TFLE n'est pas un produit SaaS commercialisé.

Son objectif est de devenir l'infrastructure interne permettant à TableFlash de :

- découvrir automatiquement des restaurants ;
- centraliser leurs informations professionnelles ;
- qualifier leur potentiel commercial ;
- prioriser les meilleurs prospects ;
- assister la prospection humaine grâce à l'intelligence artificielle ;
- suivre les conversions vers les essais gratuits TableFlash ;
- optimiser l'acquisition client.


# 2. OBJECTIF BUSINESS PRINCIPAL

L'objectif principal de TFLE est de réduire drastiquement le temps nécessaire pour trouver et convertir des restaurants partenaires TableFlash.

Problème actuel :

La recherche manuelle de restaurants est lente :

- recherche Google ;
- consultation de sites web ;
- recherche des coordonnées ;
- qualification manuelle ;
- prise de contact individuelle.

TFLE doit transformer ce processus en :

Découverte automatique

↓

Collecte données publiques

↓

Nettoyage

↓

Qualification intelligente

↓

Scoring commercial

↓

Contact personnalisé

↓

Essai gratuit 30 jours

↓

Conversion client TableFlash


# 3. RELATION AVEC TABLEFLASH

TFLE est un outil stratégique interne de TableFlash.

TableFlash :
Solution SaaS QR Ordering destinée aux restaurants traditionnels.

TFLE :
Machine d'acquisition commerciale permettant de trouver les restaurants susceptibles d'utiliser TableFlash.


TFLE doit toujours garder comme référence :

"Chaque fonctionnalité doit aider TableFlash à signer plus de restaurants."


# 4. UTILISATEURS INTERNES

Les utilisateurs principaux sont :

## Fondateur TableFlash

Responsable :

- stratégie ;
- analyse marché ;
- validation prospects ;
- pilotage commercial.


## Commercial TableFlash

Responsable :

- contact restaurants ;
- suivi prospects ;
- relances ;
- conversion.


## Analyste commercial

Responsable :

- analyse données ;
- segmentation ;
- optimisation campagnes.


## Agents IA internes

Responsables :

- analyse ;
- enrichissement ;
- recommandations ;
- assistance commerciale.


# 5. PRINCIPES FONDATEURS

## Principe 1 — Simplicité opérationnelle

TFLE doit permettre à une personne seule de gérer une prospection professionnelle.

Pas d'usine à gaz.

Chaque écran doit avoir une utilité commerciale claire.


## Principe 2 — Automatisation progressive

Ne jamais automatiser un processus avant de comprendre le fonctionnement manuel.

Ordre obligatoire :

1. Fonctionnement manuel fiable
2. Automatisation simple
3. Intelligence artificielle
4. Agents autonomes


## Principe 3 — Qualité des données avant quantité

100 prospects qualifiés valent mieux que 10 000 prospects inutilisables.


## Principe 4 — Architecture évolutive

Le MVP doit rester simple mais permettre une évolution vers :

- plusieurs régions ;
- plusieurs marchés ;
- plusieurs équipes commerciales ;
- plusieurs sources de données ;
- agents IA autonomes.


# 6. PÉRIMÈTRE MVP TFLE

Le MVP doit obligatoirement permettre :

## Module Restaurant Database

- création restaurants ;
- stockage informations ;
- recherche ;
- filtres ;
- tags.


## Module Discovery

Sources initiales :

- données publiques ;
- annuaires professionnels ;
- sites restaurants ;
- informations accessibles publiquement.


## Module Qualification

Analyse :

- type restaurant ;
- taille estimée ;
- présence digitale ;
- intérêt potentiel TableFlash.


## Module Lead Management

Gestion :

- statut prospect ;
- notes ;
- historique ;
- prochaine action.


## Dashboard simple

Afficher :

- nombre restaurants trouvés ;
- prospects qualifiés ;
- contacts effectués ;
- conversions.


# 7. ROADMAP PRODUIT

## MVP

Objectif :

Créer une base commerciale utilisable.

Modules :

- Database restaurants
- Recherche
- Import données
- Qualification manuelle
- CRM simple


## V1

Objectif :

Automatiser l'acquisition.

Ajouts :

- scraping engine ;
- enrichissement données ;
- email discovery ;
- scoring automatique ;
- assistant IA commercial.


## V2

Objectif :

Créer une intelligence commerciale autonome.

Ajouts :

- agents IA ;
- mémoire long terme ;
- optimisation automatique ;
- prédictions ;
- expansion multi-marchés.


# 8. ARCHITECTURE TECHNIQUE PRINCIPALE

Architecture cible :

Frontend :

- React / Next.js
- TypeScript
- Tailwind CSS


Backend :

- API Node.js
- Services spécialisés
- Workers asynchrones


Base données :

- PostgreSQL


IA :

- modèles LLM ;
- agents spécialisés ;
- RAG ;
- mémoire documentaire.


Infrastructure :

- Docker ;
- CI/CD ;
- monitoring ;
- environnements séparés.


# 9. ORGANISATION DES DOCUMENTS

La documentation complète se trouve dans :

docs/markdown/


Documents prioritaires :

## Vision

DOCUMENT 00


## Architecture

DOCUMENT 05 à 08


## MVP

DOCUMENT 30


## Technique

DOCUMENT 31 à 33


## Sprints

DOCUMENT 34 à 44


Avant toute décision technique importante :

Lire les documents concernés.


# 10. RÈGLES POUR L'IA DE DÉVELOPPEMENT

L'IA doit :

- comprendre avant de coder ;
- proposer un plan avant modifications majeures ;
- éviter les suppressions inutiles ;
- privilégier les solutions simples ;
- respecter l'architecture existante ;
- créer du code maintenable ;
- documenter les changements.


L'IA ne doit jamais :

- réécrire tout le projet sans validation ;
- modifier plusieurs modules critiques simultanément ;
- ignorer les contraintes métier ;
- créer des fonctionnalités hors roadmap.


# 11. MÉTHODOLOGIE DE DÉVELOPPEMENT

Chaque fonctionnalité doit suivre :

Analyse

↓

Plan technique

↓

Développement

↓

Tests

↓

Validation

↓

Documentation

↓

Commit Git


# 12. VISION LONG TERME

TFLE doit évoluer vers :

Un Revenue Operating System interne TableFlash.

Une infrastructure capable de :

- comprendre le marché restaurant ;
- identifier automatiquement les opportunités ;
- assister les commerciaux ;
- prévoir les conversions ;
- optimiser les stratégies commerciales.


# 13. PRIORITÉ ABSOLUE

La priorité numéro 1 reste :

Signer davantage de restaurants TableFlash.

Toute décision technique doit être évaluée selon cette question :

"Est-ce que cette fonctionnalité augmente la capacité de TableFlash à acquérir des restaurants ?"


FIN DU DOCUMENT