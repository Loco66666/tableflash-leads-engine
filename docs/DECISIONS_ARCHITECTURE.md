# Décisions d'architecture TFLE

Statut : validées par le responsable produit  
Date : 25 juillet 2026

## 1. Backend officiel

**Décision : Python + FastAPI**

### Justification

- Cohérence avec la documentation technique détaillée TFLE.
- Compatibilité directe avec le scraping, l'intelligence artificielle et le traitement de données.
- Évite de maintenir deux environnements backend Node.js et Python.

### Conséquence

Les futurs services API, traitements métier, workers et intégrations IA seront conçus en Python autour de FastAPI. Node.js ne sera pas introduit comme second backend.

## 2. Base de données

**Décision : modèle MVP évolutif**

Le modèle de données complet prévu pour les phases ultérieures ne sera pas créé immédiatement. Le schéma initial doit rester simple tout en permettant une évolution maîtrisée.

### Périmètre initial validé

- restaurants ;
- leads commerciaux ;
- utilisateurs ;
- interactions commerciales ;
- sources de données.

### Conséquence

Toute migration future devra partir de ce périmètre MVP et respecter l'historisation, la traçabilité des sources et les contraintes de sécurité documentées pour TFLE.

